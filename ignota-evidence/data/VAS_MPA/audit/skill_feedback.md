# Skill-feedback (ignota-evidence, run VAS_MPA)

## Context
Twee PDF's bleken één studie (DCVAS ACR/EULAR MPA-classificatiecriteria 2022, gelijktijdig in ARD en Arthritis & Rheumatology). Dat is geen prevalentiecohort-studie; dit gaf de meeste frictie.

## Onduidelijk of onhandig
1. **Geen pad voor classificatiecriteria-/diagnostische-accuracystudies.** SKILL/workflow gaan uit van cohorten met n/N per feature. Onbeantwoord: hoe leg je sensitiviteit/specificiteit/AUC/criteriagewichten vast (extraction.md noemt alleen sens/spec onder microbiology/diagnostics voor *tests*)? Ik heb ze bewust niet als observations opgeslagen. Voorstel: een apart `criteria`/`diagnostic_accuracy` domein of record-type (met referentiestandaard, set dev/val, N cases/comparators), of expliciet "niet extraheren" in extraction.md.
2. **Comparatorgroepen.** Schema kent alleen `disease_id` per cohort; comparators (822 patiënten met andere vasculitiden) passen nergens. Voorstel: regel in workflow.md "comparator-/controlegroepen niet extraheren tenzij ze zelf de doelziekte zijn" of een `cohort_role: case|comparator|control`-veld.
3. **Dubbelpublicatie niet beschreven.** Overlap-sectie gaat over paren met ≥2 signalen, maar niet over "zelfde artikel in twee tijdschriften": wel cohorten registreren (ik deed dat, met `possible_overlap`), observations maar één keer? Ik koos: observations alleen uit de eerste publicatie, de tweede alleen triage + cohortrecord. Voorstel: expliciete regel + optioneel veld `duplicate_of` / `primary_publication`.
4. **Overlap binnen één publicatie** (C2 n=404 bevat 269 van C1 n=291): `overlap_with` is nu een cohortlijst zonder soort/aantal. Voorstel: `overlap_type` (identical | subset | partial) en `overlap_n`.
5. **Raw vs normalized feature_id.** Observation-schema vereist `feature_id` in raw, maar normalisatie komt pas in stap 5. Ik gebruikte bron-slugs in raw (`pANCA_positive`) en standaard-ids in normalized plus `raw_feature_id`. Dit is niet vastgelegd; validate.py accepteert beide. Voorstel: `raw_feature_label` in schema, en `feature_id` in raw optioneel/vrij.
6. **Domeinen missen histologie/biopsie** (pauci-immune GN). Ik koos `laboratory` met voorgesteld prefix `HIST_`. Voorstel: `pathology`-domein en prefix `HIST_` in features.md. Ook ANCA-serologie: `laboratory` (LAB_) of `microbiology`/diagnostics? Ik koos laboratory.
7. **`timing`-enum mist "bij diagnose/baseline".** Bron registreert alleen data bij diagnose; `unspecified` is informatieverlies. Voorstel: waarde `at_diagnosis` of `baseline`.
8. **Percentage zonder n/N** (alleen "98%"): schema/validate staan het toe, maar `total_n: null` maakt het onbruikbaar voor pooling; niet duidelijk of `derived` iets betekent hier (ik zette `derived: false`). Voorstel: veld `percentage_rounded` / `precision` of notitie in extraction.md.
9. **Continue waarde zonder SD** (mean creatinine): `stat` zonder `sd` is oké, maar duplicaatsleutel (feature, cohort, timing, cutoff) staat niet toe dat dezelfde waarde in µmol/L én mg/dL als twee observations staat; ik koos één observation + tekst in definition. Voorstel: `alt_units` in schema of dit in extraction.md vastleggen.
10. **Interne inconsistentie** bron (tabel 5.2% vs tekst 6%): geen regel welke waarde de observation wordt. Ik nam tabel (met n/N) en loggde de tekstwaarde in issues.md. Voorstel: regel "tabel > tekst, conflict loggen" of `conflicts_with`-veld.
11. **cohort.schema.json mist `notes`**; `additionalProperties` is niet uitgesloten, dus ik voegde `notes` toe. Observation-schema mist ook `notes`/`extraction_note` terwijl SKILL "notitie in audit" vraagt; handig als veld.
12. **PMID.** Bronbestanden bevatten geen PMID. SKILL zegt "PMID of DOI"; ik heb alleen DOI. Geen netwerk; goed dat dat mag. Voorstel: expliciet in SKILL dat `pmid: null` met DOI voldoende is.
13. **not_reported-lijst**: features.md verwijst naar "secties 3-5 van de briefing" die niet in de repo staan. Ik kon niet bepalen welke `not_reported` verwacht werden en schreef er geen; voorstel: de lijst in features.md zelf opnemen.
14. **Paginanummering.** SKILL zegt form-feed voor pagina's; bij tijdschrift-PDF's verschillen PDF-pagina en tijdschriftpagina (ARD p. 321-326 = PDF 1-6). Ik noteerde beide in `source_location`. Voorstel: conventie vastleggen. Tweekolomslayout van `pdftotext -layout` verknipt lopende tekst; ik heb originele quotes tegen zowel layout- als niet-layout-uitvoer geverifieerd (voorstel: raw-modus aanbevelen voor lopende tekst, layout voor tabellen). Zachte koppeltekens (U+00AD) en hyphenation breken letterlijke matching.
15. **validate.py** controleert geen cohorts.json, geen verwijzing observation->cohort_id, en geen n/N-consistentie van cohortgrootte. Ik controleerde cohorts met het cohortschema apart. Voorstel: toevoegen, plus controle dat `original_text` in de brontekst voorkomt.
16. **pilot_notes.md / units.md** worden genoemd; niet aangemaakt omdat deze opdracht feedback in dit bestand vroeg en er geen conversies waren.

## Zelf bedenken
- Studie-id's per publicatie (`SUPPIAH2022_ARD`, `SUPPIAH2022_AR`) en cohort-id's `<study>_C1/C2`.
- Beslissing welke cohorten MPA-evidence zijn (C1: ja; C2: slechts één waarde; excluded 135 en comparators: nee).
- Feature-ids (zie issues.md) en `extraction_confidence`-niveaus.
- Dat classificatie-prestaties/criteriagewichten niet in de observation-laag horen.
