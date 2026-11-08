# Scorecard Runde 13

Revision: `fbd0a26fb67a0417602278d475ec5b1c2075285e`, 223 Dateien. Ausgangskandidat ist `4d22546b9a146e63ece26ba38ffaac697e153d7e`; der vollständige Review-Commit wurde selbst archivreproduziert. Beide Reviewer prüften unabhängig und read-only mit `reasoning_effort=max` beziehungsweise `thinking=max`. Frühere Rohberichte und Scorecards wurden nicht verwendet. Die vollständigen Begründungen stehen in `deepseek.md` und `kimi.md`, die Taskergebnisse in `deepseek_result.json` und `kimi_result.json`.

Der Prüfumfang ist der Research Paper mit den Kriterien 1, 2, 3, 4, 5, 6, 8, 9, 10, 11 und 12a. Kriterium 12b gehört nicht mehr zum Lieferumfang.

| Kriterium | DeepSeek-V4.1-Flash | Kimi K3.1 Pro |
| --- | ---: | ---: |
| 1 Qualität der Argumentation | 9 | 9 |
| 2 Vorgehen und Methodik | 9 | 9 |
| 3 Qualität der vorgeschlagenen Lösung | 9 | 9 |
| 4 Mathematische und wissenschaftliche Modellierung | 9 | 8 |
| 5 Ableitung neuer Ansätze | 9 | 9 |
| 6 Wissenschaftliche Qualität | 9 | 8 |
| 8 Klare Erklärungen | 9 | 8 |
| 9 Kritische Diskussion | 9 | 9 |
| 10 Struktur und Juryführung | 9 | 9 |
| 11 Format, Zitation und D4RT-Vergleich | 9 | 10 |
| 12a Schriftliche Bereitschaft | 9 | 8 |

## Ergebnis

Die Stoppregel ist nicht erfüllt. Kimi vergibt für Format und visuelle Qualität eine 10, für Modellierung, Wissenschaft, Erklärung und Bereitschaft jeweils 8. DeepSeek vergibt alle Kriterien mit 9. Die Punktzahlen werden nicht gemittelt und nicht auf eine neue Revision übertragen.

## DeepSeek, Ergebnis und optionale Hinweise

- Alle elf Kriterien erreichen 9, es gibt keine materiellen Mängel im Sinne der Stoppregel.
- Der Text nennt 23 statt 24 Tests. Die 8-Jahres-Zeile braucht die Erklärung der bereits erreichten Temperaturkappung. Ein Anlagenschema ist eine optionale Verbesserung.

## Kimi, materielle Befunde

- Die gedruckten Gleichungen für den Wärmekapazitätsstrom und die Speicherheizleistung lassen die Umrechnung von W in MW aus. Die Zahlen sind richtig, die Herleitungen sind unvollständig.
- Die reversible Absorptionsformel definiert ihre Temperaturen nicht als absolute Werte in Kelvin.
- Die Nachweisabschnitte nennen 23 statt 24 Testmethoden. Kriterien 4, 6, 8 und 12a bleiben deshalb bei 8.
- Kriterium 11 erreicht 10. Die Seiten sind ohne erkennbare Kollisionen, abgeschnittene Inhalte oder wesentliche visuelle Unterlegenheit.

## Nachbearbeitung

Die nächste Revision muss alle gedruckten Gleichungen dimensionell schließen, Kelvin definieren, die Testzahl korrigieren und die 8-Jahres-Kappung erklären. `review/revisions.md` ordnet die Umsetzung zu. Neue Punktzahlen werden erst nach erneuter Archivreproduktion und unabhängiger Review erhoben.
