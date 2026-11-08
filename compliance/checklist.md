# Compliance-Checkliste

Regelstand und Prüfverfahren: `compliance/regeln.md`, offizielle Dokumente von 10/2026. Der Status bezieht sich auf das aktuelle Paket. Offizielle Team-ID und Finalisten-E-Mail liegen nicht vor, deshalb wird eine Testkennung verwendet.

## Schriftliche Runde

| Anforderung | Umsetzung | Prüfnachweis | Status |
| --- | --- | --- | --- |
| Deutsch, ein PDF-Dokument | `output/pdf/TEST-K31pro-max.pdf` | `scripts/verify_report.py` | erfüllt |
| Dateiname nur Team-ID | Testkennung `TEST-K31pro-max.pdf` | Dateipfad und Deckblatt | für Testpaket erfüllt, vor Abgabe ersetzen |
| Anonymität | Keine Namen oder Schulangaben in Text und Metadaten | PDF-Text und Metadatenprüfung | erfüllt |
| Pflichtdeckblatt | Wettbewerbsname, Team-ID, Datum und Aufgabenstellung | erste PDF-Seite | erfüllt |
| Zusammenfassung höchstens eine Seite | Zusammenfassung beginnt auf Haupttextseite 1 | gerenderte Seite | erfüllt |
| Pflichtaufbau | Zusammenfassung, Einführung, Methode, Ergebnisse, Diskussion, Schlussfolgerung sowie Verbesserungsmöglichkeiten bei mehr Bearbeitungszeit | PDF-Textprüfung | erfüllt |
| Haupttext höchstens 10 Seiten | 10 Haupttextseiten nach Deckblatt, einschließlich des letzten Absatzes auf der ersten Literaturseite | automatische Seitenzählung | erfüllt |
| Literatur und Anhang höchstens 5 Seiten | 5 Seiten gemeinsamer Zählbereich ab Literaturbeginn | automatische Seitenzählung | erfüllt |
| A4 und 25 mm Rand | LaTeX-Geometrie, gemessen mindestens 25,997 mm | `report/preamble.tex`, `verify_report.py` | erfüllt |
| 12 pt und Zeilenabstand mindestens 1,0 | 12 pt auf 14,4 pt, auch Tabellen, Quellen und eingebettete Diagramme | PDF-Schriftgrößen und Sichtprüfung | erfüllt |
| Numerische Quellenverweise | Einheitliche IDs 1 bis 25 im Text und Verzeichnis | Quellenregister und PDF | erfüllt |
| Internetquellen mit Abrufdatum | Autor oder Institution, Titel, URL und 07.11.2026 | Literaturverzeichnis | erfüllt |
| KI-Offenlegung | Anhang A und Provenienzprotokoll | PDF-Text und `PROVENANCE.md` | erfüllt |
| Keine externe Wettbewerbsabgabe | Privates Repository, keine E-Mail und keine öffentliche Bereitstellung der Wettbewerbsdateien | Laufprotokoll | erfüllt |

## Historische Finalrunde, außerhalb des aktuellen Lieferumfangs

| Anforderung | Umsetzung | Prüfnachweis | Status |
| --- | --- | --- | --- |
| Video höchstens 5:00 Minuten | MP4 mit 290,232 s | `ffprobe` und `verify_presentation.py` | erfüllt |
| Fertige Präsentation | 10 PDF-Folien und editierbare LaTeX-Quelle | `output/presentation/Blautopf_Finale.pdf` | erfüllt |
| Animation erlaubt | Vollständig aus Folien erzeugtes Video | MP4 und Buildskript | erfüllt |
| Sprechtext und Quellen | `presentation/speaker_notes.md` | Folienzeiten und Quellen je Folie | erfüllt |
| Dokumentierte Zeitprobe | `presentation/rehearsal.md`, reale Audiodauer und MP4-Dauer | Zeitentabelle und Echtzeitprobe mit `real 289.67 s` | erfüllt |
| Adversariale Q&A | 27 Fragen mit Antworten und Revisionszuordnung | `presentation/jury_qa.md` | erfüllt |
| Medienrechte | Rechtenachweis ohne externe Bilder oder Musik | `presentation/rights.md` | menschliche Endfreigabe offen |
| Technische Interoperabilität | 1920 x 1080, 16:9, H.264, AAC, yuv420p | `output/presentation/verification.json` | erfüllt, Finalisten-E-Mail prüfen |
| Live-Teilnahme | Nicht behauptet | `presentation/rehearsal.md` | menschliche Restaufgabe |

## D4RT-Vergleich für Kriterium 11

Die zweispaltige Ordnung, Times-Hierarchie, numerischen Verweise, erklärenden Bildunterschriften und Tabellenlinien folgen dem visuellen Qualitätsmaßstab von D4RT. A4, 25 mm Rand und 12 pt bleiben übergeordnet. Der direkte Vergleich steht in `compliance/layout_referenz.md`. Die endgültige Bewertung erfolgt an den gerenderten Seiten, nicht nur am Quelltext.
