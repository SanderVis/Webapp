# Skill-feedback (AI_SLE, Cervera 2003)

## Onduidelijk of tegenstrijdig
1. **Periodekolommen / geneste cohorten.** Skill zegt "cohorten apart", maar een tabel met 1990-2000, 1990-1995 en 1995-2000 (zelfde patienten) past niet. `timing` is een ziektefase-enum (early/acute/...), geen kalenderperiode. Ik heb subcohorten `_P1`/`_P2` gemaakt met `possible_overlap: true`; dat blaast de overlap-telling op met niet-echte overlap. Voorstel: veld `cohort_type` (primary | period_subset | subgroup) en `parent_cohort_id` in cohort.schema; dashboard telt alleen primary.
2. **Raw vs normalized feature_id.** Schema eist `feature_id` in raw, SKILL zegt dat normalized de gestandaardiseerde ids krijgt. Ik heb in raw het bronlabel (bijv. "Table 1: Malar rash", "Table 3: Infection / Other") als feature_id gebruikt en in normalized het standaard-id plus `source_feature_id`. Dat is nergens beschreven. Gewenst: expliciet veld `feature_label_original` in schema en regel dat raw.feature_id = bronlabel of al standaard-id.
3. **Duplicaatcheck** in validate.py (feature, cohort, timing, cutoff) dwingt unieke labels af; "Other"/"Pulmonary" komen in meerdere hoofdgroepen voor, dus labels met pad nodig. Ook `domain` zit niet in de sleutel.
4. **Noemer per observation.** Table 4 (doodsoorzaken) heeft noemer 68 doden, niet cohort-N. Er is geen veld voor "denominator_population"; ik zette dit in `definition`. Voorstel: `denominator_description`.
5. **Domein vs prefix.** Thrombocytopenia: features.md zegt LAB_PLATELETS, maar de bron rapporteert het als klinische manifestatie in een manifestatietabel (ACR-criterium). Ik koos domain=laboratory. Idem haemolytische anemie. Complicaties/comorbiditeit (infectie, hypertensie, maligniteit) en doodsoorzaken/overleving hebben geen duidelijk domein of prefix; ik gebruikte SIGN_ en EPI_DEATH_CAUSE_/EPI_SURVIVAL_. Voorstel: domein `outcome` (of prefix OUT_) en `complication`.
6. **Behandeling als frequentie.** Domein treatment is beschreven met respons/dosis, maar hier is het enkel "voorgeschreven"-prevalentie. Onduidelijk of dit mag; ik deed het met definitie "prescription frequency, not response". Ook: adverse events (drug-induced cytopenia) -> treatment-domein gekozen.
7. **not_reported-regel** ("alleen als je het expliciet had verwacht (features.md)") maar features.md heeft alleen 5 ids en een verwijzing naar de briefing (niet aanwezig). Ik maakte geen not_reported-records voor ANA/CRP enz. en heb dit alleen in issues/dashboard genoemd; een lege tabelcel (Infection/Other 1990-2000) kreeg wel `not_reported`.
8. **Kwalitatieve en afgeleide percentages.** Percentages die de bron geeft naast n/N heb ik niet als `derived` gemarkeerd; `derived` alleen wanneer wij rekenen. Een regel hierover helpt. Bij "0" zonder % liet ik percentage null.
9. **Land/ancestry.** Er is geen veld voor verdelingen per land; ik maakte per land een EPI_COUNTRY_*-observation. Cohort-schema `country` is een string; `age` en `sex` zijn vrije objecten zonder voorgeschreven keys.
10. **PMID.** Skill zegt PMID/DOI is verplicht, maar de PDF bevat geen PMID. Opgelost met pmid null; zou in SKILL expliciet mogen ("DOI volstaat; PMID alleen als in de bron").
11. `pilot_notes.md` wordt in SKILL genoemd naast issues/skill_feedback; onduidelijk wat waar hoort. `disease_master.json` lijst bevat geen uitleg over verplichte velden.
12. `source_location` voor PDF: PDF-pagina vs gedrukt nummer; ik gaf beide. Wil je dat standaardiseren.
13. `original_text` voor tabelcellen: letterlijk bestaat niet (cel is los van rij). Ik construeerde "Rijlabel: cel [kolomkop]". Regel nodig.
14. Tekstextractie: `-layout` verwerpt tabellen in tweekolomsartikelen; de instructie "gebruik .txt" is dan misleidend. Advies: render pagina's met pdftoppm en lees ze visueel voor tabellen, of voeg dat aan de skill toe. Ook: pdftotext zonder -layout bracht kolommen apart (bruikbaar maar met risico op verschuiving).
15. Nuttig: validate.py valideert cohorts.json niet (ik deed dat handmatig met jsonschema) en controleert geen normalized-vs-raw consistentie, geen controle op ongeldige feature_id-prefix of onbekende ids.

## Zelf bedacht
- Cohortopzet (zie 1), feature-ids (lijst in issues.md), raw-vs-normalized labelgebruik, `definition` voor noemer-uitleg, confidence-niveaus (high voor visueel geverifieerde tabelcellen, medium voor tekst-afgeleide waarden).
- Keuze om Tables 5/6 (andere studies) niet te extraheren en p/RR/BI weg te laten.
- Overlap-notitie voor eerdere rapporten van dezelfde Euro-Lupus-cohort.
- Epidemiology-domein gebruikt voor sterfte en doodsoorzaken.

## Verbetervoorstellen (samengevat)
- cohort_type + parent_cohort_id; observation: `denominator_description`, `feature_label_original`, `period` (vrije tekst) in aanvulling op `timing`.
- features.md uitbreiden of duidelijk maken dat ids per ziekte worden voorgesteld en waar (bijv. `data/<ID>/audit/new_features.md` met vast formaat).
- validate.py: cohort-schema, id-prefix/whitelist, raw/normalized pariteit, percentage-check ook zonder n/N, en de duplicaatsleutel uitbreiden met `domain`.
- Voorbeeld-observation voor een tabelrij en voor een periode-vergelijkingstabel in extraction.md.
