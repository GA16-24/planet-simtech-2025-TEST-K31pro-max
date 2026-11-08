# Scorecard Runde 6

Revision: `473e397c4d45a909cc024e1722d572cdbd73df7d`, 164 Dateien. Beide Reviewer prüften unabhängig und read-only mit `reasoning_effort=max` beziehungsweise `thinking=max`. Keine früheren Rohberichte oder Scorecards wurden verwendet. Die vollständigen Begründungen stehen in `deepseek.md` und `kimi.md`.

Der Prüfumfang ist nach der Nutzerkorrektur nur der Research Paper. Die elf Zeilen sind 1, 2, 3, 4, 5, 6, 8, 9, 10, 11 und 12a. Kriterium 12b ist nicht mehr Teil des Lieferumfangs.

| Kriterium | DeepSeek-V4.1-Flash | Kimi K3.1 Pro |
| --- | ---: | ---: |
| 1 Qualität der Argumentation | 9 | 9 |
| 2 Vorgehen und Methodik | 9 | 8 |
| 3 Qualität der vorgeschlagenen Lösung | 9 | 9 |
| 4 Mathematische und wissenschaftliche Modellierung | 8 | 8 |
| 5 Ableitung neuer Ansätze | 9 | 9 |
| 6 Wissenschaftliche Qualität | 8 | 8 |
| 8 Klare Erklärungen | 9 | 8 |
| 9 Kritische Diskussion | 9 | 9 |
| 10 Struktur und Juryführung | 9 | 9 |
| 11 Format, Zitation und D4RT-Vergleich | 8 | 8 |
| 12a Schriftliche Bereitschaft | 8 | 8 |

## Ergebnis

Die Stoppregel ist nicht erfüllt. Kein Reviewer vergibt eine 10. Die Punktzahlen werden nicht gemittelt und nicht auf eine neue Revision übertragen.

## DeepSeek, materielle Befunde

- Teilstromszenarien skalieren den Notstrom nicht mit dem tatsächlichen betroffenen Fluss. Auch H2 verwendet die falsche Referenztechnologie.
- Abbildung 1 bezeichnet die Temperaturachse als Tiefe.
- Die Schlussfolgerung enthält nicht das geforderte Statement zu Verbesserungsmöglichkeiten bei mehr Bearbeitungszeit.
- Weitere Befunde betreffen H3 ohne Notstrom, den Manifestumfang, „Wärmeabfuhr“ in der Zusammenfassung und den URL-Bruch in Quelle [19].

## Kimi, materielle Befunde

- Jahr 0 enthält einen zusätzlichen Betriebs- und Wartungsposten, sodass die 25-Jahres-Rechnung 26 Betriebsjahre umfasst.
- Verteilungsfamilien, Parameter und Seed der Monte-Carlo-Ziehungen fehlen im Paper.
- Dieselbe falsche Achsenbezeichnung ist auch hier stopprelevant.
- Als Restrisiko bleibt die H2-Topologie ausdrücklich zu klären. Die Überarbeitung verwendet einen separaten Sekundärkreislauf und hält den Quellstrom geschlossen.

## Nachbearbeitung

Die Befundzuordnung steht in `review/revisions.md`. Eine neue Revision muss Modell, PDF, Seitenbilder und Archivreproduktion erneut prüfen. Frühere Punktzahlen gelten nicht für diese neue Revision.
