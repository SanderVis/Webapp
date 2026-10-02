---
name: ignota-evidence
description: Bouwt per ziekte een cohort-gebaseerde, bron-traceerbare evidence-database (symptomen, labwaarden, beeldvorming, epidemiologie, behandeling) voor het verbeteren van Ignota (Bayesiaanse FUO/IUO-differentiaaldiagnosetool). Gebruik dit wanneer de gebruiker evidence wil verzamelen of extraheren voor een ziekte, een pilotziekte wil uitvoeren, artikelen/PDF's wil omzetten naar n/N-gegevens, of de Master Briefing Klinische Diagnostische Kennisdatabase noemt. Eén ziekte per aanroep. Niet voor het direct wijzigen van de Ignota-kennisbank (daarvoor ignota-kennisbank).
---

# ignota-evidence

Voert de Master Briefing v1.0 uit voor **één ziekte per aanroep**. Resultaat: evidence-bestanden met volledige provenance, geschikt als onderlaag voor Ignota. Je schrijft hier **niet** in de Ignota-kennisbank; dat is een aparte, door de gebruiker goedgekeurde stap (zie `references/ignota-handoff.md`).

Projectroot: `ignota-evidence/` (schema's in `schemas/`, scripts in `scripts/`, data in `data/<DISEASE_ID>/`). Lees eerst `RULES.md`; die regels gaan boven alles.

## 0. Preflight (altijd eerst)

1. Welke `disease_id`? Zoek hem in `diseases/disease_master.json`. Onbekend: stel een entry voor en vraag akkoord.
2. Welke bronnen kun je **daadwerkelijk lezen**?
   - PDF's/tekst in `data/<ID>/raw/` (voorkeur), en/of
   - netwerktoegang tot PubMed/PMC/Europe PMC (test met één request).
3. Zijn er geen leesbare bronnen: **stop**. Zeg wat ontbreekt. Vul nooit aan uit geheugen en gebruik geen zoeksamenvattingen als bron.
4. Alleen een abstract beschikbaar: extraheer alleen wat letterlijk in het abstract staat, zet `evidence_access: abstract_only`, geef geen bronlocatie die je niet hebt gezien.

## 1. Workflow per ziekte

Voer de stappen in volgorde uit; details in `references/workflow.md`.

1. **Zoeken** – `python3 scripts/queries.py <ID>` geeft de zoekopdrachten (sectie 14). Prioriteer volgens de bronhiërarchie (sectie 15).
2. **Triage** – per artikel een record in `data/<ID>/audit/triage.jsonl`: relevantie, design, N, cohorten, welke domeinen beschikbaar, referentiestandaard, overlapverdenking. Case reports niet voor prevalentie.
3. **Cohort-extractie** – elk cohort apart in `data/<ID>/raw/cohorts.json` (schema: `schemas/cohort.schema.json`).
4. **Observation-extractie** – per domein (clinical, laboratory, imaging, functional, microbiology, epidemiology, treatment) naar `data/<ID>/raw/<domein>.jsonl`, schema `schemas/observation.schema.json`. Regels: `references/extraction.md`.
5. **Normalisatie** – feature-ids en eenheden naar `data/<ID>/normalized/`, met behoud van `original_text`. Vocabulaire: `references/features.md`.
6. **Overlapcontrole** – zie `references/workflow.md` §Overlap. Markeer `possible_overlap`/`overlap_with`; tel nooit dubbel.
7. **Synthese** – alleen als gerechtvaardigd; `references/synthesis.md`. Schrijf naar `synthesized/`; raw blijft onaangeroerd.
8. **Validatie** – `python3 scripts/validate.py data/<ID>`. Los alle fouten op of documenteer ze in `audit/issues.md`.
9. **Dashboard** – `data/<ID>/audit/dashboard.md`: coverage per domein, aantal cohorten, patiënten, studies, conflicten, overlap. Coverage = aandeel domeinen/features met ≥1 geëxtraheerde observation, geen kwaliteitsoordeel.
10. **Rapportage** – korte samenvatting aan de gebruiker: wat gevonden, wat ontbreekt, wat onzeker, welke bronnen alleen abstract.

## Niet-onderhandelbaar

- `not_reported` is niet `absent`. Statussen: present | absent | not_reported | not_assessed | unclear.
- Geen berekende gemiddelden/SD's/percentages die de bron niet geeft (percentage uit n/N in de bron mag, met `derived: true`).
- Elke observation: PMID of DOI, `study_id`, `cohort_id`, `source_location`, `original_text`.
- Therapierespons is geen diagnostisch bewijs. Kwaliteitsbeoordeling wordt nooit omgezet in een probabiliteit.
- Conflicterende studies niet middelen of kiezen; stratificeer en rapporteer heterogeniteit.
- Twijfel over een extractie: `extraction_confidence: low` plus notitie in audit, niet gokken. Kritieke extracties (N, hoofdprevalenties) laat je door de gebruiker steekproefsgewijs controleren.

## Output per ziekte

```
data/<ID>/raw/        cohorts.json, clinical|laboratory|imaging|functional|microbiology|epidemiology|treatment.jsonl, bronbestanden
data/<ID>/normalized/ dezelfde observations met gestandaardiseerde ids
data/<ID>/synthesized/ ranges, pooled (indien gerechtvaardigd), heterogeniteit
data/<ID>/audit/      triage.jsonl, issues.md, dashboard.md, overlap.md
```

## Eerste gebruik (pilot)

De pilot is 10 ziekten (zie `diseases/disease_master.json`). Begin met één ziekte, review samen met de gebruiker de eerste ~20 observations op schema, definities en bronlocaties, en pas pas daarna door naar de rest. Leg bevindingen over schema/prompt vast in `audit/pilot_notes.md`.
