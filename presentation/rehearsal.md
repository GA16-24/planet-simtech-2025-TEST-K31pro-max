# Dokumentierte Zeitprobe

Technische Laufzeitmessung am 2026-11-07 mit `ffprobe` an der tatsächlich erzeugten MP4-Datei.

| Folie | Sprache in s | Segment in s | Summe in s |
| --- | ---: | ---: | ---: |
| 1 | 17.05 | 17.40 | 17.40 |
| 2 | 28.45 | 28.80 | 46.20 |
| 3 | 28.00 | 28.35 | 74.54 |
| 4 | 26.88 | 27.23 | 101.77 |
| 5 | 44.94 | 45.29 | 147.06 |
| 6 | 28.39 | 28.74 | 175.80 |
| 7 | 38.47 | 38.82 | 214.62 |
| 8 | 29.05 | 29.40 | 244.02 |
| 9 | 25.74 | 26.09 | 270.11 |
| 10 | 19.60 | 19.95 | 290.07 |

Gesamtdauer der fertigen MP4-Datei: 290.132 s, entsprechend 4:50.1 min.
Offizielles Maximum: 300 s. Interne Produktionsgrenze: 295 s. Ergebnis: bestanden.

Die Zeitprobe misst die reale synthetische Sprachfassung und die kodierte Videodatei. Sie ist keine behauptete menschliche Live-Probe. Vor einer echten Finalteilnahme müssen die präsentierenden Personen eine eigene Probe mit Rollenverteilung, Technik und Fragen durchführen und dokumentieren.

Die zusätzliche Echtzeit-Wiedergabe und ihre Messung werden nach dem Export in diesem Dokument ergänzt. Die Integritätsprüfung durch Decodierung steht in `output/presentation/verification.json`.

## Echtzeit-Wiedergabeprobe

Am 2026-11-07 wurde die vollständige MP4-Datei mit `/usr/bin/time -p ffmpeg -v error -re -i /Users/macbook_air_m1/.t3/scratch/2026-11-07-create-a-new-separate-github-162aa05c/planet-simtech-2025-TEST-K31pro-max/output/presentation/Blautopf_Finale.mp4 -f null -` in Echtzeit dekodiert. Der Befehl endete fehlerfrei. `/usr/bin/time` maß `real 289.58 s`, `user 62.14 s` und `sys 2.23 s`. Die Dateidauer beträgt 290.132 s. Die gemessene Gesamtzeit betrug 289.584 s. Die geringe Abweichung durch Start und Ende der Prozessmessung ist plausibel. Ergebnis: bestanden.

Die Integritätsprüfung durch Decodierung steht zusätzlich in `output/presentation/verification.json`.
