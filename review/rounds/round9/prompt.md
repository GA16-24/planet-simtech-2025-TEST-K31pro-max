# Council-Prüfauftrag für Runde round9

Arbeite unabhängig und read-only. Zeige oder übermittle deine Bewertung nicht an den anderen Reviewer. Der implementierende Agent darf deine Rohbewertung erst nach Abschluss sehen.

## Aufgabe und Ausgangslage

Die Aufgabe lautet: "Wie kann dauerhaft verhindert werden, dass das Wasser im Blautopf den Siedepunkt erreicht?" Vulkanische Aktivität und die Zehnjahresprognose sind Szenarioprämissen, keine unabhängig bestätigten Fakten. Das Paket soll die Frage beantworten und zugleich die Sensitivität gegenüber diesen Prämissen prüfen.

Das Repository entstand leer und ohne Nutzung früherer Lösungen. Frühere PlaNeT-SimTech-Einreichungen, Gewinnerberichte, Lösungszusammenfassungen, Reviews, Präsentationen, Videos, Diskussionen oder aufgabenbezogene Repositories dürfen nicht gesucht oder verwendet werden. Öffne insbesondere keine ähnlich benannten Repositories oder früheren Threads. Falls du versehentlich auf solches Material stößt, nutze es nicht und dokumentiere die Exposition.

## Eingefrorene Revision

Repository: /Users/macbook_air_m1/.t3/scratch/2026-11-07-create-a-new-separate-github-162aa05c/planet-simtech-2025-TEST-K31pro-max

Commit: 8e1b72d5235162172f31b00775cd1bb0c55d24ce

Die Datei `review/rounds/round9/revision.json` enthält die SHA-256-Hashes der versionierten Dateien. Prüfe nur diese Revision. Ändere keine Datei. Frühere Reviews oder Scorecards sind nicht Teil deiner Bewertung und dürfen nicht übernommen werden.

## Vollständiges Paperpaket

Der Nutzer hat den Lieferumfang auf den Research Paper beschränkt. Präsentations- und Finaldateien sind historische Arbeitsstände und nicht Teil dieser Bewertung.

- Bericht: `output/pdf/TEST-K31pro-max.pdf`
- Berichtsquelle: `report/main.tex`, `report/preamble.tex`
- Modell und Eingaben: `model/`, `data/parameters.yml`, `data/nist_saturation_32_100.tsv`, `requirements.lock.txt`
- Modellergebnisse: `output/model/results.json`, `output/model/hybrid_schedule.csv`, `output/model/sensitivity.csv`, `output/model/manifest.json`
- Gerenderte Berichtsseiten und Kontaktübersicht: `review/rendered/report_pages/`, `review/rendered/report_contact.png`
- Regeln und Layoutvergleich: `compliance/regeln.md`, `compliance/checklist.md`, `compliance/layout_referenz.md`
- Herkunft und Unabhängigkeit: `PROVENANCE.md`, `EXCLUSION_LOG.md`, `decisions.tsv`, `sources/registry.yml`, `docs/hypothesen.md`, `docs/alternativenvergleich.md`
- Reproduktion: `README.md`, `Makefile`, `scripts/`, `review/rounds/round9/reproduction.md`
- Befundzuordnung und Reviewkonfiguration: `review/revisions.md`, `review/model_configuration.md`

Prüfe den tatsächlich gerenderten Research Paper, nicht nur LaTeX oder JSON. Öffne die Kontaktübersicht und alle dreizehn Einzelseiten. Prüfe die Diagramme und Tabellen in den gerenderten Seiten. Du darfst read-only Prüfbefehle ausführen, sofern dein Modus dies zulässt. Führe keine Builds aus und verändere keine Dateien.

Lies keine Rohberichte oder Scorecards aus früheren Runden. Vermeide auch rekursive Suchen im Verzeichnis `review/rounds/`, damit alte Bewertungen nicht versehentlich in deinen Kontext gelangen. Die Befundzuordnung enthält frühere Mängel ohne Punktzahlen. Prüfe deren Behebung an der aktuellen Revision selbst.

## Kriterien

Bewerte jedes verbleibende Kriterium mit einer ganzen Zahl von 1 bis 10:

1. Qualität der Argumentation
2. Vorgehen und Methodik
3. Qualität der vorgeschlagenen Lösung
4. Mathematische und wissenschaftliche Modellierung
5. Ableitung neuer Ansätze statt Wiederverwendung vorhandener Ergebnisse
6. Wissenschaftliche Qualität
8. Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen
9. Kritische Diskussion der Ergebnisse
10. Klare Berichtsstruktur und für die Jury nachvollziehbare Argumentation
11. Format, Zitation und Einreichungsanforderungen, einschließlich visueller Qualität im Vergleich zur D4RT-Referenz
12a. Bereitschaft für die schriftliche Runde

Kriterium 12b und die Präsentation wurden durch den Nutzer aus dem Lieferumfang entfernt. Bewerte oder erfinde dafür keine Ersatzpunkte. Fehlende Standort-, Netz-, Hersteller- und Karstdaten müssen als Grenzen sichtbar bleiben. Bewerte die Qualität des dokumentierten Szenarioentwurfs ohne eine Baufreigabe oder externe Machbarkeitsnachweise zu unterstellen.

## Bewertungsmaßstab und Nachweis

9/10 bedeutet nachweisbar abgabebereit ohne bekannten wesentlichen Mangel. Nur optionale Verbesserungen bleiben. 10/10 verlangt einen eigenen dokumentierten Versuch, substanzielle Fehler zu finden, und eine Begründung, warum keiner verbleibt. Aufwand, Länge, visuelle Wirkung oder Verbesserung gegenüber einer früheren Fassung rechtfertigen keine hohe Bewertung.

Jede Bewertung braucht eine kurze Begründung und genaue Belegorte wie Datei, Seite, Abschnitt, Gleichung, Abbildung oder reproduzierbare Ausgabe. Jede Bewertung unter 9 braucht eine konkret ausführbare Korrektur. Prüfe auch Unabhängigkeit, KI-Offenlegung, Anonymität und aktuelle Regeln. Kriterium 11 verlangt einen direkten Vergleich mit der visuellen Qualität der D4RT-Arbeit, ohne deren Verstöße gegen die offiziellen Vorgaben zu übernehmen.

## Ausgabe

Liefere auf Deutsch:

1. Eine Tabelle mit allen elf Zeilen, Bewertung, kurzer Begründung und genauen Belegorten.
2. Eine Liste materieller Mängel mit konkreten Korrekturen und Belegorten.
3. Restrisiken und Dissens, die auch nach einer hohen Bewertung sichtbar bleiben müssen.
4. Für jede 10 eine kurze Beschreibung der erfolglosen substanziellen Fehlersuche.
5. Ein abschließendes Urteil, ob auf dieser Revision alle Anforderungen an die Stoppregel erfüllt sind. Diese verlangt mindestens 9 in jeder Zeile von beiden Reviewern und keine ungelöste substantielle Einwände gegen Korrektheit, wissenschaftliche Qualität, Unabhängigkeit, Compliance oder Auslieferbarkeit des Paperpakets.

Erfinde keine Prüfungen, Seitenzahlen, Modellwerte oder Beobachtungen. Wenn etwas nicht geprüft werden kann, markiere es ausdrücklich als ungeprüft und senke die betroffene Bewertung nachvollziehbar. Bewerte nicht nach Aufwand und mittlere nicht über Kriterien hinweg.
