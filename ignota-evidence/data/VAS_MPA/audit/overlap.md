# Overlap-controle VAS_MPA

## Paren
| A | B | Signalen | Conclusie |
|---|---|---|---|
| SUPPIAH2022_ARD (Ann Rheum Dis 2022;81:321-326, DOI 10.1136/annrheumdis-2021-221796) | SUPPIAH2022_AR (Arthritis Rheumatol 2022;74:400-406, DOI 10.1002/art.41983) | Zelfde auteurs (Suppiah ... Watts), zelfde titel, zelfde DCVAS-studie, zelfde periode (jan 2011-dec 2017), zelfde N (291 MPA / 822 comparators; dev 149+408, val 142+414), identieke Table 1 en tekstpercentages; beide papers vermelden "published simultaneously" | Dezelfde patienten (dubbelpublicatie). Eén keer tellen. Alle observations komen uit de ARD-versie; AR-cohorten zijn alleen als overlap geregistreerd (`possible_overlap: true`). |
| SUPPIAH2022_ARD_C1 (n=291, expert-bevestigde MPA) | SUPPIAH2022_ARD_C2 (n=404, MPA volgens inzendend arts) | Zelfde bron (DCVAS); 269 van de 404 zitten in de 291 (tekst: "269 of 404 of the cases retained the submitting physician diagnosis of MPA") | Niet onafhankelijk; C2 is een ruimer, minder strak gedefinieerd cohort dat C1 grotendeels omvat. Niet samen poolen, noemer niet optellen. |

## Totaal N zonder dubbeltelling
Unieke MPA-patienten met expert-referentiediagnose: 291. Het 404-cohort (C2) is geen aanvulling maar een bovenverzameling (269 overlap met C1; 135 niet bevestigd door expertpanel; 22 extra in C1 via consensus-herclassificatie, dus niet in de 404 met MPA-diagnose van de inzender).

## Overlap met andere publicaties/ziektes (niet te verifieren met deze bronnen)
Beide bronnen zijn afgeleid van DCVAS. Andere DCVAS-classificatiepapers (o.a. GPA/EGPA, in VAS_GPA) gebruiken dezelfde DCVAS-database; MPA-patienten kunnen daar als comparators voorkomen en omgekeerd. Dat is hier niet gecontroleerd (geen andere bronnen). Iedere toekomstige DCVAS-bron moet als `possible_overlap` met SUPPIAH2022_ARD_C1 worden gemarkeerd.
