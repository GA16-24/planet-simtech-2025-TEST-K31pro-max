# Archivreproduktion Runde 6

Geprüft wurde am 08.11.2026 der Kandidat `a963e211813cb5bb4b34dd0e6c5b77bb6882d969` vor dem späteren Dokumentations- und Freeze-Commit. Die Arbeitskopie war bei `git archive` sauber.

## Befehle und Umgebung

Eine frische Verzeichniskopie entstand mit `git archive a963e211813cb5bb4b34dd0e6c5b77bb6882d969`. Die vorhandene `.venv` wurde als Referenzumgebung in diese Kopie verknüpft. Danach liefen in dieser Reihenfolge:

```bash
make model test report
make review-package
make verify
```

Alle 13 Modelltests bestanden. Die Berichts-, Präsentations-, Zusammenfassungs- und Repositoryprüfungen des vorhandenen `make verify` bestanden ebenfalls. Die Präsentationsdateien sind historische Bestandteile des Repositories, aber nicht mehr Lieferumfang. Ihr Prüferfolg ersetzt keine erneute Erzeugung und wird nicht als aktuelle Finalbereitschaft ausgegeben.

## Vergleich mit dem ursprünglichen Arbeitsbaum

36 von 36 verglichenen Paperartefakten sind byteweise identisch:

- alle Dateien unter `output/model/`, einschließlich Ergebnissen, Jahresreihen, Manifest und Monte-Carlo-Stichproben,
- `output/pdf/TEST-K31pro-max.pdf` und `output/verification_summary.json`,
- alle erzeugten LaTeX-Tabellen sowie Berichtsfiguren als PDF und PNG,
- `review/rendered/report_contact.png` und alle zwölf Seitenbilder unter `review/rendered/report_pages/`.

Die PDF hat den SHA-256-Hash `c308a8facad232227c1cfaa83a562be4df9de81fc33fe263e7f287556a114d58`.

Das Ergebnis belegt die Reproduktion des Research Paper in derselben Referenzumgebung. Es belegt keine Neuinstallation der Abhängigkeiten auf einem fremden Rechner, keine externe wissenschaftliche Validierung und keine menschliche Prüfung. Der temporäre Archivpfad wurde nach dem erfolgreichen Vergleich entfernt.
