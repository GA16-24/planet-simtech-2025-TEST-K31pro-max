## Prüfgrundlage

Der HEAD entspricht dem eingefrorenen Commit `01a7304980f0a3044f385e40463cf118f4a80dcb`. Alle 25 zulässigen und in `revision.json` gelisteten Prüfdateien stimmen mit ihren SHA-256-Hashes überein, ohne Abweichung.

Geprüft wurden die tatsächliche PDF, die Kontaktübersicht, alle fünfzehn Einzelseiten und die drei D4RT-Seiten. Ergänzend erfolgten PDF-Text-, Schrift- und Geometriemessungen. Das wissenschaftliche Modell war nicht Gegenstand dieser Bewertung.

## Bewertung

| Kategorie | Bewertung | Begründung und Belegorte |
|---|---:|---|
| D1, Typografie | 9 | Durchgehend lesbarer Times-ähnlicher Satz mit 12,01 pt Grundschrift und 14,4 pt Zeilenabstand. „Antriebs-energie“ ist auf PDF-Seite 2 richtig getrennt. Die Einleitung zu Gleichung 2 steht mit der Gleichung auf PDF-Seite 3 zusammen. Formeln und Quellensatz auf den PDF-Seiten 11 bis 13 sind konsistent. |
| D2, Seiten- und Spaltennutzung | 8 | Satzspiegel, Ränder und Seitenbudget sind eingehalten. Die letzte Literaturseite bleibt jedoch sichtbar unausgewogen. Auf PDF-Seite 13 stehen 20 Textzeilen links und 11 rechts. Die belegte Vertikale links ist etwa 1,8-mal so groß wie rechts. |
| D3, Lesbarkeit und visuelle Führung | 9 | Die einspaltige Zusammenfassung liegt vollständig in der linken Spalte von PDF-Seite 2 und damit innerhalb der ersten Haupttextseite. Tabelle 2 wird auf PDF-Seite 5 in Abschnitt 3.3 referenziert und erscheint oben auf PDF-Seite 6. Der Absatz wird darunter schlüssig fortgesetzt. Der Verweis auf Abbildung 3 auf PDF-Seite 9 nennt Anhang B. |
| D4, Abbildungen, Tabellen und visuelle Erklärung | 9 | Abbildung 1 auf PDF-Seite 5 erklärt Symlog-Achse und linearen Bereich. Tabelle 2 auf PDF-Seite 6 hat klare Zeilen, ausreichende Zellenabstände und keine Überläufe. Abbildung 3 auf PDF-Seite 14 enthält 1.053,3 und 2.152,5, unterscheidbare Linienmuster und keine Kollisionen. Der NIST-Wert 4.195,14 steht in der Handrechnung auf derselben Seite. Diagrammbeschriftungen messen 12,68 bis 13,35 pt. Tabellen 3 bis 5 auf PDF-Seite 15 nennen die Einheiten in ihren Unterschriften. H1 ist in den Tabellen 2 und 5 fett. |
| D5, Formale Compliance | 10 | A4, Seitenbudget, anonymes Deckblatt, Pflichtaufbau, Schriftgrade, Ränder, numerische Quellenverweise und KI-Offenlegung sind erfüllt. Die drei vollständigen NIST-URLs stehen in Eintrag [4] auf PDF-Seite 11. Anhang A auf PDF-Seite 14 dokumentiert Systeme, Einstellungen, Art und Umfang der KI-Nutzung. Anhang B erscheint auf den PDF-Seiten 14 und 15. |
| D6, Direkter D4RT-Vergleich | 9 | Die zweispaltige Ordnung, die Hierarchie, oberhalb platzierte breite Abbildungen und erklärende Unterschriften erreichen einen vergleichbaren Ordnungsgrad wie D4RT-Seiten 1, 2 und 6. Die Tabellen des Berichts sind bei der vorgeschriebenen Schriftgröße besonders gut lesbar. D4RT bietet mehr visuelle Prozessführung. Ein entsprechendes Installationsschema ist hier jedoch ausdrücklich optional. |

## Materielle Mängel

**1. D2, unausgewogene letzte Literaturseite.** Auf PDF-Seite 13 enthalten die linke Spalte die Fortsetzung von Quelle 20 sowie die Quellen 21 bis 23, die rechte nur die Quellen 24 und 25. Quelle 22 bleibt zwar vollständig zusammen, der Balancebefund ist aber nicht geschlossen. Die Seite wirkt dadurch nicht fertig ausgesetzt.

Die Korrektur ist konkret und ohne Layoutrisiko möglich:

- In `report/main.tex:269-272` den manuellen `\newpage`-Befehl von seiner Position nach Quelle 23 an die Position unmittelbar nach Quelle 22 verschieben.
- Dadurch stehen links die Fortsetzung von Quelle 20 und die Quellen 21 und 22, rechts die Quellen 23 bis 25. Nach den gegenwärtigen Zeilenzahlen ergibt das ungefähr 15 Zeilen links und 16 rechts.
- Quelle 22 bleibt ungeteilt. Es entsteht keine zusätzliche Seite. A4, 12 pt, Zeilenabstand, Ränder und das bisherige Seitenbudget bleiben unverändert.
- Anschließend ist die gerenderte PDF-Seite 13 auf Spaltenbalance und vollständige Einträge zu prüfen.

Weitere materielle Mängel habe ich nicht gefunden.

## Optionale Verbesserungen

**Installationsschema.** Ein solches Schema fehlt weiterhin, ist aber nicht erforderlich und senkt die Bewertung nicht. Falls es die visuelle Führung im Sinne des D4RT-Vergleichs verbessern soll, bietet der freie untere Bereich von PDF-Seite 15 Platz. Es müsste aus Abschnitt 2 oder Abschnitt 4.3 referenziert werden, mindestens 12 pt Beschriftung erhalten und ohne zusätzliche Seite auskommen.

## Dokumentierte Fehlersuche für D5 = 10

Ich habe gezielt nach substanziellen Compliancefehlern gesucht und keinen gefunden:

- `pdfinfo` bestätigt 15 Seiten im A4-Format mit 595,28 × 841,89 pt und leere Autorenmetadaten.
- Nach dem Deckblatt umfassen die PDF-Seiten 2 bis 11 zehn Haupttextseiten. Literaturverzeichnis und Anhänge liegen gemeinsam auf den PDF-Seiten 11 bis 15 und bleiben damit bei fünf Seiten.
- Fließtext, Tabellen und Quellenverzeichnis messen 12,01 pt. Diagrammbeschriftungen messen 12,68 bis 13,35 pt. Nur mathematische Indizes und Hoch- beziehungsweise Tiefstellungen sind mit 8,68 pt kleiner.
- Die kleinsten per PDF-Wortgeometrie gemessenen Ränder einschließlich Fußzeilen betragen links 25,802 mm, rechts 25,263 mm, oben 26,306 mm und unten 26,085 mm.
- Deckblatt, Pflichtaufbau, Seitenzählung, numerische Verweise, Internetquellen mit Abrufdatum und KI-Offenlegung sind vorhanden.
- Alle drei NIST-URLs aus dem LaTeX-Quelltext wurden zusätzlich vollständig im extrahierten PDF-Text gefunden.
- Offizielle Team-ID, Rechtefreigabe, menschliche Fachprüfung und tatsächliche Einreichung wurden als menschliche Restaufgaben nicht negativ bewertet.

## Urteil zur Design-Stoppregel

**Meine Bewertung erfüllt die Stoppregel nicht.** D2 erreicht nur 8 von 10, und der Spaltenbalancebefund auf PDF-Seite 13 ist ein ungelöster materieller Einwand. Die übrigen Kategorien erreichen mindestens 9. Das zweite, unabhängige Reviewvotum habe ich nicht eingesehen und nicht berücksichtigt.