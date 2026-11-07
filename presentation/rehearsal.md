# Dokumentierte Zeitprobe

Technische Laufzeitmessung am 2026-11-07 mit `ffprobe` an der tatsächlich erzeugten MP4-Datei.

| Folie | Sprache in s | Segment in s | Summe in s |
| --- | ---: | ---: | ---: |
| 1 | 19.51 | 19.86 | 19.86 |
| 2 | 26.17 | 26.52 | 46.39 |
| 3 | 22.43 | 22.78 | 69.17 |
| 4 | 27.89 | 28.24 | 97.41 |
| 5 | 38.26 | 38.61 | 136.02 |
| 6 | 32.79 | 33.14 | 169.16 |
| 7 | 34.00 | 34.35 | 203.51 |
| 8 | 33.76 | 34.11 | 237.62 |
| 9 | 28.12 | 28.47 | 266.09 |
| 10 | 23.70 | 24.05 | 290.14 |

Gesamtdauer der fertigen MP4-Datei: 290.232 s, entsprechend 4:50.2 min.
Offizielles Maximum: 300 s. Interne Produktionsgrenze: 295 s. Ergebnis: bestanden.

Die Zeitprobe misst die reale synthetische Sprachfassung und die kodierte Videodatei. Sie ist keine behauptete menschliche Live-Probe. Vor einer echten Finalteilnahme müssen die präsentierenden Personen eine eigene Probe mit Rollenverteilung, Technik und Fragen durchführen und dokumentieren.

Die VTT-Satzzeiten werden proportional zur Wortzahl der Sprechtexte und zur gemessenen Audiodauer berechnet. Sie sind nicht durch Forced Alignment verifiziert. Vor einer Abgabe sind sie manuell zu prüfen.

Die zusätzliche Echtzeit-Wiedergabe und ihre Messung werden nach dem Export in diesem Dokument ergänzt. Die Integritätsprüfung durch Decodierung steht in `output/presentation/verification.json`.

## Echtzeit-Wiedergabeprobe

Am 2026-11-07 wurde die vollständige MP4-Datei mit `/usr/bin/time -p ffmpeg -v error -re -i output/presentation/Blautopf_Finale.mp4 -f null -` in Echtzeit dekodiert. Der Befehl endete fehlerfrei. `/usr/bin/time` maß `real 289.67 s`, `user 65.51 s` und `sys 2.37 s`. Die Dateidauer beträgt 290.232 s. Die gemessene Gesamtzeit betrug 289.679 s. Die geringe Abweichung durch Start und Ende der Prozessmessung ist plausibel. Ergebnis: bestanden.

Die Integritätsprüfung durch Decodierung steht zusätzlich in `output/presentation/verification.json`.
