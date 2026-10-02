#!/usr/bin/env python3
"""Kwaliteitscontrole van raw/normalized observations (JSONL). Gebruik: validate.py data/<DISEASE_ID>"""
import json, sys, pathlib
try:
    import jsonschema
except ImportError:
    jsonschema = None
root = pathlib.Path(__file__).resolve().parent.parent
schema = json.load(open(root/"schemas/observation.schema.json"))
errs = 0
def err(f, i, m):
    global errs; errs += 1; print(f"{f}:{i}: {m}")
base = pathlib.Path(sys.argv[1])
files = [f for sub in ("raw", "normalized") for f in (base/sub).rglob("*.jsonl")]  # triage/audit/synthesized hebben ander schema
for f in files:
    seen = set()
    for i, line in enumerate(open(f), 1):
        if not line.strip(): continue
        o = json.loads(line)
        if jsonschema:
            for e in jsonschema.Draft202012Validator(schema).iter_errors(o): err(f, i, e.message)
        n, N, p = o.get("positive_n"), o.get("total_n"), o.get("percentage")
        if n is not None and N is not None:
            if n > N: err(f, i, "positive_n > total_n")
            if p is not None and N and abs(100*n/N - p) > 0.6: err(f, i, f"percentage {p} != {n}/{N}")
        if p is not None and (n is None or N is None) and not o.get("derived") and o.get("domain") != "epidemiology":
            pass  # bron mag alleen % rapporteren; toegestaan
        if o.get("status") in ("not_reported","not_assessed") and (n is not None or p is not None):
            err(f, i, "waarde aanwezig bij status not_reported/not_assessed")
        if o.get("status") == "absent" and o.get("original_text", "") == "":
            err(f, i, "absent zonder brontekst")
        if not (o.get("pmid") or o.get("doi")): err(f, i, "geen PMID/DOI")
        key = (o.get("feature_id"), o.get("cohort_id"), o.get("timing"), o.get("cutoff"))
        if key in seen: err(f, i, f"duplicaat observation {key}")
        seen.add(key)
print("OK" if not errs else f"{errs} problemen"); sys.exit(1 if errs else 0)
