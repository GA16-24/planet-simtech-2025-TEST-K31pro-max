# Design-Scorecard Runde 18

Geprüfter Commit: `30462b6ca5057626bb0f990377f1673deac9983e`.

Beide Reviewer erhielten denselben Auftrag mit früheren Befunden ohne Punktzahlen und der dokumentierten Änderungsantwort. Sie arbeiteten read-only in getrennten Kontexten. DeepSeek V4.1 Flash verwendete `reasoning_effort=max`, Kimi K3.1 Pro verwendete `thinking=max`. Der implementierende Agent hatte keine Stimme.

Die frische Archivkopie erzeugte 40 von 40 Paperartefakten bytegleich. Alle 24 Modelltests und `make verify` bestanden. Der geprüfte PDF-SHA-256 ist `4aaa3d6fe29f8f77ab1906037c642e6cda9f928309de696d22f2bdb051f13388`. Die PDF hat 15 Seiten mit 10 Haupttextseiten nach dem Deckblatt und 5 Literatur-/Anhangsseiten.

| Kategorie | DeepSeek | Kimi |
| --- | ---: | ---: |
| D1, Typografie | 9 | 9 |
| D2, Seiten- und Spaltennutzung | 8 | 8 |
| D3, Lesbarkeit und visuelle Führung | 9 | 9 |
| D4, Abbildungen, Tabellen und visuelle Erklärung | 9 | 9 |
| D5, formale Compliance | 10 | 10 |
| D6, direkter D4RT-Vergleich | 8 | 9 |

## Urteil

Die Design-Stoppregel ist nicht erfüllt. Beide Reviewer beanstanden nur den rund 77 bis 80 mm großen Leerraum in der linken Spalte auf PDF-Seite 7. Er entsteht, weil die erzwungene Platzierung von Abbildung 2 in die nächste Spalte wechselt.

Die Korrektur verkleinert Abbildung 2 auf 90 % der Spaltenbreite und kürzt die Unterschrift. Die Platzierung nach H3 und vor Abschnitt 4 bleibt erhalten. Die effektive Diagrammschrift bleibt über 12 pt. Der Leerraum ist in der neuen Revision deutlich reduziert, und `make verify` besteht erneut.

Beide Reviewer vergeben D5 10 für formale Compliance. Diese Einzelbewertung gleicht den früheren Umbruchmangel nicht aus. Es wird keine Mittelung gebildet.

## Rohberichte

- `deepseek.md` und `deepseek_result.json`
- `kimi.md` und `kimi_result.json`

Die nächste Revision muss die neue Platzierung und Spaltenfüllung erneut archivreproduziert und bewertet werden. Diese Punktzahlen dürfen nicht fortgetragen werden.
