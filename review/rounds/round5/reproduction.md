# Reproduktionsnachweis Runde 5

Geprüft wurde der exakte Kandidaten-Commit `9d8f4df4983335aed38bbd6cbd717d378ee3eba6` in einer frischen, aus `git archive` erzeugten Kopie. Der implementierende Agent führte die Prüfung durch. Sie ist keine unabhängige Council-Stimme, Feldvalidierung oder menschliche Darbietung.

## Verfahren

Der Befehl `git archive 9d8f4df4983335aed38bbd6cbd717d378ee3eba6 | tar -x -C <neues-ziel>` erzeugte die Kopie. Die Umgebung aus `requirements.lock.txt` wurde über eine Verknüpfung als `.venv` eingebunden. Danach liefen nacheinander:

```bash
make model
make test
make report
bash scripts/build_presentation.sh --regenerate-tts
make review-package
make verify
```

Die Referenzumgebung ist Python 3.14.6, Tectonic 0.17.0, FFmpeg 9.0.2, Poppler 26.10.0 und eSpeak NG 1.52.0. Bericht und Präsentation verwenden `SOURCE_DATE_EPOCH=1794009600`.

## Ergebnisse

- Alle elf Modelltests bestanden. `make report`, `make review-package` und `make verify` bestanden ohne Fehler und ohne Overfull-Warnungen.
- Der Bericht umfasst 12 Seiten, davon 6 Haupttextseiten und 5 Seiten für Literatur und Anhang.
- Alle 41 direkt verglichenen, neu erzeugten Dateien waren byteweise identisch. Dazu gehören Modellergebnisse, Manifest, CSV- und NPZ-Daten, LaTeX-Tabellen, Berichts- und Projektfiguren, Berichts-PDF, Folien-PDF, MP4, WebVTT, Medienprüfung, Folienzeiten, Sprechtext und alle zehn Audiodateien.
- Alle 33 gerasterten PNG-Seiten, Folien und Videoframes waren ebenfalls byteweise identisch.
- SHA-256 des Berichts: `af0883cd95d3aaac9fe342d02f052d7d4368f86599e0a06623f025f4b5051bf3`.
- SHA-256 des Videos: `c80cd24cdc2f7311f9004343db26704bbc15e712c8750b0d78b036a26ac943cf`.
- Die MP4 dauert 290,23175 s. Die Echtzeitdecodierung endete im Hauptarbeitsbaum mit 289,67 s und in der Archivkopie mit 289,66 s. Befehl, Dateidauer, Exitcode und der Status `live_human_delivery=false` stimmen überein. Diese Messungen sind keine menschliche Live-Probe.
- Die Prüfbereiche `report`, `model_validation` und `presentation` in `output/verification_summary.json` stimmen überein. Der Artefakthash und die Wiedergabezeiten können sich wegen der realen Prozesslaufzeit unterscheiden. Der Inhalt des Zeitprotokolls vor der Echtzeitprobe ist identisch.

Die Kopie wurde nach der Prüfung entfernt. Der spätere Freeze-Commit ergänzt diese Dokumentation und die zugehörigen Protokolle. Der geprüfte Kandidaten-Commit enthält bereits alle Modelle, Quellen und Artefakte des Reviewpakets. Menschliche Hör- und Sichtfreigabe, manuelle VTT-Freigabe, Rechteprüfung, offizielle Team-ID, Feldversuche und eine echte Teamprobe bleiben offen.
