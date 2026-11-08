# Design-Council-Bericht Runde 17

## Prüfumfang und Reproduktion

Geprüft wurde ausschließlich die eingefrorene Revision `f7f1a1f4da527e1c7ff2f1885123c6eb096d3134`. Die PDF `output/pdf/TEST-K31pro-max.pdf` hat den SHA-256-Wert `8dcddc5921345c14338d266e72de07e0f44e85ef7a631e022e0747d7d190004a`; die Hashes der PDF-, Render- und Quelldateien stimmen mit `review/rounds/round17-design/revision.json` überein.

Gelesen wurden: die gerenderte PDF, alle fünfzehn Seitenbilder `page-01.png` bis `page-15.png`, `report_contact.png`, die drei D4RT-Seiten 1, 2 und 6, `compliance/regeln.md`, `compliance/checklist.md`, `report/main.tex`, `report/preamble.tex` sowie `revision.json`, `reproduction.md` und `prompt.md`. Keine anderen Dateien in `review/rounds/`, keine früheren Rohberichte, Scorecards oder Übersichten mit Punktzahlen. Keine Kommunikation mit dem anderen Reviewer; keine Builds, keine Änderungen am Repository.

Die PDF ist A4 (595,28 × 841,89 pt) und hat 15 Seiten: Deckblatt plus 14 nummerierte Seiten. Für Detailprüfungen wurden die gerenderten Seiten in 200/300 dpi lokal vergrößert; die Belegorte beziehen sich auf die PDF-Seiten, gedruckte Seitenzahlen sind in Klammern ergänzt.

## Bewertung D1 bis D6

| Kategorie | Bewertung | Kurzbegründung | Belegorte |
|---|---:|---|---|
| **D1 Typografie** | **9** | 12 pt auf 14,4 pt, klare Hierarchie (22 pt Titel, 14 pt Abschnitte, 12 pt Fließtext und Captions), korrekte deutsche Dezimal- und Tausendersetzung, sauberer Mathematik- und Quellensatz. Keine Zahl-Einheit-Trennung im gerenderten PDF gefunden. Nur optionale Feinheiten: Achsen/Legende von Abbildung 2 mit 15,3 pt größer als der Fließtext; einzelne kurze Trennreste; lange Literatur-URLs dicht, aber vollständig. | PDF S. 2–15; Gleichungen (1)–(10) auf S. 3–8; Literatur S. 11–13; Tabellen 2 und 5 auf S. 7 und 15. |
| **D2 Seiten- und Spaltennutzung** | **8** | Satzspiegel und Seitenbudget stimmen, aber die Float-Platzierung ist materiell fehlerhaft: Tabelle 1 steht zwei Seiten nach ihrem Verweis und unterbricht Abschnitt 3.1; Tabelle 2 erzeugt eine etwa 20 mm kurze rechte Spalte auf S. 6; auf S. 13 ist die rechte Spalte zu rund zwei Dritteln leer. | PDF S. 4 (Tab. 1), S. 6–7 (Tab. 2), S. 13 (Literatur); Verweis auf Tab. 1 auf S. 2, auf Tab. 2/Abb. 2 auf S. 6. |
| **D3 Lesbarkeit und visuelle Führung** | **8** | Zusammenfassung, Überschriften und Absatzfluss sind klar. Zwei Floats zerschneiden jedoch Sätze bzw. trennen den Verweis [19] von seinem Satz; Tabelle 1 steht im falschen Abschnitt. Das ist eine konkrete Führungs- und Verweisschwäche, kein Schönheitsfehler. | PDF S. 4 (Tab. 1 nach Gleichung (5), Text „Für das isolierte …“ darunter); S. 6/7 (Satz „… bei 54 kW“ / „[19]“); S. 7/8 (Satz „… mit“ / „höchstens 1 K/h“). |
| **D4 Abbildungen, Tabellen und visuelle Erklärung** | **9** | Abbildungen 1–3 sind konsistent, farblich zurückhaltend und lesbar; Tabellen 1–5 nutzen Booktabs-Linien, klare Einheiten und die geforderte H1-Fettung. Abbildung 3 steht gestapelt in voller Spaltenbreite, die Legenden sind numerisch und kollidieren nicht sichtbar mit Daten oder Linien. Optional: Abbildung 2 mit zu großer Beschriftung, Abbildung 3 oben mit zu hohem y-Limit; Captions beschreiben eher, als dass sie die Erkenntnis voranstellen. Die Platzierungsfehler werden unter D2/D3 bewertet. | PDF S. 5 (Abb. 1), S. 7 (Tab. 2), S. 8 (Abb. 2), S. 14 (Abb. 3), S. 15 (Tab. 3–5). |
| **D5 Formale Compliance** | **9** | A4, Satzspiegel 26 mm (optischer Randausgleich bis 25,3 mm; 25-mm-Grenze eingehalten), 12 pt/14,4 pt, Times-Klon, anonymes Deckblatt ohne Namen oder Schulangabe, Pflichtaufbau, 10 Haupttextseiten plus 5 Seiten Literatur/Anhang, 25 numerische Quellen mit URL und Abrufdatum, KI-Offenlegung in Anhang A. Ein Installationsschema fehlt, ist laut Aufgabe aber optional. | PDF S. 1 (Deckblatt), S. 2–11 (Haupttext), S. 11–13 (Literatur), S. 14–15 (Anhang); `preamble.tex` (Geometrie, Schrift, 14,4 pt); `compliance/regeln.md` und `checklist.md`. |
| **D6 Direkter D4RT-Vergleich** | **9** | Der Bericht ist typografisch klarer und bei den Tabellen lesbarer als D4RT; D4RT ist bei der visuellen Erklärungsdichte der Abbildungen stärker (Methodenschema, Fotomosaik, dichte Ergebnistabelle). D4RTs US-Letter-Format, 10-pt-Satz und Autorenblock wurden nicht übernommen. Die Float-Unterbrechungen sind kein D6-spezifischer Rückstand; D4RT zeigt auf S. 6 eine vergleichbare Unterbrechung. | D4RT S. 1 (Titel/Abstract/Teaser), S. 2 (Methodenabbildung), S. 6 (Ergebnisfiguren und Tabelle 4) gegen Bericht S. 1–2, 7–8 und 14–15. |

## Materielle Mängel

Die drei Float-Fehler haben eine gemeinsame Ursache: Die `table*`-/`figure*`-Blöcke werden zu früh eingereiht und von LaTeX auf spätere Seiten geschoben. Dadurch unterbrechen sie fremde Abschnitte und erzeugen Spaltenlücken. Die folgenden Korrekturen sind konkret ausführbar und halten 12 pt, 25 mm Rand sowie das Seitenbudget ein.

### M1 — Tabelle 1 steht im falschen Abschnitt (D2/D3)

**Beleg:** Der Verweis „Tabelle 1 trennt Quellenwerte von bewussten Modellannahmen“ steht in Abschnitt 2.1 auf **PDF S. 2 (gedr. 1)**. Die Tabelle selbst steht am Kopf von **PDF S. 4 (gedr. 3)**, also zwei Seiten später. Der Text unter der Tabelle beginnt mit „Für das isolierte, angenommene Beckenvolumen …“ und gehört bereits zu **Abschnitt 3.1** nach Gleichung (5) auf PDF S. 3. Die Tabelle unterbricht damit Abschnitt 3.1, obwohl sie zu Abschnitt 2.1 gehört.

**Korrektur:** Verschiebe den `table*`-Block (main.tex Z. 54–73) vor den Absatz „Tabelle 1 trennt …“ (Z. 50) bzw. an den Kopf von PDF S. 3 und erzwinge `[!t]`. Alternativ: Kürze die Tabelle auf Spaltenbreite, ohne unter 12 pt zu gehen. Prüfe anschließend, dass der Text „Für das isolierte …“ nicht mehr unter Tabelle 1 beginnt, die Tabelle auf S. 2/3 steht und der Haupttext weiterhin höchstens 10 Seiten umfasst. 25-mm-Rand und 12-pt-Satz sind beizubehalten.

### M2 — Tabelle 2 zerschneidet den H8-Absatz und den Verweis [19] (D2/D3)

**Beleg:** Auf **PDF S. 6 (gedr. 5)** endet die rechte Spalte mit „… entsprechend dem HAW-Beispiel 3 kW bei 54 kW“. Auf **PDF S. 7 (gedr. 6)** steht am Kopf Tabelle 2; der Text unter der Tabelle beginnt mit „[19]. Einschließlich Kältemaschinen …“. Der Verweis [19] ist damit durch die Tabelle von seinem Satz getrennt. Zugleich endet die rechte Spalte auf S. 6 etwa 20 mm höher als die linke Spalte (666 pt gegenüber 724 pt), weil der Satz nicht fortgesetzt wird.

**Korrektur:** Verschiebe den `table*`-Block (main.tex Z. 159–164) hinter den Absatz „Der Hilfsstrom der Absorptionsstufe …“ (Z. 177) oder vor den H8-Absatz (Z. 175), sodass „… bei 54 kW [19]“ nicht durch die Tabelle getrennt wird; setze `[!t]` bzw. `[!b]` und prüfe die Spaltenfüllung auf PDF S. 6. Die Tabelle bleibt in Abschnitt 3.3, muss aber nicht unmittelbar nach ihrem ersten Verweis stehen. 12 pt, 25 mm Rand und 10 Haupttextseiten sind einzuhalten.

### M3 — Abbildung 2 zerschneidet Abschnitt 4.1 (D2/D3)

**Beleg:** Auf **PDF S. 7 (gedr. 6)** endet die rechte Spalte mit „… vom gemessenen Ausgangswert mit“. Auf **PDF S. 8 (gedr. 7)** steht am Kopf Abbildung 2; der Text unter der Abbildung beginnt mit „höchstens 1 K/h.“. Die Abbildung zerschneidet damit den Satz „Die geplante Inbetriebnahme senkt … mit höchstens 1 K/h“ in Abschnitt 4.1. Ihr Verweis steht auf **PDF S. 6** („Tabelle 2 und Abbildung 2 zeigen diesen Unterschied“), also zwei Seiten vorher; die Abbildung gehört zu Abschnitt 3.3.

**Korrektur:** Setze Abbildung 2 auf `\columnwidth` mit 12–13 pt Achsen- und Legendentext und platziere sie am Ende von Abschnitt 3.3 vor Abschnitt 4 (main.tex Z. 166–171 vor Z. 181); alternativ `[!b]` auf PDF S. 7. Prüfe, dass der Satz „… mit höchstens 1 K/h“ nicht zerschnitten wird, die Abbildung nicht in Abschnitt 4.1 steht und PDF S. 8 nicht überläuft. Die Verkleinerung behebt zugleich die zu große 15,3-pt-Beschriftung; 12 pt dürfen nicht unterschritten werden.

### M4 — Letzte Literaturseite ist unbalanciert (D2)

**Beleg:** Auf **PDF S. 13 (gedr. 12)** ist die linke Spalte mit den Einträgen [16]–[23] bis etwa 738 pt gefüllt. Die rechte Spalte enthält nur den Schluss von [23], [24] und [25] und endet bei etwa 280 pt; rund zwei Drittel der rechten Spalte bleiben leer. Das ist eine sichtbare Spaltenungleichheit am Ende des Literaturverzeichnisses.

**Korrektur:** Füge `\balance` nach dem Literaturverzeichnis (main.tex Z. 272, vor `\clearpage` in Z. 275) ein; das `balance`-Paket ist in `preamble.tex` Z. 13 bereits geladen. Prüfe, dass PDF S. 13 beide Spalten gleichmäßig füllt und die 5-Seiten-Grenze für Literatur plus Anhang (PDF S. 11–15) eingehalten bleibt. Falls `\balance` die Description-Liste nicht ausreichend balanciert, ist das Literaturverzeichnis auf der letzten Seite manuell zu entlasten, ohne die Quellen zu kürzen.

## Optionale Verbesserungen

Diese Punkte sind keine materiellen Mängel und senken die Bewertung nicht:

1. **Abbildung 2:** Achsen- und Legendentexte von 15,3 pt auf 12–13 pt angleichen; die Abbildung wirkt dadurch weniger dominant gegenüber Caption und Fließtext. Die vorgeschlagene Spaltenbreite aus M3 erledigt das mit.
2. **Abbildung 3, oberes Histogramm:** Das y-Limit von 600 bei einem Maximum von etwa 430 ist großzügig; 450–500 würden die Verteilung besser ausnutzen. Die Legende steht in einem leeren Bereich und ist lesbar; eine weiße, undurchsichtige Legendenfläche ist nicht zwingend, könnte aber die Linienführung noch beruhigen.
3. **Abbildung 1:** Achsenbeschriftung „Kühlleistung in MW, Symlog“ besser als „Kühlleistung in MW (Symlog-Skala)“. Die Symlog-Erklärung im Caption ist vorhanden.
4. **Captions:** D4RT zeigt vor den Details eine Erkenntnis („D4RT demonstrates …“). Die Captions von Abbildung 2 und 3 könnten den Satz „H2 ist günstiger, H1 ist die robustere Variante“ bzw. „Die p90-Linie liegt außerhalb der Masse“ voranstellen. Rein optional.
5. **Quelltexthärtung Zahl-Einheit:** Die Behauptung in Befund 1, alle literalen Zahl-Einheit-Verbindungen seien geschützt, ist im Quelltext nicht vollständig. In `main.tex` stehen u. a. `138 €/MWh` (Z. 100), `0,50 €/m³`, `15 €/kW`, `500 €/kW`, `120 €/kW`, `80 €/kW`, `250 €/kW`, `179 €/MWh`, `363 g/kWh` (Z. 149), `1,2 m/s` (Z. 128), `2 m/s` (Z. 149) und `9,8 kWh/L` (Z. 198) mit normalen Leerzeichen. Ein Wort-/Zeilen-Scan der gerenderten PDF fand aktuell keine Trennung von Zahl und Einheit; die sichtbare Fassung ist also sauber. Für zukünftige Umbrüche wären `~` bzw. `\mbox{}` die robustere Lösung. Keine Abwertung, da die PDF sauber ist.
6. **Tabellen 1 und 2, erste Spalte:** „Trocken- und feuchte Annäherung“ bricht in Tabelle 1 um; „Kühlleistung (Wärmer entzug)“ hypheniert in Tabelle 2 als „Wärmeent-zug“. Eine geringfügig breitere erste Spalte oder eine kürzere Zeilenbeschriftung würde das beruhigen; 12 pt sind beizubehalten.
7. **PDF S. 15:** Die Tabellen 3–5 stehen am Kopf, der untere Seitenbereich bleibt frei. Das ist als letzte Anhangseite vertretbar; eine gleichmäßigere vertikale Verteilung wäre rein ästhetisch.
8. **Installationsschema:** Fehlt weiterhin. Die Aufgabe stellt es optional; bei 12 pt und im vorhandenen 10-Seiten-Budget wäre es nur mit Kürzungen möglich. Kein Abzug.

## Zu den 10er-Wertungen

Es wurde keine Kategorie mit 10 bewertet. Für D1, D4, D5 und D6 wurden die typischen Fehlerquellen geprüft: Randmaß und optischer Randausgleich, Schriftgrößen und Grundlinienraster, Zahl-Einheit-Trennung, Tabellenlinien und Spaltenausrichtung, Vollständigkeit der drei NIST-URLs, H1-Fettung, Symlog-Erklärung, Seitenbudget 10 + 5, Anonymität, Quellenform und KI-Offenlegung. Die verbleibenden Punkte sind entweder optional (Abbildung 2/3, Captions, Quelltexthärtung) oder liegen in den materiellen D2/D3-Mängeln M1–M4. Ein 10er wäre erst nach deren Beseitigung und ohne die optionalen Punkte vertretbar.

## Abschließendes Urteil

**Die Design-Stoppregel ist nicht erfüllt.** D2 und D3 liegen mit 8 unter der geforderten 9; die materiellen Mängel M1–M4 sind konkret belegt und behebbar. Der Bericht ist nahe an der Stoppregel: Typografie, Tabellen, Abbildungen, formale Compliance und der D4RT-Vergleich erreichen 9. Nach einer gezielten Float- und Balance-Runde mit den oben genannten Korrekturen und einer erneuten Sichtprüfung der PDF-Seiten 4, 6–8 und 13 sind 9er-Werte in allen Kategorien plausibel. Bis dahin keine Freigabe für das technische Testpaket.
