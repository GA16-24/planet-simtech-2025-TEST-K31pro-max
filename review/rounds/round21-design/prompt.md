# Design-Council für Runde 21

Arbeite unabhängig und read-only. Zeige oder übermittle deine Bewertung nicht an den anderen Reviewer. Ändere keine Dateien und führe keine Builds aus. Der implementierende Agent hat keine Council-Stimme.

## Eingefrorene Revision

Repository: `/Users/macbook_air_m1/.t3/scratch/2026-11-07-create-a-new-separate-github-162aa05c/planet-simtech-2025-TEST-K31pro-max`

Commit: `1d589122b197834507a39a65280a9b676e775ad0`

Prüfe nur diese Revision. `review/rounds/round21-design/revision.json` enthält die SHA-256-Hashes der versionierten Dateien. Frühere Punktzahlen und Bewertungen sind nicht Teil deiner Bewertung und dürfen nicht übernommen werden.

Das Repository entstand ohne Nutzung früherer PlaNeT-SimTech-Lösungen. Suche nicht nach früheren Einreichungen, Gewinnerberichten, Lösungszusammenfassungen, Reviews, Präsentationen, Videos, Diskussionen oder aufgabenbezogenen Repositories. Öffne keine ähnlich benannten Repositories oder früheren Threads. Falls du versehentlich auf solches Material stößt, nutze es nicht und dokumentiere die Exposition.

## Aufgabe und zulässige Prüfgrundlage

Bewerte ausschließlich die Gestaltung und formale Umsetzung des Research Paper. Prüfe nicht das wissenschaftliche Modell, die physikalischen Annahmen, Rechenwerte oder früheren fachlichen Bewertungen. Übernimm keine fachlichen oder gestalterischen Punktzahlen. Der Lieferumfang ist nur der Research Paper. Präsentations-, Video- und Finaldateien sind historische Arbeitsstände und nicht Teil dieser Bewertung.

Prüfe die tatsächlich gerenderte PDF, nicht nur LaTeX. Öffne die Kontaktübersicht und jede der fünfzehn Einzelseiten. Sichte die Diagramme und Tabellen in den gerenderten Seiten und vergleiche sie direkt mit den drei D4RT-Seiten.

Zulässige Dateien:

- `output/pdf/TEST-K31pro-max.pdf`
- `review/rendered/report_contact.png`
- alle fünfzehn Bilder `review/rendered/report_pages/page-01.png` bis `page-15.png`
- `review/rendered/d4rt_page01.png`, `d4rt_page02.png` und `d4rt_page06.png`
- `compliance/regeln.md` und `compliance/checklist.md`
- `report/main.tex` und `report/preamble.tex`
- zur Commit- und Reproduktionskontrolle nur `review/rounds/round21-design/revision.json`, `reproduction.md` und `prompt.md`

Lies keine anderen Dateien in `review/rounds/`. Lies weder `review/README.md` noch `decisions.tsv`, `review/revisions.md`, frühere Rohberichte oder Scorecards. Lies auch keine Übersichten mit früheren Punktzahlen. Du darfst read-only Befehle für PDF-Text, Geometrie und Commitprüfung ausführen, aber keine erzeugenden Befehle.

## Vorherige Befunde und Antwort der Revision

Diese Hinweise beschreiben die ursprünglichen Einwände ohne frühere Punktzahlen. Prüfe selbst, ob die Antwort sie wirklich schließt. Neue oder weiterhin bestehende Mängel musst du normal bewerten.

1. Die letzte Literaturseite war unausgewogen und mehrere Einträge waren über Seitengrenzen getrennt. Nun stehen Quellen 19 bis 22 links und 23 bis 25 rechts auf PDF-Seite 13. Quellen 6, 19 und 20 verwenden lokale Absatzgruppen und sollen vollständig auf einer Seite stehen. Prüfe jede Seitengrenze, die tatsächliche Spaltenbalance und die verbleibende Leerfläche am Literatur Ende. Ein zusätzlicher erzwungener Seitenumbruch wurde nach einer Zusatzseite verworfen.
2. Tabelle 2 stand vor ihrer ersten Textreferenz. Ein kurzer Vorausverweis folgt nun unmittelbar auf Abschnitt 3.3 und steht vor dem Float. Er soll auf PDF-Seite 5 erscheinen, die Tabelle oben auf PDF-Seite 6. Prüfe die sichtbare Reihenfolge und den Absatzfluss.
3. Tabelle 3 trennte Fallnamen und Zahlen auf verschiedene Zeilen. Eigene Gruppenzeilen für Abfluss und Sieden gliedern die Fälle. Jede Wertzeile soll Fall und Zahlen auf derselben Zeile enthalten. Prüfe Gruppierung, Einheiten und Überläufe auf PDF-Seite 15.
4. In Abbildung 3 stand die Kapazitätslegende zu nahe am MW-Achsentitel. Sie wurde abgesenkt. Eine Führungslinie verbindet H1 4,14 mit der gestrichelten Barwertlinie, und die Unterschrift erklärt diese Linie. Prüfe Abstände, Linienmuster, Datenfreiheit und effektive Schriftgröße auf PDF-Seite 14.
5. In Abbildung 2 lag die H1/H2-Legende im Zeilenkasten von Betriebsjahr. Sie steht nun oben links im freien Diagrammbereich. Prüfe auf PDF-Seite 7, ob sie weder Achsen noch Kurven beeinträchtigt.
6. Abbildung 1 erhielt die Panelbezeichnungen (a) und (b). Eine kürzere Legende steht unter dem rechten Panel. Prüfe Zuordnung, Abstände und mindestens 12 pt effektive Diagrammschrift auf PDF-Seite 5.
7. Frühere Korrekturen bleiben zu prüfen: Tabelle 1 auf PDF-Seite 3, Tabelle 2 mit 54 mm erster Spalte, vollständige NIST-URLs in [4], deutsches Zahlenformat, H1 fett in den Tabellen 2 und 5, Symlog-Erklärung sowie Anhang A auf PDF-Seite 14 und Anhang B auf PDF-Seiten 14 und 15. Ein Installationsschema bleibt optional.
8. Die PDF hat 15 Seiten mit 10 Haupttextseiten nach dem Deckblatt und 5 Literatur-/Anhangsseiten. Der Berichtsbuild meldet keine Overfull-Warnungen. Bewerte die sichtbare Ausgabe selbst, nicht diese Behauptung.

## Bewertungskategorien

Bewerte jede Kategorie mit einer ganzen Zahl von 1 bis 10:

- D1, Typografie: Schriftgrößen, Hierarchie, Zeilenfall, Wortabstände, Trennungen, Mathematik- und Quellensatz.
- D2, Seiten- und Spaltennutzung: Satzspiegel, Ränder, Umbrüche, Spaltenbalance, Leerräume und Seitenbudget.
- D3, Lesbarkeit und visuelle Führung: Zusammenfassung, Absatzfluss, Überschriften, Verweise und nachvollziehbare Reihenfolge. Bewerte nur Darstellung und Verständlichkeit, nicht die fachliche Richtigkeit.
- D4, Abbildungen, Tabellen und visuelle Erklärung: Bildgrößen, Beschriftungen, Legenden, Achsen, Tabellenlinien, Unterschriften und Erkenntnisgewinn der Grafiken.
- D5, Formale Compliance: A4, mindestens 25 mm Rand, mindestens 12 pt und Zeilenabstand 1,0, anonymes Deckblatt, Pflichtaufbau, Seitenzählung, Zitier- und Quellenform sowie KI-Offenlegung. Menschliche Restaufgaben sind nach dem nächsten Abschnitt gesondert zu behandeln.
- D6, Direkter D4RT-Vergleich: visuelle Qualität und Leserführung gegen D4RT-Seiten 1, 2 und 6, ohne D4RT-Verstöße gegen die offiziellen Vorgaben zu übernehmen.

Prüfe ausdrücklich die einspaltige Zusammenfassung, Anhang A auf PDF-Seite 14, Anhang B auf PDF-Seiten 14 und 15, das weiterhin fehlende Installationsschema und die vollständigen NIST-URLs. Verlange nicht pauschal mehr Inhalt, kleinere Schriften, D4RTs US Letter oder geringere Ränder. Ein etwa vorgeschlagenes Prozessschema muss im vorhandenen Seitenbudget Platz finden und mindestens 12 pt beschriftet sein. Vermeide Float-Experimente ohne nachgewiesenen konkreten Mangel.

Offizielle Team-ID, Rechtefreigabe, menschliche wissenschaftliche Prüfung und tatsächliche Einreichung sind menschliche Restaufgaben außerhalb des Testpakets. Ihr Fehlen allein ist kein Papermangel und darf keine Bewertung senken. Bewerte reale Mängel im vorliegenden Testpaket normal. `TEST-K31pro-max` ist eine Testkennung, keine offizielle Team-ID.

## Maßstab und Ausgabe

9/10 bedeutet gestalterisch und formal bereit für das technische Testpaket ohne bekannten wesentlichen Mangel. Nur optionale Verbesserungen bleiben. 10/10 verlangt einen eigenen dokumentierten Versuch, substanzielle Gestaltungs- oder Compliancefehler zu finden, und eine Begründung, warum keiner verbleibt. Aufwand, Seitenzahl oder Verbesserung gegenüber einer früheren Fassung rechtfertigen keine hohe Bewertung.

Liefere auf Deutsch:

1. Eine Tabelle mit den sechs Zeilen D1 bis D6, Bewertung, kurzer Begründung und genauen Belegorten wie PDF-Seite, Abschnitt, Abbildung oder Tabelle.
2. Eine Liste materieller Mängel. Jede Bewertung unter 9 braucht eine konkret ausführbare Korrektur mit Belegort und muss die genannten Seiten-, Schrift- und Randbedingungen einhalten.
3. Optionale Verbesserungen getrennt von materiellen Mängeln.
4. Für jede 10 eine kurze Beschreibung der erfolglosen substanziellen Fehlersuche.
5. Ein abschließendes Urteil, ob deine Bewertung die Design-Stoppregel erfüllt. Diese verlangt mindestens 9 in jeder Kategorie und keine ungelösten materiellen Einwände. Beide Reviewer müssen sie unabhängig erfüllen.

Erfinde keine Prüfungen, Seitenzahlen oder Beobachtungen. Kennzeichne Ungeprüftes ausdrücklich und senke die betroffene Bewertung nachvollziehbar. Mittlere nicht über Kategorien und trage keine früheren Punktzahlen fort.
