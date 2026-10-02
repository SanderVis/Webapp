# PDF-flow

Waarom: een PDF direct lezen kost veel tokens en gebeurt elke sessie opnieuw. Markdown is kleiner en herbruikbaar.

1. Zoek `<naam>.md` naast `<naam>.pdf`. Bestaat die en is hij nieuwer dan de PDF: lees alleen de `.md`. Klaar.
2. Anders: zet om met de skill `anthropic-skills:pdf-markitdown`, resultaat naast het origineel opslaan als `<naam>.md`. Wijzig of verplaats het origineel nooit.
3. Controleer het resultaat:
   - Vrijwel leeg (minder dan ~100 tekens per pagina): waarschijnlijk een scan zonder tekstlaag. Meld dat de omzetting weinig oplevert en vraag of je de PDF op de gewone manier (met beeld) moet lezen.
   - Duidelijk visuele inhoud (flowcharts, formulieren, figuren, ingewikkelde tabellen) of een rommelige omzetting: meld dat informatie verloren kan zijn en vraag wat je moet doen.
4. Lees daarna alleen de `.md`, en gericht (Grep, offset/limit), niet in één keer helemaal als dat niet nodig is.

Let op: pdf-markitdown zelf raadt omzetten bij korte of visuele PDF's af. Hier geldt bewust "altijd omzetten", omdat dat zo is gekozen. De controle in stap 3 vangt de gevallen op waar het misgaat.
