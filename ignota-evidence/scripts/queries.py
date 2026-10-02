#!/usr/bin/env python3
"""Genereer de zoekopdrachten uit sectie 14 voor een disease_id."""
import json, sys, pathlib
T = {
 "clinical": ['"{d}" clinical manifestations cohort','"{d}" symptom prevalence cohort','"{d}" signs symptoms prospective cohort','"{d}" complications cohort'],
 "laboratory": ['"{d}" laboratory findings cohort','"{d}" hematological findings cohort','"{d}" CRP ESR ferritin cohort','"{d}" liver enzymes cohort','"{d}" renal laboratory findings cohort'],
 "imaging": ['"{d}" radiological findings cohort','"{d}" CT MRI ultrasound findings','"{d}" imaging manifestations'],
 "epidemiology": ['"{d}" epidemiology age sex geography','"{d}" incidence prevalence systematic review','"{d}" incubation period','"{d}" travel exposure risk factors'],
 "treatment": ['"{d}" treatment response cohort','"{d}" response rate remission cohort','"{d}" relapse treatment cohort'],
 "subgroups": ['"{d}" pediatric cohort','"{d}" adult cohort','"{d}" ICU severe cohort','"{d}" outpatient cohort'],
 "synthesis": ['"{d}" systematic review clinical manifestations','"{d}" meta-analysis clinical features','"{d}" diagnostic accuracy'],
}
root = pathlib.Path(__file__).resolve().parent.parent
master = {r["disease_id"]: r for r in json.load(open(root/"diseases/disease_master.json"))}
r = master[sys.argv[1]]
for dim, qs in T.items():
    print(f"## {dim}")
    for q in qs: print(q.format(d=r["synonyms"][0] if r["synonyms"] else r["name"]))
