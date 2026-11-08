# Design-Scorecard Runde 15

Geprüfter Commit: `7ca2f3dc2137e958a6b0e8c5efbb7b4ac2f7a6eb`.

Beide Reviewer erhielten denselben Auftrag in `prompt.md` und arbeiteten read-only in getrennten Kontexten. DeepSeek V4.1 Flash verwendete `reasoning_effort=max`, Kimi K3.1 Pro verwendete `thinking=max`. Der implementierende Agent hatte keine Stimme. Frühere fachliche und gestalterische Punktzahlen wurden nicht übernommen.

Die frische Archivkopie erzeugte 39 von 39 Paperartefakten bytegleich. Alle 24 Modelltests und `make verify` bestanden. Der geprüfte PDF-SHA-256 ist `0cb592f082ac0db20baa15ba862759b6b7252e39fa08ef4176da1b5507e3403f`. Die PDF hat 14 Seiten mit 10 Haupttextseiten nach dem Deckblatt und 4 Literatur-/Anhangsseiten.

| Kategorie | DeepSeek | Kimi |
| --- | ---: | ---: |
| D1, Typografie | 8 | 9 |
| D2, Seiten- und Spaltennutzung | 8 | 9 |
| D3, Lesbarkeit und visuelle Führung | 9 | 9 |
| D4, Abbildungen, Tabellen und visuelle Erklärung | 8 | 9 |
| D5, formale Compliance | 8 | 9 |
| D6, direkter D4RT-Vergleich | 8 | 9 |

## Urteil

Die Design-Stoppregel ist nicht erfüllt. Kimi findet keinen materiellen Mangel. DeepSeek verlangt Korrekturen an Typografie, Gleichungsumfeld, Anhangsplatzierung, Abbildung 3, gedruckten NIST-URLs und visueller H1-Führung. Es wird keine Mittelung über Kategorien oder Reviewer gebildet.

Die Reviewer beurteilen zwei Punkte unterschiedlich. Kimi hält die Platzierung von Anhang A und die gedruckte NIST-Kurz-URL mit vollständigem Hyperlink für formal ausreichend. DeepSeek bewertet beides als materielle Mängel. Für die nächste Revision werden die konkreten DeepSeek-Befunde behoben, ohne ein Installationsschema zu erzwingen oder D4RTs Papierformat und engere Ränder zu übernehmen.

## Rohberichte

- `deepseek.md` und `deepseek_result.json`
- `kimi.md` und `kimi_result.json`

Die nächste Designbewertung braucht einen neuen eingefrorenen Commit und darf diese Punktzahlen nicht auf eine geänderte Revision übertragen.
