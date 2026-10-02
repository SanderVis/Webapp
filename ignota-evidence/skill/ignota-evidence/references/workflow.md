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

## Brontypen
| source_type | cohort-regel | noemer | evidentieweging |
|---|---|---|---|
| primary_cohort, registry | echte cohorten, per cohort | n/N uit de bron | hoog |
| review_citing_primary | één `review_container` (sample_size null) | alleen als in reviewtekst; nooit uit referentielijst | laag; `cited_source` alleen bij expliciete koppeling |
| classification_study | case-cohort(en) van de doelziekte; comparator = `cohort_role: comparator`, niet extraheren | casegroep | middel; criteriaprestaties horen in `diagnostic_accuracy`, niet in clinical/lab |
| guideline | geen cohort; alleen definities | n.v.t. | gebruik als context, niet als prevalentiebron |

## Cohortstructuur
- Kolommen voor periodes (1990-95, 1995-2000) van dezelfde patiënten: `cohort_type: period_subset`, `parent_cohort_id`, `possible_overlap: false` (structureel, geen echte overlap). Tel nooit op.
- Overlap binnen één publicatie (subset): `overlap_type` (identical | subset | partial), `overlap_n`.
- Cohorten die in de bron wel genoemd maar niet geëxtraheerd zijn: `overlap_with_unextracted`.
- Dubbelpublicatie: `duplicate_of`, geen eigen observations.

## Conflicten binnen één bron
Tabelwaarde > tekstwaarde. Log de tekstwaarde in `audit/issues.md` en zet `conflicts_with` op de observation.
