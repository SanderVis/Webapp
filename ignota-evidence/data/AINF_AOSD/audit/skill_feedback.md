# Skill feedback (ignota-evidence), run AINF_AOSD / Mahroum2014 narrative review

## Onduidelijk of ontbrekend
1. Geen regel voor narratieve reviews zonder eigen cohort. workflow.md zegt "extraheer primaire data uit de primaire bron" maar niet wat te doen als alleen de review beschikbaar is. observation.schema vereist `cohort_id` en cohort.schema `sample_size`/`possible_overlap`. Ik gebruikte een pseudo-cohort `<study_id>_C0` (sample_size null, possible_overlap true). Voorstel: expliciet `cohort_type: "review_container"` (of `source_type`) in cohort.schema, en regel in extraction.md dat reviewcijfers nooit in pooling/total N tellen.
2. Gecitede primaire studie binnen een review: geen veld voor "wie zei dit oorspronkelijk" (ref-nummer, N van de primaire). Ik voegde extra velden `cited_primary_ref` en `notes` toe (schema staat dat toe). Voorstel: `cited_source` {ref_label, pmid, doi, n} en `notes` in observation.schema, plus `source_type: primary|review_citing_primary`.
3. Noemer: bij reviews staat N van de primaire vaak alleen in de referentielijst ("a study of 104 cases"). Regel nodig: mag total_n daaruit komen? Ik zei nee en liet total_n null. Voorstel: dit expliciet vastleggen (of toestaan met `total_n_source: reference_list`).
4. PMID niet in het artikel: validate eist PMID of DOI; ok, maar skill zegt "haal PMID/DOI uit de bron" zonder te zeggen dat null is toegestaan voor PMID. Verduidelijk.
5. Raw versus normalized: unclear of raw `feature_id` al een standaard-id mag zijn. SKILL.md stap 5 suggereert dat vrije namen "later niet te koppelen" zijn, maar normalized moet toch iets anders zijn dan raw. Ik koos raw = brontermen, normalized = ids + `feature_id_raw`. Leg dit vast.
6. Geen domein/feature-conventie voor: pathologie/biopsie, classificatiecriteria en diagnostische nauwkeurigheid (sens/spec van criteria of testen), complicaties (RHS, leverfalen). Prefixlijst mist CRIT_/PATH_/COMP_. Ik zette sens/spec van ferritine in laboratory.stat en liet criteria en pathologie weg. Voorstel: domein `pathology` en `diagnostic_accuracy` (met velden sensitivity, specificity, reference_standard, N cases/controls).
7. "Negatief in X%" / "normaal in X%" (ANA, RF, bilirubine): geen conventie. Ik gebruikte features LAB_ANA_NEGATIVE etc. om niet 100-x te hoeven berekenen. Beter: veld `finding_direction` (abnormal|normal|negative) of afspraak.
8. Bereikwaarden voor percentage ("30-65%", "20-25%") en grenswaarden ("up to 20%", "about 40%"): geen veld. Ik zette min/max in `stat` en percentage null; "about" in definition. Voorstel: `percentage_qualifier` (about|up_to|range) en `percentage_range`.
9. Kwalitatieve woorden ("common", "rare", "frequent"): extraction.md zegt status present + low, maar "rare" en "not uncommon" zijn ook informatie; geen veld voor `qualitative_frequency`. Voorstel toevoegen.
10. Timing-enum: "late finding" (radiografisch) = chronic? Ik koos chronic en "initial acute phase" = acute; mapping niet gedefinieerd.
11. Page break binnen een zin en tweekoloms-layout: `pdftotext -layout` mengt kolommen; ik moest de niet-layout-uitvoer gebruiken om original_text te verifiëren. Voorstel: workflow-tip en een scriptje `verify_quotes.py` dat original_text tegen de brontekst controleert (met ligatuur-/whitespace-normalisatie; 'ﬁ' ligaturen en verloren gradenteken).
12. features.md "Verwachte features voor not_reported" verwijst naar "secties 3-5 van de briefing", die niet in het project staan. Een reviewbron kan geen not_reported rechtvaardigen; ik heb er geen gemaakt. Maak lijst expliciet en zeg dat not_reported alleen bij primaire cohorten mag.
13. Cohortschema: overlap_with is lijst van cohort_id's, maar de primaire studies zijn niet geextraheerd; ik gebruikte placeholders "(not_extracted)". Voorstel: aparte `overlap_with_unextracted` of `cited_primary_refs`.
14. workflow.md zegt triage veld `N`; voor review is N null en het aantal gecitede patientengroepen verschilt; geen veld voor "aantal gecitede primaire studies".
15. validate.py: controleert alleen raw/normalized observations; geen check op cohorts.json, triage-schema, ontbrekende normalized-laag, of original_text in bron. Duplicate-sleutel (feature, cohort, timing, cutoff) botst voor reviews waar twee citaten dezelfde feature met verschillende bron geven (bijv. sens/spec ferritine vs. prevalentie ferritine; ik moest `cutoff` misbruiken als discriminator). Voorstel: voeg `cited_source` aan de sleutel toe, of een `observation_type` (prevalence|diagnostic_accuracy|continuous|...), zodat ik cutoff niet hoef te misbruiken.
16. Het wegschrijven van `percentage` dat de bron geeft zonder n/N: validate heeft een lege `pass`; derived-regel is vaag voor "bron geeft alleen %". Duidelijk maken: derived=false en n/N null is de norm.
17. disease_master status 'pilot_pending' wordt niet bijgewerkt (mocht ik niet wijzigen); wie doet dat?

## Zelf bedacht
Pseudo-cohort-conventie, extra velden (cited_primary_ref, notes, feature_id_raw), *_NEGATIVE/*_NORMAL features, 46 nieuwe feature-id voorstellen (zie issues.md), confidence-regels (low voor kwalitatief of ingeleide attributie, medium voor een duidelijk getal zonder N, high niet gebruikt omdat elk cijfer secundair is), niet synthetiseren.

## Verbetervoorstellen (kort)
- Bronsoort-beslisboom in SKILL.md (primair cohort / review / guideline / case) met per type: cohort_id-regel, total_n-regel, prioriteit.
- Schema-uitbreiding: source_type, cited_source, observation_type, percentage_qualifier/range, finding_direction, notes.
- Extra domeinen: pathology, diagnostic_accuracy/criteria; prefixes COMP_, CRIT_, PATH_.
- Script verify_quotes.py en validate-checks voor cohorts.json en normalized-pariteit met raw.
