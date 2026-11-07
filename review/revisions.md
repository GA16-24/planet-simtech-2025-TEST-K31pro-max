# Revisions- und Befundzuordnung

Diese Datei verbindet Juryfragen und Council-Befunde mit konkreten Änderungen oder begründeten offenen Grenzen. Rechennachweise sind keine Feldvalidierung und keine Baufreigabe.

## Fragen 1 bis 27

| Frage | Nachweis der Herleitung und späteren Änderung | Status |
| --- | --- | --- |
| 1, Speicher statt Vollstrom | `49eb33fb652215a09fd154042d3df922edadded2`, `model/core.py` | Vollstrom und Speichergrenze getrennt |
| 2, Tiefendruck | NIST und IAPWS [4,5], `data/parameters.yml` | Hydrostatisches Beispiel, kein Druckprofil |
| 3, Kühlung bei 35 °C | `cooling_stage` | Trockenkühlung und Kältestufe getrennt |
| 4, Kondensatorwärme | `baseline` und `design` in `output/model/results.json` | Externe Wärmeabgabe einschließlich Hilfsenergie |
| 5, COP | `data/parameters.yml`, gekoppelte Ziehungen | Referenz von 5 auf 4 gesenkt, Bereich 3 bis 6,5, keine Produktkurve |
| 6, Prognosezeit | `output/model/sensitivity.csv` | Endlast und Ausbaupfad getrennt |
| 7, Verdunstung | `alternatives[1]`, Feuchtkugel und Kältestufe | Physikalisch gleichwertig im Szenario, Wasser und Hygiene als Zielkonflikt |
| 8, Kälteschock | `planned_return_temperature_c` | 91-Stunden-Sollwerttest, kein Wiederanlaufnachweis |
| 9, Reserve | `design`, `module_count` | p90 mit zwölf Strängen, elf aktiv und einer Reserve |
| 10, Stromausfall | `validation.recovery_peak_temperature_c` | Dynamischer Test mit 0,5/5/10 min, keine reale Zuschaltprobe |
| 11, Stromerfassung | Messplan in Bericht und Folie 9 | Tracer und Durchfluss vor Detailauslegung |
| 12, Wärmevermarktung | `heat_recovery_mw: 0.0` | Kein Erlös ohne gemessenen Abnehmer |
| 13, Hochwasser | `baseline.flood_stress_cooling_mw` | 12,48 GW für 9 °C nicht abgedeckt |
| 14, Dauerhaftigkeit | `scenario.premise`, `hydrology.affected_fraction_design_note` | Nur innerhalb der erklärten Hülle |
| 15, Kosten | `baseline`, `design`, `tariff_scenarios` | Szenarien mit gekoppelter Unsicherheit, keine Angebote |
| 16, Falsifikation | Bericht und `docs/alternativenvergleich.md` | Explizite Abbruchkriterien |
| 17, Genehmigung | WHG [14], BNatSchG [24] | Keine Genehmigung behauptet |
| 18, Synthetische Präsentation | `presentation/rehearsal.md`, `timings.json` | Slidecast und Echtzeitprobe, keine Live-Darbietung |
| 19, D4RT | `sources/D4RT_paper.pdf`, Referenzbilder in `review/rendered/` | Direkter visueller Vergleich möglich |
| 20, Menschliche Restaufgaben | `PROVENANCE.md`, `README.md`, `presentation/rights.md` | Weiterhin offen |
| 21, Überlast | `uncertainty.mean_capacity_overload_fraction`, `design_overload_fraction` | p90-Reserve deckt begrenzte Stichprobe ab |
| 22, Feuchtkugel | `plant.wet_bulb_design_c`, `alternatives[1]` | 28 °C plus 4 K, Kältestufe bis 9 °C |
| 23, Tarif | BDEW [16], `tariff_scenarios` | 138 €/MWh als Proxy, 179 €/MWh als Alternative |
| 24, Wiederanlauf | `validation.recovery_peak_temperature_c`, `recovery_margin_minutes` | Höchstwert 12,6 °C im Szenario |
| 25, Reiner Siedeschutz | `boil_guard` | 48,5 MW statt 877,8 MW, aber kein ökologischer Normalzustand |
| 26, Standort | `design.air_service_area_m2`, `electricity_mw`, `backup_fuel_m3`, AwSV und BNatSchG | Screening vorhanden, Standort nicht nachgewiesen |
| 27, Same-Model-Review | `review/model_configuration.md`, Nutzervorgabe | Kein Modellwechsel, unabhängiger Kontext statt externer Prüfung |

## Erhaltene Korrekturen aus Runde 1

| Befund | Konkrete Änderung | Verifikation |
| --- | --- | --- |
| Folie 8 läuft über die Seite | Grafik und Text kompakt, Fußzeile gekürzt | Alle Textzeichen gegen die Folienfläche geprüft |
| Pfeil ins Leere in Folie 5 | Beide Wärmepfeile führen direkt auf `air.south` | Sichtprüfung |
| Legendenkollisionen | Legenden außerhalb der Datenflächen | Neue Figuren und Sichtprüfung |
| Gleichung 3 mit eigener Nummernzeile | Szenariogleichung gekürzt | PDF-Geometrie und Sichtprüfung |
| Gemischte Dezimaltrennzeichen | Makros und Diagrammlabels mit deutschem Komma | `report/generated/numbers.tex`, PDF und Folien |
| Falscher Vergleich „mehr als doppelt“ | Auf rund 1,7-fache Reserveauslegung korrigiert | Modellwerte |
| 1-K/h-Aussage unmodelliert | Sollwertrampe am Kälteauslass statt Pufferbehauptung | Intervalltest mit 921 Stützstellen |
| Ventilrampe als unzureichender Zwischenmechanismus | Linearer Ventilhub verworfen, Wiederanlauf getrennt | `planned_return_temperature_c` |
| Seitenzahl außerhalb des Randes | Unterer Satzspiegel und angehobene Fußzeile | Alle Textzeichen, gemessener Mindestabstand 25,85 mm |
| Quellenregisterfehler | DOI-Titel und zweite NIST-Tabelle korrigiert | `sources/registry.yml`, Bericht |
| Ersatzinvestition ohne Zuschlag | 60-%-Zuschlag auch auf Ersatz | `test_replacement_uses_engineering_multiplier` |
| Monte-Carlo-Kopplung | Jede Ziehung rechnet alle Jahresreihen | `coupled_npv_error_eur = 0.0` |
| Manifest ignoriert Umlautpfade | `git ls-files -z`, `git ls-tree -r -z` | Exakte Dateimenge |
| Wärmesenke und Notstrom offen | Fläche, NPSH, zwei Einspeisungen, 48 Stunden und Dieselvorrat | `design`, `validation` |
| Visuelle Qualität unter D4RT | Doppelte Labels entfernt, Verweise ergänzt, Anhänge umgebrochen | Marken- und Referenzprüfung |
| URLs und Zitierweise | Links umbrechbar, linksbündig, NIST-Abfrage verkürzt | PDF-Text und Sichtprüfung |
| SAR statt 1:1 | `setsar=1` und verlustfreie Einpassung | `ffprobe` verlangt SAR 1:1 und DAR 16:9 |
| Q&A ohne Commitbezug | Fragen und Befunde sind dieser Datei zugeordnet | `review/revisions.md` |
| CO2 und Luftkühlerfläche fehlen | UBA-Faktor, Face- und Servicefläche | `emissions_tco2_year`, `design.air_face_area_m2` |
| Dieseleinheit | MWh mit 1000 in kWh umgerechnet | Exakter Brennstofftest |
| Folie 7 zu voll | Kürzere Kennzahlen, Mathematiksatz für CO2, geringere Abstände | Text innerhalb der Folie |
| Fast leere Anhangsseite | Anhang A und B einspaltig und kompakt | Gerenderte Seiten, keine fast leere Seite |

## Befunde aus Runde 2, DeepSeek

| Befund | Konkrete Änderung | Verifikation |
| --- | --- | --- |
| M1, 0,1 % wird 0 % | Prozentformat mit einer Nachkommastelle | `report/generated/flow_fractions.tex`, PDF |
| M2, Komma in Gleichung 3 mehrdeutig | `9{,}1\,t` im Mathematiksatz | PDF-Seite mit der Szenariogleichung |
| M3, Nummer von Gleichung 10 auf eigener Zeile | Kondensatorbilanz zweizeilig mit `aligned` und Makros | PDF-Seite 4, Gleichung 9 |
| M4, fast leere Seite 14 | Anhang A und B gemeinsam einspaltig | Keine fast leere Seite im neuen Bericht |
| M5, Kühlleistung und Wärmeabgabe vermischt | Tabelle trennt Wärmeentzug und Abgabe an Luft | `report/generated/alternatives.tex` |
| M6, gequetschte Tabelle und lange NIST-URL | Einspaltige Anhänge, NIST-Abfrage mit Parametern im Text | PDF-Anhang und Quelle [4] |
| M7, getrennte Komposita | Sollwertrampe, Ventilrampe, Sollwertfunktion, Dieselvorrat | Texte und Folien |
| M8, Speicherlinie im Diagramm abgeschnitten | Untergrenze 0,02 MW und eigener Tick 0,03 MW | `fig06_teilstrom`, Folie 3 |
| M9, Worttrennung auf Folie 4 | Urteilsspalte 45 mm, Befund 79,5 mm, sachliche Abwägung | Folie 4 |
| M10, gespreizte Folientabelle | Beide Spalten 68 mm, linksbündig, kürzere Texte | Folie 9 |
| M11, COP 5 über Feldbereich | Referenz 4,0 als Szenario, Bereich 3,0 bis 6,5 | `data/parameters.yml`, Unsicherheitsanalyse |
| M12, Verfügbarkeit senkt Kosten | Fehlende Netzenergie mit Diesel bepreist | `economic_schedule(..., backup_shortfall=True)` und Test |
| M13, fester Posten ohne 60 % | 95 Mio. € als All-in-Schätzposten einschließlich Reserve erklärt | `cost.fixed_cost_basis`, Bericht |
| M14, „unabhängige Validierung“ | Interne Konsistenz- und Plausibilitätsprüfung genannt, externe Handrechnung und Archivreproduktion | `model/validation.py`, Reproduktionsnachweise |
| M15, 9 °C nicht gegen Siedeschutz abgewogen | `boil_guard` mit 94,9743 °C, eigene Kostenrechnung, p90-Auslegung | `boil_guard`, `design` |
| M16, Standortfeasibilität offen | Screening für Fläche, Netz, Diesel, Luft und FFH als Zulassungsbedingung | Bericht und Q&A 26, Standort weiterhin offen |
| M17, Council B modellgleich | Vorgeschriebene Modelle nicht gewechselt, Same-Model-Kontext benannt | `review/model_configuration.md` |
| M18, Hashweichung durch Zeitstempel | Deterministischer Artefakthash, Git-Blob-Abgleich und Statuskontrolle nach Prüfung | `verification_summary.py`, `freeze_revision.py` |
| M19, stale Revision und Hypothesenherkunft | Runde-2-Commit dokumentiert, `fig:unsicherheit` eingebunden, Skalierung erklärt | `review/revisions.md`, `docs/hypothesen.md` |

## Befunde aus Runde 2, Kimi

| Befund | Konkrete Änderung | Verifikation |
| --- | --- | --- |
| M1, 38,57 % Überlast bei Mittelwert | p90-Kapazität 2152,5 MW statt 1053,3 MW, Überlast separat ausgewertet | `uncertainty`, `test_design_capacity` |
| M2, H2 nicht gleichwertig | 28 °C Feuchtkugel, 4 K Annäherung, Kältestufe bis 9 °C | `alternatives[1]`, `test_evaporative_has_summer_chiller` |
| M3, Senke und Notfall nicht betriebsfähig | Standort-Screening, dynamischer Wiederanlauf, sechs Aggregate plus Reserve | `design`, `validation.recovery_peak_temperature_c` |
| M4, falscher Stromtarif | 138 €/MWh als Proxy für den nächstpassenden Bereich, 179 €/MWh als Alternative | `tariff_scenarios` |
| M5, falscher Prozentwert | 0,1 % statt 0 % | `report/generated/flow_fractions.tex` |
| M6, Folie 10 und Sprechtext überbehaupten | „angenommene Hülle“, Messungen erst vor dem Bau | `presentation/main.tex`, `narration.json` |
| M7, visuelle Restfehler | Dezimalkommas in Diagrammen, Speicherlinie sichtbar, Anhänge kompakt | Bericht und Folien im Renderbild |
| M8, menschliche Auslieferung offen | Keine Erledigung behauptet | `README.md`, `presentation/rehearsal.md`, `presentation/rights.md` |

## Befunde aus Runde 3, DeepSeek

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, Zusammenfassung nach „20“ abgeschnitten | Prozentzeichen maskiert und vollständiger Satz wiederhergestellt | `report/main.tex`, Abschnitt Zusammenfassung; `scripts/verify_report.py` verlangt den vollständigen Schlusssatz |
| M2, Fachbegriffe in der Zusammenfassung | p90, H1, Barwert und Quantil durch allgemein verständliche Erläuterungen ersetzt | PDF-Seite 2; Textprüfung auf verbotene Kurzbegriffe |
| M3, Kommas in WebVTT-Zeitstempeln | Punkte als Millisekundentrenner gesetzt | 62 von FFmpeg ausgegebene Cues gegen Eingabe-Cues geprüft |
| M4, 38,57 % ohne passende Kapazitätslinie | Mittelstrom, Mittelstrom mit 20 % und p90 mit 20 % als drei beschriftete Linien dargestellt | `model/run_all.py`, `report/figures/fig05_unsicherheit.pdf`, `uncertainty.mean_capacity_overload_fraction` |
| M5, leere rechte Schluss-Spalte | Literaturbeginn ohne erzwungenen Seitenumbruch, Anhang ohne isolierte Abbildungsseite | `report/main.tex`, `report/preamble.tex`, 11 statt 13 Seiten, Literatur und Anhang zusammen 4 Seiten |
| M6, URL-Bruch nach „https:“ | Vollständige Hyperlinkziele mit kurzen Hostnamen als Anzeige | Literaturverzeichnis auf PDF-Seiten 8 und 9, `sources/registry.yml` |
| M7, Dezimalpunkte in Unsicherheitsdiagramm | Deutsche Dezimalkommas durch Achsenformatierer | `model/run_all.py`, `report/figures/fig05_unsicherheit.pdf` |
| M8, gespreizte und getrennte Überschriften | Überschriften linksbündig, Codeblock im Anhang linksbündig | `report/preamble.tex`, `report/main.tex`, gerenderte Seiten |
| M9, Folie 8 zeigt deterministische statt Monte-Carlo-Abbildung | Unsicherheitsdiagramm mit drei Kapazitätslinien auf Folie 8 eingebunden | `presentation/main.tex`, `review/rendered/presentation_pages/slide-08.png`, Sprechtext |
| M10, Testkennung statt offizieller Team-ID | Keine offizielle ID erfunden. Die Testkennung bleibt ausdrücklich nur für dieses nicht eingereichte Paket. | `compliance/checklist.md`, `PROVENANCE.md`; menschliche Restaufgabe bleibt offen |
| M11, Prüfskripte übersehen Textverlust und ungültige VTT | Schlusssatz, Alltagssprache, WebVTT-Cues und Kapazitätslinien automatisiert geprüft | `scripts/verify_report.py`, `scripts/verify_presentation.py`, `make verify` |
| M12, „unabhängige Handrechnungen“ ohne Beleg | Auf dokumentierte Handrechnung präzisiert und ausgeschriebene Rechnung in Anhang B aufgenommen | `report/main.tex`, Abschnitt 5 und Anhang B, Gleichung ohne Nummer |

## Befunde aus Runde 3, Kimi

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, beschädigte Zusammenfassung | Mit DeepSeek M1 und M2 behoben | Vollständiger PDF-Text und Renderbild der Seite 2 |
| M2, dynamischer Test nur für Mittelstrom | `simulate_failure` für Mittelstrom und p90 getrennt, mit 0,5 min Detektion, 5 min Start und 10 min bis voller Kühlung | `validation.failure_mean`, `failure_p90`; 12,6448 °C und 16,2045 °C; 23,3393 und 11,4214 min bis 20 °C |
| M2, fehlende Konvergenzprobe | p90 mit 30 und 5 Sekunden bei `rtol/atol=1e-9` gegen `1e-11` gerechnet | `failure_p90_convergence_error_k = 7,398218180298954e-07`; Modelltest |
| M3, Kapazitätsgrafik zeigt nicht die installierte Endleistung | Drei Linien für 877,8 MW, 1053,3 MW und 2152,5 MW mit ausgewiesener p90-Skalierung | `model/run_all.py`, Unsicherheitsdiagramm im Bericht und auf Folie 8 |
| M4, freie Flächen und kleine Beschriftungen im D4RT-Vergleich | Redundante Stufengrafik entfernt, Literatur direkt angeschlossen, Überschriften, Tabellen und Diagrammbeschriftungen bereinigt | 11 Berichtsseiten, `review/rendered/report_pages/`, D4RT-Seiten 1, 2 und 6 |
| M4, temperaturabhängige Stoffwerte für die Detailauslegung | Nicht als fertige Detailauslegung ausgegeben. Konstante NIST-Werte bleiben eine benannte Näherung, IAPWS ist für die spätere Auslegung gefordert. | `report/main.tex`, Methodik und Modellgrenzen; `sources/registry.yml` [4,5]. Die Feldauslegung bleibt offen. |
| M5, Karst, Standort, Netz, COP und Extremwertverteilung nicht nachgewiesen | Diese reale Machbarkeit kann ohne Messungen und Angebote nicht bestätigt werden. Das Paket beschränkt sein Ergebnis auf einen falsifizierbaren Szenarioentwurf und macht die Nachweise zu Zulassungsbedingungen. | Bericht Abschnitte 4.3 und 5, `docs/alternativenvergleich.md`, `boil_guard`, Hochwasser-Stresstest. Keine unbegründete Dauerzusage. |
| M6, VTT-Satzzeiten und menschliche Restaufgaben | WebVTT technisch repariert und echte MP4-Wiedergabe erneut gemessen. Wortproportionale Satzzeiten bleiben offengelegt. Menschliche Hörprobe, Team-ID, Rechtefreigabe, Finalisten-E-Mail und Live-Probe werden nicht als erfolgt behauptet. | `output/presentation/playback.json`, `presentation/rehearsal.md`, `presentation/rights.md`, `PROVENANCE.md` |

## Offene physikalische und menschliche Grenzen

- Betroffener Stromanteil, Karsterfassung und Verhalten oberhalb 4,7 m³/s sind nicht feldkalibriert.
- COP, Teillast, Feuchtkugel, Wärmeübertragung, Luftführung, Schall und Plume benötigen Hersteller- oder Standortdaten.
- Netzanschluss, Flächeneigentum, Diesellogistik, Genehmigung und gemeinsame Ausfallursachen sind offen.
- Der Wiederanlauf ist ein Rechenszenario, keine durchgeführte Zuschaltprobe.
- Offizielle Team-ID, menschliche Fachprüfung, Medienfreigabe, Finalisten-E-Mail und echte Live-Probe fehlen.

Runde 2 wurde mit Commit `cc25cc903681ebbc4d6865309236885f729d6d77` bewertet und nicht bestanden. Der Runde-3-Kandidat `babe04c` wurde in einer frischen Archivkopie reproduziert. `review/rounds/round3/reproduction.md` dokumentiert ausdrücklich diesen Kandidaten, nicht den späteren Dokumentationscommit. Runde 3 wurde anschließend mit Commit `77c1f972df9c67a00354e395ce31f27fd0c1b95c` bewertet und nicht bestanden. Für Runde 4 ist eine neue Archivreproduktion des exakten Kandidaten-Commits erforderlich. Erst danach werden Revision und Council-Auftrag eingefroren. Diese Zuordnung behauptet keine neue Punktzahl.
