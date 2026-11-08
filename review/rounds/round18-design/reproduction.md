# Archivreproduktion Design-Runde 18

Ausgangskandidat ist `6d57ea53491cd93261799157eb6ce739de76599a`. Der Dokumentationscommit mit dieser Reproduktionsdatei und der Entscheidungsaufzeichnung wird selbst mit `git archive HEAD` erzeugt und geprüft. Der genaue geprüfte Review-Commit steht in `revision.json`. Damit bezieht sich die Prüfung nicht nur auf den Ausgangskandidaten.

## Befehle und Umgebung

Die Arbeitskopie ist bei `git archive` sauber. Die vorhandene `.venv` wird als Referenzumgebung in die frische Archivkopie verknüpft. Danach laufen in dieser Reihenfolge:

```bash
make model test report
make review-package
make verify
```

Alle 24 Modelltests müssen bestehen. Die Präsentationsdateien sind historische Bestandteile des Repositories, aber nicht mehr Lieferumfang. Ihr Prüferfolg ersetzt keine erneute Erzeugung und wird nicht als aktuelle Finalbereitschaft ausgegeben. Der Freeze-Nachweis weist die Paperbefehle und diese Abgrenzung separat aus.

## Vergleich mit dem ursprünglichen Arbeitsbaum

Verglichen werden 40 Paperartefakte:

- alle Dateien unter `output/model/`, einschließlich Ergebnissen, Jahresreihen, Manifest und Monte-Carlo-Stichproben für H1 und H8,
- `output/pdf/TEST-K31pro-max.pdf` und `output/verification_summary.json`,
- alle erzeugten LaTeX-Tabellen einschließlich der H8-Bilanz sowie Berichtsfiguren als PDF und PNG,
- `review/rendered/report_contact.png` und alle fünfzehn Seitenbilder unter `review/rendered/report_pages/`.

Der Vergleich verlangt bytegleiche Dateien in allen 40 Fällen. Der PDF-SHA-256 des Kandidaten ist `4aaa3d6fe29f8f77ab1906037c642e6cda9f928309de696d22f2bdb051f13388` und ist zusätzlich in `revision.json` enthalten.

Das Ergebnis belegt die Reproduktion des Research Paper in derselben Referenzumgebung. Es belegt keine Neuinstallation der Abhängigkeiten auf einem fremden Rechner, keine externe wissenschaftliche Validierung und keine menschliche Prüfung. Der temporäre Archivpfad wird nach dem erfolgreichen Vergleich entfernt.
