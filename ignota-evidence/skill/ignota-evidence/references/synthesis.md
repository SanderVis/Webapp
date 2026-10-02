# Synthese

Doel: samenvatten over cohorten heen zonder raw te vervangen.

## Wanneer poolen?
Alleen als: ≥3 onafhankelijke cohorten (geen overlap), vergelijkbare definitie/cutoff/timing/populatie, noemer duidelijk. Anders: alleen range en afzonderlijke cohortwaarden tonen.

## Wat opslaan (synthesized/<domein>.jsonl)
`{disease_id, feature_id, n_studies, n_cohorts, total_N, range, pooled_estimate|null, ci|null, heterogeneity|null, stratification_factors, method, cohort_ids_used, pooled: bool, notes}`.

## Methode
- Proporties: random-effects (bijv. Freeman-Tukey of logit) met heterogeniteit (I², tau²). Rapporteer het ook als de gebruiker er niet naar vraagt.
- Heterogeniteit klinisch relevant (leeftijd, ernst, setting, geografie, definitie, cutoff, periode, behandeling, selectie): stratificeer; pool niet over strata.
- Continue waarden: pool alleen met bronstatistieken in dezelfde vorm; geen omrekening mediaan→gemiddelde.
- Conflict (bijv. 30% vs 70%): beschrijf verklarende verschillen in `notes`, laat beide cohorten staan, kies niet.
- Pooled waarde heeft altijd `cohort_ids_used` zodat terugtraceren naar de bron kan.

## Nooit
Schijnprecisie, pooling met overlappende cohorten, synthese over therapierespons als diagnostisch signaal.
