# Design-Scorecard Runde 19

Geprüfter Commit: `40f26be1ff1158d527492ef4913dbeca25d86f30`.

Beide Reviewer erhielten denselben Auftrag mit früheren Befunden ohne Punktzahlen und der dokumentierten Änderungsantwort. Sie arbeiteten read-only in getrennten Kontexten. DeepSeek V4.1 Flash verwendete `reasoning_effort=max`, Kimi K3.1 Pro verwendete `thinking=max`. Der implementierende Agent hatte keine Stimme.

Die frische Archivkopie erzeugte 40 von 40 Paperartefakten bytegleich. Alle 24 Modelltests und `make verify` bestanden. Der geprüfte PDF-SHA-256 ist `c6c069c853e8aa1d97333dc93a282ec91f6fcbc6837b8867e55e708b0313d291`. Die PDF hat 15 Seiten mit 10 Haupttextseiten nach dem Deckblatt und 5 Literatur-/Anhangsseiten.

| Kategorie | DeepSeek | Kimi |
| --- | ---: | ---: |
| D1, Typografie | 8 | 9 |
| D2, Seiten- und Spaltennutzung | 7 | 8 |
| D3, Lesbarkeit und visuelle Führung | 8 | 8 |
| D4, Abbildungen, Tabellen und visuelle Erklärung | 8 | 9 |
| D5, formale Compliance | 9 | 10 |
| D6, direkter D4RT-Vergleich | 8 | 8 |

## Urteil

Die Design-Stoppregel ist nicht erfüllt. Die frühere Lücke auf PDF-Seite 7 ist geschlossen. Die letzte Literaturseite ist jedoch unausgewogen, und Tabelle 2 erscheint drei Seiten nach ihrer ersten Referenz. DeepSeek nennt außerdem Kostenkolonnen ohne Größenbezeichnung, uneinheitliche Tausenderpunkte, eine geteilte Formeleinleitung und weitere lokale Satzfehler.

Beide Reviewer bestätigen die Datenfreiheit der Histogrammlegende und die Einhaltung der formalen Vorgaben. Kimi vergibt D5 10. Diese Ergebnisse gleichen die verbleibenden Mängel nicht aus. Es wird keine Mittelung gebildet.

## Rohberichte

- `deepseek.md` und `deepseek_result.json`
- `kimi.md` und `kimi_result.json`

Die nächste Revision muss die Quellengruppierung, Tabellenposition, Kostenheader, Zahlenformat, Formeleinleitung und übrigen kleinen Satzfehler korrigieren und erneut archivreproduziert werden. Diese Punktzahlen dürfen nicht fortgetragen werden.
