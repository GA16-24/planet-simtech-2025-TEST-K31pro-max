# Archivreproduktion Runde 7

Geprüft wurde am 08.11.2026 der Kandidat `1878af8f0a66802696b65243ea4db759fd40c919` vor dem späteren Dokumentations- und Freeze-Commit. Die Arbeitskopie war bei `git archive` sauber.

## Befehle und Umgebung

Eine frische Verzeichniskopie entstand mit `git archive 1878af8f0a66802696b65243ea4db759fd40c919`. Die vorhandene `.venv` wurde als Referenzumgebung in diese Kopie verknüpft. Danach liefen in dieser Reihenfolge:

```bash
make model test report
make review-package
make verify
```

Alle 16 Modelltests bestanden. Die Berichts-, Präsentations-, Zusammenfassungs- und Repositoryprüfungen des vorhandenen `make verify` bestanden ebenfalls. Die Präsentationsdateien sind historische Bestandteile des Repositories, aber nicht mehr Lieferumfang. Ihr Prüferfolg ersetzt keine erneute Erzeugung und wird nicht als aktuelle Finalbereitschaft ausgegeben.

## Vergleich mit dem ursprünglichen Arbeitsbaum

36 von 36 verglichenen Paperartefakten sind byteweise identisch:

- alle Dateien unter `output/model/`, einschließlich Ergebnissen, Jahresreihen, Manifest und Monte-Carlo-Stichproben,
- `output/pdf/TEST-K31pro-max.pdf` und `output/verification_summary.json`,
- alle erzeugten LaTeX-Tabellen sowie Berichtsfiguren als PDF und PNG,
- `review/rendered/report_contact.png` und alle zwölf Seitenbilder unter `review/rendered/report_pages/`.

Die PDF hat den SHA-256-Hash `44a5751389b6ae580ba9d560ed6292867a78f188f035fb4e66705efa7bd80da7`.

Das Ergebnis belegt die Reproduktion des Research Paper in derselben Referenzumgebung. Es belegt keine Neuinstallation der Abhängigkeiten auf einem fremden Rechner, keine externe wissenschaftliche Validierung und keine menschliche Prüfung. Der temporäre Archivpfad wurde nach dem erfolgreichen Vergleich entfernt.
