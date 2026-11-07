# Rohbericht zu Commit `2fd9f3cd11e2f984f4fb8ce693b855529cabc580`

## Prüfumfang und verifizierte Ausgaben

- Der Arbeitsbaum entspricht exakt dem Prüfcommit. Von den 142 versionierten Dateien habe ich 122 Dateihashes gegen `review/rounds/round4/revision.json` geprüft, ohne frühere Reviewinhalte zu lesen. Es gab keine Abweichung. Frühere Rohreviews und Scorecards blieben ungelesen. Nur die ausdrücklich erlaubte Befundzuordnung wurde berücksichtigt.
- Ich habe alle elf gerenderten Berichtsseiten, alle zehn Folien und die D4RT-Referenzseiten 1, 2 und 6 geöffnet. Der Bericht hat sechs Haupttextseiten und vier Seiten für Literatur und Anhang. Die gemessenen Textaußenabstände bleiben bei mindestens 25,93 mm.
- Die MP4 wurde geöffnet und vollständig fehlerfrei decodiert. `ffprobe` bestätigt 1920 x 1080, H.264 High, AAC LC, yuv420p, SAR 1:1, DAR 16:9 und 290,174958 s. Der Videostream enthält 8.704 Frames. Alle zehn zeitlich zugehörigen Videopositionen wurden direkt aus der MP4 decodiert und mit den Folien abgeglichen.
- Alle 62 WebVTT-Cues wurden durch FFmpeg gelesen. Texte und Zeitstempel stimmen mit der Quelldatei überein. Der letzte Cue endet bei 00:04:49.706. Die gemessene Lautheit liegt bei durchschnittlich -17,3 dB und maximal -1,0 dB. Sprachverständlichkeit und natürliche Wirkung der synthetischen Stimme habe ich nicht subjektiv auditiv beurteilt.
- Zentrale Wärme-, Kondensator-, Speicher-, Diesel-, Rohr- und Kaltwasserwerte habe ich unabhängig nachgerechnet. Alle elf Modelltests bestehen mit `PYTHONDONTWRITEBYTECODE=1`. Auch die 10.000 gespeicherten Unsicherheitsziehungen und die Manifesthashes stimmen mit den ausgewiesenen Ergebnissen überein.
- Die Abflusswerte 2,3, 0,7 und 4,7 m³/s sind in der Fan-Studie belegt. NIST bestätigt Dichte, Wärmekapazität und den Sättigungspunkt 135,413 °C bei 3,17007 bar. LAWA stützt die Empfehlung von höchstens etwa 1 K/h. Die aktuellen [Berichtsvorgaben](https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Vorgaben-Bericht.pdf), [Teilnahmebedingungen](https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Teilnahmebedingungen.pdf) und das [Fünf-Minuten-Limit](https://www.planet-simtech.de/) wurden direkt gegengeprüft.
- Der reproduzierte Kandidaten-Commit unterscheidet sich vom Bewertungscommit nur durch `review/rounds/round4/reproduction.md`. Damit gilt die Archivreproduktion für denselben fachlichen Inhalt. Das MP4 wurde dort allerdings nicht erneut kodiert.
- Ich habe keine Builds ausgeführt und keine Dateien verändert. `make verify` wurde wegen seiner Schreibzugriffe nicht wiederholt. Die Git-Ausgabe bleibt unverändert bei den beiden bereits vorhandenen unversionierten Prüfdateien `prompt.md` und `revision.json`.

## Einzelbewertungen

| Kriterium | Bewertung | Kurze Begründung und genaue Belegorte |
|---|---:|---|
| 1. Qualität der Argumentation | 9 | Die Argumentation führt von der Szenarioprämisse über die offene Wärmebilanz zur Vollstromkühlung. Der Speicherfehlschluss, die Kondensatorwärme und der Unterschied zwischen Siedeschutz und ökologischem Normalzustand werden ausdrücklich behandelt. Belege: Bericht PDF S. 2 bis 4, Gleichungen 1 bis 9, S. 6 § 4.4, Folien 2, 3, 8 und 10. |
| 2. Vorgehen und Methodik | 9 | Sieben Ansätze werden vor der quantitativen Auswahl registriert und danach mit gemeinsamen Randbedingungen verglichen. Dynamische Ausfallrechnung, gekoppelte Unsicherheit, Sensitivitäten und Archivreproduktion ergänzen die stationäre Auslegung. Belege: `docs/hypothesen.md` H1 bis H7, `docs/alternativenvergleich.md`, `model/validation.py:27-164`, `output/model/sensitivity.csv`, `review/rounds/round4/reproduction.md`. |
| 3. Qualität der vorgeschlagenen Lösung | 9 | H1 schließt den Wasser- und Energiepfad mit Trockenkühlung, Kältemaschine, externer Luftsenke, Reserve und Ersatzstrom. Standort, Karsterfassung, Netz und Genehmigung bleiben ausdrücklich Zulassungsbedingungen statt erfundener Nachweise. Belege: Bericht PDF S. 4 bis 6 §§ 3.2, 4.2 und 4.3, `output/model/results.json` `baseline`, `design`, `boil_guard`, Folien 5, 8 und 9. |
| 4. Mathematische und wissenschaftliche Modellierung | 9 | Die unabhängig nachgerechneten 877,781145 MW, 1793,726688 MW, 2152,472026 MW, 373,780433 MW und 2.236.544,98 L Diesel stimmen exakt. Energie- und Mischungsbilanzen schließen. Die ODE- und Konvergenzfehler sind klein. Belege: `model/core.py:39-113`, `model/validation.py:67-164`, `output/model/results.json` `baseline`, `design`, `validation`; elf bestandene Tests. |
| 5. Ableitung neuer Ansätze | 9 | Die Hypothesen sind vor der Rechercheauswertung dokumentiert, und die Skalierung von H1 folgt aus der eigenen Wärmebilanz. Allgemeine Fachquellen werden verwendet, frühere Wettbewerbslösungen nicht. Die Nichtverwendung früherer Ergebnisse ist dokumentiert, aber als Negativnachweis nicht extern überprüfbar. Belege: `docs/hypothesen.md:3-59`, `PROVENANCE.md`, `EXCLUSION_LOG.md`, `decisions.tsv`, `sources/registry.yml`. |
| 6. Wissenschaftliche Qualität | 9 | Zentrale Eingaben beruhen auf Primärquellen und wurden an Fan, LGRB, Stadt Blaubeuren, NIST und LAWA bestätigt. COP, Kosten, Feuchtkugel und konstante Stoffwerte sind als Annahmen oder Näherungen gekennzeichnet. Feldvalidierung wird nicht behauptet. Belege: Bericht PDF S. 3 Tabelle 1, S. 7 § 5, Anhang B, `sources/registry.yml` Einträge 1 bis 5 und 10. |
| 8. Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen | 9 | Messwerte, Szenarioprämissen und technische Annahmen werden getrennt. Die einseitige Zusammenfassung nennt Ergebnis, Kosten, Alternativen und Grenzen ohne unerklärte Kurzbegriffe wie p90, H1 oder Barwert. Belege: Bericht PDF S. 2 Zusammenfassung und Einführung, S. 3 Tabelle 1, S. 8 § 6, `presentation/speaker_notes.md`. |
| 9. Kritische Diskussion der Ergebnisse | 9 | Der Bericht behandelt Wasserverbrauch gegen Stromemissionen, Mittelwertüberlast, Hochwasser, COP, Tarif, Verfügbarkeit, gemeinsame Ausfallursachen, Standort und Falsifikation. Die 27 Juryfragen greifen diese Schwachstellen erneut auf. Belege: Bericht PDF S. 5 bis 7 §§ 4.1 bis 5, `presentation/jury_qa.md` Fragen 5 bis 26, `output/model/results.json` `uncertainty`, `availability_scenarios`, `tariff_scenarios`. |
| 10. Berichtsstruktur und Jury-Nachvollziehbarkeit | 9 | Zusammenfassung, Einführung, Methode, Ergebnisse, Diskussion, Nachweis und Schlussfolgerung folgen einer klaren Kette. Abbildungen, Tabellen und Anhänge sind referenziert und vollständig. Belege: Bericht PDF S. 2 bis 8, Anhänge A bis C auf PDF S. 10 und 11, `report/main.tex:27-306`. |
| 11. Format, Zitation, Einreichung und D4RT-Qualität | 8 | Seitenbudget, A4, Ränder, Anonymität, Pflichtdeckblatt, numerische Verweise, KI-Anhang und vollständige Hyperlinkziele sind erfüllt. Der direkte D4RT-Vergleich bestätigt die geordnete Typografie. Abbildung 1 hat jedoch 9,63-pt-Achsenbeschriftung, Abbildung 3 nur 8,33 bis 9,52 pt und eine 5,95-pt-Legende. Das widerspricht der 12-pt-Vorgabe und ist im Video zu klein. Belege: PDF S. 5 Abbildung 1, PDF S. 10 Abbildung 3, Folie 8, `review/rendered/video_frames/frame_4.png`, `scripts/verify_report.py:85-89`, `compliance/layout_referenz.md:15-19`. Zusätzlich fehlt die zweite NIST-Abfrage im Register, siehe M2. |
| 12a. Bereitschaft für die schriftliche Runde | 8 | Inhalt und Dokument sind weitgehend abgabefertig. Die nachgewiesenen Diagrammschriftgrößen verhindern jedoch das Prädikat "nachweisbar regelkonform abgabebereit". Team-ID und menschliche Endprüfung bleiben korrekt ausgewiesene Restaufgaben. Belege: PDF S. 5 und 10, Anhang A, `compliance/checklist.md`, `PROVENANCE.md:41-43`. Korrekturen: M1 und M2. |
| 12b. Bereitschaft für die Finalrunde | 8 | Folien, echte MP4, Sprechtext, 62 VTT-Cues, dokumentierte Echtzeitdecodierung, Rechteprotokoll und 27 adversariale Fragen sind vorhanden. Die kleine Diagrammbeschriftung ist nicht präsentationsreif. Zudem bleiben die subjektive AV-Prüfung, manuelle VTT-Prüfung, Rechtefreigabe und eine Archiv-Neukodierung des Videos offen. Belege: `presentation/rehearsal.md:18-29`, `presentation/rights.md:26-28`, `review/rounds/round4/reproduction.md:24`, Folie 8 und `frame_4.png`. Korrekturen: M1 und M3. |

## Materielle Mängel und konkrete Korrekturen

### M1. Diagrammschrift ist zu klein und entgeht der automatischen Prüfung

Die offizielle Vorgabe nennt 12 pt ohne dokumentierte Ausnahme für Diagrammbeschriftungen. Im gerenderten Bericht habe ich mit `pdfplumber` gemessen:

- PDF S. 5, Abbildung 1: Achsen- und Tickbeschriftungen mit 9,63 pt.
- PDF S. 10, Abbildung 3: Achsen und Ticks mit 8,33 bis 9,52 pt, Legende mit 5,95 pt.
- `scripts/verify_report.py:85-89` prüft nur den Median aller alphabetischen Zeichen. Dadurch bleiben diese Abweichungen unentdeckt.
- Folie 8 und der tatsächliche MP4-Frame `review/rendered/video_frames/frame_4.png` verwenden dieselbe kleine Legende. Auf einem gestreamten Finalvideo ist sie nicht ausreichend lesbar. Auch unabhängig von der wörtlichen 12-pt-Auslegung bleibt dies ein Darstellungsmangel.

**Korrektur:** `fig01_prognose_last` und `fig05_unsicherheit` so erzeugen, dass jede Achsen-, Tick- und Legendenbeschriftung nach der endgültigen PDF-Skalierung mindestens 12 pt beträgt. Die übrigen Figuren ebenfalls einzeln messen. Für Folie 8 die Grafik vergrößern, die Legende auf mehrere Zeilen verteilen oder die drei Linien direkt beschriften. Bericht, Folien und MP4 neu erzeugen und anschließend PDF und Video erneut sichtprüfen. `scripts/verify_report.py` muss kleine Diagrammschrift einzeln erkennen statt nur den Median zu prüfen. Hashes und Reproduktionsnachweise aktualisieren.

### M2. Die zweite NIST-Abfrage ist nicht wie behauptet registriert

`report/main.tex:224` erklärt: "Vollständige Abfragen stehen im Quellenregister und im Modell." `sources/registry.yml:22-26` enthält jedoch nur die Isobarentabelle bei 1,01325 bar. Die verwendete Drucktabelle bei 3,17007 bar ist dort nicht als zweite vollständige URL hinterlegt. Der Wert 135,413 °C ist selbst korrekt und wurde direkt bei NIST bestätigt.

**Korrektur:** Für die Drucktabelle eine zweite vollständige NIST-URL mit `Type=IsoBar`, `P=3.17007`, `TLow=130`, `THigh=140` und `TInc=1` in `sources/registry.yml` aufnehmen und die Abfrage maschinenlesbar in `data/parameters.yml` verknüpfen. Alternativ den Satz im Literaturverzeichnis auf die tatsächlich vorhandenen Nachweise beschränken.

### M3. Die Finalreife ist technisch weit fortgeschritten, aber nicht abgeschlossen

`presentation/rehearsal.md:23` kennzeichnet die Satzzeiten als nicht durch Forced Alignment verifiziert. `presentation/rights.md:26-28` lässt die menschliche Rechte- und Stimmfreigabe offen. `review/rounds/round4/reproduction.md:24` bestätigt, dass das MP4 in der Archivkopie nicht erneut kodiert wurde. Meine eigene Prüfung deckt Streams, Pegel, Frames und Textzeiten ab, aber keine verlässliche subjektive Beurteilung der synthetischen Sprache.

**Korrektur:** Nach M1 das Video neu erzeugen. Danach eine vollständige menschliche Hör- und Sichtprobe auf 1920 x 1080 durchführen, die VTT-Cues manuell an der tatsächlichen Sprache ausrichten und die synthetische Vertonung und Rechte ausdrücklich freigeben. Rollenverteilung, Technik und Juryfragen in einer echten Teamprobe erproben. Schließlich `make presentation` in einer frischen Archivkopie desselben Kandidaten-Commits ausführen und das Ergebnis erneut decodieren und vergleichen. Die Finalisten-E-Mail muss vor Abgabe auf Dateiformat und weitere Vorgaben geprüft werden.

## Restrisiken und Dissens

- Die reale Machbarkeit bleibt unbewiesen. Betroffener Karststrom, thermischer Kurzschluss zwischen Entnahme und Rückführung, COP, Teillast, Feuchtkugel, Luftführung, Schall, Netzanschluss, Fläche und Genehmigung benötigen Messungen oder externe Nachweise. Der Bericht verschweigt das nicht. Meine 9 für Lösung und Wissenschaftlichkeit bewertet den Szenarioentwurf, keine Baufreigabe.
- Der Hochwasserfall 32,7 m³/s ist für das 9-°C-Ziel nicht ausgelegt. Eine uneingeschränkte Dauerzusage wäre falsch. Die vorhandene Begrenzung auf höchstens 4,7 m³/s und 100 °C ist deshalb fachlich notwendig, bleibt aber eine wesentliche Einschränkung der Antwort.
- Konstante Wasserstoffwerte und der pauschale latente Wärmestrom bei H2 sind Screening-Näherungen. Für eine Detailauslegung sind temperatur- und druckabhängige Stoffwerte sowie eine vollständige Verdunstungsbilanz erforderlich.
- Der Kostenzeitplan enthält 26 Jahreszeilen von Jahr 0 bis Jahr 25. Dies kann als vereinfachende und im Referenzfall eher konservative Diskretisierung gelesen werden. Eine eindeutige Definition der Kostenperioden wäre besser. Ich bewerte das nicht als nachgewiesenen zentralen Rechenfehler, aber als verbleibendes Modellrisiko. Netzanschlusskosten fehlen ausdrücklich.
- Die Unabhängigkeit der Herleitung ist gut dokumentiert. Council B bleibt dennoch ein Same-Model-Kontext und keine externe oder menschliche Fachprüfung.
- Die VTT-Datei ist technisch gültig, aber wortproportional zeitverteilt. Sie beweist keine satzgenaue Synchronisation. Die MP4 enthält nur einen Video- und einen Audiostream; die Untertitel liegen als separate VTT-Datei vor. Ob ein eingebetteter Untertitelstream verlangt wird, muss die Finalisten-E-Mail klären.

## Fehlersuche für Bewertungen von 10

Ich vergebe keine 10. Die eigene substanzielle Fehlersuche war nicht erfolglos. Sie bestätigte zwar die zentralen Energiebilanzen, Primärquellen, Tests und Videodaten, fand aber die genannten Darstellungs-, Nachweis- und Finalreifeprobleme. Damit fehlt die für eine 10 erforderliche Begründung, dass kein substanzieller Fehler verbleibt.

## Stoppregelurteil

**Die Stoppregel ist auf diesem Commit nicht erfüllt.**

Die Kriterien 11, 12a und 12b liegen mit jeweils 8 unter dem verlangten Mindestwert von 9. Der entscheidende materielle Einwand ist die nachgemessene Diagrammschrift einschließlich ihrer Übernahme ins Finalvideo. Hinzu kommen der unvollständige NIST-Nachweis und die offenen AV-, Rechte- und Videoreproduktionsprüfungen.

Die physikalische Kernargumentation, die Modellwerte und die bisherige Berichtsreproduktion tragen das Paket weit, ersetzen diese Korrekturen aber nicht. Erst nach M1 bis M3 sollte ein neuer gemeinsamer Commit eingefroren und erneut von beiden Reviewern bewertet werden.