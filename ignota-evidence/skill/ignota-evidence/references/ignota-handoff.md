# Overdracht naar Ignota

Deze skill schrijft **niet** direct in de Ignota-kennisbank. Je maakt een voorstel; de gebruiker keurt goed; wijziging verloopt via de skill `ignota-kennisbank` (validatie, build, regressietests, changelog).

## Voorstelbestand
`data/<ID>/synthesized/ignota_proposal.md`, per feature:
- entiteit en feature (Ignota-id indien bekend)
- voorgestelde frequentie in de ziekte met range en onderliggende cohorten (N, studies)
- populatie, tijdsfase, definitie/cutoff
- evidence quality, heterogeniteit, onzekerheid
- vergelijking met de huidige Ignota-waarde (indien opgegeven door de gebruiker)
- bronnen (PMID/DOI + bronlocatie)

## Let op
- Frequentie P(feature|ziekte) is niet dezelfde grootheid als een likelihood ratio; LR vereist ook de frequentie in de vergelijkingsgroep. Zeg het expliciet als die ontbreekt en verzin hem niet.
- Gecorreleerde features (koorts, CRP, BSE, fibrinogeen) niet als onafhankelijk markeren.
- Een prior volgt uit epidemiologie (incidentie, populatie, blootstelling), niet uit cohortfrequenties.
- Open vraag voor de gebruiker: formaat van de Ignota-kennisbank (zie de skill `ignota-kennisbank`) en welke mapping van feature_ids naar Ignota-ids geldt.
