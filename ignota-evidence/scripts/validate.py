#!/usr/bin/env python3
"""Kwaliteitscontrole van data/<DISEASE_ID>: observations (raw+normalized), cohorts.json, verwijzingen, pariteit.
Gebruik: validate.py data/<DISEASE_ID>"""
import json, sys, pathlib
try:
    import jsonschema
except ImportError:
    jsonschema = None
root = pathlib.Path(__file__).resolve().parent.parent
obs_schema = json.load(open(root/"schemas/observation.schema.json"))
coh_schema = json.load(open(root/"schemas/cohort.schema.json"))
PREFIXES = ("SYM_","SIGN_","LAB_","MICRO_","IMG_","FUNC_","EXP_","EPI_","TX_","HIST_","CRIT_","COMP_","OUT_")
base = pathlib.Path(sys.argv[1]); errs = 0
def err(where, m):
    global errs; errs += 1; print(f"{where}: {m}")
def load_jsonl(f):
    return [(i, json.loads(l)) for i, l in enumerate(open(f), 1) if l.strip()]
# cohorts
cohorts = {}
cf = base/"raw"/"cohorts.json"
if cf.exists():
    data = json.load(open(cf)); data = data if isinstance(data, list) else data.get("cohorts", [])
    for c in data:
        cohorts[c.get("cohort_id")] = c
        if jsonschema:
            for e in jsonschema.Draft202012Validator(coh_schema).iter_errors(c): err(f"cohorts.json[{c.get('cohort_id')}]", e.message)
        for o in c.get("overlap_with", []):
            pass
else:
    print("waarschuwing: raw/cohorts.json ontbreekt")
layers = {}
for layer in ("raw", "normalized"):
    rows = []
    for f in sorted((base/layer).glob("*.jsonl")):
        rows += [(f, i, o) for i, o in load_jsonl(f)]
    layers[layer] = rows
    seen = set()
    for f, i, o in rows:
        w = f"{f.parent.name}/{f.name}:{i}"
        if jsonschema:
            for e in jsonschema.Draft202012Validator(obs_schema).iter_errors(o): err(w, e.message)
        n, N, p = o.get("positive_n"), o.get("total_n"), o.get("percentage")
        if n is not None and N is not None:
            if n > N: err(w, "positive_n > total_n")
            if p is not None and N and abs(100*n/N - p) > 0.6: err(w, f"percentage {p} != {n}/{N}")
        if o.get("status") in ("not_reported", "not_assessed") and (n is not None or p is not None):
            err(w, "waarde aanwezig bij status not_reported/not_assessed")
        if not (o.get("pmid") or o.get("doi")): err(w, "geen PMID/DOI (DOI volstaat; PMID alleen als in de bron)")
        if cohorts and o.get("cohort_id") not in cohorts: err(w, f"onbekend cohort_id {o.get('cohort_id')}")
        if layer == "raw" and not (o.get("feature_id") or o.get("feature_label_original")): err(w, "geen feature_id of feature_label_original")
        if layer == "normalized":
            fid = o.get("feature_id") or ""
            if not fid.startswith(PREFIXES): err(w, f"feature_id '{fid}' heeft geen geldig prefix {PREFIXES}")
        label = o.get("feature_label_original") or o.get("feature_id")
        key = (o.get("domain"), label, o.get("cohort_id"), o.get("timing"), o.get("period"), o.get("cutoff"), o.get("finding_direction"))
        if key in seen: err(w, f"duplicaat observation {key}")
        seen.add(key)
if layers["normalized"] and len(layers["raw"]) != len(layers["normalized"]):
    err("pariteit", f"raw heeft {len(layers['raw'])} observations, normalized {len(layers['normalized'])}")
for c in cohorts.values():
    if c.get("duplicate_of") and any(o.get("cohort_id") == c["cohort_id"] for _, _, o in layers["raw"]):
        err(f"cohort {c['cohort_id']}", "duplicate_of-cohort mag geen eigen observations hebben")
print("OK" if not errs else f"{errs} problemen"); sys.exit(1 if errs else 0)
