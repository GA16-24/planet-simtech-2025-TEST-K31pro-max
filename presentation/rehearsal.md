# Dokumentierte Zeitprobe

Technische Laufzeitmessung am 2026-11-07 mit `ffprobe` an der tatsächlich erzeugten MP4-Datei.

| Folie | Sprache in s | Segment in s | Summe in s |
| --- | ---: | ---: | ---: |
| 1 | 20.00 | 20.35 | 20.35 |
| 2 | 26.83 | 27.18 | 47.52 |
| 3 | 22.99 | 23.34 | 70.87 |
| 4 | 28.58 | 28.93 | 99.80 |
| 5 | 33.84 | 34.19 | 133.99 |
| 6 | 31.76 | 32.11 | 166.09 |
| 7 | 34.85 | 35.20 | 201.29 |
| 8 | 34.60 | 34.95 | 236.25 |
| 9 | 28.82 | 29.17 | 265.42 |
| 10 | 24.29 | 24.64 | 290.06 |

Gesamtdauer der fertigen MP4-Datei: 290.175 s, entsprechend 4:50.2 min.
Offizielles Maximum: 300 s. Interne Produktionsgrenze: 295 s. Ergebnis: bestanden.

Die Zeitprobe misst die reale synthetische Sprachfassung und die kodierte Videodatei. Sie ist keine behauptete menschliche Live-Probe. Vor einer echten Finalteilnahme müssen die präsentierenden Personen eine eigene Probe mit Rollenverteilung, Technik und Fragen durchführen und dokumentieren.

Die VTT-Satzzeiten werden proportional zur Wortzahl der Sprechtexte und zur gemessenen Audiodauer berechnet. Sie sind nicht durch Forced Alignment verifiziert. Vor einer Abgabe sind sie manuell zu prüfen.

Die zusätzliche Echtzeit-Wiedergabe und ihre Messung werden nach dem Export in diesem Dokument ergänzt. Die Integritätsprüfung durch Decodierung steht in `output/presentation/verification.json`.

## Echtzeit-Wiedergabeprobe

Am 2026-11-07 wurde die vollständige MP4-Datei mit `/usr/bin/time -p ffmpeg -v error -re -i /Users/macbook_air_m1/.t3/scratch/2026-11-07-create-a-new-separate-github-162aa05c/planet-simtech-2025-TEST-K31pro-max/output/presentation/Blautopf_Finale.mp4 -f null -` in Echtzeit dekodiert. Der Befehl endete fehlerfrei. `/usr/bin/time` maß `real 289.62 s`, `user 59.75 s` und `sys 2.16 s`. Die Dateidauer beträgt 290.175 s. Die gemessene Gesamtzeit betrug 289.637 s. Die geringe Abweichung durch Start und Ende der Prozessmessung ist plausibel. Ergebnis: bestanden.

Die Integritätsprüfung durch Decodierung steht zusätzlich in `output/presentation/verification.json`.
