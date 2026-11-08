# Archivreproduktion Design-Runde 15

Ausgangskandidat ist `4f1cc7ae55055828eacbf329e25fe21bcd4a40b1`. Der Dokumentationscommit mit dieser Reproduktionsdatei und der Entscheidungsaufzeichnung wird selbst mit `git archive HEAD` erzeugt und geprüft. Der genaue geprüfte Review-Commit steht in `revision.json`. Damit bezieht sich die Prüfung nicht nur auf den Ausgangskandidaten.

## Befehle und Umgebung

Die Arbeitskopie ist bei `git archive` sauber. Die vorhandene `.venv` wird als Referenzumgebung in die frische Archivkopie verknüpft. Danach laufen in dieser Reihenfolge:

```bash
make model test report
make review-package
make verify
```

Alle 24 Modelltests müssen bestehen. Die Präsentationsdateien sind historische Bestandteile des Repositories, aber nicht mehr Lieferumfang. Ihr Prüferfolg ersetzt keine erneute Erzeugung und wird nicht als aktuelle Finalbereitschaft ausgegeben. Der Freeze-Nachweis weist die Paperbefehle und diese Abgrenzung separat aus.

## Vergleich mit dem ursprünglichen Arbeitsbaum

Verglichen werden 39 Paperartefakte:

- alle Dateien unter `output/model/`, einschließlich Ergebnissen, Jahresreihen, Manifest und Monte-Carlo-Stichproben für H1 und H8,
- `output/pdf/TEST-K31pro-max.pdf` und `output/verification_summary.json`,
- alle erzeugten LaTeX-Tabellen einschließlich der H8-Bilanz sowie Berichtsfiguren als PDF und PNG,
- `review/rendered/report_contact.png` und alle vierzehn Seitenbilder unter `review/rendered/report_pages/`.

Der Vergleich verlangt bytegleiche Dateien in allen 39 Fällen. Der PDF-Hash wird beim Lauf protokolliert und ist zusätzlich in `revision.json` enthalten.

Das Ergebnis belegt die Reproduktion des Research Paper in derselben Referenzumgebung. Es belegt keine Neuinstallation der Abhängigkeiten auf einem fremden Rechner, keine externe wissenschaftliche Validierung und keine menschliche Prüfung. Der temporäre Archivpfad wird nach dem erfolgreichen Vergleich entfernt.
