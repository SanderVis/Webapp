#!/usr/bin/env python3
"""Programmatische beoordeling van een run. Gebruik: grade.py <eval-dir> <config>"""
import json, sys, pathlib, subprocess, glob
ev, cfg = sys.argv[1], sys.argv[2]
proj = pathlib.Path(ev)/cfg/"outputs"/"project"
dd = proj/"data"/"INF_DENGUE"
def rows(pattern):
    out=[]
    for f in glob.glob(str(dd/"**"/pattern), recursive=True):
        if "/raw/fixture" in f or not ("/raw/" in f or "/normalized/" in f): continue
        for l in open(f):
            if l.strip():
                try: out.append(json.loads(l))
                except Exception: pass
    return out
raw = [r for r in rows("*.jsonl") if "disease_id" in r and "feature_id" in r]
cohort_files = glob.glob(str(dd/"**"/"cohorts*.json*"), recursive=True)
cohorts=[]
for f in cohort_files:
    try:
        d=json.load(open(f)); cohorts += d if isinstance(d,list) else d.get("cohorts",[])
    except Exception:
        cohorts += [json.loads(l) for l in open(f) if l.strip()]
name=pathlib.Path(ev).name
Path_validate=pathlib.Path("/home/user/Webapp/ignota-evidence/scripts/validate.py")  # altijd de actuele validator
res=[]
def a(text, passed, evidence): res.append({"text":text,"passed":bool(passed),"evidence":evidence})
def _grp(c):
    s=json.dumps(c).lower()
    return "child" if ("child" in s or "pediatric" in s) else ("adult" if "adult" in s else "?")
grp={str(c.get("cohort_id")):_grp(c) for c in cohorts}
SYN={"crp":["crp","c-reactive","c_reactive"],"rash":["rash","exanthem"],"platelet":["platelet","thrombocyt"],"thrombocytopenia":["platelet","thrombocyt"],"alt":["alt ","alt_","_alt","alanine","alt)"],"myalgia":["myalgia","muscle"]}
def feat(pat, cohort_pat=None):
    keys=SYN.get(pat.lower(),[pat.lower()])
    def hit(r):
        h=(r.get("feature_id","")+" "+r.get("original_text","")).lower()+" "
        return any(k in h for k in keys)
    def coh(r):
        if cohort_pat is None: return True
        cp="child" if cohort_pat.startswith("child") else "adult"
        g=grp.get(str(r.get("cohort_id")),"?")
        return g==cp or (g=="?" and cp in json.dumps(r).lower())
    return [r for r in raw if hit(r) and coh(r)]
if name.startswith("eval-0"):
    a("Geen observations geschreven (geen bron)", len(raw)==0, f"{len(raw)} observations")
    txt=" ".join(open(f).read() for f in glob.glob(str(dd/"**"/"*.md"),recursive=True))
    a("Er is een melding/notitie dat bron ontbreekt", True if txt else None, "audit-notitie aanwezig" if txt else "geen md-notitie; zie samenvatting")
else:
    c_ids={str(c.get("cohort_id")) for c in cohorts}
    a("Cohorten adults en children apart opgeslagen (>=2 cohorten voor fixture A)", len(c_ids)>=2, f"cohort_ids={sorted(c_ids)}")
    a("Alle observations hebben PMID of DOI", bool(raw) and all(r.get("pmid") or r.get("doi") for r in raw), f"{len(raw)} obs")
    a("Alle observations hebben source_location en original_text", bool(raw) and all(r.get("source_location") and r.get("original_text") for r in raw), "")
    crp=feat("crp","adult")
    a("CRP volwassenen als median/IQR (stat.median=18) zonder mean", any((r.get("stat") or {}).get("median")==18 for r in crp) and not any("mean" in (r.get("stat") or {}) for r in crp), json.dumps([r.get("stat") for r in crp]))
    crpc=feat("crp","child")
    a("CRP kinderen: niet als present met waarde gevuld", not any(r.get("status")=="present" or r.get("stat") for r in crpc), json.dumps([(r.get("status"),r.get("stat")) for r in crpc]))
    rash=[r for r in feat("rash","adult")]
    a("Rash volwassenen: geen verzonnen positive_n/total_n", all(r.get("positive_n") is None for r in rash) if rash else None, json.dumps([(r.get("positive_n"),r.get("total_n"),r.get("percentage")) for r in rash]))
    my=feat("myalgia","child")
    a("Myalgie kinderen niet als absent geregistreerd", not any(r.get("status")=="absent" for r in my), json.dumps([r.get("status") for r in my]))
    plt=feat("platelet","adult")+feat("thrombocytopenia","adult")
    a("Trombocytopenie volwassenen 140/200 correct", any(r.get("positive_n")==140 and r.get("total_n")==200 for r in plt), json.dumps([(r.get("positive_n"),r.get("total_n")) for r in plt]))
    alt=feat("alt","adult")
    a("ALT noemer 120 (niet 200)", any(r.get("total_n")==120 and r.get("positive_n")==55 for r in alt), json.dumps([(r.get("positive_n"),r.get("total_n")) for r in alt]))
    tx=[r for r in raw if r.get("domain")=="treatment" or "steroid" in r.get("feature_id","").lower()]
    a("Behandelrespons 8/12 aanwezig als treatment (niet als diagnostisch bewijs)", any(r.get("positive_n")==8 and r.get("total_n")==12 for r in tx), json.dumps([(r.get("domain"),r.get("positive_n"),r.get("total_n")) for r in tx]))
    v=subprocess.run([sys.executable,str(Path_validate),str(dd)],capture_output=True,text=True)
    a("validate.py slaagt", v.returncode==0, (v.stdout+v.stderr)[-300:])
if name.startswith("eval-2"):
    ov=[c for c in cohorts if c.get("possible_overlap") is True]
    a("Overlap tussen fixture A-adults en B gemarkeerd", len(ov)>=1, f"{len(ov)} cohorten met possible_overlap")
    syn=[json.loads(l) for f in glob.glob(str(dd/"synthesized"/"*.jsonl")) for l in open(f) if l.strip()]
    pooled=[s for s in syn if s.get("pooled") is True or s.get("pooled_estimate") not in (None,"")]
    a("Geen gepoolde schatting over overlappende cohorten", len(pooled)==0, f"{len(pooled)} gepoolde records")
    sfiles=[f for f in glob.glob(str(dd/"synthesized"/"*")) if not f.endswith(".gitkeep")]
    a("Synthese-bestand aanwezig", len(sfiles)>0, str([pathlib.Path(f).name for f in sfiles]))
json.dump({"expectations":res},open(pathlib.Path(ev)/cfg/"grading.json","w"),indent=1)
print(name,cfg,sum(1 for r in res if r["passed"]),"/",len(res))
