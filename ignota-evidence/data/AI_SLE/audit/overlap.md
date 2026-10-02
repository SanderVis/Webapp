# Overlap AI_SLE

Bron: Cervera2003_EuroLupus (Medicine 2003;82:299-308), alleen deze publicatie verwerkt.

## Binnen de publicatie (geneste cohorten, geen onafhankelijke cohorten)
- `Cervera2003_EuroLupus_C1` (1990-2000, n=1000) is het totaalcohort.
- `..._C1_P1` (1990-1995, n=1000) en `..._C1_P2` (1995-2000, n=840) zijn periodekolommen van dezelfde patienten. Ze zijn `possible_overlap: true`, `overlap_with: [C1]`.
- Tel nooit C1 + P1 + P2 op. P1 en P2 zijn dezelfde patienten (P2 = de 840 die in 1995 nog in de studie zaten), dus ook P1 en P2 onderling niet poolen. Voor totaal-N telt alleen C1 (1000).

## Met andere publicaties (niet in dataset, wel genoemd in de bron)
De bron zegt zelf dat dezelfde Euro-Lupus-cohort eerder is gerapporteerd: ref 11 (baseline, Cervera et al., Medicine 1993), ref 12 (5-jaarsfollow-up, Cervera et al., Medicine 1999), ref 10 (Cervera et al., Lupus 2001;10:892-894, 10-year report). Titels/jaren zoals in de referentielijst van de PDF. De 1990-1995 kolom (P1) komt uit dezelfde patienten als ref 12. Elke toekomstige extractie uit die artikelen moet `possible_overlap: true`, `overlap_with: [Cervera2003_EuroLupus_C1]` krijgen (signalen: zelfde consortium, auteurs, periode, N=1000).
