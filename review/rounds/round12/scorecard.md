# Scorecard Runde 12

Revision: `a4005b20d5c19efcba1755ce6bd7b82eb1ecfc84`, 215 Dateien. Der Ausgangskandidat ist `94927f986b015f4ab03cf151b97fc41f245cbdd0`; der vollständige Review-Commit wurde selbst archivreproduziert. Beide Reviewer prüften unabhängig und read-only mit `reasoning_effort=max` beziehungsweise `thinking=max`. Frühere Rohberichte und Scorecards wurden nicht verwendet. Die vollständigen Begründungen stehen in `deepseek.md` und `kimi.md`, die Taskergebnisse in `deepseek_result.json` und `kimi_result.json`.

Der Prüfumfang ist der Research Paper mit den Kriterien 1, 2, 3, 4, 5, 6, 8, 9, 10, 11 und 12a. Kriterium 12b gehört nicht mehr zum Lieferumfang.

| Kriterium | DeepSeek-V4.1-Flash | Kimi K3.1 Pro |
| --- | ---: | ---: |
| 1 Qualität der Argumentation | 9 | 9 |
| 2 Vorgehen und Methodik | 8 | 9 |
| 3 Qualität der vorgeschlagenen Lösung | 9 | 9 |
| 4 Mathematische und wissenschaftliche Modellierung | 8 | 9 |
| 5 Ableitung neuer Ansätze | 9 | 9 |
| 6 Wissenschaftliche Qualität | 8 | 9 |
| 8 Klare Erklärungen | 8 | 9 |
| 9 Kritische Diskussion | 9 | 9 |
| 10 Struktur und Juryführung | 9 | 9 |
| 11 Format, Zitation und D4RT-Vergleich | 9 | 9 |
| 12a Schriftliche Bereitschaft | 8 | 9 |

## Ergebnis

Die Stoppregel ist nicht erfüllt. Kein Reviewer vergibt eine 10. Die Punktzahlen werden nicht gemittelt und nicht auf eine neue Revision übertragen.

## DeepSeek, materielle Befunde

- Tabelle 3 wertet die Wärmeleistung im Siedejahr aus, der Barwert dagegen im zehnten Jahr. Für die 12-Jahres-Prognose sind im zehnten Jahr 731,5 MW und -16,7 % erforderlich, nicht 877,8 MW und +0,0 %. Kriterien 2, 4, 6, 8 und 12a bleiben dadurch bei 8.
- Gleichung 10 muss den Wärmestrom in MW mit dem Faktor 10^6 in W umrechnen, weil der Nenner in J/K angegeben ist. Ohne die Einheit ist die Gleichung mehrdeutig.
- Die linke Spalte in Anhang A ist unausgeglichen, die übrige visuelle Qualität erreicht 9.

## Kimi, Ergebnis und optionale Hinweise

- Alle elf Kriterien erreichen 9, es gibt keine materiellen Mängel.
- Optionale Hinweise betreffen eine Temperatur-Sensitivitätstabelle, die Pufferformulierung und die Nennung von Tabelle 5.11 für das Hilfsstrombeispiel.

## Nachbearbeitung

Die nächste Revision muss die Sensitivität einheitlich auf das zehnte Jahr beziehen und die Einheiten der Ausfallgleichung ausweisen. Ein Regressionstest muss die 12-Jahres-Prognose mit 731,5 MW und -16,7 % bestätigen. `review/revisions.md` ordnet die Umsetzung zu. Neue Punktzahlen werden erst nach erneuter Archivreproduktion und unabhängiger Review erhoben.
