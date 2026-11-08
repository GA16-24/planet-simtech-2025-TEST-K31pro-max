# Design-Scorecard Runde 17

Geprüfter Commit: `f7f1a1f4da527e1c7ff2f1885123c6eb096d3134`.

Beide Reviewer erhielten denselben Auftrag mit früheren Befunden ohne Punktzahlen und der dokumentierten Änderungsantwort. Sie arbeiteten read-only in getrennten Kontexten. DeepSeek V4.1 Flash verwendete `reasoning_effort=max`, Kimi K3.1 Pro verwendete `thinking=max`. Der implementierende Agent hatte keine Stimme.

Die frische Archivkopie erzeugte 40 von 40 Paperartefakten bytegleich. Alle 24 Modelltests und `make verify` bestanden. Der geprüfte PDF-SHA-256 ist `8dcddc5921345c14338d266e72de07e0f44e85ef7a631e022e0747d7d190004a`. Die PDF hat 15 Seiten mit 10 Haupttextseiten nach dem Deckblatt und 5 Literatur-/Anhangsseiten.

| Kategorie | DeepSeek | Kimi |
| --- | ---: | ---: |
| D1, Typografie | 9 | 8 |
| D2, Seiten- und Spaltennutzung | 8 | 9 |
| D3, Lesbarkeit und visuelle Führung | 8 | 9 |
| D4, Abbildungen, Tabellen und visuelle Erklärung | 9 | 8 |
| D5, formale Compliance | 9 | 10 |
| D6, direkter D4RT-Vergleich | 9 | 8 |

## Urteil

Die Design-Stoppregel ist nicht erfüllt. DeepSeek beanstandet die Platzierung von Tabelle 1, Tabelle 2 und Abbildung 2 sowie die Balance der letzten Literaturseite. Kimi beanstandet eine getrennte Minutenangabe und die Abdeckung von Histogrammdaten durch die undurchsichtige Legende.

Typografie, Abbildungen, formale Compliance und D4RT erreichen bei DeepSeek 9. Kimi vergibt D5 10. Diese Ergebnisse gleichen die verbleibenden Mängel nicht aus. Es wird keine Mittelung gebildet.

## Rohberichte

- `deepseek.md` und `deepseek_result.json`
- `kimi.md` und `kimi_result.json`

Die nächste Revision muss die Floatfolge, die Literaturbalance, die Minutenverbindung und die Datenabdeckung korrigieren und erneut archivreproduziert werden. Diese Punktzahlen dürfen nicht fortgetragen werden.
