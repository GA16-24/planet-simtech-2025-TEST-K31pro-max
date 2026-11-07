# Rohbericht Kimi K3.1 Pro, Runde 1

Revision: `9b3a83bcea1358184b14de6759af117a049114f5`.
Prüfmodus: read-only, keine Datei geändert. Der Reviewer las keine anderen Bewertungen.

## Bewertungen

| Kriterium | Note | Begründung und Beleg |
| --- | ---: | --- |
| 1 Argumentation | 9 | Vollstrom und Speicher tragen die Argumentation. Sieben Ansätze werden einheitlich geprüft, Prämissen und Falsifikation sichtbar. PDF S. 2, 5, 8 bis 11 und `docs/alternativenvergleich.md`. |
| 2 Methodik | 8 | Parameter, Code und Tests nachvollziehbar. Abzug für inkonsistente Ersatzinvestition und begrenzte Monte-Carlo-Kopplung. Parameter, `model/run_all.py`, `model/core.py`, Tests. |
| 3 Lösung | 8 | Stimmige zweistufige Kühlung und Rückführung. Wärmesenke, Netzanschlüsse und Notstromdauer nicht standortbezogen ausgelegt. PDF S. 5 bis 7, 10 bis 11, Folien 5, 6, 8. |
| 4 Modellierung | 8 | Nachrechnung bestätigt zentrale Leistungen, Zumischung, Ausfallzeit und NPV. Ersatzinvestitionsfehler und Monte-Carlo-Kopplung verhindern 9. Modellcode, Validierung und Ergebnisse. |
| 5 Neue Ansätze | 9 | H1 bis H7 vor quantitativer Auswahl dokumentiert und physikalisch verschieden. Keine Übernahme früherer Lösungen. Hypothesen und Provenienz. |
| 6 Wissenschaftliche Qualität | 8 | Zentrale Werte bestätigt, aber drei falsche Publikationstitel und fehlende zweite NIST-Tabelle. Feldvalidierung fehlt. PDF S. 3 bis 6, 11 bis 14 und Register. |
| 8 Erklärungen | 9 | Tabelle 1 trennt Messwerte, Prämissen und Annahmen. Einheiten, Auslegungshülle und Restaufgaben klar. Sprechtext, VTT und Segmente konsistent. |
| 9 Kritische Diskussion | 9 | Durchfluss, Teilstrom, Prognosezeit, COP, Kosten, Hochwasser, Schichtung und Verfügbarkeit diskutiert. 12,48-GW-Grenze und fehlende Feldvalidierung ausdrücklich. |
| 10 Struktur und Juryführung | 9 | Klare Kette von Zusammenfassung bis Falsifikation. Haupttext und Anhang im Budget. PDF S. 2 bis 16 und offizielle Vorgaben. |
| 11 Format und D4RT | 7 | A4, 16 Seiten, 10+5 Budget, anonyme Metadaten und 12 pt bestanden. Randverstoß, Quellenfehler und redaktionelle Schwächen. PDF S. 10, Quellenregister, D4RT-Seiten 1 und 6. |
| 12a Schriftliche Runde | 7 | Vollständig, aber wegen Randverstoß, Kosten- und Quellenmängeln nicht abgabebereit. Offizielle Team-ID und menschliche Prüfung fehlen ausdrücklich. |
| 12b Finalrunde | 7 | Zehn Folien, echte MP4, Sprechtext, Untertitel, Zeitprobe, Rechte und 20 Q&A vorhanden. Abgeschnittene Folie 8 und kleine Diagrammbeschriftungen verhindern Abgabebereitschaft. |

## Materielle Mängel und verlangte Korrekturen

### M1, Folie 8 schneidet Text und Fußzeile ab

Textzeichen liegen bis 288,50 pt bei einer Seitenhöhe von 255,12 pt. Derselbe Fehler ist im MP4-Frame. Korrektur: Textblock und Fußzeile verkürzen oder neu aufteilen, PDF und MP4 neu erzeugen und alle zehn Folien und Frames sichtbar prüfen. `scripts/verify_presentation.py` muss Text außerhalb der Seitenbegrenzung und abgeschnittene Randpixel erkennen. Belege: `presentation/main.tex:154-165`, Folie 8 und Videoframe 4.

### M2, Gleichung 16 unterschreitet den Mindestrand

Die zweite Zeile reicht bis 69,49 pt vom unteren Blattrand, etwa 24,51 mm statt 25 mm. Korrektur: Gleichung oder Absatz umbrechen, damit sämtlicher Inhalt mindestens 25 mm vom Rand bleibt. `scripts/verify_report.py` muss auch obere und untere Begrenzungen messen. Seitenbudgets erneut nachweisen. Beleg: PDF S. 10, Gl. 16, `report/main.tex:314-320`.

### M3, Ersatzinvestition und Unsicherheitsanalyse

Die initiale Ausrüstung erhält 20 % Reserve und 60 % Zuschlag, die Ersatzinvestition in Jahr 15 verwendet nur 25 % ohne den 60-%-Zuschlag. Für H1 beträgt der unterschlagene Barwertanteil rund 37,57 Mio. €. Korrektur: denselben Zuschlag anwenden oder Ausschluss begründen, H1 bis H3 und alle Darstellungen neu rechnen. Belege: `model/core.py:120-127,180-181`, Regeltext PDF S. 4.

Die Monte-Carlo-Rechnung koppelt Abfluss nicht an jährliche Kostenreihen. Korrektur: Abfluss, COP und Investitionsfaktor gemeinsam einspeisen, betroffener Stromanteil, Wetter und Verfügbarkeit als Szenarien ergänzen, Wirtschaftlichkeits- und Grenzfalltests erweitern. Belege: `model/run_all.py:147-161`, PDF S. 9.

### M4, Quellenregister und NIST-Referenz

Drei Titel widersprechen den Originalen:

- Fan et al. muss „Quantifying the historic and future response...“ heißen, nicht „Hydrological functioning of a karst system with multiple recharge pathways“.
- Ouellet und Caissie muss „Towards a better understanding of the evaporative cooling of rivers...“ heißen, nicht „River water temperature and heat exchange modelling“.
- Lauber et al. muss „Spatially resolved information on karst conduit flow from in-cave dye tracing“ heißen, nicht „Flow and transport in the Blau karst system“.

Zudem fehlt der zweite NIST-Link bei 3,17007 bar im Literaturverzeichnis. Korrektur: Titel angleichen und zweiten Link aufnehmen, Register und Bericht automatisiert vergleichen. Belege: `sources/registry.yml`, DOI- und Preprint-Seiten, `report/main.tex:353`, `research_notes/Blautopf Wärmeschutz/physical_system.md:140`.

### M5, Einfrier- und Prüfnachweis unvollständig

Das Manifest enthält 116 Dateien, der Commit 120. Fehlend sind `reports/Blautopf Wärmeschutz.md` und drei Recherchenotizen. Git kodiert Umlautpfade, wodurch `path.is_file()` fehlschlägt. Korrektur: `git ls-files -z` und NUL-getrennte Verarbeitung verwenden, anschließend exakte Übereinstimmung mit `git ls-tree -r -z --name-only <commit>` verlangen. Vertikal- und Folienoverflow aus M1 und M2 ebenfalls prüfen.

### M6, Wärmesenke und Stromversorgung nicht belastbar ausgelegt

Fläche, Luftführung, Rückverwirbelung, Lärm, Netzanschluss und Notstromdauer fehlen. Folie 6 behauptet zwei Netzeinspeisungen ohne Parameter oder Kostenzeile. Korrektur: vorläufige Senken- und Versorgungsauslegung mit Fläche, Luftführung, Rückverwirbelung, Lärm, zwei Einspeisungen, Brennstoffvorrat und Überbrückungsdauer ergänzen. Bis dahin Detailversprechen auf konzeptionellen Entwurf begrenzen. Belege: PDF S. 5 bis 6 und 11, `presentation/main.tex`, Parameterdatei.

### M7, visuelle Qualität hinter D4RT

Zweispaltigkeit, Times-Hierarchie und Tabellenlinien gelingen. D4RT integriert Abbildungen präziser und dichter. Der Bericht verwendet kleine Achsenbeschriftungen und wiederholt automatische Beschriftungen im Caption-Text. PDF-Seite 14 lässt viel Raum frei. Korrektur: manuell wiederholte Labels entfernen, Achsen und Legenden vergrößern, Folien 3, 7 und 8 vereinfachen, Anhang neu umbrechen. D4RTs kleinere Schriftgrade und Ränder nicht übernehmen. Belege: `report/main.tex`, gerenderte Seiten 2, 8 und 14, D4RT-Seiten 1 und 6.

## Restrisiken und Dissens

- Vulkanische Erwärmung und Prognose bleiben Prämissen. Der betroffene Stromanteil ist die größte offene Auslegungsfrage.
- Hochwasser 12,48 GW, Temperaturen über 100 °C, größere Ströme und gemeinsame Ausfallursachen sind nicht abgedeckt.
- H1 gegen H2 ist eine Wertentscheidung. H1 kostet mehr, vermeidet aber Wasserverbrauch und offene Verdunstung. Vollstrom oder gemessener Teilstrom kann anders bewertet werden.
- Unabhängigkeit ist dokumentiert, aber nicht extern beweisbar. Keine verbotenen Inhalte geöffnet.
- KI-Offenlegung ist umfassend. Persönliche Auseinandersetzung und Prüfung durch registrierte Teammitglieder fehlen.
- Finalisten-E-Mail, Dateiname, Exportvorgaben, Abgabekanal, Rechtefreigabe und Live-Teilnahme bleiben menschliche Restaufgaben.
- Kein Dissens mit anderen Reviewern feststellbar, weil keine anderen Bewertungen gelesen wurden.

## Prüfgrenzen

- `make model`, `make report`, `make presentation` und `make verify` wurden wegen Schreibzugriffen nicht erneut ausgeführt. Die fünf Modelltests liefen mit deaktiviertem Bytecode-Schreiben erfolgreich. Zentrale Werte, NPZ-Stichproben, Hashes, Geometrie und Medien wurden unabhängig read-only geprüft.
- Alle 16 Berichtsseiten, zehn Folien, Kontaktübersichten und fünf Videoframes wurden geöffnet. Die vollständige MP4-Decodierung war fehlerfrei. Dauer 289,933594 s, H.264/yuv420p und AAC/48 kHz mono. Lautheit −17,4 dB Mittelwert und −1,3 dB Maximum.
- Sprachliche Verständlichkeit und exakte Übereinstimmung der Tonspur mit dem Sprechtext wurden nicht durch ein unabhängiges Transkript oder menschliches Hören geprüft. Keine menschliche Live-Darbietung.
- D4RT-Seiten 1 und 6 wurden direkt als verkleinerte Seiten verglichen, die übrigen 15 Seiten nicht visuell geprüft.
- Zentrale Quellen und Regeln wurden live gegengeprüft, aber nicht jede der 22 Quellen vollständig.
- Das Video weist SAR 1215:1216 und DAR 135:76 auf. Beim Neuexport soll `setsar=1` gesetzt werden.

## Urteil zur Stoppregel

Nicht erfüllt. Abgeschnittene Folie 8 und Verstoß gegen den 25-mm-Mindestrand sind unmittelbare Abgabefehler. Kostenmodell, Quellenregister und Einfriernachweis enthalten weitere materielle Mängel. Nach Korrekturen sind Bericht, Präsentation und Manifest vollständig neu zu erzeugen und erneut unabhängig zu prüfen.
