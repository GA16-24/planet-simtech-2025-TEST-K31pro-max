# Scorecard Runde 11

Revision: `a8368ef77e14dcea7afb19c61b7f3b664c1344c9`, 207 Dateien. Der reproduzierte Paperkandidat ist `94736f771aea1db20d8c7eeca5ded11d7ff42389`. Beide Reviewer prüften unabhängig und read-only mit `reasoning_effort=max` beziehungsweise `thinking=max`. Frühere Rohberichte und Scorecards wurden nicht verwendet. Die vollständigen Begründungen stehen in `deepseek.md` und `kimi.md`, die Taskergebnisse in `deepseek_result.json` und `kimi_result.json`.

Der Prüfumfang ist der Research Paper mit den Kriterien 1, 2, 3, 4, 5, 6, 8, 9, 10, 11 und 12a. Kriterium 12b gehört nicht mehr zum Lieferumfang.

| Kriterium | DeepSeek-V4.1-Flash | Kimi K3.1 Pro |
| --- | ---: | ---: |
| 1 Qualität der Argumentation | 9 | 9 |
| 2 Vorgehen und Methodik | 9 | 9 |
| 3 Qualität der vorgeschlagenen Lösung | 9 | 9 |
| 4 Mathematische und wissenschaftliche Modellierung | 9 | 10 |
| 5 Ableitung neuer Ansätze | 9 | 9 |
| 6 Wissenschaftliche Qualität | 9 | 9 |
| 8 Klare Erklärungen | 8 | 9 |
| 9 Kritische Diskussion | 9 | 9 |
| 10 Struktur und Juryführung | 9 | 9 |
| 11 Format, Zitation und D4RT-Vergleich | 8 | 9 |
| 12a Schriftliche Bereitschaft | 9 | 10 |

## Ergebnis

Die Stoppregel ist nicht erfüllt. Kimi vergibt für die Modellierung und die technische Bereitschaft jeweils 10 und dokumentiert eigene erfolglose substanzielle Fehlersuchen. DeepSeek vergibt keine 10. Die Punktzahlen werden nicht gemittelt und nicht auf eine neue Revision übertragen.

## DeepSeek, materielle Befunde

- Der H2-Satz muss drei Zyklen mit 12,48 und fünf Zyklen mit 10,40 Mio. m³ eindeutig zuordnen. Kriterium 8 bleibt dadurch bei 8.
- H3 enthält die 95-Mio.-€-Fixkostenbasis, nicht nur Pumpen und Wasser. Die Teilstrom-Fixkostenskalierung ist im Paper zu erklären.
- Anhang A zeigt zwei große vertikale Leerräume. Tabelle 1 ordnet den COP fälschlich der Strompreisquelle zu und bricht die Luftbezeichnung unruhig. Kriterium 11 bleibt dadurch bei 8.
- Kleinere Hinweise betreffen zwei gleiche MW-Header, die Modulllast, die nicht ausgelegte Nassrückkühlung und die Näherung des sekundären Wärmekapazitätsstroms.

## Kimi, Ergebnis und optionale Hinweise

- Alle elf Kriterien erreichen mindestens 9, Kriterien 4 und 12a erreichen 10. Es gibt keine materiellen Mängel.
- Die eigene Fehlersuche umfasst 669 numerische Prüfpunkte, die Manifest- und Freeze-Hashes, alle 10.000 H8-Ziehungen und vier analytisch gelöste Ausfallfälle.
- Ein Prozessschema und eigene Achsentitel in Abbildung 3 sind optionale Verbesserungen, keine Mängel.

## Nachbearbeitung

Die nächste Revision soll die verbleibenden Klarheits- und Layoutbefunde ohne Änderung der bestätigten physikalischen Bilanzen schließen. `review/revisions.md` ordnet die Umsetzung zu. Neue Punktzahlen werden erst nach erneuter Archivreproduktion und unabhängiger Review erhoben.
