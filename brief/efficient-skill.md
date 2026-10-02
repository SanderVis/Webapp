# Brief: Skill `efficient`

_Datum: 2026-10-02_

## Objective
Een skill `efficient` bouwen (met anthropic-skills:skill-creator) waarmee de gebruiker in Claude Code altijd tokenzuinig werkt. De skill staat altijd aan, zet PDF's automatisch om naar markdown voordat ze gelezen worden, onthoudt voorkeuren in een lokaal geheugenbestand en verbetert het proces via een goedkeuringslus. Het probleem: onnodig lange antwoorden, herhaald lezen van bestanden en PDF's die elke sessie opnieuw verwerkt worden kosten tokens en tijd.

## Eisen
### Must-haves
- **Altijd aan, compact:** `SKILL.md` is maximaal ongeveer 40 regels. Details staan in aparte referentiebestanden die alleen worden geladen als ze nodig zijn.
- **Tokenregels:**
  - Antwoorden zijn kort en direct, zonder inleiding, samenvatting of herhaling van de vraag.
  - Eerst zoeken (Grep/Glob), daarna alleen het relevante deel lezen (offset/limit). Niets herlezen wat al in het gesprek staat.
  - Zware zoektaken gaan naar een subagent. Kleine taken niet.
  - Bij lange sessies stelt de skill een samenvatting en nieuwe start voor.
- **Uitzondering uitgebreid antwoord:** bij woorden als "uitgebreid", "leg uit", "volledig" of "stap voor stap" geeft de skill voor die ene beurt een uitgebreid antwoord. Ziet de skill zelf dat het nodig is (uitleg, schrijfwerk, risicovolle beslissingen), dan doet hij dat ook, met één korte melding. Daarna terug naar kort.
- **PDF-flow:**
  - Elke PDF wordt eerst omgezet met anthropic-skills:pdf-markitdown naar `.md` naast het origineel.
  - Een bestaande `.md` die nieuwer is dan de PDF wordt hergebruikt.
  - De ruwe PDF wordt nooit gelezen.
  - Bij een scan zonder tekstlaag meldt de skill dat de omzetting weinig oplevert.
  - Bij ingewikkelde tabellen of afbeeldingen is een uitzondering mogelijk (aanname: de skill meldt het en vraagt wat te doen).
- **Geheugen:** `memory.md` per project, maximaal ongeveer 50 regels. Bij overschrijding stelt de skill voor oude regels samen te voegen of te schrappen. Geen NotebookLM.
- **Verbeterlus:** aan het einde van een sessie stelt de skill maximaal drie regels voor `memory.md` voor. Alleen na goedkeuring van de gebruiker wordt iets toegevoegd.
- **find-skills:** alleen op verzoek of bij de derde herhaling van dezelfde taak. Eén zoekopdracht voorstellen, nooit automatisch installeren.
- **learn:** alleen als vrijwillige modus wanneer de gebruiker iets wil begrijpen. Niet in de standaardflow.

### Nice-to-haves
- De kernregels van de terse-plugin worden overgenomen in de skill.

### Randvoorwaarden
- Taal: Nederlands.
- Gebruiker draait vooral lokaal. In cloudsessies werkt de skill zonder `memory.md` en meldt dat in één regel.
- Naam: `efficient` (aanroepbaar met `/efficient`).
- Toon: zakelijk en direct.

### Buiten scope
- NotebookLM-koppeling.
- Automatisch skills installeren.
- De terse-plugin zelf bundelen of installeren.

## Publiek
Alleen de gebruiker zelf, werkend in Claude Code (lokaal), in het Nederlands. Doel: dat Claude minder tokens gebruikt zonder dat de gebruiker er iets voor hoeft te onthouden.

## Toon en stijl
Zakelijk en direct. Geen inleiding of beleefdheidsfrases, geen herhaling van de vraag. Nederlands. Alleen uitgebreider wanneer de gebruiker erom vraagt of wanneer de skill het nodig acht.

## Wat een fantastisch resultaat is
_(Aanname, door de gebruiker bevestigd.)_ De gebruiker merkt dat antwoorden korter zijn en dat sessies langer meegaan zonder dat hij iets hoeft te onthouden. PDF's worden nooit twee keer omgezet. De gebruiker hoeft nooit om "meer uitleg" te vragen, omdat de skill dat zelf oppikt.

## Definition of done
- [ ] `SKILL.md` is maximaal ongeveer 40 regels en laadt details alleen uit aparte referentiebestanden.
- [ ] Een gegeven PDF wordt omgezet naar `.md` naast het origineel, en de tweede keer wordt die `.md` hergebruikt.
- [ ] Een antwoord op een gewone vraag is korter dan zonder de skill en bevat geen inleiding.
- [ ] Het woord "uitgebreid" of "leg uit" levert voor die ene beurt een uitgebreid antwoord op.
- [ ] `memory.md` blijft onder ongeveer 50 regels en wordt alleen bijgewerkt na goedkeuring van de gebruiker.
- [ ] In een cloudsessie werkt de skill zonder `memory.md` en meldt dat in één regel.

## Risico's en aannames
- Te korte antwoorden kunnen extra vragen veroorzaken. De uitzonderingsregel moet dat opvangen.
- `memory.md` staat per project en is alleen lokaal beschikbaar.
- markitdown verliest soms informatie bij ingewikkelde tabellen en afbeeldingen.
- De terse-plugin (community, Karl Lowenbjer) heeft brede hook-rechten en is een aanbevolen losse installatie.

## Open punten
- Of de gebruiker de terse-plugin daadwerkelijk installeert.
