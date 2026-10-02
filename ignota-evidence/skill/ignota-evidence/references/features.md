# Feature-ids en synoniemen (startset, uitbreiden per ziekte)

Prefixen: SYM_ (symptoom), SIGN_ (lichamelijk teken), LAB_, MICRO_, IMG_, FUNC_, EXP_ (blootstelling), EPI_, TX_.
Een nieuwe feature_id toevoegen: zoek eerst of er al een synoniem bestaat; leg nieuwe ids vast onderaan dit bestand met synoniemen.

| feature_id | synoniemen |
|---|---|
| LAB_PLATELETS | platelet count, platelet level, thrombocyte count, thrombocytes, thrombocytopenia, low platelets, decreased platelet count |
| LAB_WBC | white blood cell count, WBC, leukocyte count, white cell count, leukopenia, leukocytosis |
| LAB_CRP | C-reactive protein, CRP, C reactive protein, acute phase protein |
| SYM_FEVER | fever, pyrexia, febrile, temperature elevation |
| SYM_MYALGIA | myalgia, muscle pain, muscular pain |

Let op: "thrombocytopenia" (categorisch, met cutoff) en "platelet count" (continu) zijn verschillende observationtypes onder dezelfde feature; bewaar beide vormen, vermeng ze niet.

Prefixen: SYM_, SIGN_, LAB_, MICRO_, IMG_, FUNC_, EXP_, EPI_, TX_, HIST_ (pathologie), CRIT_ (criteria/diagnostische accuracy), COMP_ (complicatie), OUT_ (uitkomst).

## Verwachte features (alleen voor `not_reported`, en alleen bij primaire cohorten)
- Symptomen: koorts, rillingen, nachtzweten, gewichtsverlies, vermoeidheid, malaise, anorexie, hoofdpijn, myalgie, artralgie, artritis, rug-/thoracale/abdominale pijn, misselijkheid/braken, diarree, hoesten, dyspneu, hemoptoë, verwardheid, nekstijfheid, insulten.
- Tekenen: rash, purpura/petechiën, urticaria, erythema nodosum, lymfadenopathie, spleno-/hepatomegalie, icterus, oedeem, orale ulcera, Raynaud, digitale ulcera, serositis.
- Lab: CRP, ESR, ferritine, fibrinogeen, D-dimeer, procalcitonine, Hb, leukocyten, neutrofielen, lymfocyten, trombocyten, ASAT, ALAT, ALP, GGT, bilirubine, albumine, creatinine, proteïnurie, hematurie, ANA, anti-dsDNA, C3, C4, ANCA, RF, anti-CCP, CK, LDH.
Een feature uit deze lijst die een primair cohort niet noemt: geen record, tenzij het cohort expliciet zegt dat ze niet is gemeten (`not_assessed`) of de cel leeg/NR is (`not_reported`). Bij reviews: nooit `not_reported`.
