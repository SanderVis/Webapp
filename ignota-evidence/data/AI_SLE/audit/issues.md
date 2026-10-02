# Issues AI_SLE (Cervera2003_EuroLupus)

## Bron / provenance
- PMID staat niet in de bron (alleen DOI 10.1097/01.md.0000091181.93122.55). `pmid: null` bewust; niet uit geheugen aangevuld. Een mens kan PMID later toevoegen.
- `.txt` (layout) is voor tabellen niet bruikbaar (kolommen door elkaar); tabellen zijn gelezen uit PDF-pagina-afbeeldingen (Tables 1-4 visueel gecontroleerd). Paginanummers = PDF-pagina (form feed) met gedrukt paginanummer tussen haakjes (PDF p.3 = gedrukt 301).
- Table 1 titel zegt "(1999-2000)"; de kolomkop en tekst zeggen 1990-2000. Als typfout in de bron beschouwd.
- Tekst-/tabeldiscrepantie: azathioprine p-waarde 0.01 in tekst, 0.001 in Table 2. P-waarden niet geextraheerd.
- Verwijzingsnummering in de bron lijkt verschoven (tekst noemt "elsewhere9,10", referentie 9 is een Ann Intern Med-review); niet relevant voor de data.
- Tekst noemt "Hypertension 169 (16.9)" en "Urinary infection 169 (16.9)" apart; beide kloppen met Table 3 (toevallig gelijk).
- Table 3 "Infection / Other" 1990-2000: lege cel in de bron -> `not_reported` (zonder waarde); 1990-1995 en 1995-2000 wel gegeven (62, 31).

## Cohortmodel
- Een cohort (n=1000), plus twee periode-subcohorten die dezelfde patienten bevatten (zie overlap.md). Dit was nodig omdat validate.py duplicaten detecteert op (feature_id, cohort_id, timing, cutoff) en `timing` geen kalenderperiode kent.
- Noemers per rij: 1000 / 1000 / 840 (Tables 1-3), 68 / 45 / 23 doden (Table 4, noemer = overledenen, niet cohort-N; staat in `definition`).

## Lage/gemiddelde confidence
- EPI_SURVIVAL_10Y_NEPHROPATHY_AT_ENTRY: medium. Alleen percentages uit tekst (88% vs 94%), groepsgroottes niet gegeven; Figure 2 niet gekwantificeerd.
- EPI_AUTOPSY_DONE: medium. Noemer 68 afgeleid uit de zinscontext, niet expliciet gegeven.
- Alle Table 1 "definition" verwijst naar ref 11 voor detail; die is niet gelezen.

## Voorgestelde nieuwe feature-ids (niet in features.md; aan features.md toe te voegen na akkoord)
Bestaand hergebruikt: SYM_FEVER, LAB_PLATELETS (thrombocytopenia, categorisch, geen cutoff in bron).
Nieuw: SIGN_MALAR_RASH, SIGN_DISCOID_LESIONS, SIGN_SUBACUTE_CUTANEOUS_LESIONS, SYM_PHOTOSENSITIVITY, SIGN_ORAL_ULCERS, SIGN_ARTHRITIS, SIGN_SEROSITIS, SIGN_NEPHROPATHY_ACTIVE, SIGN_NEUROLOGIC_INVOLVEMENT, LAB_HEMOLYTIC_ANEMIA, SIGN_RAYNAUD_PHENOMENON, SIGN_LIVEDO_RETICULARIS, SIGN_THROMBOSIS, SIGN_MYOSITIS;
SIGN_INFECTION_{ANY,URINARY,CUTANEOUS,RESPIRATORY,ABDOMINAL,CNS,OTHER}, SIGN_SEPSIS, SIGN_HYPERTENSION, SIGN_OSTEOPOROSIS, SIGN_GI_BLEEDING, SIGN_CATARACT, SIGN_DIABETES, SIGN_AVASCULAR_NECROSIS, SIGN_RETINOPATHY, SIGN_MALIGNANCY_{ANY,UTERUS,BREAST,NHL,COLON,LUNG,OTHER};
TX_AE_CYTOPENIA_IMMUNOSUPPRESSIVE, TX_NSAID, TX_ANTIMALARIALS, TX_STEROIDS_ORAL, TX_STEROIDS_PULSE, TX_CYCLOPHOSPHAMIDE_ORAL, TX_CYCLOPHOSPHAMIDE_PULSE, TX_AZATHIOPRINE, TX_METHOTREXATE, TX_ANTIAGGREGANTS, TX_ANTICOAGULANTS, TX_HEMODIALYSIS, TX_KIDNEY_TRANSPLANTATION, TX_PLASMAPHERESIS;
EPI_SEX_{FEMALE,MALE}, EPI_ANCESTRY_{WHITE,BLACK,OTHER}, EPI_AGE_AT_PROTOCOL, EPI_COUNTRY_<NAME>, EPI_LOST_TO_FOLLOWUP, EPI_MORTALITY_10Y, EPI_SURVIVAL_10Y, EPI_SURVIVAL_10Y_NEPHROPATHY_AT_ENTRY, EPI_DEATH_SEX_*, EPI_AGE_AT_DEATH, EPI_DISEASE_DURATION_AT_DEATH, EPI_AUTOPSY_DONE, EPI_DEATH_CAUSE_* (zie normalized/epidemiology.jsonl).
Ontbrekende koppeling: ANA, anti-dsDNA, complement, etc. zijn in deze bron niet gerapporteerd (verwijzing naar ref 11); `not_reported` niet aangemaakt (zie skill_feedback).

## Bewust niet geextraheerd
- Table 5 (Petri, Wang, Alarcon) en Table 6 (Abu-Shakra): data van andere studies, tweedehands; haal uit primaire bronnen.
- P-waarden, RR en 95% BI (afgeleide vergelijkingen tussen perioden); jaarlijkse uitval- en sterftetellingen per jaar (tekst); Kaplan-Meier-curves (Fig 1-2, alleen tekstwaarden); 6 patienten met gecombineerde doodsoorzaak (voetnoten, alleen in original_text/definition vermeld); "all cancers diagnosed antemortem"; 8 patienten met immunosuppressiva voor kanker.
- Serologie/immunologie bij entry: niet in deze publicatie (alleen verwezen naar 1993-artikel).
- Imaging/functional/microbiology: geen data in de bron.
