# Archivreproduktion Runde 10

Geprüft wurde am 08.11.2026 der Kandidat `3f2324cb7b7323f1a04fbbad82a87c6e48dd8f64` vor dem späteren Dokumentations- und Freeze-Commit. Die Arbeitskopie war bei `git archive` sauber.

## Befehle und Umgebung

Eine frische Verzeichniskopie entstand mit `git archive 3f2324cb7b7323f1a04fbbad82a87c6e48dd8f64`. Die vorhandene `.venv` wurde als Referenzumgebung in diese Kopie verknüpft. Danach liefen in dieser Reihenfolge:

```bash
make model test report
make review-package
make verify
```

Alle 22 Modelltests bestanden. Die Berichts-, Präsentations-, Zusammenfassungs- und Repositoryprüfungen des vorhandenen `make verify` bestanden ebenfalls. Die Präsentationsdateien sind historische Bestandteile des Repositories, aber nicht mehr Lieferumfang. Ihr Prüferfolg ersetzt keine erneute Erzeugung und wird nicht als aktuelle Finalbereitschaft ausgegeben.

## Vergleich mit dem ursprünglichen Arbeitsbaum

40 von 40 verglichenen Paperartefakten sind byteweise identisch:

- alle Dateien unter `output/model/`, einschließlich Ergebnissen, Jahresreihen, Manifest und Monte-Carlo-Stichproben für H1 und H8,
- `output/pdf/TEST-K31pro-max.pdf` und `output/verification_summary.json`,
- alle erzeugten LaTeX-Tabellen einschließlich der H8-Bilanz sowie Berichtsfiguren als PDF und PNG,
- `review/rendered/report_contact.png` und alle fünfzehn Seitenbilder unter `review/rendered/report_pages/`.

Die PDF hat den SHA-256-Hash `c866bb3b42b7b5273e4fc0d286b8e6ecc1db250fc386d2eea022dcdd634869e7`.

Das Ergebnis belegt die Reproduktion des Research Paper in derselben Referenzumgebung. Es belegt keine Neuinstallation der Abhängigkeiten auf einem fremden Rechner, keine externe wissenschaftliche Validierung und keine menschliche Prüfung. Der temporäre Archivpfad wurde nach dem erfolgreichen Vergleich entfernt.
