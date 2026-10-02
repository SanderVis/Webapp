# Harde regels (uit Master Briefing v1.0, 2 okt 2026)

1. Verzin nooit ontbrekende data; geen bronloze percentages.
2. `not_reported` != `absent`. Statussen: present | absent | not_reported | not_assessed | unclear.
3. Bereken alleen een percentage als n en N in de bron staan (of expliciet als `derived: true` met beide getallen uit de bron).
4. Reconstrueer geen continue waarden (geen gemiddelde uit mediaan, geen SD uit IQR).
5. Bewaar originele eenheid, statistische vorm, referentiegebied, cutoff, definitie.
6. Cohorten binnen één publicatie apart houden; cohort-overlap tussen publicaties detecteren (`possible_overlap`, `overlap_with`).
7. Geen pooling zonder methodologische rechtvaardiging; synthese vervangt nooit raw.
8. Therapierespons is geen diagnostisch bewijs. Case reports nooit voor algemene prevalentie.
9. Ancestry/etniciteit alleen zoals gerapporteerd; geen causale conclusies.
10. Elke observation traceerbaar: disease -> feature -> cohort -> study -> source_location (PMID/DOI).
11. Drie lagen gescheiden: raw / normalized / synthesized. Plus audit/.
12. Alleen data uit de bron die daadwerkelijk is gelezen (abstract of volledige tekst); vermeld welke (`evidence_access`: full_text | abstract_only).
