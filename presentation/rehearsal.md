# Dokumentierte Zeitprobe

Technische Laufzeitmessung am 2026-11-07 mit `ffprobe` an der tatsächlich erzeugten MP4-Datei.

| Folie | Sprache in s | Segment in s | Summe in s |
| --- | ---: | ---: | ---: |
| 1 | 18.16 | 18.51 | 18.51 |
| 2 | 30.30 | 30.65 | 49.16 |
| 3 | 29.82 | 30.17 | 79.33 |
| 4 | 28.62 | 28.97 | 108.30 |
| 5 | 36.65 | 37.00 | 145.30 |
| 6 | 29.90 | 30.25 | 175.55 |
| 7 | 34.96 | 35.31 | 210.86 |
| 8 | 29.63 | 29.98 | 240.84 |
| 9 | 27.41 | 27.76 | 268.61 |
| 10 | 20.88 | 21.23 | 289.83 |

Gesamtdauer der fertigen MP4-Datei: 289.934 s, entsprechend 4:49.9 min.
Offizielles Maximum: 300 s. Interne Produktionsgrenze: 295 s. Ergebnis: bestanden.

Die Zeitprobe misst die reale synthetische Sprachfassung und die kodierte Videodatei. Sie ist keine behauptete menschliche Live-Probe. Vor einer echten Finalteilnahme müssen die präsentierenden Personen eine eigene Probe mit Rollenverteilung, Technik und Fragen durchführen und dokumentieren.

## Echtzeit-Wiedergabeprobe

Am 2026-11-07 wurde die vollständige MP4-Datei mit `/usr/bin/time -p ffmpeg -v error -re -i /Users/macbook_air_m1/.t3/scratch/2026-11-07-create-a-new-separate-github-162aa05c/planet-simtech-2025-TEST-K31pro-max/output/presentation/Blautopf_Finale.mp4 -f null -` in Echtzeit dekodiert. Der Befehl endete fehlerfrei. `/usr/bin/time` maß `real 289.38 s`, `user 64.65 s` und `sys 2.35 s`. Die Dateidauer beträgt 289.934 s. Die gemessene Gesamtzeit betrug 289.407 s. Die geringe Abweichung durch Start und Ende der Prozessmessung ist plausibel. Ergebnis: bestanden.

Die Integritätsprüfung durch Decodierung steht zusätzlich in `output/presentation/verification.json`.
