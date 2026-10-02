# Issues VAS_MPA

## Aard van de bronnen
1. De twee PDF's zijn één studie in twee tijdschriften (ARD en Arthritis & Rheumatology; "published simultaneously"). Eén keer geëxtraheerd (ARD). Zie overlap.md.
2. Het is een classificatiecriteria-studie (DCVAS). De MPA-cases zijn door expertpanel bevestigd en comparators zijn een niet-willekeurige mix. Percentages in Table 1 zijn geen populatieprevalenties van MPA in de gewone kliniek (selectie op classificeerbare/evidente gevallen, ANCA-testing is onderdeel van de selectie, geen koorts/rash/artralgie enz. gerapporteerd). Gebruik als beschrijving van "expert-bevestigde MPA bij diagnose", niet als FUO-prevalentie.
3. PMID staat niet in de bronbestanden; `pmid: null`, DOI ingevuld. Niet uit geheugen aangevuld.
4. Supplementary appendices (kandidaat-items, per-item prevalenties 9C/10C/11C/12C, flowchart expertreview) worden genoemd maar zijn niet beschikbaar; daar zou meer MPA-feature-data in kunnen zitten (bv. klinische items, longfibrose, sino-nasaal). Niet geextraheerd.

## Inconsistenties in de bron
5. Maximum eosinofielen >=1x10^9/L bij de 291 MPA-cases: Table 1 zegt 15/291 (5.2%), de tekst zegt "12% vs 6%". 5.2% rondt af naar 5, niet 6. Alleen Table 1 geextraheerd (positive_n/total_n), tekstwaarde niet als observation opgenomen (zou dubbele sleutel geven en is strijdig); beide ARD- en AR-versie bevatten dit. Menselijke check.
6. Samengestelde ANCA-percentages in de tekst (pANCA/MPO 98%, cANCA/PR3 4%) zijn afgerond zonder n/N; consistent met Table 1 maar niet te herleiden naar n. Geen n afgeleid.
7. Pauci-immuun glomerulonefritis 49% (tekst): noemer onduidelijk (alle 291 of alleen gebiopteerde patienten). `total_n: null`, confidence medium.
8. "91% of this group being pANCA positive or MPO-ANCA positive" (Discussion): "this group" lijkt de 404 door inzender gediagnosticeerde MPA-cases van de sensitiviteitsanalyse; niet expliciet. `extraction_confidence: low`, geen n/N. Menselijke check.
9. Table 1 geeft "Maximum serum creatinine, mean" zonder SD; alleen `stat.mean`. Eenheid µmol/L bewaard; mg/dL (1.4) staat in definition/original_text, geen conversie.
10. De detectiemethode van c/pANCA (IF vs ELISA) en cutoffs staan niet in de hoofdtekst.

## Voorstellen voor features.md (nieuwe ids, niet in startset)
EPI_AGE, EPI_SEX_FEMALE, LAB_CREATININE, LAB_EOSINOPHILS (categorisch >=1x10^9/L met cutoff; continue vorm apart), LAB_ANCA_CANCA, LAB_ANCA_PANCA, LAB_ANTI_PR3, LAB_ANTI_MPO, LAB_ANCA_PANCA_OR_MPO (samengesteld), LAB_ANCA_CANCA_OR_PR3 (samengesteld), HIST_PAUCI_IMMUNE_GN (nieuw prefix HIST_ voorgesteld voor histopathologie; domain `laboratory` gekozen omdat er geen histologie-domein is).

## Bewust niet opgenomen
- Comparator-kolom van Table 1 (822 patiënten: GPA, EGPA, PAN, enz.): geen MPA-evidence, heterogene niet-willekeurige mix; ziekte-id onbekend.
- 135 door het expertpanel uitgesloten "MPA"-cases (76%/16%/12%/20%): geen MPA volgens referentiestandaard.
- Sensitiviteit 90.8%, specificiteit 94.2%, AUC, 82.4%/92.5% sensitiviteitsanalyse, criteriagewichten (+6, +3, +3, -3, -1, -4) en drempel >=5: eigenschappen van de criteria, geen prevalenties; en therapie/diagnostische-waarde-regels. Staan in triage-notes.
- Niet-gerapporteerde klinische features (koorts, nierinvolvement, longinvolvement, ...) zijn niet als `not_reported` opgeslagen: features.md verwijst naar briefing-secties die niet beschikbaar zijn, en de bron is geen manifestatiestudie.
