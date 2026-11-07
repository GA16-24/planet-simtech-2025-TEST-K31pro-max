# Reproduktionsnachweis Runde 2

Geprüft wurde Commit `cc25cc903681ebbc4d6865309236885f729d6d77` außerhalb des ursprünglichen Arbeitsbaums. Die Prüfung wurde vom implementierenden Agenten durchgeführt und ist keine unabhängige Council-Stimme.

## Verfahren

Eine neue Kopie wurde mit `git archive cc25cc903681ebbc4d6865309236885f729d6d77 | tar -x -C <ziel>` erzeugt. Die bereits aus `requirements.lock.txt` installierte Python-Umgebung wurde eingebunden. Darin liefen `make model`, `make test` und anschließend `make verify`.

## Ergebnisse

- Alle sieben damaligen Modelltests bestanden.
- `results.json`, `hybrid_schedule.csv`, `sensitivity.csv` und alle Dateien in `report/generated/` waren nach erneuter Berechnung byteweise identisch mit dem eingefrorenen Paket.
- `make verify` bestätigte PDF, MP4, Streams, Modellhashes, Quellenregister und Pflichtdateien in der separaten Kopie.
- Der Bericht umfasste 16 Seiten, davon 10 Haupttextseiten und 5 Seiten für Literatur und Anhang.
- Die geprüfte MP4-Datei dauerte 290,131706 s. Die vorhandene Echtzeitmessung betrug 289,58 s.

Die Kopie wurde nach der Prüfung gelöscht. Der Nachweis betrifft reproduzierbare Berechnungen und vorhandene Artefakte, keine Feldvalidierung oder unabhängige wissenschaftliche Bewertung.

## Festgestellte Prozessabweichung

`verification_summary.py` schrieb damals bei jedem Lauf einen neuen Zeitstempel. Dadurch unterschied sich ein Dateihash vom Commit. Runde 3 ersetzt den Zeitstempel durch einen deterministischen Hash der geprüften Artefakte und vergleicht jede Datei beim Einfrieren direkt mit ihrem Git-Blob.
