# Archivreproduktion Runde 11

Geprüft wurde am 08.11.2026 der Kandidat `94736f771aea1db20d8c7eeca5ded11d7ff42389` vor dem späteren Dokumentations- und Freeze-Commit. Die Arbeitskopie war bei `git archive` sauber.

## Befehle und Umgebung

Eine frische Verzeichniskopie entstand mit `git archive 94736f771aea1db20d8c7eeca5ded11d7ff42389`. Die vorhandene `.venv` wurde als Referenzumgebung in diese Kopie verknüpft. Danach liefen in dieser Reihenfolge:

```bash
make model test report
make review-package
make verify
```

Alle 23 Modelltests bestanden. Die Berichts-, Präsentations-, Zusammenfassungs- und Repositoryprüfungen des vorhandenen `make verify` bestanden ebenfalls. Die Präsentationsdateien sind historische Bestandteile des Repositories, aber nicht mehr Lieferumfang. Ihr Prüferfolg ersetzt keine erneute Erzeugung und wird nicht als aktuelle Finalbereitschaft ausgegeben. Der Freeze-Nachweis weist die Paperbefehle und diese Abgrenzung separat aus.

## Vergleich mit dem ursprünglichen Arbeitsbaum

39 von 39 verglichenen Paperartefakten sind byteweise identisch:

- alle Dateien unter `output/model/`, einschließlich Ergebnissen, Jahresreihen, Manifest und Monte-Carlo-Stichproben für H1 und H8,
- `output/pdf/TEST-K31pro-max.pdf` und `output/verification_summary.json`,
- alle erzeugten LaTeX-Tabellen einschließlich der H8-Bilanz sowie Berichtsfiguren als PDF und PNG,
- `review/rendered/report_contact.png` und alle vierzehn Seitenbilder unter `review/rendered/report_pages/`.

Die PDF hat den SHA-256-Hash `38ff4f88b7b34a0d060773bc815de99c2adaa450be84169aa21afe17e47d09af`.

Das Ergebnis belegt die Reproduktion des Research Paper in derselben Referenzumgebung. Es belegt keine Neuinstallation der Abhängigkeiten auf einem fremden Rechner, keine externe wissenschaftliche Validierung und keine menschliche Prüfung. Der temporäre Archivpfad wurde nach dem erfolgreichen Vergleich entfernt.
