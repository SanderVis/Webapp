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

## Verwachte features per domein (voor not_reported-beslissing)
Klinisch en lab: zie secties 3–5 van de briefing (koorts, rash, lymfadenopathie, CRP, ESR, ferritine, Hb, leukocyten, trombocyten, ASAT/ALAT, creatinine, ANA, complement, enz.).
