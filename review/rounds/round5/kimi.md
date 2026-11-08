# Rohbericht zu Commit `e821bf60ef9fe637a5c5915a50d7748ab829c46c`

Ausschließlich dieser Commit wurde bewertet. Frühere Rohreviews und Scorecards habe ich nicht gelesen. Die Befundzuordnung ohne frühere Punktzahlen wurde entsprechend dem Auftrag geprüft. Seitenangaben bezeichnen physische PDF-Seiten einschließlich Deckblatt.

## Prüfnachweis

- Alle 155 SHA-256-Hashes aus `review/rounds/round5/revision.json` stimmen mit den Git-Blobs, dem Arbeitsbaum und einem direkt gestreamten `git archive` des Zielcommits überein.
- Ich habe die Kontaktübersichten, alle zwölf Berichtsseiten, alle zehn Folien und die D4RT-Seiten 1, 2 und 6 geöffnet.
- Die 22 vorhandenen PDF-Renderbilder ließen sich durch direktes Rendern nach stdout byteweise reproduzieren. Auch die fünf Review-Videoframes waren bei direkter Decodierung identisch.
- Die MP4 wurde vollständig decodiert. Zusätzlich lief eine eigene Echtzeitdecodierung fehlerfrei mit `real 289.72`, `user 46.05` und `sys 1.81`. Die Dateidauer beträgt 290,23175 s.
- Alle zehn unabhängig aus der MP4 entnommenen Folienbilder passen zu den PDF-Folien. Die 63 VTT-Cues sind monoton, innerhalb ihrer Segmente und textgleich mit dem Sprechtext.
- Zentrale Modellwerte, Jahresreihen, Ersatzinvestition, 42 Manifest-Hashes, 10.000 Stichproben und der p90-Ausfallverlauf wurden unabhängig nachgerechnet.
- Die aktuellen offiziellen Berichtsvorgaben, Teilnahmebedingungen, FAQ und Finaleinformationen wurden direkt gegengeprüft.
- Den vollständigen Build in einer Archivkopie habe ich wegen des Read-only-Auftrags nicht erneut ausgeführt. Geprüft habe ich stattdessen den dokumentierten Lauf, die Buildkette, sämtliche Archivinhalte und die Dateidifferenzen zwischen Kandidaten- und Zielcommit.
- Projektdateien und Git-Stand blieben unverändert. Es wurde kein Review in Dateien geschrieben.

## Einzelbewertungen

| Kriterium | Bewertung | Begründung und genaue Belegorte |
|---|---:|---|
| 1. Qualität der Argumentation | 9 | Die Argumentation führt schlüssig vom Kontrollvolumen über die Wärmebilanz zur Vollstromkühlung, externen Wärmesenke und falsifizierbaren Betriebsgrenzen. Siedeschutz und ökologisches 9-°C-Ziel werden nicht vermischt. Belege: Bericht PDF S. 2, Abschnitt 1, PDF S. 4 bis 8, insbesondere Abschnitte 4.4, 5 und 6; Abbildung 1 auf S. 5. |
| 2. Vorgehen und Methodik | 9 | Quellenwerte, Szenarioprämissen und technische Annahmen sind getrennt. Sieben Ansätze werden vor der quantitativen Auswahl registriert und danach mit gemeinsamer Last, Reserve und Kostenlogik verglichen. Sensitivität, Monte Carlo, Rampe und Ausfallmodell ergänzen die stationäre Bilanz. Belege: Tabelle 1 auf PDF S. 3; `docs/hypothesen.md`; `model/core.py`, `model/run_all.py`, `model/validation.py`; Ergebnisse auf PDF S. 4 bis 8. |
| 3. Qualität der vorgeschlagenen Lösung | 8 | Die zweistufige Kühlung ist als Szenarioentwurf physikalisch stimmig und enthält Reserve, Wiederanlauf und Alternativen. Die reale Umsetzbarkeit der empfohlenen Vollstromanlage bleibt jedoch unbewiesen. Es gibt weder einen konkreten Standort noch eine Netzzusage, Herstellerkurven oder einen Nachweis der vollständigen Strömungserfassung. Das ist für dieses Kriterium mehr als eine optionale Verbesserung. Belege: Bericht PDF S. 6, Abschnitt 4.3, und S. 8, Abschnitt 5; `output/model/results.json`, Bereich `design`; `presentation/jury_qa.md`, Fragen 11, 24 und 26. |
| 4. Mathematische und wissenschaftliche Modellierung | 9 | Die Gleichungen und gespeicherten Ergebnisse sind konsistent. Meine unabhängigen Rechnungen ergaben 877,781145245 MW, 1793,726688109 MW p90-Bedarf, 2152,472025731 MW installierte Leistung und 2.236.544,982 Liter Diesel. Der analytische p90-Höchstwert liegt bei 16,66377884 °C gegenüber 16,66377598 °C im Integrationsgitter. Der NIST-Enthalpievergleich ergab 866,605 MW; das konstante Stoffwertmodell liegt damit 1,29 % konservativ darüber. Belege: Gleichungen 1 bis 10 auf PDF S. 3 bis 6; `output/model/results.json`, `baseline`, `design`, `validation`; `model/test_model.py`. |
| 5. Ableitung neuer Ansätze | 9 | Die sieben physikalischen Wege werden aus der Enthalpiefrage entwickelt, nicht aus früheren Wettbewerbslösungen abgeleitet. Die Skalierung vom Teilkreislauf zum Vollstrom ist dokumentiert. Bekannte Technik wird nicht als weltweite Neuheit ausgegeben. Belege: `docs/hypothesen.md`, Abschnitte H1 bis H7 und „Skalierung nach der Wärmebilanz“; `PROVENANCE.md`, Unabhängigkeit und KI-Beteiligung; `EXCLUSION_LOG.md`; Bericht PDF S. 3 und Anhang A auf S. 11. |
| 6. Wissenschaftliche Qualität | 9 | Die Arbeit stützt zentrale Eingaben auf 25 nummerierte Quellen und kennzeichnet Rechenannahmen ausdrücklich. Fan et al. bestätigen Mittelwert 2,3 m³/s sowie die Quantile 0,7 und 4,7 m³/s. NIST bestätigt die Stoffwerte, BDEW den Tarifproxy und UBA den Emissionsfaktor. Fehlende Feldvalidierung, Herstellerdaten und Angebote werden offengelegt. Belege: Literaturverzeichnis auf PDF S. 8 bis 10; `sources/registry.yml`; `research_notes/Blautopf Wärmeschutz/`; Anhang A und B auf PDF S. 11. |
| 8. Klare Erklärung | 9 | Zusammenfassung, Methodik, Ergebnisse, Schlussfolgerung und Tabellen vermitteln die Aussagen mit nachvollziehbaren Einheiten. Die Zusammenfassung vermeidet die Abkürzungen p90, H1 und Barwert. Folien und Sprechtext verwenden denselben Modellstand. Belege: PDF S. 2 bis 8; Tabellen 1 bis 4; Folien 2 bis 10; `presentation/speaker_notes.md`; `report/generated/numbers.tex`. |
| 9. Kritische Diskussion | 9 | Die Arbeit diskutiert Wasser- und Emissionsfolgen, fehlende Standort- und Herstellernachweise, gemeinsame Ausfallursachen, Tarif- und Wetterempfindlichkeit sowie die Begrenzung der Monte-Carlo-Verteilung. Der 32,7-m³/s-Fall wird ausdrücklich nicht abgedeckt. Belege: Bericht PDF S. 5 bis 8, Abschnitte 4.1 bis 5; `presentation/jury_qa.md`, Fragen 13, 21 bis 26; `output/model/sensitivity.csv`. |
| 10. Berichtsstruktur und Jury-Nachvollziehbarkeit | 9 | Die Struktur folgt dem Pflichtaufbau und führt von Aufgabenprämisse über Methode und Auslegung zu Falsifikation und Schluss. Die Jury kann die zentrale Rechnung ohne Repository verstehen. Der einzelne Fortsetzungssatz am Anfang von PDF S. 8 und der Weißraum auf S. 10 und 11 sind kleine Satzschönheitsfehler. Belege: PDF S. 2 bis 8 sowie Anhang auf S. 11 und 12. |
| 11. Format, Zitation, visuelle Qualität | 9 | A4, mindestens 26 mm gemessener Rand, etwa 12 pt Text, sechs Haupttextseiten und fünf Seiten Literatur plus Anhang sind eingehalten. Numerische Verweise, Abrufdaten, KI-Offenlegung und leere Autorenmetadaten sind vorhanden. Gegenüber D4RT ist der Satz weniger dicht, aber sauber, konsistent und gut lesbar. D4RTs kleinere Schriften und Ränder wurden nicht übernommen. Belege: alle Berichtsseiten; `compliance/layout_referenz.md`; D4RT-Bilder 1, 2 und 6; direkte Geometrie- und Renderprüfung aller 22 Seitenbilder. |
| 12a. Bereitschaft für die schriftliche Runde | 9 | Die tatsächliche PDF erfüllt als Testpaket die aktuellen formalen Anforderungen. Der dokumentierte Archivlauf des Kandidaten `9d8f4df...` erzeugte 41 Artefakte und 33 Renderbilder identisch. Zum Zielcommit unterscheiden sich nur `decisions.tsv`, `review/revisions.md` und der Reproduktionsnachweis. Offizielle Team-ID und menschliche Einreichungsfreigabe bleiben ausdrücklich organisatorische Restaufgaben. Belege: `output/pdf/TEST-K31pro-max.pdf`; `review/rounds/round5/reproduction.md`; `review/rounds/round5/revision.json`; `PROVENANCE.md`, menschliche Restaufgaben. |
| 12b. Bereitschaft für die Finalrunde | 8 | Folien, echte MP4, Sprechtext, VTT, technische Zeitprobe, Rechtenachweis und 27 adversariale Fragen mit Revisionen liegen vor. Die technische Bereitschaft ist hoch. Eine menschliche Hör- und Sichtfreigabe, manuelle VTT-Freigabe und echte Teamprobe fehlen jedoch. Ich konnte die subjektive Sprachverständlichkeit nicht menschlich beurteilen. Die VTT-Zeiten sind nur wortproportional verteilt. Belege: `presentation/rehearsal.md`, besonders S. 21 bis 29; `presentation/timings.json`, `subtitle_alignment`; `presentation/rights.md`, verbleibende Freigabe; `presentation/jury_qa.md`, Frage 18. |

## Materielle Mängel und konkrete Korrekturen

### M1. Reale Machbarkeit der Referenzlösung ist noch offen, Kriterium 3

Die Konzeptqualität ist hoch, aber die einzige als Referenz empfohlene Anlage besitzt noch keinen nachgewiesenen realen Standort- und Betriebsfall. Die offene Erfassung des gesamten betroffenen Stroms, die fehlende Netzzusage und die fehlenden Herstellerdaten begrenzen die Lösungsqualität. Die Checkliste darf dies nicht als bereits nachgewiesene Machbarkeit lesen.

Belege: Bericht PDF S. 6, Abschnitt 4.3; PDF S. 8, Abschnitt 5; `presentation/jury_qa.md`, Fragen 11, 24 und 26; `output/model/results.json`, `design.air_service_area_m2`, `design.electricity_mw`.

Korrektur:

1. Einen konkreten Standort mit Flächenplan, Luftführung, Schall- und Rückverwirbelungsprüfung auswählen und die 8,19 ha sowie die Wärmeabgabe von 1976,4 MW dort bilanzieren.
2. Vom Netzbetreiber die benötigte Leistung von 182,7 MW je unabhängiger Einspeisung bestätigen lassen und Netzanschlusskosten ergänzen.
3. Herstellerkurven für Kältemaschinen, Trockenkühler und Aggregate bei den angenommenen Temperaturen und im p90-Wiederanlauf einholen.
4. Durch Tracer-, Durchfluss- und Druckmessungen nachweisen, welcher Karstast die Wärme trägt und ob die Anlage diesen Strom vollständig erfasst.
5. Die Referenzlösung anhand dieser Ergebnisse bestätigen, verkleinern oder verwerfen. Erst danach kann Kriterium 3 mit mindestens 9 bewertet werden.

### M2. Subjektive Medienfreigabe und echte Teamprobe fehlen, Kriterium 12b

Die technische MP4-Prüfung ersetzt keine Beurteilung der synthetischen Sprache durch das Team. Die wortproportionalen Untertitel können von der tatsächlichen Aussprache abweichen. Eine echte Teamprobe mit Rollenverteilung und Fragen ist nicht dokumentiert.

Belege: `presentation/rehearsal.md`, Abschnitte zur menschlichen Probe und VTT; `presentation/timings.json`, `subtitle_alignment`; `presentation/rights.md`, „Verbleibende menschliche Freigabe“.

Korrektur:

1. Das Team muss die tatsächliche MP4 vollständig hören und sehen und dabei Verständlichkeit, Zahlenaussprache, Tempo und Folienwechsel freigeben oder nachbearbeiten.
2. Die 63 VTT-Cues gegen den Ton prüfen und ihre Zeiten manuell korrigieren.
3. Eine echte Teamprobe mit Rollenverteilung, Wiedergabetechnik und adversarialem Fragenteil durchführen und Ergebnis, Dauer und festgestellte Änderungen in `presentation/rehearsal.md` dokumentieren.
4. Rechte und synthetische Stimme in `presentation/rights.md` ausdrücklich freigeben und die Finalisten-E-Mail auf Dateiformat und Abgabeweg prüfen.

## Kleinere, nicht bewertungsmindernde Befunde

- `review/revisions.md`, Abschnitt „Befunde aus Runde 3, DeepSeek“, nennt 62 VTT-Cues. Die aktuelle Datei enthält 63. Die Zahl sollte beim nächsten redaktionellen Abgleich korrigiert werden.
- `presentation/jury_qa.md`, Frage 6, verweist für 8 und 12 Jahre auf Jahresreihen. Exportiert sind dafür in `output/model/sensitivity.csv` nur Endlast und Barwert. Entweder die zugehörigen Jahresreihen ebenfalls ausgeben oder die Antwort auf die intern berechneten Kostenpfade präzisieren.
- Die D4RT-Integration ist funktional gelungen. Für eine weitere Satzverbesserung könnten der Fortsetzungssatz am Beginn von PDF S. 8 und der Weißraum auf S. 10 und 11 reduziert werden. Das sind keine Abgabehindernisse.

## Restrisiken und Dissens

- Vulkanische Tiefenerwärmung, lineare Prognose und die Kappung bei 100 °C bleiben Szenarioprämissen. Ein späterer Temperaturanstieg oder eine andere Wärmequelle verlangt einen neuen Entwurf.
- Der betroffene Stromanteil ist ungemessen. Der Vollstromfall mit 32,7 m³/s würde 12,48 GW Kühlleistung verlangen und ist nicht abgedeckt.
- Die Monte-Carlo-Verteilung endet bei 4,7 m³/s. Ihre vollständige Abdeckung ist eine Folge der Kapazitätswahl, keine Extremwertgarantie.
- Konstante Stoffwerte und nicht angerechnete natürliche Wärmeverluste bleiben Näherungen. Der unabhängige Enthalpievergleich begrenzt den Fehler der zentralen Leistung auf konservative 1,29 %, ersetzt aber keine temperaturabhängige Detailauslegung.
- Kosten, COP, Feuchtkugel, Luftführung, Diesellogistik, gemeinsame Ausfallursachen und reale Anlaufkurven bleiben unsicher.
- Der Reproduktionslauf nutzte eine verknüpfte `.venv`. Er belegt die Archiv- und Artefaktreproduktion in derselben Referenzumgebung, nicht eine Neuinstallation aller Abhängigkeiten auf einem fremden Rechner.
- Council B bleibt ein Same-Model-Kontext, keine externe menschliche Fachprüfung.
- Offizielle Team-ID, Medienrechte, Einwilligungen, Finalisten-E-Mail und tatsächliche Einreichung sind weiterhin offen.

Ich habe keinen anderen Reviewer kontaktiert und keine fremden Punktzahlen gesehen. Ein abgestimmter Konsens oder Dissens ist daher nicht Gegenstand dieses Berichts. Mein Dissens zur optimistischen Lesart der Paket-Checkliste betrifft die Kriterien 3 und 12b: Ich werte die offene reale Machbarkeit und die fehlende subjektive Medien- sowie Teamprobe nicht als bereits geschlossene Punkte.

## Bewertungen mit 10 und Fehlersuche

Ich vergebe keine Bewertung 10. Daher gibt es keine zehnerspezifischen Berichte über eine erfolglose substanzielle Fehlersuche.

Die allgemeine Fehlersuche umfasste unabhängige Wärme-, Kosten-, Ersatz- und Ausfallrechnungen, Stichproben- und Manifestvergleiche, NIST-Enthalpiekontrolle, PDF-Geometrie, sämtliche Renderbilder, VTT-Inhalte und direkte MP4-Decodierung. Sie bestätigte die technische Konsistenz, führte aber zu den zwei offenen Bewertungsmängeln oben.

## Stoppregelurteil

**Die Stoppregel ist auf diesem Commit nicht erfüllt.**

Kriterium 3 und Kriterium 12b liegen mit jeweils 8 unter der geforderten Mindestbewertung von 9. Die technischen Prüfungen der tatsächlichen Ausgabedateien bestehen, aber die offene Machbarkeit der Referenzlösung und die fehlende subjektive Medien- sowie Teamprobe bleiben substanzielle Einwände. Eine Mittelung über die übrigen Bewertungen ist nicht zulässig.