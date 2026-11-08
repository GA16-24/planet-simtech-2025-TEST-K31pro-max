# Design-Council-Bericht Runde 19 — TEST-K31pro-max

## Prüfgrundlage

- **Revision:** `40f26be1ff1158d527492ef4913dbeca25d86f30`; `git rev-parse HEAD` bestätigt diesen Commit. Die 272 in `review/rounds/round19-design/revision.json` gelisteten Dateien wurden per SHA-256 geprüft; alle Hashes stimmen. Der PDF-Hash `c6c069c853e8aa1d97333dc93a282ec91f6fcbc6837b8867e55e708b0313d291` stimmt mit `reproduction.md` überein.
- **PDF:** `output/pdf/TEST-K31pro-max.pdf`, 15 Seiten, A4 595,28 × 841,89 pt, 130.490 Bytes. Keine Builds, keine Dateiänderungen, read-only.
- **Sichtung:** Kontaktübersicht `report_contact.png`, alle 15 Seiten `page-01.png`–`page-15.png`, die drei D4RT-Seiten `d4rt_page01/02/06.png`. Zusätzlich Geometrie-, Schriftgrößen- und Textprüfungen mit `pdfinfo`, `pdftotext`, `pdftohtml` und Pixelmessungen an den Renderbildern.
- **Abgrenzung:** Bewertet werden nur D1–D6 und nur die Gestaltung/formale Umsetzung. Wissenschaftliches Modell, Physik, Rechenwerte, Präsentation, Video und Finaldateien sind nicht Gegenstand. Offizielle Team-ID, Rechtefreigabe, menschliche Fachprüfung und Einreichung sind menschliche Restaufgaben und senken die Bewertung nicht.
- **Keine früheren Rohberichte, Scorecards oder Übersichten mit Punktzahlen gelesen; keine Kommunikation mit dem anderen Reviewer.** Es kam zu keiner Exposition mit früheren Einreichungen oder Lösungen.

## 1. Bewertung D1–D6

| Kategorie | Bewertung | Kurzbegründung | Beleg |
|---|---:|---|---|
| **D1 Typografie** | **8** | 12-pt-Times-Satz mit 14,4 pt Durchschuss, klare 14/12-pt-Hierarchie, Captions und Tabellen 12 pt. Aber: Trennfehler „Antriebsen-ergie“ (S. 2), Spaltenbruch „Mit Q̇ in / MW folgt“ (S. 3), auffällig weite Wortabstände (S. 2: Median 3,7 pt, p90 5,9 pt, Max 8,9 pt), NIST-URL-Block über den Spaltenumbruch (S. 11) und Zahlenformat-Ausreißer „1053,3/2152,5“ statt „1.053,3/2.152,5“ (S. 14 vs. S. 2/9) sowie „4195,14“ ohne Tausenderpunkt. | PDF-S. 2, 3, 11, 14; `report/main.tex` Z. 269/276 |
| **D2 Seiten- und Spaltennutzung** | **7** | Satzspiegel (158 mm, zwei 75-mm-Spalten, 8 mm Zwischenraum) und Seitenbudget (10 Haupttextseiten, 5 Seiten Literatur + Anhang) stimmen. Aber PDF-S. 13 ist zu etwa drei Vierteln leer (links 6 Zeilen, rechts 17 Zeilen); S. 14 hat rechts 55 mm Leerraum; S. 2 endet die rechte Spalte 16 mm über der linken. | PDF-S. 13, 14, 2; Kontaktübersicht |
| **D3 Lesbarkeit und visuelle Führung** | **8** | Zusammenfassung einspaltig, kürzer als eine Seite, endet vor Abschnitt 1. Klare Numerierung, numerische Verweise, guter Absatzfluss. Aber Tabelle 2 erscheint erst auf S. 8, nach dem Beginn von Abschnitt 4 auf S. 7 und drei Seiten nach ihrem Verweis auf S. 5; der Abbildung-3-Verweis auf S. 9 nennt nicht „Anhang B“; der H3–H7-Absatz auf S. 7 ist ein langer Block. | PDF-S. 2, 5, 7, 8, 9, 14 |
| **D4 Abbildungen, Tabellen, visuelle Erklärung** | **8** | Abbildungen 1–3 sind mit 12,0–12,7 pt effektiver Schrift lesbar, Captions 12 pt und erklärend, Booktabs sauber, H1 in Tabellen 2 und 5 fett. Aber: Tabellen-2-Zeilenumbruch „Kühlleistung (Wärmeent-/zug)“ (S. 8), Tabellen-4-Kostenkolonnen nur mit „Mio. €/Mrd. €“ ohne Größenbezeichnung (S. 15), Tabellen-3-Header „%/Mrd. €“ knapp, Abb.-3-Referenzlinien-Legende gedrängt (S. 14), Abb.-2-Legende direkt unter der Achsenbeschriftung (S. 7). | PDF-S. 5, 7, 8, 14, 15 |
| **D5 Formale Compliance** | **9** | A4, Tintenrand links/rechts 25,8 mm, oben 26,0 mm, Fuß 27,4 mm; Fließtext 12 pt/14,4 pt; Tabellen, Captions und Grafiktext ≥ 12 pt; anonymes Deckblatt und Metadaten ohne Autor; Pflichtaufbau; 10 Haupttextseiten; 5 Seiten Literatur + Anhang; Seitenzahlen; 25 numerische Quellen mit vollständigen URLs und Abrufdatum; KI-Offenlegung. Kein formaler Verstoß gefunden. | PDF-S. 1–15; `pdfinfo`; `report/preamble.tex` |
| **D6 Direkter D4RT-Vergleich** | **8** | Zweispaltiger Times-Satz, numerische Verweise, erklärende Captions und Booktabs folgen dem D4RT-Maßstab. D4RT S. 1, 2 und 6 sind jedoch dichter und ohne Leerseiten; unsere S. 13 und die Tabellenumschläge bleiben sichtbar zurück. A4, 26 mm Rand und 12 pt werden zu Recht nicht durch D4RTs US Letter/10 pt ersetzt. | D4RT S. 1, 2, 6 vs. PDF-S. 5, 7, 13, 14 |

## 2. Prüfung der im Auftrag genannten sieben Punkte

1. **Tabelle 1 / Tabelle 2 / HAW-Verweis:** Tabelle 1 steht auf PDF-S. 3 im Umfeld von Abschnitt 2.1; das ist im Wesentlichen geschlossen. Tabelle 2 steht auf PDF-S. 8 und damit weiterhin erst nach H2, H8 und H3 — zusätzlich erst nach dem Beginn von Abschnitt 4 auf PDF-S. 7. Der HAW-Verweis bleibt im H8-Absatz (PDF-S. 6). **Punkt 1 ist nur teilweise geschlossen.**
2. **Abbildung 2:** Die Abbildung steht auf PDF-S. 7 unten links, nach dem H3-Absatz und vor Abschnitt 4 (der rechts oben beginnt). Sie nutzt 90 % der Spaltenbreite; die effektive Grafikschrift misst 12,7 pt, die Caption 12 pt. Die linke Spalte ist bis 260,7 mm gefüllt; die frühere Lücke ist geschlossen. **Punkt 2 ist geschlossen.**
3. **Quellen 19–22 / 23–25 auf PDF-S. 13:** Die im Auftrag genannte Verteilung ist im gerenderten PDF **nicht vorhanden**. [19]–[21] stehen bereits auf PDF-S. 12, [22] beginnt dort und endet mit sechs Zeilen auf PDF-S. 13 links. Rechts stehen [23]–[25]. Die linke Spalte endet bei 56,2 mm, die rechte bei 112,7 mm; der Satzspiegel reicht bis 263 mm. Damit bleiben unter der rechten Spalte rund 150 mm leer; die Seite ist zu etwa 25 % gefüllt. Die verworfene `\balance`-Anweisung hat keine tragfähige Balance hinterlassen. **Punkt 3 ist nicht geschlossen.**
4. **Zahl-Einheit-Trennung:** Der `pdftotext -raw`-Scan findet nur die Achsenlabels von Abbildung 3 („0 1000 2000“/„MW“ und „5 10“/„Mrd. €“) als Zahl-Einheit-Zeilenumbruch; außerhalb der Achsenbilder keine Trennung. **Punkt 4 hält dem PDF-Scan stand.** Auffällig ist nur, dass einige Quellpaare (z. B. „165 km²“, „12 m“, „877,8 MW“, „8.760 Stunden“, „3 kW/54 kW“, „10.000 m³“, „48 Stunden“) nicht mit `~` gebunden sind; im aktuellen Render brechen sie nicht. Das ist eine Robustheits-, keine aktuelle Renderabweichung.
5. **Kapazitätslegende zwischen den Histogrammen:** Die drei Einträge überdecken keine Balken, Referenzlinien oder Achsentext; sie sind bei 12 pt lesbar. Allerdings stehen „877,8“ und „1053,3“ sehr eng, die Legendensymbole sind nicht an die Referenzlinien ausgerichtet, und die Zuordnung erfolgt nur über Farbe/Strichart. **Punkt 5 ist ohne Kollision geschlossen, mit Lesbarkeitsvorbehalt.**
6. **NIST-URLs / H1 fett / Symlog / Installationsschema:** Alle drei NIST-Abfrage-URLs stehen vollständig im gedruckten Eintrag [4] (PDF-S. 11); die erste läuft über den Spaltenumbruch. H1 ist in Tabellen 2 und 5 fett. Die Symlog-Achse und ihr linearer Bereich bis 1 MW sind in der Abb.-1-Caption erklärt. Ein Installationsschema fehlt weiterhin; die Aufgabe nennt es optional. **Punkt 6 ist geschlossen; das Schema bleibt optional.**
7. **Zahlenformat / Anhang A / Anhang B:** Dezimalkomma und Tausenderpunkt sind überwiegend umgesetzt; negative Werte stehen im Mathematikmodus (z. B. „−5,93 Minuten“, Tabelle 3). Anhang A steht im Blocksatz auf PDF-S. 14 links; Anhang B steht mit Abbildung 3 auf PDF-S. 14 rechts und den Tabellen 3–5 auf PDF-S. 15. Ausnahmen: „1053,3“ und „2152,5“ in Abb.-3-Caption/Grafik statt „1.053,3“/„2.152,5“, und „4195,14“ ohne Tausenderpunkt. **Punkt 7 ist überwiegend, aber nicht vollständig geschlossen.**

## 3. Materielle Mängel

### M1 — PDF-Seite 13 ist fast leer (D2, stopprelevant)

**Beleg:** PDF-S. 13 (gedruckte S. 12). Linke Spalte: nur der sechszeilige Schluss von [22], Ende bei 56,2 mm. Rechte Spalte: [23]–[25], Ende bei 112,7 mm. Satzspiegel bis 263 mm; rund 150 mm Leerraum unter der rechten Spalte; die Seite ist zu etwa 25 % gefüllt. In der Kontaktübersicht ist die Seite als fast weiße Fläche sofort sichtbar.

**Ursache:** `report/main.tex` Z. 269 (`\newpage` vor [23]) und Z. 276 (`\clearpage` vor Anhang A). Der erzwungene Umbruch beendet die linke Spalte nach [22] und schiebt [23]–[25] in die rechte Spalte; der anschließende `\clearpage` beendet die Seite.

**Korrektur:** Den `\newpage` vor [23] und den `\clearpage` vor Anhang A entfernen und Anhang A nach [25] auf PDF-S. 13 beginnen lassen. Dann füllen die Restliteratur und Anhang A/B die Seite; das 5-Seiten-Budget (S. 10–13) bleibt eingehalten, die Schrift bleibt 12 pt, die Ränder bleiben 26 mm. Falls Anhang A zwingend auf einer neuen Seite beginnen soll, muss die Literatur um mindestens 23 Zeilen gekürzt werden (z. B. ein gemeinsamer Abrufvermerk für alle Quellen oder ein kompakterer, weiterhin 12-pt-URL-Satz), sonst bleibt die Seite leer. Nach dem Umbau mit `pdftotext`/Render prüfen, dass S. 13 nicht wieder fast leer ist.

### M2 — Tabelle 2 steht nach dem Beginn von Abschnitt 4 (D3/D4, stopprelevant)

**Beleg:** Der Verweis steht auf PDF-S. 5 (gedruckte S. 4), Abschnitt 3.3, rechte Spalte: „Tabelle 2 und Abbildung 2 zeigen diesen Unterschied.“ Die Tabelle steht auf PDF-S. 8 (gedruckte S. 7) oben. Auf PDF-S. 7 beginnt rechts bereits „4. Betrieb, Standort und Diskussion“ mit 4.1, 4.2 und Gleichung (10). Die Tabelle erscheint damit drei Seiten nach ihrem Verweis und mitten in Abschnitt 4, obwohl sie zu Abschnitt 3.3 gehört.

**Korrektur:** Den `table*`-Block (`report/main.tex` Z. 167–172) hinter den Absatz verschieben, der Tabelle 2 zuerst nennt (Z. 153–155, vor dem H2-Absatz). Neu kompilieren und prüfen, dass die Tabelle auf PDF-S. 6 oder 7 **vor** Abschnitt 4 steht und die Seitenzahl 15 nicht überschreitet. Falls der Float dann noch zu spät landet, am Ende von Abschnitt 3.3 einen zweiten Verweis („Tabelle 2 fasst … zusammen“) ergänzen; keine Float-Experimente ohne diesen konkreten Mangel.

### M3 — Tabelle 4 nennt die Kostenkolonnen nicht (D4, stopprelevant)

**Beleg:** PDF-S. 15 (gedruckte S. 14), linke Spalte unten: Kopfzeile „Anteil | Q | P_el | Mio. € | Mrd. €“. Die Caption erklärt Q und P_el, aber nicht die beiden Kostenkolonnen. Ein Leser sieht „1.595“ und „4,136“ für 100 %, ohne dass die Spalten als Investition und Barwert benannt sind.

**Korrektur:** Die letzten beiden Header auf „Investition in Mio. €“ und „Barwert in Mrd. €“ ändern, ggf. zweizeilig mit `\shortstack`; die Caption um „Investition in Mio. €, Barwert in Mrd. €“ ergänzen. Bei 12 pt und der 79-mm-Spalte prüfen, dass die Header nicht überlaufen. Tabelle 3 analog: „%“ → „Änderung in %“, „Mrd. €“ → „Barwert in Mrd. €“. Tabellenlinien und Schriftgröße bleiben unverändert.

### M4 — Zahlenformat-Ausreißer (D1/D4, bewertungsrelevant)

**Beleg:** PDF-S. 14, Abbildung 3: Caption und Grafiklabels „1053,3“ und „2152,5“; auf PDF-S. 2 und 9 steht dagegen „2.152,5“ und „1.053,3“. PDF-S. 3 (Gleichung/Text) und PDF-S. 14 (Handrechnung): „4195,14“ ohne Tausenderpunkt, während der Bericht sonst „1.595“, „2.152,5“, „25.000“ setzt.

**Korrektur:** Die Abb.-3-Caption auf „1.053,3“ und „2.152,5“ ändern; die Grafiklabels mit einem deutschen Tausenderformat neu erzeugen. „4195,14“ als „4.195,14“ setzen oder als bewusste Ausnahme für den NIST-Stoffwert dokumentieren. Danach alle Zahlen mit einem kurzen Scan auf Tausenderpunkt/Dezimalkomma prüfen; 12 pt beibehalten.

### M5 — Tabellen-2-Zeilenumbruch „Wärmeent-/zug“ (D4, bewertungsrelevant)

**Beleg:** PDF-S. 8, Tabelle 2: „Kühlleistung (Wärmeent-“ / „zug)“ und „Davon Wärmeabgabe an“ / „Luft“. Die erste Spalte ist mit 46 mm zu schmal; die Zellen wirken zudem teilweise im Blocksatz, sodass „Davon Wärmeabgabe an“ große Wortabstände bekommt.

**Korrektur:** Die erste Spalte auf 54 mm, die dritte auf 53 mm setzen (54 + 32 + 53 = 139 mm plus 12,7 mm Tabellenabstand = 151,7 mm; passt in 158 mm), die Zellen mit `\raggedright` setzen und „Davon Wärmeabgabe an Luft“ zu „Wärmeabgabe an Luft“ kürzen. Prüfen, dass kein Zeilenumbruch mit einem vierzeichenlangen Rest wie „zug)“ bleibt.

### M6 — Trennfehler „Antriebsen-ergie“ (D1, bewertungsrelevant)

**Beleg:** PDF-S. 2, linke Spalte, zweiter Absatz: „Einschließlich Antriebsen-“ / „ergie würden 967,2 MW …“. Die korrekte Trennung wäre „Antriebs-energie“ bzw. „An-triebs-ener-gie“.

**Korrektur:** `\hyphenation{An-triebs-ener-gie}` in die Präambel aufnehmen oder die Stelle umformulieren („Einschließlich der Antriebsenergie“); neu kompilieren und PDF-S. 2 prüfen.

### M7 — Spaltenbruch „Mit Q̇ in / MW folgt“ (D1, bewertungsrelevant)

**Beleg:** PDF-S. 3: Die linke Spalte endet mit „Mit Q̇ in“; die rechte Spalte beginnt mit „MW folgt“, danach folgt Gleichung (2). Die einleitende Formelzeile wird über den Spaltenumbruch zerrissen.

**Korrektur:** Die Einleitung und Gleichung (2) in eine `\samepage`-Gruppe setzen oder mit `\needspace{5\baselineskip}` zusammenhalten; alternativ die Einleitung umformulieren, sodass sie nicht direkt vor dem Umbruch endet. Neu kompilieren und prüfen, dass „Mit Q̇ in MW folgt“ nicht mehr getrennt ist.

### M8 — Abbildung-3-Verweis ohne „Anhang B“ (D3, bewertungsrelevant)

**Beleg:** PDF-S. 9, Abschnitt 4.4: „… und sind in Abbildung 3 dargestellt.“ Die Abbildung steht auf PDF-S. 14 in Anhang B.

**Korrektur:** „… und sind in Anhang B, Abbildung 3 dargestellt.“ Keine Layoutänderung nötig.

## 4. Optionale Verbesserungen

- **PDF-S. 14/15:** Der 55-mm-Leerraum am Fuß der rechten Spalte von S. 14 und die 85–101 mm am Fuß von S. 15 sind sichtbar. Prüfen, ob Tabelle 4 (Teilströme) mit Caption in die freie rechte Spalte von S. 14 passt, wenn Abbildung 3 auf 0,95 der Spaltenbreite gesetzt wird; die effektive Schrift muss ≥ 12 pt bleiben. Wenn es nicht passt, ist der Leerraum bei erzwungenem Anhangumbruch hinzunehmen; keine Schrift verkleinern.
- **PDF-S. 2:** Die rechte Spalte endet 15,9 mm über der linken (247,1 mm vs. 262,3 mm). Ein `\flushbottom` oder eine angepasste Umbruchstelle könnte den Fuß beruhigen; auf Overfull-Boxes achten.
- **Wortabstände:** Die weiten Zeilen auf S. 2 (Median 3,7 pt, p90 5,9 pt, Max 8,9 pt bei 12 pt) könnten durch Feinjustage von `\tolerance`/`\emergencystretch` und gezielte Trennungen etwas ruhiger werden. 12 pt und 26 mm Rand bleiben unverändert.
- **NIST-URL-Block:** Die drei URLs sind vollständig, aber der erste läuft über den Spaltenumbruch auf S. 11 und ist im romanischen 12-pt-Satz schwer zu verfolgen. Eine eingerückte URL-Gruppe oder `\urlstyle{tt}` (weiterhin 12 pt, vollständige URLs) könnte die Lesbarkeit verbessern; die Seitenbilanz danach neu prüfen.
- **Abbildung 2:** Die Legende steht direkt unter der Achsenbeschriftung „Betriebsjahr“; sie überdeckt nichts, wirkt aber wie ein Teil der Achse. Eine Legende im oberen linken Plotbereich oder oberhalb der Achse wäre klarer.
- **Abbildung 3:** Die drei Referenzlinien-Labels stehen eng und sind nicht an die Linien ausgerichtet. Direkte Annotationen an den Linien oder eine Legende mit größerem Abstand wären lesbarer. Die Caption sollte „Basis mit 20 % Reserve: 1.053,3 MW; p90 mit 20 % Reserve: 2.152,5 MW“ sagen.
- **Abbildung 1:** Panelbezeichnungen (a)/(b) fehlen; die grüne Annotation „Regelziel 9 °C“ teilt die Farbe der 0,1-%-Serie; die senkrechte Linie bei Jahr 10 ist nicht erklärt. Das sind kleine Klarheitsgewinne.
- **Installationsschema:** Es fehlt weiterhin und ist laut Aufgabe optional. Ein einfaches Schema (Quelle → Wärmetauscher → Trockenkühler → Kältemaschine → Rückführung) mit mindestens 12-pt-Beschriftung könnte die freie Fläche auf S. 13 nutzen, wenn Anhang A dort beginnt; es darf das 5-Seiten-Budget nicht sprengen und den Haupttext nicht über 10 Seiten treiben.
- **Lange Absätze:** Der H3–H7-Block auf S. 7 und die „drei Nachweise“ auf S. 10 gewinnen als kurze Listen an Scanbarkeit.
- **Tabellen 1/3/5:** Die Zeilenlabels „Trocken- und feuchte Annäherung“ (Tabelle 1), „Sieden, 8 Jahre“ (Tabelle 3) und „Direkte Trockenkühlung“ (Tabelle 5) brechen teils unschön. Breitere erste Spalten oder kürzere Labels prüfen; 12 pt beibehalten.
- **Captions Tabelle 2/5:** Die Captions nennen „Leistungsangaben in MW“, obwohl die Tabellen auch €, GWh, m³, kt CO₂ und Liter enthalten. Eine knappe Einheitenzeile („Leistungen in MW; Kosten in Mio./Mrd. €; Wasser in m³“) wäre präziser.
- **„Die Vergleichsseiten 1, 2 und 6 liegen bei“:** Im PDF selbst sind die D4RT-Seiten nicht enthalten; sie liegen im Prüfpaket. Eine Formulierung „liegen im Prüfpaket bei“ vermeidet Missverständnisse.
- **Tabelle 5, fette Nullen:** Die fett gesetzten H1-Nullen („0,0“) sind visuell schwer; optional nur die Überschrift/Zahlenkolonne hervorheben.

## 5. 10er-Prüfung

Keine Kategorie erhält 10. Damit entfällt die geforderte Beschreibung einer erfolglosen substanziellen 10er-Fehlersuche. D5 ist mit 9 die stärkste Kategorie; ich erhebe keinen 10er-Anspruch, weil die Prüfung keine externe URL-Validierung, keine Barrierefreiheits-/Tagging-Prüfung und keine vollständige Overfull-Box-Analyse umfasst und die Gesamtgestaltung wegen M1–M3 nicht stop-fähig ist.

## 6. Grenzen der Prüfung / Ungeprüftes

- **Externe URL-Ziele** wurden nicht abgerufen; geprüft wurden nur die gedruckten Quellenstrings, ihre Vollständigkeit und das Abrufdatum.
- **Kein LaTeX-Build und kein Build-Log**; Overfull-Box-Warnungen wurden nicht ausgewertet. Die gerenderte Geometrie und die Tintenränder wurden gemessen.
- **Generierte Tabellenquellen** (`report/generated/*.tex`) wurden nicht gelesen, da sie nicht in der zulässigen Dateiliste stehen; die Tabellenbefunde stammen aus dem Render und aus `main.tex`.
- **Wissenschaftliches Modell, Physik und Rechenwerte** wurden nicht bewertet; das ist ausdrücklich nicht Gegenstand.
- **Präsentation, Video und Finaldateien** wurden nicht bewertet; sie sind historische Arbeitsstände und nicht Lieferumfang.
- **D4RT-Eigenkonformität** wurde nicht bewertet; die drei D4RT-Seiten dienen nur dem visuellen Vergleich. Ihre US-Letter- und 10-pt-Eigenschaften wurden nicht übernommen.
- **Barrierefreiheit, PDF-Tagging und Font-Lizenzen** wurden nicht geprüft.
- **Keine früheren Rohberichte, Scorecards oder Übersichten mit Punktzahlen gelesen; keine Kommunikation mit dem anderen Reviewer.** Es kam zu keiner Exposition mit früheren Einreichungen oder Lösungen.

## 7. Abschließendes Urteil

**Die Design-Stoppregel ist nicht erfüllt.**

Die Bewertung lautet: **D1 = 8, D2 = 7, D3 = 8, D4 = 8, D5 = 9, D6 = 8.** Damit fehlen mindestens 9 in D1, D2, D3, D4 und D6. Die materiellen Einwände **M1 (fast leere PDF-Seite 13)**, **M2 (Tabelle 2 nach dem Beginn von Abschnitt 4)** und **M3 (Tabelle 4 ohne benannte Kostenkolonnen)** sind ungelöst; M4–M8 halten die betroffenen Kategorien zusätzlich unter 9. Das Paket ist gestalterisch noch nicht bereit für das technische Testpaket; eine weitere Runde ist erforderlich. Der andere Reviewer muss die Stoppregel unabhängig ebenfalls erfüllen.
