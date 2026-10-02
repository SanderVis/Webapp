# Workflow-details

## Zoeken en selecteren
- Gebruik de queries uit `scripts/queries.py`; voeg synoniemen uit `disease_master.json` toe.
- Prioriteit: grote prospectieve cohorten > multicenter > goed gedefinieerde retrospectieve cohorten > registries > systematische reviews > meta-analyses > kleine cohorten > case series > case reports.
- Systematische reviews/meta-analyses: gebruik ze om primaire cohorten te vinden en voor synthese-vergelijking; extraheer primaire data uit de primaire bron wanneer beschikbaar. Zo voorkom je dubbeltelling.
- Leg per artikel vast of je volledige tekst hebt gelezen of alleen een abstract.

## Triage-record (audit/triage.jsonl)
`{study_id, pmid, doi, year, disease_id, relevant: bool, reason, design, population, N, cohorts: [...], domains: {clinical, laboratory, imaging, epidemiology, treatment}, reference_standard, possible_overlap, evidence_access}`.
Geef alleen informatie die in de bron staat; onbekend = null.

## Cohorten
Meerdere cohorten in één publicatie (volwassenen/kinderen/ICU, derivation/validation) zijn aparte `cohort_id`'s, bijv. `<study_id>_C1`. Validatiecohorten die dezelfde patiënten hergebruiken zijn geen onafhankelijke cohorten.

## Overlap
Vergelijk per paar publicaties: instelling, land, studieperiode, N, auteurs (gedeelde eerste/laatste auteur), inclusiecriteria, registry/database, interventie, follow-up. Bij ≥2 overeenkomstige signalen: `possible_overlap: true`, `overlap_with: [<cohort_id>]` en noteer in `audit/overlap.md` waarom. Niet-twijfelloos onafhankelijke cohorten worden niet samen gepoold.

## Dashboard-velden
Clinical/Laboratory/Imaging/Functional/Epidemiology/Time-course/Treatment coverage, aantal cohorten, totaal N (zonder overlap-dubbeltelling, overlap apart vermeld), primaire studies, reviews, evidence conflicts, potentiële overlaps.
