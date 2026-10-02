#!/usr/bin/env python3
"""Controleer raw-observations tegen de bron-PDF's.
Niveaus per observation:
  verbatim  - original_text staat letterlijk in de bron (spaties, koppeltekens, ligaturen genegeerd)
  numbers   - niet letterlijk (bijv. hergebouwde tabelrij), maar alle getallen staan in de bron
  MISSING   - citaat niet gevonden en/of getallen ontbreken in de bron -> handmatig nakijken
Gebruik: check_quotes.py data/<DISEASE_ID>   (vereist pdftotext)"""
import json, sys, re, subprocess, pathlib, unicodedata
base = pathlib.Path(sys.argv[1])
def alnum(s): return re.sub(r"[^0-9a-z]+", "", unicodedata.normalize("NFKC", s).lower())
def run(args): return subprocess.run(args, capture_output=True, text=True).stdout
srcs, nums = [], set()
for pdf in (base/"raw").glob("*.pdf"):
    for extra in ([], ["-layout"]):
        t = run(["pdftotext", *extra, str(pdf), "-"]); srcs.append(alnum(t))
        nums |= set(re.findall(r"\d+(?:[.,]\d+)?", unicodedata.normalize("NFKC", t)))
if not srcs: sys.exit("geen bron-PDF in raw/")
cnt = {"verbatim": 0, "numbers": 0, "MISSING": 0}
for f in sorted((base/"raw").glob("*.jsonl")):
    for i, line in enumerate(open(f), 1):
        if not line.strip(): continue
        o = json.loads(line); q = o.get("original_text", "")
        if alnum(q) and any(alnum(q) in s for s in srcs): cnt["verbatim"] += 1; continue
        qn = set(re.findall(r"\d+(?:[.,]\d+)?", q))
        if qn and qn <= nums: cnt["numbers"] += 1; continue
        cnt["MISSING"] += 1; print(f"{f.name}:{i} [{o.get('feature_id')}] MISSING: {q[:110]!r}")
print(cnt); sys.exit(1 if cnt["MISSING"] else 0)
