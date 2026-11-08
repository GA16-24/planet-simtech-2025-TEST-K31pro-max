# Design-Council für Runde 18

Arbeite unabhängig und read-only. Zeige oder übermittle deine Bewertung nicht an den anderen Reviewer. Ändere keine Dateien und führe keine Builds aus. Der implementierende Agent hat keine Council-Stimme.

## Eingefrorene Revision

Repository: `/Users/macbook_air_m1/.t3/scratch/2026-11-07-create-a-new-separate-github-162aa05c/planet-simtech-2025-TEST-K31pro-max`

Commit: `30462b6ca5057626bb0f990377f1673deac9983e`

Prüfe nur diese Revision. `review/rounds/round18-design/revision.json` enthält die SHA-256-Hashes der versionierten Dateien. Frühere Punktzahlen und Bewertungen sind nicht Teil deiner Bewertung und dürfen nicht übernommen werden.

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
- zur Commit- und Reproduktionskontrolle nur `review/rounds/round18-design/revision.json`, `reproduction.md` und `prompt.md`

Lies keine anderen Dateien in `review/rounds/`. Lies weder `review/README.md` noch `decisions.tsv`, frühere Rohberichte oder Scorecards. Lies auch keine Übersichten mit früheren Punktzahlen. Du darfst read-only Befehle für PDF-Text, Geometrie und Commitprüfung ausführen, aber keine erzeugenden Befehle.

## Vorherige Befunde und Antwort der Revision

Diese Hinweise beschreiben die ursprünglichen Einwände ohne frühere Punktzahlen. Prüfe selbst, ob die Antwort sie wirklich schließt. Neue oder weiterhin bestehende Mängel musst du normal bewerten.

1. Tabelle 1 wird mit Abschnitt 2.1 eingereiht und steht auf PDF-Seite 3. Tabelle 2 folgt erst nach H2, H8 und H3. Der HAW-Verweis bleibt im H8-Absatz.
2. Abbildung 2 steht als einspaltige Grafik nach H3 und vor Abschnitt 4. Ihre Schrift bleibt mindestens 12 pt.
3. Quellen 19 bis 22 stehen links und 23 bis 25 rechts auf PDF-Seite 13. Prüfe die Balance und die Nummerierung. Eine Balancierungsanweisung mit `\balance` wurde nach einem Überlauf verworfen.
4. Minuten und weitere literale Einheiten sind geschützt, darunter Preise, Geschwindigkeiten und Brennstoffwerte. Ein separater PDF-Scan findet keine Zahl-Einheit-Trennung außerhalb der Achsenbilder.
5. Die Kapazitätslegende steht frei zwischen den Histogrammen. Drei kurze Linien- und Texteinträge überdecken weder Balken, Referenzlinien noch Achsentext. Prüfe Abdeckung, Kollisionen und Lesbarkeit bei Vergrößerung.
6. Alle drei vollständigen NIST-Abfrage-URLs stehen im gedruckten Eintrag [4]. H1 ist in den Tabellen 2 und 5 fett. Die Symlog-Achse und ihr linearer Bereich sind erklärt. Ein Installationsschema bleibt optional.
7. Zahlenmakros und generierte Tabellenwerte verwenden deutsches Dezimalkomma und Tausenderpunkt. Negative Werte stehen im Mathematikmodus. Anhang A ist im Blocksatz und Anhang B steht auf PDF-Seiten 14 und 15.

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
