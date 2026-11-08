# Design-Scorecard Runde 20

Geprüfter Commit: `01a7304980f0a3044f385e40463cf118f4a80dcb`.

Beide Reviewer erhielten denselben Auftrag mit früheren Befunden ohne Punktzahlen und der dokumentierten Änderungsantwort. Sie arbeiteten read-only in getrennten Kontexten. DeepSeek V4.1 Flash verwendete `reasoning_effort=max`, Kimi K3.1 Pro verwendete `thinking=max`. Der implementierende Agent hatte keine Stimme.

Die frische Archivkopie erzeugte 40 von 40 Paperartefakten bytegleich. Alle 24 Modelltests und `make verify` bestanden. Der geprüfte PDF-SHA-256 ist `7d495aa752c00ce9ca430e1dd775fb933fe498db4a31f883594f62bea6268f25`. Die PDF hat 15 Seiten mit 10 Haupttextseiten nach dem Deckblatt und 5 Literatur-/Anhangsseiten.

| Kategorie | DeepSeek | Kimi |
| --- | ---: | ---: |
| D1, Typografie | 9 | 9 |
| D2, Seiten- und Spaltennutzung | 7 | 8 |
| D3, Lesbarkeit und visuelle Führung | 8 | 9 |
| D4, Abbildungen, Tabellen und visuelle Erklärung | 7 | 9 |
| D5, formale Compliance | 10 | 10 |
| D6, direkter D4RT-Vergleich | 8 | 9 |

## Urteil

Die Design-Stoppregel ist nicht erfüllt. Beide Reviewer beanstanden die letzte Literaturseite. DeepSeek nennt außerdem getrennte Quelleneinträge, die Referenzreihenfolge von Tabelle 2, Fallgruppen in Tabelle 3 und lokale Mängel in den Abbildungen 2 und 3. Kimi empfiehlt einen Spaltenumbruch nach Quelle 22. Die Referenzlage von Tabelle 2 bewerten die Reviewer unterschiedlich; die nächste Revision setzt den ersten Verweis ausdrücklich vor den Float.

Beide Reviewer vergeben D5 10. Diese Ergebnisse gleichen die verbleibenden Mängel nicht aus. Es wird keine Mittelung gebildet.

## Rohberichte

- `deepseek.md` und `deepseek_result.json`
- `kimi.md` und `kimi_result.json`

Die nächste Revision muss die Literaturbalance und Eintragstrennungen, die eindeutige Vorausreferenz, Tabellengruppierung und Figurenabstände korrigieren und erneut archivreproduziert werden. Diese Punktzahlen dürfen nicht fortgetragen werden.
