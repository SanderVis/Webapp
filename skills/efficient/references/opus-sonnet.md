# Plannen met Opus, uitvoeren met Sonnet

Waarom: goed plannen is het moeilijke denkwerk en loont op een sterker model. Uitvoeren van een helder plan kan goedkoper en sneller op Sonnet. Zo betaal je alleen voor Opus waar het iets oplevert.

## Wanneer wel
Taken met meerdere stappen of bestanden, ontwerpkeuzes, of een onduidelijke aanpak.

## Wanneer niet
Kleine, duidelijke taken (een bestand aanpassen, een vraag beantwoorden, een korte zoekactie). Een subagent kost zelf tokens, dus dan direct uitvoeren.

## Werkwijze
1. **Plan:** start een subagent via het Agent-hulpmiddel met `model: "opus"` (bij voorkeur `subagent_type: "Plan"`). Geef de taak en alle context die nodig is mee. Vraag om een beknopt plan: genummerde stappen, betrokken bestanden, risico's. Het plan mag geen uitvoering bevatten.
2. **Toets:** lees het plan kort. Bij grote of onomkeerbare acties legt de gebruiker het plan eerst voor goedkeuring voor.
3. **Uitvoeren:** voer de stappen uit met `model: "sonnet"`. Dat kan via een subagent met `model: "sonnet"`, of zelf als de hoofdsessie al op Sonnet draait. Geef de uitvoerder het plan en alleen de context die hij nodig heeft.
4. **Afronden:** meld kort wat gedaan is. Blijkt het plan niet te kloppen, ga dan terug naar stap 1 in plaats van te improviseren.

## Let op
- De hoofdsessie kan niet van model wisselen. Draai de hoofdsessie bij voorkeur op Sonnet (`/model`), dan gaat alleen het plannen naar Opus.
- Subagenten zien jouw gesprek niet. Geef dus alles mee wat ze nodig hebben.
- Controleer of beide modellen beschikbaar zijn in je abonnement. Zo niet, meld dat en voer het hele werk uit op het beschikbare model.
