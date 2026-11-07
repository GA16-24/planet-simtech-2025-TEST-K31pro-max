# Dokumentierte Zeitprobe

Technische Laufzeitmessung am 2026-11-07 mit `ffprobe` an der tatsächlich erzeugten MP4-Datei.

| Folie | Sprache in s | Segment in s | Summe in s |
| --- | ---: | ---: | ---: |
| 1 | 20.57 | 20.92 | 20.92 |
| 2 | 27.60 | 27.95 | 48.87 |
| 3 | 23.65 | 24.00 | 72.87 |
| 4 | 29.40 | 29.75 | 102.62 |
| 5 | 34.81 | 35.16 | 137.79 |
| 6 | 29.70 | 30.05 | 167.84 |
| 7 | 35.85 | 36.20 | 204.04 |
| 8 | 30.23 | 30.58 | 234.62 |
| 9 | 29.65 | 30.00 | 264.62 |
| 10 | 24.99 | 25.34 | 289.95 |

Gesamtdauer der fertigen MP4-Datei: 290.025 s, entsprechend 4:50.0 min.
Offizielles Maximum: 300 s. Interne Produktionsgrenze: 295 s. Ergebnis: bestanden.

Die Zeitprobe misst die reale synthetische Sprachfassung und die kodierte Videodatei. Sie ist keine behauptete menschliche Live-Probe. Vor einer echten Finalteilnahme müssen die präsentierenden Personen eine eigene Probe mit Rollenverteilung, Technik und Fragen durchführen und dokumentieren.

Die VTT-Satzzeiten werden proportional zur Wortzahl der Sprechtexte und zur gemessenen Audiodauer berechnet. Sie sind nicht durch Forced Alignment verifiziert. Vor einer Abgabe sind sie manuell zu prüfen.

Die zusätzliche Echtzeit-Wiedergabe und ihre Messung werden nach dem Export in diesem Dokument ergänzt. Die Integritätsprüfung durch Decodierung steht in `output/presentation/verification.json`.

## Echtzeit-Wiedergabeprobe

Am 2026-11-07 wurde die vollständige MP4-Datei mit `/usr/bin/time -p ffmpeg -v error -re -i /Users/macbook_air_m1/.t3/scratch/2026-11-07-create-a-new-separate-github-162aa05c/planet-simtech-2025-TEST-K31pro-max/output/presentation/Blautopf_Finale.mp4 -f null -` in Echtzeit dekodiert. Der Befehl endete fehlerfrei. `/usr/bin/time` maß `real 289.46 s`, `user 63.68 s` und `sys 2.27 s`. Die Dateidauer beträgt 290.025 s. Die gemessene Gesamtzeit betrug 289.469 s. Die geringe Abweichung durch Start und Ende der Prozessmessung ist plausibel. Ergebnis: bestanden.

Die Integritätsprüfung durch Decodierung steht zusätzlich in `output/presentation/verification.json`.
