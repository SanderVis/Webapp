# Issues, AINF_AOSD (Mahroum2014)

## Source
- Narrative review, 4 pages (PDF page 5 in the txt is only the trailing form feed). No PMID in the source; `pmid` = null, DOI = 10.1016/j.jaut.2014.01.011 (article footer). Nothing was looked up.
- Page numbers in source_location: PDF page (journal page 34-36). Text uses 'e' for en dashes and loses the degree sign (39 C); original_text is copied as in the text layer.

## Design choices
- No own cohorts. All observations use `Mahroum2014_AOSD_review_C0` (sample_size null, possible_overlap true). Cited primary studies are not made into cohorts (task rule). The cited ref is in the extra field `cited_primary_ref`; `notes` is also extra (schema does not forbid extras).
- Therefore `total_n` is null for nearly everything. Exception: RHS 6/50 (Arlet), where n and N are stated in the review text (percentage derived=true). Kong's N=104 comes only from the reference list, so it was NOT used as total_n.
- Raw `feature_id` = source term; normalized `feature_id` = standard/proposed id (`feature_id_raw` kept).
- "Negative in X%" and "normal in X%" features were stored as positive observations of a *_NEGATIVE / *_NORMAL feature (LAB_ANA_NEGATIVE, LAB_RF_NEGATIVE, LAB_BILIRUBIN_NORMAL), not as inverted prevalences of ANA/RF/bilirubin abnormality, to avoid computing 100-x.
- Qualitative statements ("common", "frequent", "rare") = present, confidence low, no n/N.
- Range reported ("30-65%", "20-25%") in `stat` min/max, percentage null.
- "up to 20%" (fever between spikes) and "about 40%" (carpal ankylosis): the first has no percentage (upper bound); the second has percentage 40 with definition noting 'about'.

## Proposed new feature ids (not in features.md)
SYM_FEVER_PERSISTENT, SYM_ARTHRITIS, SYM_ARTHRALGIA, SIGN_RASH_SALMON, SIGN_HEPATIC_INVOLVEMENT, SIGN_FULMINANT_HEPATIC_FAILURE, SIGN_SPLENOMEGALY, SIGN_LYMPHADENOPATHY, SYM_PHARYNGITIS, SIGN_PERICARDITIS, SIGN_PLEURITIS, SIGN_PLEURAL_EFFUSION, SIGN_REACTIVE_HEMOPHAGOCYTIC_SYNDROME, IMG_PULMONARY_INFILTRATE, IMG_XRAY_NONSPECIFIC, IMG_CARPAL_ANKYLOSIS, IMG_TARSAL_CHANGES, IMG_CERVICAL_SPINE_ANKYLOSIS, IMG_HIP_DESTRUCTION, LAB_HB, LAB_HEPATOCELLULAR_ENZYMES, LAB_CHOLESTATIC_ENZYMES, LAB_BILIRUBIN_NORMAL, LAB_ESR, LAB_IMMUNOGLOBULINS, LAB_COAGULATION_ABNORMAL, LAB_FERRITIN, LAB_GLYCOSYLATED_FERRITIN, LAB_ANA_NEGATIVE, LAB_RF_NEGATIVE, LAB_IL6, LAB_TNF, LAB_IFNG, LAB_IL18, LAB_GLK_TCELLS, EPI_INCIDENCE, EPI_SEX_RATIO, EPI_AGE_DISTRIBUTION, EPI_HLA_ASSOCIATION, EXP_STRESSFUL_LIFE_EVENTS, TX_NSAID, TX_GLUCOCORTICOID, TX_METHOTREXATE, TX_ANTI_TNF, TX_ANAKINRA, TX_IVIG.
Existing ids reused: SYM_FEVER, SYM_MYALGIA, LAB_WBC (neutrophilic leukocytosis), LAB_CRP, LAB_PLATELETS (thrombocytosis, categorical).

## Uncertain attributions / extractions
- Laboratory percentages (98, 69, 96, 92, 99): the citation [13] appears after later sentences; whether it covers each figure is inferred (marked "(inferred)").
- Splenomegaly 30-65% cites [15,16]; the review gives no per-study values.
- Ferritin >5x sens 80% / spec 41% (N=49) and glycosylated ferritin 43%/93%: stored as laboratory observations with stat; no reference standard or cutoff in the review. Not prevalences.
- RHS 6/50: review says "6 AOSD patients from a series of 50 patients"; not verified against primary.
- Fulminant hepatic failure "8 patients; four died": case-level count, no denominator, do not use for prevalence.
- Hyphen/page break: the carpal ankylosis sentence spans PDF p.2 columns/page break in the flow text; located on journal p.34-35 boundary (PDF p.2 start).

## Not extracted (and why)
- Infectious triggers (viruses/bacteria): listed as theories, not observations.
- Late-onset case reports (age ~70): case reports.
- Pathology/biopsy findings (skin biopsy, liver biopsy, synovial fluid, effusions): no pathology domain in schema.
- Classification criteria (Yamaguchi, Fautrel, Cush, Calabro, Masson comparison; Table 1; sens/spec 96.2/92.1, 80.6/98.5, 93.5): criterion-derived accuracy from cited primaries, circular, no diagnostic-criteria domain/feature prefix.
- Treatment: canakinumab (juvenile/sJIA, >80%), tocilizumab (children), rituximab (case report), DMARDs/immunosuppressants without data, pulse methylprednisolone recommendation, doses of NSAIDs other than as note. Non-adult-AOSD populations or case report or no data.
- Ferritin correlation with disease activity / predictive of chronic course, pancytopenia as alert sign: no prevalence data.
- Not synthesized: single secondary source, no independent cohorts; synthesis not justified.
