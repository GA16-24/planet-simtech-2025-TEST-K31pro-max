# Scorecard Runde 5

Revision: `e821bf60ef9fe637a5c5915a50d7748ab829c46c`, 155 Dateien. Beide Reviewer prüften unabhängig und read-only mit `reasoning_effort=max` beziehungsweise `thinking=max`. Keine früheren Rohberichte oder Scorecards wurden verwendet. Die vollständigen Begründungen stehen in `deepseek.md` und `kimi.md`.

| Kriterium | DeepSeek-V4.1-Flash | Kimi K3.1 Pro |
| --- | ---: | ---: |
| 1 Qualität der Argumentation | 8 | 9 |
| 2 Vorgehen und Methodik | 8 | 9 |
| 3 Qualität der vorgeschlagenen Lösung | 9 | 8 |
| 4 Mathematische und wissenschaftliche Modellierung | 8 | 9 |
| 5 Ableitung neuer Ansätze | 9 | 9 |
| 6 Wissenschaftliche Qualität | 8 | 9 |
| 8 Klare Erklärungen | 8 | 9 |
| 9 Kritische Diskussion | 9 | 9 |
| 10 Struktur und Juryführung | 8 | 9 |
| 11 Format, Zitation und D4RT-Vergleich | 7 | 9 |
| 12a Schriftliche Bereitschaft | 8 | 9 |
| 12b Finale Bereitschaft | 8 | 8 |

## Ergebnis

Die Stoppregel ist nicht erfüllt. Kein Reviewer vergibt eine 10. Die Punktzahlen werden nicht gemittelt und nicht auf eine neue Revision übertragen.

## DeepSeek, materielle Befunde

- `coupled_npv` skaliert die variable Investition am Auslegungspunkt doppelt: 7,421 statt 5,449 Mrd. €. Der bisherige Test prüft nur den Mittelstrompunkt.
- Der Siedeschutz enthält trotz nur 1,07 MW Antriebsleistung einen vollen Notstromposten von rund 60 Mio. €.
- Die Verdunstungsenthalpie von 2,45 MJ/kg passt eher zu 20 °C als zum Prozess von 100 auf 32 °C.
- Eine fast leere Seite, geteilte Literaturangaben, gequetschte Tabelle, Dezimalkomma im Mathematiksatz und falsche Anführungszeichen sind sichtbar.
- Abbildung 3 steht unter Anhang B statt C, und die Zahl 1053,3 kollidiert auf Folie 8 mit einer Achsenmarke.
- Weitere Befunde betreffen die 38,57-%-Formulierung, die Speicherrechnung, die Hochwasserstatistik, Messunsicherheit, veraltete Hinweise und die Cuezahl.

## Kimi, materielle Befunde und offene Grenzen

- Kriterium 3 bleibt bei 8, weil Standort, Netzzusage, Herstellerkurven und vollständige Karsterfassung fehlen. Diese reale Machbarkeit darf nicht behauptet werden.
- Kriterium 12b bleibt bei 8, weil menschliche Hör- und Sichtfreigabe, manuelle VTT-Freigabe, Rechtefreigabe und echte Teamprobe fehlen.
- Kleinere Befunde betreffen 62 statt 63 Cues und den Verweis auf nicht exportierte Jahresreihen für Prognosezeiten.

Die physikalische Kernlösung bleibt ein begrenzter Szenarioentwurf, keine Baufreigabe. Offizielle Team-ID, menschliche Prüfung und externe technische Nachweise sind weiterhin offen. Die Bearbeitung erfolgt in `review/revisions.md` und einer neuen Revision.
