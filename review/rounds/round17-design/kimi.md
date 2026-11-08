## Prüfrahmen

Geprüft wurde die eingefrorene Revision `f7f1a1f4da527e1c7ff2f1885123c6eb096d3134` der Research-Paper-PDF :codex-file-citation{path="/Users/macbook_air_m1/.t3/scratch/2026-11-07-create-a-new-separate-github-162aa05c/planet-simtech-2025-TEST-K31pro-max/output/pdf/TEST-K31pro-max.pdf" purpose="source"}.

Der Git-HEAD entspricht dem Prüfcommit. Alle 24 zulässigen Prüfdateien sind hashgleich mit `revision.json`. Ich habe die Kontaktübersicht, alle 15 Seitenbilder und die drei D4RT-Seiten vollständig gesichtet. Die PDF wurde zusätzlich durch Text-, Schrift-, Geometrie- und Umbruchprüfungen untersucht. Ich habe keine Dateien verändert, keine Builds ausgeführt und keine früheren Berichte oder Scorecards gelesen.

## Bewertung

| Kategorie | Bewertung | Begründung und Belegorte |
| --- | ---: | --- |
| D1, Typografie | **8/10** | Times-Hierarchie, Mathematiksatz, Dezimalkommata und die zweizeilige Gleichung 6 auf PDF-Seite 4 sind sauber. Anhang A auf PDF-Seite 14 ist lesbar und kontrolliert gesetzt. Auf PDF-Seite 8, Abschnitt 4.2, steht jedoch "weitere 5" am Zeilenende und "min" am Anfang der nächsten Zeile. Quelle: `report/main.tex:194`. |
| D2, Seiten- und Spaltennutzung | **9/10** | Das Deckblatt auf PDF-Seite 1, zehn Haupttextseiten auf PDF-Seiten 2 bis 11 sowie fünf gemeinsame Literatur- und Anhangsseiten auf PDF-Seiten 11 bis 15 halten das Budget ein. Die einspaltige Zusammenfassung auf PDF-Seite 2, Anhang A auf PDF-Seite 14 und Anhang B auf PDF-Seiten 14 und 15 sind ohne Überlauf angeordnet. Die Leerräume auf PDF-Seiten 6, 13 und 15 sind keine wesentlichen Umbruchfehler. |
| D3, Lesbarkeit und visuelle Führung | **9/10** | Die Zusammenfassung vermittelt Ergebnis, Kosten und Grenzen vor der Einführung. Abschnittsfolge, Überschriften und Verweise auf Gleichungen, Abbildungen und Tabellen sind nachvollziehbar. Besonders klar sind die Übergänge von Methode zu Ergebnissen auf PDF-Seiten 3 bis 5 und von Diskussion zu Nachweis und Schlussfolgerung auf PDF-Seiten 10 und 11. |
| D4, Abbildungen, Tabellen und visuelle Erklärung | **8/10** | Abbildungen 1 und 2, die Symlog-Erklärung, die Tabellen 1 bis 5 und die Fettung von H1 sind gut lesbar. In Abbildung 3 auf PDF-Seite 14 verdeckt die undurchsichtige Legende des oberen Histogramms jedoch Histogrammflächen und Referenzlinien. Dadurch lassen sich Teile der dargestellten Verteilungen nicht mehr zuverlässig verfolgen. |
| D5, Formale Compliance | **10/10** | A4, mindestens 25 mm Rand, nominaler 12-pt-Satz mit 14,4 pt Zeilenabstand, anonymes Pflichtdeckblatt, Pflichtaufbau, Seitenbudget, numerische Quellenverweise und KI-Offenlegung sind erfüllt. Alle drei vollständigen NIST-URLs stehen in Eintrag [4] auf PDF-Seiten 11 und 12. Die eigene Fehlersuche ist unten dokumentiert. |
| D6, Direkter D4RT-Vergleich | **8/10** | Spaltenordnung, Hierarchie, Tabellenlinien und erklärende Unterschriften erreichen den D4RT-Maßstab unter den strengeren A4-, Rand- und Schriftvorgaben. D4RT-Seite 2 bietet eine stärkere Prozessübersicht, deren Fehlen hier nur optional ist. Die Bewertung unter 9 folgt aus der tatsächlichen Qualitätsdifferenz bei Abbildung 3: D4RT-Seite 6 führt seine Visualisierungen ohne eine vergleichbare Datenabdeckung. |

## Materielle Mängel und Korrekturen

1. **Getrennte Zahl und Einheit, D1.**  
   Beleg: PDF-Seite 8, Abschnitt 4.2, Absatz zum dynamischen Ausfalltest. Im Fließtext wird "weitere 5 min" als "weitere 5" und "min" auf zwei Zeilen getrennt. Die Revisionsaussage, keine solche Trennung außerhalb der Achsenbilder zu haben, ist daher nicht erfüllt.  
   Korrektur: In `report/main.tex:194` "weitere 5 min" durch "weitere `5~min`" ersetzen. Danach den vollständigen Umbruchscan erneut ausführen und PDF-Seite 8 sichtprüfen. Der Zeilenabstand von 14,4 pt, die 12-pt-Schrift, die Ränder und das Seitenbudget bleiben unverändert. Ein etwaig veränderter Umbruch darf keine zusätzliche Seite erzeugen.

2. **Legende verdeckt Diagrammdaten, D4 und D6.**  
   Beleg: PDF-Seite 14, Abbildung 3, oberes Histogramm. Die weiße Legendenfläche bedeckt Balken der Verteilungen und unterbricht den sichtbaren Verlauf vertikaler Referenzlinien.  
   Korrektur: Die dreiteilige Legende aus dem Achsenbereich nehmen und beispielsweise einzeilig zwischen den beiden Histogrammen oder oberhalb des oberen Panels platzieren. Dafür kann der vorhandene Freiraum auf PDF-Seite 14 genutzt werden. Die Einbindung erfolgt an `report/main.tex:301-306`. Spaltenbreite, mindestens 12 pt Beschriftung und die bestehende Seitenzahl bleiben erhalten. Anschließend ist bei Vergrößerung zu prüfen, dass weder Balken, Achsen, Referenzlinien noch Text verdeckt werden.

Für D6 genügt dieselbe Diagrammkorrektur. Ein Installationsschema ist nicht Voraussetzung für die Korrektur.

## Optionale Verbesserungen

- Ein kompaktes Installationsschema in Abschnitt 3.2 könnte Quellstrom, Trockenkühlung, Kältemaschinen und externe Wärmesenke schneller erklären. Es müsste innerhalb der zehn Haupttextseiten Platz finden, mindestens 12 pt Beschriftungen verwenden und die bestehenden Ränder einhalten. Sein Fehlen ist kein Compliance- oder Papermangel.
- Der Literatur-Eintrag [16] wird zwischen PDF-Seite 12 und 13 nach der Institutionsangabe getrennt. Ein Zusammenhalten des Eintrags würde den Quellensatz glätten, ist aber nicht erforderlich. Die vollständigen Angaben sind vorhanden und lesbar.
- In der Zusammenfassung auf PDF-Seite 2 könnten einzelne stark gehäufte Trennungen durch kurze Umformulierungen reduziert werden. Kleinere Schrift oder breitere Spalten sind dafür nicht nötig.

## Fehlersuche für die 10 in D5

Ich habe gezielt nach Compliancefehlern gesucht:

- `pdfinfo` bestätigt 15 A4-Seiten und keine Autorenangabe in den Metadaten.
- Die geometrische Auswertung aller PDF-Textzeichen fand auf keiner Seite ein Zeichen außerhalb des 25-mm-Rands. Die Sichtprüfung bestätigte dies auch für Tabellen und Diagramme.
- Fließtext, Tabellen, Quellen und Diagrammbeschriftungen verwenden den nominalen 12-pt-Satz oder größere Schrift. Kleinere PDF-Werte betreffen mathematische Indizes und Extraktionsartefakte rotierter Achsentexte, nicht die sichtbare Grundschrift.
- Deckblatt, Zusammenfassung, Einführung, Methode, Ergebnisse, Diskussion, Schlussfolgerung, Literaturverzeichnis und beide Anhänge sind vorhanden und im Seitenbudget.
- Die Zusammenfassung bleibt auf einer Seite und in einer Spalte. Die Seitenzählung ist fortlaufend.
- Die numerischen Verweise und 25 Literatur-Einträge sind vorhanden. Die drei vollständigen NIST-Abfragen wurden in der PDF-Textausgabe gefunden.
- Anhang A dokumentiert Systeme, Einsatzbereich, Art und Umfang der KI-Nutzung sowie Reproduktionsbefehle.

Dabei blieb kein substanzieller D5-Verstoß. Die gefundenen Mängel betreffen Mikrotypografie und Diagrammgestaltung, nicht die geforderten Formalia. Offizielle Team-ID, Rechtefreigabe, menschliche Fachprüfung und tatsächliche Einreichung wurden nach Vorgabe nicht negativ bewertet. Wissenschaftliche Richtigkeit und die Erreichbarkeit der URLs waren nicht Gegenstand dieser Designprüfung.

## Abschließendes Urteil

**Meine Bewertung erfüllt die Design-Stoppregel nicht.** D1, D4 und D6 liegen unter 9. Mit der getrennten Zahl-Einheit-Verbindung und der abdeckenden Histogrammlegende bleiben zwei materielle Einwände offen. Die 10 in D5 gleicht diese Einwände nicht aus; eine Mittelung über Kategorien ist nicht zulässig.
