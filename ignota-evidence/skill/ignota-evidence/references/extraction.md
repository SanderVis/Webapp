# Extractieregels per domein

Algemeen: één observation = één feature in één cohort op één timing/cutoff. Kopieer `original_text` letterlijk. `source_location` = tabel/figuur/sectie die je echt hebt geraadpleegd.

## Status
present / absent / not_reported / not_assessed / unclear.
- `absent`: de bron zegt expliciet dat het niet voorkwam (0/N of "none").
- `not_reported`: de bron noemt het niet. Dit vul je alleen in als je de feature expliciet had verwacht (lijst in features.md); sla anders niets op.
- `not_assessed`: de bron zegt dat het niet is onderzocht ("not tested").
- "not recorded" / "not systematically recorded" = `not_reported`. Gebruik `unclear` alleen als de bronformulering echt twee lezingen toelaat.
- Alleen een kwalitatief woord ("common", "frequent") zonder getallen: `present`, `extraction_confidence: low`, geen n/N of percentage.

## Clinical
`positive_n`, `total_n`, `percentage` zoals gerapporteerd, `definition`, `timing`, `severity`. Noemer kan per feature verschillen (bijv. alleen onderzochte patiënten): gebruik de noemer uit de bron, nooit het cohort-N als die niet gegeven is.

## Laboratory
- Continue waarden: bewaar in `stat` de vorm uit de bron (`{n, median, q1, q3}` of `{n, mean, sd}` of `{min,max}`), met `unit`.
- Alleen "verhoogd/verlaagd": `positive_n`/`total_n` + `cutoff`/`reference_range`.
- Geen eenheidsconversie op raw; conversie alleen in normalized met factor en bron van de factor in `audit/units.md`.
- Nooit mediaan→gemiddelde, IQR→SD of range→SD.

## Imaging
`modality`, `anatomy`, `finding`, `distribution`, `severity`, `timing`, n/N. Normaliseer naar een feature_id, bewaar de oorspronkelijke formulering.

## Functional
Test, `unit`, `stat`, abnormal n/N, definitie, timing.

## Microbiology/diagnostics
Test, specimen, timing, n/N positief. Sensitiviteit/specificiteit/PPV/NPV alleen als de bron ze rapporteert, met referentiestandaard.

## Epidemiology
Drie soorten: pathogeen-/ziekte-epidemiologie, patiënt-epidemiologie, blootstelling. Ancestry/etniciteit letterlijk zoals gerapporteerd. Geen biologische of causale conclusies.

## Treatment
Therapie, indicatie, dosis, duur, `response_definition` (zoals de studie), responders/total, tijd tot respons, relapse, follow-up, adverse events. Altijd label `domain: treatment`; nooit gebruiken als diagnostisch bewijs.

## Tijdsfase
early | acute | acute_peak | hyperinflammatory | recovery | chronic | relapse | unspecified. Alleen invullen als de bron de timing noemt; anders `unspecified`.

## Kwaliteit per studie/cohort
design, directheid, representativiteit, sample size, risk-of-bias-indicatoren, extraction_confidence, overlap, volledigheid. Dit is beschrijvend; zet het niet om in een kans.
