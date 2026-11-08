# Design-Council Runde 18

Geprüft wurde ausschließlich die Gestaltung und formale Umsetzung des Research Paper im eingefrorenen Commit `30462b6ca5057626bb0f990377f1673deac9983e`. Die PDF und alle 19 Prüfbilder stimmen per SHA-256 mit dem Freeze überein. Wissenschaftliche Inhalte wurden nicht bewertet.

Prüfgrundlage: :codex-file-citation{path="/Users/macbook_air_m1/.t3/scratch/2026-11-07-create-a-new-separate-github-162aa05c/planet-simtech-2025-TEST-K31pro-max/output/pdf/TEST-K31pro-max.pdf" purpose="source"}

## Bewertung

| Kategorie | Bewertung | Begründung und Belegorte |
|---|---:|---|
| D1, Typografie | 9 | Durchgehend klare Times-Hierarchie, sauberer Mathematiksatz und konsistente Quellenform. Grundschrift, Tabellen und Literaturverzeichnis stehen in nominell 12 pt mit 14,4 pt Zeilenabstand. Deutsche Dezimalkommata und Tausenderpunkte sind umgesetzt, negative Tabellenwerte stehen im Mathematikmodus. Belege: PDF-Seiten 3 bis 5, 11 bis 15 sowie `report/preamble.tex:26-43`. Nur lokale Trennungsschönheitsfehler wie „Tarifpro-xy“ auf PDF-Seite 4 und „READ-ME“ auf PDF-Seite 14 bleiben. |
| D2, Seiten- und Spaltennutzung | 8 | Auf PDF-Seite 7 entsteht durch den erzwungenen Platz von Abbildung 2 ein wesentliches Ungleichgewicht. Bis zur gemeinsamen Textfußmarke bleiben links rund 226 pt beziehungsweise 80 mm frei, rechts nur rund 25 pt beziehungsweise 9 mm. Das ist mitten im Haupttext sichtbar verschwendeter Satzspiegel. Die Quellen 19 bis 22 links und 23 bis 25 rechts auf PDF-Seite 13 sind dagegen ausgewogen und durchgehend nummeriert. |
| D3, Lesbarkeit und visuelle Führung | 9 | Die Zusammenfassung steht vollständig in der linken Spalte von PDF-Seite 2; die rechte Spalte setzt bereits die Einführung fort. Die Abschnittsfolge ist klar. Tabelle 1 gehört sichtbar zu Abschnitt 2.1 auf PDF-Seite 3. Tabelle 2 folgt nach H2, H8 und H3 auf PDF-Seite 8. Der HAW-Verweis [19] bleibt im H8-Absatz auf PDF-Seite 6. Abbildung 2 steht vor Abschnitt 4. Quellen- und Anhangsverweise sind nachvollziehbar. |
| D4, Abbildungen, Tabellen und visuelle Erklärung | 9 | Abbildung 1 nutzt auf PDF-Seite 5 die volle Breite; Symlog-Achse und linearer Bereich bis 1 MW erklärt die Unterschrift. Abbildung 2 ist auf PDF-Seite 7 einspaltig und ausreichend beschriftet. Die Kapazitätslegende in Abbildung 3 auf PDF-Seite 14 überdeckt weder Balken noch Referenzlinien oder Achsentext. Die H1-Legende steht kollisionsfrei neben der Verteilung. Tabellen 1 bis 5 haben klare Linien und verständliche Unterschriften; H1 ist in den Tabellen 2 und 5 fett. |
| D5, Formale Compliance | 10 | Alle 15 Seiten sind A4. Die kleinsten gemessenen Ränder einschließlich Seitenzahlen betragen links 25,80 mm, rechts 25,26 mm, oben 26,31 mm und unten 26,08 mm. Deckblatt, anonyme Metadaten, Pflichtaufbau, Seitenbudget, Quellenform und KI-Offenlegung sind erfüllt. Anhang A steht blocksatzsauber auf PDF-Seite 14; Anhang B beginnt dort und endet auf PDF-Seite 15. Alle drei vollständigen NIST-Abfrage-URLs stehen in Eintrag [4] auf PDF-Seite 11. |
| D6, Direkter D4RT-Vergleich | 9 | Die zweispaltige Ordnung, numerischen Verweise, erklärenden Unterschriften und Tabellenlinien erreichen einen geordneten, an D4RT orientierten Lesefluss. Die größere Schrift und die vorgeschriebenen A4-Ränder verbessern die Drucklesbarkeit gegenüber den kleineren D4RT-Texten. D4RT ist auf den Seiten 1, 2 und 6 stärker bildgeführt; das ist hier keine Pflicht. Kein zusätzlicher vergleichsspezifischer Mangel, der Umbruchfehler auf PDF-Seite 7 wird ausschließlich unter D2 bewertet. |

## Materielle Mängel

### D2: Spaltenungleichgewicht auf PDF-Seite 7

Die Platzierungsanweisung `[H]` für Abbildung 2 in `report/main.tex:174-179` schiebt den vollständigen Abbildungsblock in die rechte Spalte. Die linke Spalte endet nach H3 bereits bei etwa 522 pt, die rechte erst bei etwa 723 pt. Der entstehende weiße Bereich von rund 80 mm in der linken Spalte ist ein realer Umbruchfehler, nicht nur eine Geschmacksfrage.

Konkrete Korrektur:

- Die Unterschrift von Abbildung 2 von fünf auf höchstens drei Zeilen kürzen. Die Erläuterungen zu Investition und erwartetem Abfluss können im angrenzenden Fließtext bleiben.
- Der Abbildungsblock benötigt aktuell etwa 240 pt. Zwei eingesparte Unterschriftszeilen geben rund 29 pt frei und decken den fehlenden Platz von etwa 14 pt in der linken Spalte.
- Dadurch kann Abbildung 2 nach H3 in der linken Spalte stehen, während Abschnitt 4 oben in der rechten Spalte beginnt.
- Achsen, Legende und Schrift nicht verkleinern. Mindestens 12 pt und 25 mm Rand beibehalten. Das bisherige Budget von zehn Haupttextseiten sowie fünf Seiten für Literatur und Anhang nicht überschreiten.
- Nach dieser Korrektur die Folgeseiten erneut sichten, da sich die späteren Umbrüche verschieben können.

## Optionale Verbesserungen

- Auf PDF-Seite 4 die Trennung „Tarifpro-xy“ durch eine gezielte Trennausnahme an der Wortfuge vermeiden. Auf PDF-Seite 14 kann „README“ ungeteilt gesetzt werden. Beide Stellen sind lesbar und rechtfertigen keinen materiellen Einwand.
- In Abbildung 3 auf PDF-Seite 14 könnten die drei Kapazitätsangaben unter dem oberen Histogramm etwas großzügiger verteilt werden. Die Einträge sind derzeit eng, aber vollständig lesbar und frei von Überdeckungen.
- Das weiterhin fehlende Installationsschema bleibt optional und wurde nicht abgewertet. Auch ein zusätzliches Prozessschema ist nicht erforderlich.
- Die großen Restflächen auf PDF-Seite 13 nach dem Literaturverzeichnis und auf PDF-Seite 15 nach Anhang B stehen an natürlichen Dokumentgrenzen. Sie sind keine Aufforderung, weiteren Inhalt aufzunehmen.

## Erfolglose substanzielle Fehlersuche für D5

Für die 10 in D5 habe ich gezielt nach formalen Fehlern gesucht:

- Commit, PDF-Hash und Hashes sämtlicher Prüfbilder abgeglichen.
- Alle 15 Seiten auf A4, Ränder, Seitenzahlen, Überläufe und abgeschnittene Inhalte geprüft.
- Grundschrift, Tabellen, Quellen und eingebettete Diagrammbeschriftungen kontrolliert. Die effektiven Diagrammgrößen liegen bei nominell 12 pt oder darüber. Kleinere mathematische Indizes folgen dem normalen TeX-Mathematiksatz.
- Den PDF-Text auf Zahl-Einheit-Trennungen gescannt. Die einzigen drei Treffer sind die erwarteten Achsenbeschriftungen auf PDF-Seite 5 und PDF-Seite 14.
- Deckblatt und Metadaten auf Anonymität geprüft. `pdfauthor` ist leer; die Testkennung wird nicht als offizielle Team-ID ausgegeben.
- Haupttext und gemeinsamen Bereich für Literatur und Anhang nachgezählt.
- Numerierung der Quellen 1 bis 25, die drei NIST-URLs, Abrufdaten und die KI-Offenlegung kontrolliert.
- Anhang A und Anhang B einschließlich ihrer Seitenzuordnung gesichtet.

Dabei blieb kein substanzieller Compliancefehler übrig. Offizielle Team-ID, Rechtefreigabe, menschliche wissenschaftliche Prüfung und tatsächliche Einreichung wurden als menschliche Restaufgaben nicht abgewertet.

## Abschließendes Urteil

Meine Bewertung erfüllt die Design-Stoppregel **nicht**. D2 erreicht nur 8 von 10, und der materielle Spaltenfehler auf PDF-Seite 7 ist noch ungelöst. D1, D3, D4, D5 und D6 erreichen mindestens 9. Nach der beschriebenen Umbruchkorrektur und einer erneuten Sichtung der Folgeseiten ist die Stoppregel aus meiner Sicht erreichbar.
