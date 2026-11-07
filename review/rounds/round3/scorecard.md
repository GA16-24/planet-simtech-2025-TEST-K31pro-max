# Scorecard Runde 3

Revision: `77c1f972df9c67a00354e395ce31f27fd0c1b95c`, 136 Dateien. Beide Reviewer prüften unabhängig mit `reasoning_effort=max` beziehungsweise `thinking=max`, ohne die jeweils andere Punktzahl oder frühere Scorecards zu lesen. Beide arbeiteten read-only mit `runtimeMode=full-access`.

| Kriterium | DeepSeek-V4.1-Flash | Kimi K3.1 Pro |
| --- | ---: | ---: |
| 1 Qualität der Argumentation | 8 | 8 |
| 2 Vorgehen und Methodik | 8 | 8 |
| 3 Qualität der vorgeschlagenen Lösung | 8 | 8 |
| 4 Mathematische und wissenschaftliche Modellierung | 8 | 8 |
| 5 Ableitung neuer Ansätze | 9 | 9 |
| 6 Wissenschaftliche Qualität | 8 | 8 |
| 8 Klare Erklärungen | 8 | 8 |
| 9 Kritische Diskussion | 9 | 8 |
| 10 Struktur und Juryführung | 8 | 8 |
| 11 Format, Zitation und D4RT-Vergleich | 6 | 7 |
| 12a Schriftliche Bereitschaft | 7 | 7 |
| 12b Finale Bereitschaft | 8 | 8 |

## Ergebnis

Die Stoppregel ist nicht erfüllt. Kein Reviewer vergibt eine 10. Die Rohberichte stehen in `deepseek.md` und `kimi.md`.

## Gemeinsame materielle Einwände

- Ein unmaskiertes Prozentzeichen kürzt die Zusammenfassung im tatsächlichen PDF. Außerdem ist sie zu fachsprachlich.
- Die dynamische Ausfallrechnung gilt für 2,3 m³/s, nicht für den p90-Auslegungsfall mit 4,7 m³/s.
- Kapazitätsgrafiken und Kennzahlen sind nicht konsistent mit dem Text und der tatsächlichen Endkapazität.
- Standort, vollständige Karsterfassung, Netzanschluss, COP und Feldvalidierung bleiben offen.
- Offizielle Team-ID, menschliche Fachprüfung, Medienfreigabe, Finalisten-E-Mail und echte Live-Probe fehlen weiterhin.

## Zusätzliche Einwände und Dissens

- DeepSeek findet ungültige WebVTT-Zeitstempel mit Komma statt Punkt, eine halbleere Schlussseite, URL-Umbrüche, Dezimalpunkte in Diagrammen und Layoutprobleme bei Überschriften.
- Kimi fordert eine Konvergenzprobe des p90-Ausfallmodells, temperaturabhängige Stoffwerte für die Detailauslegung und eine klarere Kapazitätsgrafik.
- DeepSeek beanstandet den Zeitstempel in `reproduction.md`, weil er sich auf `babe04c` statt auf den exakten Freeze-Commit bezieht.
- Beide Reviewer sehen einen begrenzten Szenarioentwurf, nicht eine nachgewiesene reale Anlage. Menschliche Aufgaben werden nicht durch Council-Punktzahlen ersetzt.
- DeepSeek dokumentiert versehentlichen Kontakt mit Teilen der früheren Reviewdateien und keine Übernahme ihrer Punktzahlen. Kimi dokumentiert, dass diese Dateien nicht geöffnet oder verwendet wurden. Diese Expositionen werden zusätzlich im Ausschlussprotokoll erfasst.

Die Bearbeitung erfolgt in `review/revisions.md` und einer neuen Revision. Frühere Punktzahlen werden nicht übertragen.
