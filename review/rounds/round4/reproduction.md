# Reproduktionsnachweis Runde 4

Geprüft wurde der exakte Kandidaten-Commit `85127420f90cc7fc742c5698e78fc1214e262a42` in einer neuen, aus `git archive` erzeugten Kopie. Der implementierende Agent führte die Prüfung durch. Sie ist keine unabhängige Council-Stimme und keine Feldvalidierung.

## Verfahren

Der Befehl `git archive 85127420f90cc7fc742c5698e78fc1214e262a42 | tar -x -C <neues-ziel>` erzeugte die Kopie. Die vorhandene Umgebung aus `requirements.lock.txt` wurde über eine Verknüpfung als `.venv` eingebunden. Danach liefen in dieser Kopie nacheinander:

```bash
make model
make test
make report
make verify
```

Die Berichtserzeugung verwendet `SOURCE_DATE_EPOCH=1794009600`. Der Vergleich erfolgte anschließend direkt zwischen den Dateibytes der Archivkopie und des Hauptarbeitsbaums.

## Ergebnisse

- Alle elf Modelltests bestanden.
- `make report` und `make verify` bestanden ohne Fehler. Der Bericht umfasst 11 Seiten, davon 6 Haupttextseiten und 4 Seiten für Literatur und Anhang.
- Alle 23 verglichenen Dateien waren byteweise identisch: `results.json`, `manifest.json`, `hybrid_schedule.csv`, `sensitivity.csv`, `uncertainty_samples.npz`, der fertige Bericht, `verification_summary.json`, vier erzeugte LaTeX-Tabellen und zwölf PDF- oder PNG-Figuren.
- Der SHA-256-Hash des Berichts ist `9dbdd33b0231b8c27857a61869141a2897c98a847b13f64cf5c82c78c3da08fc`.
- Die Archivkopie bestätigte außerdem die vorhandene MP4, die 62 WebVTT-Cues, die Folien und die Repositorystruktur. Das Video wurde dort nicht erneut kodiert. `make presentation` im Hauptarbeitsbaum erzeugte zuvor das Video und führte danach eine neue Echtzeitwiedergabe durch. Diese endete mit `real 289.62 s`. Es fand keine menschliche Live-Darbietung statt.

Die Kopie wurde nach der Prüfung entfernt. Der Freeze-Commit ergänzt diesen Nachweis zur Version. Der geprüfte Kandidaten-Commit enthält bereits alle Modelle, Quellen und Artefakte, die dem Council vorgelegt werden. Die offenen Standort-, Hersteller-, Genehmigungs- und Menschennachweise werden durch diese Reproduktion nicht ersetzt.
