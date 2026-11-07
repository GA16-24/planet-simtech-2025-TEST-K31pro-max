# Reproduktionsnachweis Runde 3

Geprüft wurde der Kandidaten-Commit `babe04c` in einer neuen, aus `git archive` erzeugten Kopie außerhalb des ursprünglichen Arbeitsbaums. Die Prüfung wurde vom implementierenden Agenten durchgeführt und ist keine unabhängige Council-Stimme.

## Verfahren

Der Kandidaten-Commit wurde mit `git archive babe04c | tar -x -C <ziel>` entpackt. Die aus `requirements.lock.txt` installierte Python-Umgebung wurde eingebunden. Darin liefen `make model`, `make test`, `make report` und `make verify`.

`build_report.sh` setzt `SOURCE_DATE_EPOCH` standardmäßig auf den Berichtstag 07.11.2026, damit das PDF-Erstellungsdatum reproduzierbar ist. Ein erster Vergleich hatte gezeigt, dass sich ohne diese Festlegung nur die PDF-Metadaten ändern. Der finale Vergleich erfolgte mit derselben festen Datumsangabe.

## Ergebnisse

- Alle zehn Modelltests bestanden.
- `results.json`, `hybrid_schedule.csv`, `sensitivity.csv` und sämtliche Dateien in `report/generated/` waren byteweise identisch.
- Auch `output/pdf/TEST-K31pro-max.pdf` und `output/verification_summary.json` waren nach dem Neuaufbau byteweise identisch.
- Die Berichtsprüfung bestätigte 13 Seiten, davon 7 Haupttextseiten und 5 Seiten für Literatur und Anhang.
- Die Präsentationsprüfung bestätigte die vorhandene MP4, Codecs, SAR, DAR, Segmente und Frames in der Kopie.
- Die Repositoryprüfung bestätigte Pflichtdateien, Quellenregister, TSV-Struktur und Modellhashes.

Die Präsentation wurde in der Hauptarbeitskopie vollständig aus Folien und neuer synthetischer Sprachausgabe erzeugt. Die MP4 dauert 290,025458 s; die vollständige Echtzeitdecodierung endete nach 289,46 s. In der Archivkopie wurde sie nicht erneut kodiert, sondern zusammen mit dieser aktuellen Wiedergabeprobe geprüft. Eine menschliche Live-Darbietung fand nicht statt.

Die Kopie wurde nach der Prüfung entfernt. Der Nachweis betrifft reproduzierbare Berechnungen und Artefakte, keine Feldvalidierung oder externe wissenschaftliche Bewertung.
