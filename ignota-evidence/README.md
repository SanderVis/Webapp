# Ignota Evidence – klinische kennisdatabase (pilot)

Uitvoering van de Master Briefing v1.0 (2 okt 2026). Doel: cohort-gebaseerde, bron-traceerbare evidence per ziekte, als basis om het Ignota-artifact te verbeteren.

## Structuur
- `RULES.md` – harde regels (niet verzinnen, not_reported != absent, geen reconstructie, ...)
- `diseases/disease_master.json` – 10 pilotziekten
- `schemas/` – JSON-schema's voor observations en cohorten
- `scripts/queries.py <DISEASE_ID>` – zoekopdrachten (briefing sectie 14)
- `scripts/validate.py data/<DISEASE_ID>` – n/N-, percentage-, provenance- en duplicaatcontrole
- `data/<DISEASE_ID>/{raw,normalized,synthesized,audit}/` – drie evidence-lagen + audit

## Pilot (10 ziekten)
Dengue, Lyme, invasieve candidiasis, tuberculose, influenza, GPA, SLE, FMF, SAVI, AOSD.
(COVID-19 is weggelaten: de briefing zegt "influenza of COVID-19"; kies je COVID-19, voeg die toe.)

## Werkwijze per ziekte
zoeken -> triage -> cohort-extractie -> klinisch/lab/imaging/epi/behandeling -> overlapcontrole -> synthese -> dashboard -> validate.py

## Status
Geraamte klaar. Literatuurtoegang (PubMed/Europe PMC/PMC) wordt door het netwerkbeleid van deze cloudomgeving geblokkeerd; extractie is nog niet gestart.
