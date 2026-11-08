# Design-Council-Bericht Runde 15

## 1. Prüfgrundlage, Revision und Unabhängigkeit

Geprüft wurde ausschließlich die eingefrorene Revision `7ca2f3dc2137e958a6b0e8c5efbb7b4ac2f7a6eb`. Dieser Commit ist `HEAD`; die Arbeitskopie enthält keine Änderungen an versionierten Dateien, nur die untracked Review-Artefakte `prompt.md` und `revision.json`.

Die für die Prüfung relevanten SHA-256-Werte aus `review/rounds/round15-design/revision.json` stimmen überein für:

- `output/pdf/TEST-K31pro-max.pdf`,
- `review/rendered/report_contact.png`,
- alle vierzehn `review/rendered/report_pages/page-01.png` bis `page-14.png`,
- `review/rendered/d4rt_page01.png`, `d4rt_page02.png`, `d4rt_page06.png`,
- `report/main.tex`, `report/preamble.tex`,
- `compliance/regeln.md`, `compliance/checklist.md`,
- `review/rounds/round15-design/reproduction.md`.

Die PDF ist 14 Seiten lang, A4 (595,28 × 841,89 pt), die Schriften sind eingebettet. Ich habe die PDF, die Kontaktübersicht, alle vierzehn Einzelseiten und die drei D4RT-Seiten 1, 2 und 6 gesichtet sowie PDF-Text, Seitengeometrie und Schriftgrößen geprüft. `make verify` habe ich nicht selbst ausgeführt, weil der Auftrag read-only ist; `revision.json` weist `verification_result: passed` aus. Es wurden keine Dateien im Repository geändert und keine Builds ausgeführt.

Nicht gelesen wurden `review/README.md`, `decisions.tsv`, frühere Rohberichte, Scorecards, Übersichten mit Punktzahlen, `compliance/layout_referenz.md` und andere Runden. Es gab keine Kommunikation mit dem anderen Reviewer und keine Exposition gegenüber früheren Lösungen oder aufgabenbezogenen Repositories. Frühere Punktzahlen wurden nicht übernommen.

Wissenschaftliche Richtigkeit, physikalische Annahmen, Rechenwerte und frühere fachliche Bewertungen sind nicht Gegenstand dieses Berichts. Die Tabellen und Diagramme wurden nur auf Gestaltung, Lesbarkeit und formale Umsetzung geprüft.

## 2. Bewertung D1 bis D6

| Kategorie | Bewertung | Kurzbegründung | Beleg |
|---|---:|---|---|
| **D1 Typografie** | **8** | Schriftbild, Hierarchie, Mathematik- und Quellensatz sind im Grundsatz sauber. Mehrere Zeilen sind jedoch durch `\sloppy` und abgeschaltete Mikrotypografie stark gespreizt; Zahlen und Einheiten werden an Spaltenumbrüchen getrennt; drei Wörter werden über Seitengrenzen hinweg getrennt. | PDF S. 2 (Druck 1), Zusammenfassung; PDF S. 3 (2), Abschn. 2.2; PDF S. 8 (7), Abschn. 4.2; PDF S. 10 (9), Abschn. 5; PDF S. 11 (10), Abschn. 5; PDF S. 13 (12), Anhang A; `report/preamble.tex` Z. 7, 31; `report/main.tex` Z. 170, 191 |
| **D2 Seiten- und Spaltennutzung** | **8** | Ränder, Satzspiegel und Seitenbudget stimmen. Um Gleichung (4) steht jedoch ein großer Leerraum von ca. 70 pt über und unter der Formel; Anhang A beginnt am Fuß der linken Spalte und läuft nach zwei Zeilen in der rechten Spalte weiter. Seite 10 und 11 sind links jeweils ca. fünf Zeilen kürzer als rechts. | PDF S. 3 (2), rechte Spalte, Gl. (4); `report/main.tex` Z. 93–98; PDF S. 13 (12), Anhang A; `report/main.tex` Z. 271–292; PDF S. 10–11 (9–10) |
| **D3 Lesbarkeit und visuelle Führung** | **9** | Die Zusammenfassung ist klar überschrieben und bleibt unter einer Seite; Absatzfluss, Überschriftenhierarchie, numerische Verweise und die Reihenfolge der Hauptabschnitte sind nachvollziehbar. Es bleiben nur optionale Kleinigkeiten: der Verweis auf Tabelle 5 ohne „Anhang B“ und der unerklärte Begriff „Council“. | PDF S. 2 (1), Zusammenfassung; PDF S. 7 (6), Abschn. 3.3; PDF S. 11–12 (10–11), Literaturverzeichnis; `report/main.tex` Z. 28–36, 174, 233–267 |
| **D4 Abbildungen, Tabellen und visuelle Erklärung** | **8** | Abbildungen 1 und 2 sowie Tabellen 1 und 2 sind klar, maßstäblich und gut beschriftet. Abbildung 3 in Anhang B hat keine Achsentitel, mischt die Legende beider Panels und ist auf 75 mm Spaltenbreite sehr dicht. Ein Installationsschema fehlt; die vorhandenen Grafiken und Textbeschreibungen genügen aber für den Berichtsumfang, ein Schema wäre optional. | PDF S. 5 (4), Abb. 1; PDF S. 8 (7), Abb. 2; PDF S. 14 (13), Abb. 3 und Tab. 3–5; `report/main.tex` Z. 118–123, 163–168, 296–322 |
| **D5 Formale Compliance** | **8** | A4, mindestens 26 mm Rand, 12 pt auf 14,4 pt, anonymes Deckblatt, Pflichtaufbau, Seitenzählung, numerische Zitate und KI-Offenlegung sind erfüllt. Die NIST-URL in Quelle [4] ist jedoch nur als Kurz-URL gedruckt; die vollständige Query steht nur im externen Quellenregister, nicht im Literaturverzeichnis. | PDF S. 1, 11–13; `report/preamble.tex` Z. 1–5, 26; `report/main.tex` Z. 245; `compliance/regeln.md` Z. 7–14; `compliance/checklist.md` Z. 9–22; `pdfinfo`, `pdffonts` |
| **D6 Direkter D4RT-Vergleich** | **8** | Die Hauptseiten sind visuell solide und durch 12 pt besser lesbar als D4RTs kleine Tabellenschrift; D4RTs US-Letter-Format und enge Tabellen wurden bewusst nicht übernommen. Gegenüber D4RT S. 1, 2 und 6 fehlen jedoch visuelle Anker und Führung: kein Prozessschema, keine hervorgehobene H1-Variante, dichtere Anhänge A/B. | D4RT S. 1, 2, 6; PDF S. 2 (1), 7 (6), 13–14 (12–13) |

Keine Summenbildung und keine Mittelung über die Kategorien.

## 3. Materielle Mängel

### M1 – D1: Gespreizte Zeilen, getrennte Zahlen/Einheiten und Trennungen über Seitengrenzen

**Befund.** Der Satz ist an mehreren Stellen sichtbar gespreizt. Besonders deutlich:

- PDF S. 2 (Druck 1), Zusammenfassung: „Im zehnten Jahr wären dafür“ und „877,8 Megawatt Kühlleistung nötig.“
- PDF S. 3 (2), Abschn. 2.2: „für positive Differenzen. Natürliche“ und „Oberflächen- und Sohlverluste werden“.
- PDF S. 8 (7), Abschn. 4.2: „tät in J/(kg K) und der Wärme-“.
- PDF S. 10 (9), Abschn. 5: „Vierundzwanzig Tests und interne“.
- PDF S. 11 (10), Abschn. 5: „höchstens 8,1 × 10⁻¹⁰ K von der analytischen“.
- PDF S. 13 (12), Anhang A: „Kimi K3.1 Pro bei thinking=max erstellte“.

Die Ursache ist die Kombination aus `\sloppy` und `\usepackage[protrusion=false]{microtype}` in `report/preamble.tex` Z. 7 und 31. Zusätzlich werden Zahlen und Einheiten an Spaltenumbrüchen getrennt:

- PDF S. 6 (5), Abschn. 3.2: links endet „… Verdunstungsmenge 8,32“, rechts beginnt „Mio. m³ pro Jahr“.
- PDF S. 8 (7), Abschn. 4.2: links endet „… beträgt dann 0,9“, rechts beginnt nach Abbildung 2 „Minuten und ist keine frei verfügbare Wartezeit“.

Drei Wörter werden über Seitengrenzen hinweg getrennt: „ge-nannten“ (S. 2→3), „Stun-den“ (S. 8→9), „verwen-det“ (S. 9→10).

**Korrektur.** `\sloppy` entfernen, Mikrotypografie mit Protrusion aktivieren und `\emergencystretch` auf einen verträglichen Wert (ca. 1–2 em) setzen. Die genannten Zeilen manuell durch Umformulieren oder gezielte Umbrüche entlasten. Zahlen/Einheiten mit geschützten Leerzeichen setzen, z. B. `8,32~Mio.~m³` und `0,9~Minuten`, oder als `\mbox{8,32 Mio.~m³}` zusammenhalten. `\brokenpenalty=10000` verhindert Trennungen an Seitengrenzen. Die Korrektur darf keine neue Haupttextseite erzeugen; 12 pt, A4 und 26 mm Rand bleiben unverändert. Nach dem Neusatz ist die Seitenzahl erneut zu prüfen.

### M2 – D2: Leerraum um Gleichung (4) und Platzierung von Anhang A

**Befund.** Auf PDF S. 3 (Druck 2) steht Gleichung (4) in der rechten Spalte mit ca. 70 pt Leerraum über und unter der Formel (ca. 25 mm). Das ist für eine Display-Gleichung ungewöhnlich und unterbricht den Lesefluss. Die Quelle `report/main.tex` Z. 93–98 enthält keine bewusste `\vspace`-Anweisung; die Ursache liegt im Zusammenspiel von Spaltenumbruch, Display-Abständen und ggf. der Float-Queue und ist vor der Korrektur zu prüfen.

Anhang A beginnt auf PDF S. 13 (12) am Fuß der linken Spalte: Die Überschrift steht bei ca. 677 pt, der erste Absatz beginnt bei ca. 717 pt und wird nach „Grafiken.“ in der rechten Spalte fortgesetzt. Die Überschrift wirkt dadurch wie ein Nachtrag zur Literatur; der erste Absatz ist nach zwei Zeilen getrennt. Der Satz selbst ist 12 pt, klar und mit zentrierter Handrechnung; die Platzierung ist das Problem.

**Korrektur.** Die Display-Abstände um Gleichung (4) lokal auf normale Werte zurücksetzen (z. B. `\abovedisplayskip` und `\belowdisplayskip` auf ca. 12 pt) und die Ursache im Spalten-/Float-Aufbau prüfen; 12 pt, A4 und 26 mm Rand bleiben erhalten. Anhang A an den Kopf einer Spalte oder Seite setzen: entweder `\clearpage` vor Anhang A — dann 15 Seiten, was mit 1 Deckblatt + 10 Haupttextseiten + 5 Literatur-/Anhangseiten im offiziellen Budget bleibt — oder, wenn zwingend 14 Seiten, Anhang A an den Kopf der rechten Spalte setzen und den ersten Absatz um zwei Zeilen straffen. Die Seite 10/11 ist links jeweils ca. fünf Zeilen kürzer als rechts; das ist ein sekundärer Ausgleichspunkt und kann optional über `\balance`/`\raggedbottom` geprüft werden, ist aber nicht der Hauptmangel.

### M3 – D4: Abbildung 3 ohne Achsentitel und zu dicht gesetzt

**Befund.** Auf PDF S. 14 (Druck 13), Anhang B, hat Abbildung 3 zwei Histogramme in einer 75-mm-Spalte. Die x-Achsen tragen nur die Zahlen 0/2000 bzw. 0/5/10, aber keine Achsentitel; die Einheiten stehen nur in der Bildunterschrift. Die Legende mischt Werte des linken Panels („Basis: 877,8“, „Basis +20 %: 1053,3“, „p90 + 20 %: 2152,5“) und des rechten Panels („Referenz: 4,14“). Bei zwei ca. 35 mm breiten Panels sind die Histogramme und die gestrichelten Referenzlinien sehr klein; die Legende dominiert die Grafik. Die Tabellen 3–5 und die Captions sind formal sauber, aber die Seite ist insgesamt sehr dicht.

**Korrektur.** In Abbildung 3 kurze Achsentitel „MW“ (links) und „Mrd. €“ (rechts) ergänzen; die Legende in zwei Gruppen teilen oder die Referenzlinien direkt beschriften. Die freie Höhe zwischen Abbildung 3 und Tabelle 3 beträgt ca. 49 pt (Abbildung/Caption enden bei ca. 377 pt, Tabelle 3 beginnt bei ca. 426 pt); die Grafik kann in diesem Rahmen höher gesetzt werden, ohne Tabelle 3 zu verschieben. 12 pt, eine Spalte und die vorhandene Seite bleiben erhalten; keine neue Seite.

Ein Installationsschema fehlt. Die Textbeschreibungen in Abschn. 2.2 und 3.2 sowie die drei Grafiken erklären die Anlage für den Berichtsumfang ausreichend; ein zusätzliches Schema wäre eine optionale Verbesserung, müsste aber im 10+5-Seiten-Budget Platz finden und mindestens 12 pt beschriftet sein. Derzeit ist dafür kein Platz ohne zusätzliche Seite; allein das Fehlen des Schemas senkt die Bewertung nicht.

### M4 – D5: NIST-URL nur als Kurz-URL im Literaturverzeichnis

**Befund.** In Quelle [4] auf PDF S. 11–12 (Druck 10–11) steht als gedruckte URL nur:

`webbook.nist.gov/cgi/fluid.cgi`

Die vollständige Query-URL ist im `\href`-Ziel von `report/main.tex` Z. 245 enthalten, aber nicht gedruckt. Der Eintrag verweist für „Vollständige URLs und die Sättigungsdaten“ auf das Quellenregister und das Modell. Das Quellenregister ist nicht Teil der PDF. Die formale Regel in `compliance/regeln.md` Z. 13 verlangt bei Internetquellen Autor oder Institution, Titel, URL und Abrufdatum. Die gedruckte Kurz-URL führt nur auf die allgemeine NIST-Fluid-Seite; ohne die Query-Parameter sind die konkret zitierten Tabellen aus der PDF allein nicht unmittelbar reproduzierbar. Das ist der einzige festgestellte formale Mangel.

**Korrektur.** In [4] die vollständige Query-URL drucken, z. B.:

`https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Type=IsoBar&Digits=6&P=1.01325&TLow=0&THigh=100&TInc=10&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3`

Dabei `xurl` bzw. die vorhandenen `\UrlBreaks` zum Umbruch nutzen und den Hinweis auf das externe Quellenregister streichen. Die „Abfragen“-Beschreibung auf eine Zeile straffen, damit die Ergänzung ohne neue Seite in das Literaturbudget passt; falls die Seite dadurch wächst, mit der Anhang-A-Korrektur abstimmen (15 Seiten bleiben im Limit). Abrufdatum 07.11.2026 und 12 pt bleiben erhalten.

Alle übrigen Formalien sind erfüllt: A4, Textblock 26,0 mm links/rechts, 26 mm oben, 34 mm unten, Seitenzahl ca. 26 mm über der Unterkante; 12 pt auf 14,4 pt; anonymes Deckblatt ohne Personen- oder Schulnamen; PDF-Metadaten ohne Autor; Pflichtaufbau mit Zusammenfassung, Einführung, Methode, Ergebnissen, Diskussion und Schlussfolgerung; fortlaufende Seitenzählung 1–13; numerische Zitate [1]–[25]; KI-Offenlegung in Anhang A mit System, Ort, Art und Umfang. Offizielle Team-ID, Rechtefreigabe, menschliche Fachprüfung und Einreichung sind menschliche Restaufgaben und wurden nicht als Papermangel gewertet.

### M5 – D6: D4RT-Vergleich und visuelle Führung in den Anhängen

**Befund.** D4RT S. 1 zeigt eine klare Titel-/Abstract-Ordnung mit einem visuellen Anker rechts; D4RT S. 2 zeigt ein großes Prozessschema; D4RT S. 6 zeigt eine dichte, aber durch die fett markierte „D4RT (Ours)“-Zeile gut geführte Tabelle. Die eigene Arbeit hat einen sauberen Titel, eine funktionierende einspaltige Zusammenfassung und gute Hauptgrafiken, aber keine vergleichbare visuelle Führung in den Anhängen: Anhang A beginnt am Spaltenfuß, Anhang B ist dicht, Abbildung 3 ohne Achsentitel, und die gewählte H1-Variante ist in Tabelle 2 nicht hervorgehoben. D4RTs US-Letter-Format und die kleine Tabellenschrift werden ausdrücklich nicht als Vorgabe übernommen.

**Korrektur.** Die D2- und D4-Korrekturen (Anhang A an den Spaltenkopf, Abbildung 3 mit Achsentiteln und mehr Höhe) umsetzen. Zusätzlich in Tabelle 2 die H1-Spalte und in Tabelle 5 die H1-Zeile fett oder leicht hinterlegt hervorheben, analog zur „D4RT (Ours)“-Zeile, ohne die 12-pt-Vorgabe zu ändern und ohne eine neue Seite zu erzeugen. Damit wird die Leserführung dem D4RT-Maßstab angenähert, ohne dessen Format- oder Schriftverstöße zu übernehmen.

## 4. Optionale Verbesserungen

Diese Punkte sind keine materiellen Mängel und für eine 9 nicht zwingend:

- **D3:** Auf PDF S. 7 (Druck 6) „Tabelle 5 zeigt die Bilanz“ zu „Tabelle 5 in Anhang B zeigt die Bilanz“ ergänzen. Den Begriff „Council“ auf PDF S. 3 (Druck 2) als internen Review-Hinweis erläutern oder neutral formulieren.
- **D3:** Eine dünne Trennlinie oder ein vollbreiter Zusammenfassungssatz auf PDF S. 2 würde die Abgrenzung zur Einführung stärken; das kostet jedoch Platz und ist nicht erforderlich.
- **D4:** In Tabelle 2 die H1-Spalte und in Tabelle 5 die H1-Zeile optisch hervorheben; in Tabelle 3 ein echtes Minuszeichen „−“ statt des Bindestrichs verwenden; in Abbildung 2 zusätzlich zur Farbe eine Strichart für Schwarz-Weiß-Druck verwenden.
- **D4:** Ein kompaktes Prozessschema wäre eine sinnvolle Ergänzung, findet aber im vorhandenen 10+5-Seiten-Budget keinen Platz ohne zusätzliche Seite; nur in einer späteren Fassung mit 12-pt-Beschriftung und ohne neue Seite umsetzen.
- **D2:** Die letzten Haupttextseiten 10/11 links/rechts besser ausgleichen; der Effekt ist gering und die aktuelle Lösung ist funktional.
- **D5:** Für die NIST-Quelle zusätzlich einen persistenten Permalink oder DOI prüfen, falls verfügbar; die vollständige Query-URL hat Vorrang.

## 5. 10er-Prüfung

Es wurde keine 10 vergeben. Damit entfällt die im Auftrag für eine 10 verlangte Beschreibung einer erfolglosen substanziellen Fehlersuche.

Die einzige 9 ist **D3**. Dort habe ich die einspaltige Zusammenfassung, die Absatzfolge, die Überschriftenhierarchie, die Tabellen- und Abbildungsverweise, die numerischen Zitate und die Reihenfolge der Hauptabschnitte geprüft. Die verbleibenden D3-Punkte (Tabelle-5-Verweis, „Council“) sind optional; sie rechtfertigen keine Absenkung unter 9. Eine 10 wäre erst nach Behebung der materiellen Mängel und einer erneuten, dokumentierten Fehlersuche vertretbar.

## 6. Abschließendes Urteil

**Die Design-Stoppregel ist nicht erfüllt.**

Es verbleiben die materiellen Mängel M1 bis M5:

- **D1 = 8:** gespreizte Zeilen, getrennte Zahlen/Einheiten, Trennungen über Seitengrenzen.
- **D2 = 8:** Leerraum um Gleichung (4), Anhang A am Spaltenfuß, leichte Spaltenimbalance auf Seite 10/11.
- **D3 = 9:** keine materiellen D3-Einwände; nur optionale Kleinigkeiten.
- **D4 = 8:** Abbildung 3 ohne Achsentitel und zu dicht; kein Installationsschema, aber für den Umfang optional.
- **D5 = 8:** NIST-URL nur als Kurz-URL; vollständige Query nur im externen Quellenregister.
- **D6 = 8:**D4RT-Vergleich; Hauptseiten solide, Anhänge und visuelle Führung schwächer.

Damit liegt keine design-seitige Freigabe für das technische Testpaket vor. Die Korrekturen sind im vorhandenen Seitenbudget grundsätzlich möglich; die Anhang-A-Korrektur kann mit einer 15. Seite innerhalb der 5-Seiten-Obergrenze für Literatur und Anhang erfolgen. Nach den Korrekturen ist die PDF neu zu rendern und erneut gegen A4, 26 mm Rand, 12 pt, Seitenzählung und Quellenform zu prüfen. Beide Reviewer müssen die Stoppregel unabhängig erfüllen; dieser Bericht erfüllt sie nicht.
