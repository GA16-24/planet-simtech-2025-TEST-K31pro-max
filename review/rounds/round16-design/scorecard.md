# Design-Scorecard Runde 16

Geprüfter Commit: `11ba6fbf803b229f42b1f289d627851bdc8b8e92`.

Beide Reviewer erhielten denselben Auftrag mit den früheren Befunden ohne Punktzahlen und der dokumentierten Änderungsantwort. Sie arbeiteten read-only in getrennten Kontexten. DeepSeek V4.1 Flash verwendete `reasoning_effort=max`, Kimi K3.1 Pro verwendete `thinking=max`. Der implementierende Agent hatte keine Stimme.

Die frische Archivkopie erzeugte 40 von 40 Paperartefakten bytegleich. Alle 24 Modelltests und `make verify` bestanden. Der geprüfte PDF-SHA-256 ist `430281f1532aefbaeff2e2a728332c11123aac822027407b9afd720ea9ce575c`. Die PDF hat 15 Seiten mit 10 Haupttextseiten nach dem Deckblatt und 5 Literatur-/Anhangsseiten.

| Kategorie | DeepSeek | Kimi |
| --- | ---: | ---: |
| D1, Typografie | 7 | 8 |
| D2, Seiten- und Spaltennutzung | 8 | 9 |
| D3, Lesbarkeit und visuelle Führung | 9 | 9 |
| D4, Abbildungen, Tabellen und visuelle Erklärung | 7 | 8 |
| D5, formale Compliance | 10 | 10 |
| D6, direkter D4RT-Vergleich | 8 | 9 |

## Urteil

Die Design-Stoppregel ist nicht erfüllt. Beide Reviewer bestätigen getrennte Zahl-Einheit-Verbindungen, Probleme in Abbildung 3 und Tabellenwaisen. DeepSeek dokumentiert außerdem Mathematikspatien, eine versetzte Gleichungsnummer, Flattersatz in Anhang A, zu große Spaltenlücken und uneinheitliche Zahlenkonventionen.

Beide Reviewer vergeben D5 10. A4, Seitenbudget, Ränder, Schriftgrößen, Pflichtaufbau, Quellenform und alle drei vollständigen NIST-URLs sind formal bestanden. Diese Einzelbewertung gleicht die offenen Gestaltungsmängel nicht aus. Es wird keine Mittelung gebildet.

## Rohberichte

- `deepseek.md` und `deepseek_result.json`
- `kimi.md` und `kimi_result.json`

Die nächste Revision muss die konkreten Umbrüche, Tabellen, Mathematikspatien und Achsenkollisionen korrigieren und erneut archivreproduziert werden. Diese Punktzahlen dürfen nicht fortgetragen werden.
