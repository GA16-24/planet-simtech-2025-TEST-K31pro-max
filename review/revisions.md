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
| 10, Stromausfall | `validation.failure_mean`, `failure_p90` | Detektion 0,5 min, Start 5,5 min und volle Kühlung 10,5 min nach Ausfall; keine reale Zuschaltprobe |
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
| 24, Wiederanlauf | `validation.failure_mean`, `failure_p90`, `failure_p90_convergence_error_k` | Höchstwerte 12,88 °C und 16,66 °C; Margin 0,921 min im p90-Fall; kein Feldversuch |
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

## Befunde aus Runde 4, DeepSeek

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, Seitenzahl im Text und im Spaltengraben | Unterer Rand auf 34 mm, `footskip=7mm`, normale Fußzeile ohne `raisebox` | `report/preamble.tex`; Kollisionsprüfung für jede Seitenzahl in `scripts/verify_report.py` |
| M2, uneinheitliche KI-Offenlegung | Regel- und Physikrecherche von Kimi, Technik- und Wirtschaftsrecherche von DeepSeek sowie getrennte Reviewrollen einheitlich benannt | `report/main.tex` Anhang A, `presentation/main.tex` Folie 10, `PROVENANCE.md` |
| M3, Strangleistung mehrdeutig | Zwölf Stränge à 179,4 MW installiert; im p90-Fall elf Stränge à 163,1 MW bei etwa 91 % Last | `baseline.per_module_installed_mw`, `per_module_required_mw`; Bericht, Folie 5 und Q9 |
| M4, Detektionszeit nicht im Ausfallmodell | Absolute Start- und Vollastzeitpunkte 5,5 und 10,5 min; Integration an beiden Schaltpunkten neu gestartet | `simulate_failure`; Mittelstrom 12,88 °C, p90 16,66 °C, Margin 0,921 min; analytischer Test und Konvergenzfehler 1,79e-12 K |
| M5, statische Druckhöhe als NPSH bezeichnet | Auf statische Druckhöhe über Atmosphäre präzisiert; Dampfdruck und Saugverluste bleiben offen | `baseline.static_overpressure_head_m`, Bericht §3.1 |
| M6, kleine Diagramme auf Folien 3, 7 und 8 | Eigene Projektgrafiken mit größeren Schriften und direkten Linienlabels statt verkleinerter Berichtsgrafiken | `presentation/figures/`, Folien 3, 7, 8 und tatsächliche MP4-Frames |
| M7, MW statt MW/K auf Folie 2 | Einheit auf MW/K korrigiert | `presentation/main.tex`, `scripts/verify_presentation.py` |
| M8, nur Hostnamen im Quellendruck | Auflösbare DOI- und URL-Pfade mit umbrechbarem `\nolinkurl` gedruckt; vollständige Hyperlinks bleiben erhalten | Literaturverzeichnis, `sources/registry.yml` |
| M9, D4RT ohne Jahr und Venue | Jahr 2025 und Preprint-Status aus der referenzierten Version ergänzt, keine Venue erfunden | Quelle [22], PDF-Metadaten vom 10.12.2025, `sources/registry.yml` |
| M10, Arial als Systemschrift | `newtxtext` und `newtxmath` statt macOS-Arial | `presentation/main.tex`; Folienbuild ohne absolute Schriftpfade |
| M11, 655,8 statt 655,9 MW | Beide Dokumente auf den generierten Modellwert 655,9 MW vereinheitlicht | `docs/alternativenvergleich.md`, Q22, `EvapDry` |
| M12, Manifest unvollständig | Eingaben, Programme, CSV- und NPZ-Ergebnisse, LaTeX-Tabellen und alle Figuren gehasht | `output/model/manifest.json`, `scripts/verify_repository.py` |
| M13, absolute lokale Pfade | Wiedergabebefehl mit Repository-Arbeitsverzeichnis und relativem Videopfad | `scripts/record_playback.py`, `output/presentation/playback.json` |
| M14, Jahresendleistung für alle Jahresstunden | Die konservative Diskretisierung wird ausdrücklich erklärt statt als Stundenmodell ausgegeben; Jahr 0 und Netzanschlussgrenze präzisiert | `plant.operation_year_convention`, Bericht §3.3 |
| M15, 9 °C als historisch überzeichnet | „Angenommener Normalzustand“ statt „historischer Zustand“ | Bericht §1 |
| M16, Worttrennungen und überflüssige Grafikflächen | Breitere Eingabespalten, direkte Linienlabels und keine isolierte Wiederholungstabelle am Ende | `report/main.tex`; Alternativen H4 bis H7 bleiben im Haupttext und in `docs/alternativenvergleich.md` |
| M17, alte Videodauer im Entscheidungsprotokoll | Der Eintrag ist als historischer Build gekennzeichnet; aktuelle Dauer steht im neuen Zeitprotokoll | `decisions.tsv`, `presentation/rehearsal.md` |
| M18, Margenschwelle und unentdeckte Diagrammschrift | Exakt 25 mm in Punkt, Fußzeilenkollisionen und effektive Glyphengröße in beiden Ausrichtungen geprüft | `scripts/verify_report.py` |

## Befunde aus Runde 4, Kimi

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, Diagrammschrift unter 12 pt und zu klein im Video | Berichtsgrafiken neu skaliert, Achsen- und Legendentexte mindestens 12 pt nach PDF-Skalierung; Projektgrafiken mit direkten Labels | `scripts/verify_report.py` misst die größere Glyphendimension, Seiten 5, 7 und 12; Folien und Videoframes |
| M2, zweite NIST-Abfrage fehlt | Vollständige Drucktabellen-URL bei 3,17007 bar in Quellenregister und Eingabedatei verknüpft | `sources/registry.yml` Eintrag 4, `hydrology.pressure_table_url` |
| M3, menschliche und technische Finalrestaufgaben | Video mit 290,232 s und Echtzeitprobe mit 289,67 s neu erzeugt. Eine frische Archivkopie erzeugte Modell, Bericht, Sprache und Video erneut; 41 Artefakte und 33 Renderbilder sind byteweise identisch. Menschliche Hörprobe, manuelle VTT-Freigabe, Rechte und echte Teamprobe werden nicht erfunden. | `review/rounds/round5/reproduction.md`, `presentation/rehearsal.md`, `presentation/rights.md`, `make verify`; menschliche Restaufgaben bleiben ausdrücklich offen |

## Befunde aus Runde 5, DeepSeek

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, doppelte Kapazitätsskalierung in `coupled_npv` | Die Unsicherheit verwendet eine feste p90-Anlage mit 20 % Reserve. Abfluss und COP verändern nur den Betrieb, der explizite Faktor nur die Investition. Eine erneute Kapazitätsskalierung entfällt. | `model/run_all.py`, `uncertainty.capacity_policy`, `test_coupled_npv_at_design_point`; Referenzfehler am Mittelstrom- und p90-Punkt jeweils null |
| M2, voller Notstromposten beim kleinen Siedeschutz | Notstrom und Kraftstoff werden mit der elektrischen Leistung der Variante relativ zur p90-Referenzanlage skaliert. Die Referenz bleibt über die Ausbaustufen konstant. | `model/core.py`, `test_guard_backup_scales_with_electricity`, `boil_guard.backup_power_eur`; 0,370 statt rund 60 Mio. € |
| M3, fast leere Seite und geteilte Literaturangaben | Anhang A/B nutzt die freie zweite Spalte. Literaturabsätze dürfen nicht mehr über Spalten oder Seiten brechen. | `report/main.tex`, PDF-Seiten 9 bis 11, `review/rendered/report_pages/` |
| M4, gequetschte Tabelle und Satzfehler | Annahmentabelle über beide Spalten, geschützte Einheitenabstände, Dezimalkommas ohne Mathematikzwischenraum, `\texttt` statt Backticks, URL-Brüche nur an Trennstellen | PDF-Seiten 2 bis 5 und 8 bis 11; `macro()` in `model/run_all.py` |
| M5, Unsicherheitsfigur unter falschem Anhang | Abbildung 3 steht unmittelbar unter Anhang C statt vor dessen Überschrift | PDF-Seite 12 |
| M6, Foliengrafik überlappt Achsenmarke | Die Präsentation ist nach Nutzerkorrektur kein Produkt mehr. Der Befund wird nicht als Paperfehler übernommen. Eine unabhängig sichtbar gewordene Kollision zweier Ticklabels im Bericht wurde dagegen durch Entfernen des redundanten 0,1-Ticks behoben. | `model/run_all.py`, `report/figures/fig01_prognose_last.pdf`, PDF-Seite 5 |
| M7, Verdampfungsenthalpie für 20 °C statt Prozessbereich | Arithmetisches Mittel der NIST-Sättigungswerte bei 32 und 100 °C, 2340,730 kJ/kg, mit ausdrücklicher Grenze statt vollständiger Temperaturintegration | `data/nist_saturation_32_100.tsv`, `data/parameters.yml`, Bericht §3.3, Wasserbedarf 8,84 Mio. m³ und 12,2 % |
| M8, kleinere Text- und Belegmängel | Speichergröße als untere Grenze statt Kühlbedarf, korrekte Überlastungsrichtung, HQ 1951 bis 2007 ohne genanntes Wiederkehrintervall, `u_T=0` und Sensitivitätsformel, 19 statt elf Tests | Bericht §§2.1, 3.1, 4.4 und 5; `sources/registry.yml` |
| M8, veraltete Finalhinweise und Cuezahl | Diese Punkte betreffen ausschließlich das zurückgezogene Finalprodukt. Sie werden nicht weiterentwickelt und nicht als abgeschlossen ausgegeben. | Nutzerkorrektur zum Lieferumfang, `README.md` |
| Selbstberichtete Archivreproduktion | Für den Paperkandidaten wird eine neue Archivkopie erzeugt und mit den tatsächlichen Artefakten verglichen. Kein früherer Reproduktionsnachweis wird auf die neue Revision übertragen. | `review/rounds/round6/reproduction.md`, sobald geprüft |

## Befunde aus Runde 5, Kimi

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, reale Machbarkeit der Referenzlösung | Keine Standortwahl, Netzzusage, Herstellerkurve oder vollständige Karsterfassung wird erfunden. Der Paper bleibt ein bedingter Szenarioentwurf mit harten Zulassungs- und Verwerfungsbedingungen. Diese externe Grenze ist nicht geschlossen und muss im Council ausdrücklich bewertet werden. | Bericht §§1, 4.3, 5 und 6; offene Restrisiken bleiben bestehen |
| M2, fehlende menschliche Medien- und Teamprobe | Das Finalprodukt und Kriterium 12b wurden durch den Nutzer aus dem Lieferumfang entfernt. Es wird keine menschliche Probe oder Freigabe behauptet. | `README.md`, `review/README.md` |
| Jahresreihen in Juryfrage 6 | Die Jurydatei gehört nicht mehr zum Lieferumfang. Der Paper verweist für die Sensitivität auf die tatsächlich vorhandenen Tabellen und Modellreihen. | `report/generated/sensitivity.tex`, `output/model/sensitivity.csv` |

## Befunde aus Runde 6, DeepSeek

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, Notstromskalierung in Teilstromfällen | Designstrom wird aus p90-Verhältnis und tatsächlichem betroffenem Anteil gebildet. Referenzanlage und Kraftstoff verwenden dieselbe Kühltechnologie wie die Variante. | `model/core.py`, `test_partial_flow_backup_and_capex`, `test_evaporative_backup_uses_evaporative_reference`; Tabelle 4 mit 141, 17 und 3 Mio. € statt 233, 118 und 104 Mio. € |
| M2, Achsenlabel „Tiefe in °C“ | Label auf „Szenariotemperatur in °C“ korrigiert und semantische Prüfung ergänzt | `model/run_all.py`, `scripts/verify_report.py`, PDF-Seite 5 |
| M3, H3 ohne Notstrom | H3 wird ausdrücklich als reine Pumpen- und Wasserkostenschätzung ohne Notstromposten beschrieben, statt identische Kostenregeln zu behaupten | Bericht §3.3 und Tabelle 2, `docs/alternativenvergleich.md` |
| M4, Manifestumfang | Text präzisiert Hashes für Modell-Eingaben, Programme und Modellergebnisse. PDF-Hash und Renderbilder bleiben ausdrücklich im Reproduktionsnachweis. | Bericht Anhang A, `review/rounds/round8/reproduction.md` nach erneutem Lauf |
| M5, „Wärmeabfuhr“ in der Zusammenfassung | 877,8 MW als Kühlleistung bezeichnet und 967,2 MW externe Wärmeabgabe getrennt genannt | PDF-Seite 2 |
| M7, URL-Bruch in Quelle [19] | Numerischer Pfadteil 20.500.12738 als untrennbare Box gesetzt, vollständiger Hyperlink erhalten | PDF-Seite 11, Quelle [19] |
| M9, Statement bei mehr Bearbeitungszeit | Konkrete Prioritäten für Karst- und Standortmessungen, Teillast- und Pinch-Auslegung sowie Angebote ergänzt; automatische Textprüfung ergänzt | Bericht §6, `scripts/verify_report.py` |
| Optionale Hinweise | Die obere ODE-Schranke bleibt korrekt. Das Deckblatt wird im eigenen Design-Council geprüft. Der kollidierende 0,1-Tick bleibt entfernt, weil Lesbarkeit der Kurve wichtiger ist als ein zusätzlicher Zahlenwert. | PDF-Seiten 1 und 5 |

## Befunde aus Runde 6, Kimi

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, 26 statt 25 Betriebsjahre | Jahr 0 enthält nur Investitionen. Betrieb, Wartung und Ersatzstrom beginnen erst in den 25 Betriebsjahren 1 bis 25. Gekoppelte und direkte Kostenrechnung bleiben konsistent. | `model/core.py`, `model/run_all.py`, `test_operating_year_count`; H1-Barwert 3,663 statt 3,666 Mrd. € |
| M2, fehlende Monte-Carlo-Annahmen | Dreiecksverteilungen für Abfluss und COP, lognormaler Investitionsfaktor mit Parametern, Seed und Unabhängigkeit der Ziehungen im Paper dokumentiert; keine empirische Kalibrierung behauptet | Bericht §4.4, generierte Makros aus `data/parameters.yml` |
| M3, falsche Achsenbezeichnung | Mit DeepSeek M2 behoben und durch den PDF-Test abgesichert | PDF-Seite 5 |
| H2-Topologie | Separater Sekundärkreislauf ausdrücklich beschrieben. Der Quellstrom bleibt geschlossen und wird vollständig weitergekühlt, der Dampfstrom gehört nicht zum Quellabfluss. | Bericht §3.3, `docs/alternativenvergleich.md` |
| Kosten- und Auslegungsgrenzen | Der ungenutzte Kondensatorparameter wurde entfernt. Teillast- und Pinch-Auslegung bleiben ausdrücklich zukünftige Herstellerarbeit. Der lognormale Investitionsfaktor bleibt die dokumentierte Kostensensitivität. | `data/parameters.yml`, Bericht §4.4 und §6 |

Die neue Revision enthält 19 bestandene Modelltests und 13 Seiten. Frühere Punktzahlen werden nicht übernommen. Vor Runde 8 sind Modell, PDF, alle Seitenbilder und die Archivreproduktion erneut zu prüfen.

## Befunde aus Runde 7, DeepSeek

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| A1, „Anhang C“ ohne „Anhang B“ | Ergänzende Ergebnisse und beide Textverweise heißen jetzt Anhang B | `report/main.tex`, PDF-Seiten 9 und 13 |
| A2, Tabelle mitten im Absatz | Annahmentabelle steht nach dem abgeschlossenen Hypothesenabsatz statt mitten in „Wärmeentnahme“ | `report/main.tex`, PDF-Seiten 2 bis 4 |
| A3, gespreizte Appendixtypografie | Anhang A steht rechtsbündig statt mit erzwungenen Wortabständen | `report/main.tex`, PDF-Seiten 11 und 12 |
| A4, Zitationsdetails | Quelle [6] mit Untertitel, [5] mit 2007, [7] mit 2011 und [8] mit 2016 | `report/main.tex`, PDF-Seiten 9 bis 11 |
| B1, H2-Wärmeübertrager-Pinch | Sekundärkreislauf 32 °C, Quellstrom 36 °C. Die 4 K sind damit ein physikalisch möglicher Pinch statt eines widersprüchlichen gemeinsamen Austritts. | `plant.evaporative_source_outlet_c`, `test_evaporative_pinch`, H2 617,3/260,4 MW |
| B2, lokaler Siedepunkt | Die Schutzmarke wird ausdrücklich als Standarddruckszenario geführt. Höhenabhängiger Druck ist vor Ort zu messen, keine Standortgarantie. | Bericht §4.4 |
| B3, Kostenbasis 2012 | Pauschaler Szenarioaufschlag von 30 % auf Kälte-, Trockenkühl- und Verdunstungskosten, ohne amtlichen Index oder Angebot zu behaupten | `cost.legacy_escalation_factor`, Bericht §2.2, alle Kosten neu berechnet |
| B4, Beckenvolumen und Mischung | Sensitivität für 10.000, 25.000 und 50.000 m³. Der kleine Fall zeigt 26,4 °C und -5,93 min, der große 12,34 min. | `volume_sensitivity`, `test_volume_sensitivity`, Bericht §4.2 |
| B5, Dieselvorrat gegen 95-%-Fall | Kostensensitivität mit unbegrenzter Dieselverfügbarkeit ausdrücklich von der 48-Stunden-Lagerplanung getrennt | Bericht §4.4, `availability_scenarios` |
| Archiv und externe Grenzen | Keine externe Validierung erfunden. Archivreproduktion und Same-Model-Review bleiben als Grenzen sichtbar. | `review/rounds/round8/reproduction.md`, `review/model_configuration.md` |

## Befunde aus Runde 7, Kimi

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, fehlende elektrische Auslegung am minimalen COP | Einheitliche Min-COP-Auslegung für Netz, Aggregate, Diesel und Luftsenke. Der Randfall umfasst 234,336 MW elektrische Leistung und 2028,062 MW Wärmeabgabe. Sieben Aggregate mit 35 MW plus Reserve, 2,869 Mio. Liter Diesel und 8,41 ha Servicefläche. | `design_electrical_stage`, `test_electrical_design_at_minimum_cop`, Bericht §§3.2, 4.2 und 4.4 |
| Monte-Carlo nur thermisch | Elektrische Leistung und Wärmeabgabe aller 10.000 Ziehungen werden separat gegen die Min-COP-Grenzen geprüft und in NPZ gespeichert. Beide Überlastanteile sind 0,00 %. | `uncertainty.electricity_overload_fraction`, `air_rejection_overload_fraction`, Stichprobenmaxima 211,546 und 1982,279 MW |
| Team und Freigabe | Keine offizielle Team-ID, menschliche Prüfung oder Einreichung erfunden. Diese Restaufgaben bleiben ausdrücklich offen. | `README.md`, `PROVENANCE.md`, Anhang A |
| Hydrostatischer Nebenbefund | Druck aus Dichte, Gravitation und Tiefe auf 3,17080686 bar gesetzt; NIST-Abfrage und Sättigungspunkt 135,421 °C exakt verknüpft | `data/parameters.yml`, `sources/registry.yml`, Bericht §3.1 und Quelle [4] |

Die neue Revision enthält 19 bestandene Modelltests und 13 Seiten. Frühere Punktzahlen werden nicht übernommen. Vor Runde 8 sind Modell, PDF, alle Seitenbilder und die Archivreproduktion erneut zu prüfen.

## Befunde aus Runde 8, DeepSeek

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, 9-°C-Legende kollidiert und ist falsch zugeordnet | Direkte Beschriftung neben der 9-°C-Linie statt entfernter Legende | `model/run_all.py`, `report/figures/fig01_prognose_last.pdf`, PDF-Seite 5 |
| M2, Appendixtext und kleine Handrechnung | Absatzabstand und Einzug festgelegt, Handrechnung als mehrzeilige Displayformel gesetzt | `report/main.tex`, Anhang A, PDF-Seite 12 |
| M3 und M4, Anhangsumbruch und schwach genutzte Fläche | Anhang A beginnt nicht mehr als isolierte Überschrift. Anhang B nutzt eine seitenbreite Abbildung und zwei seitenbreite Tabellen. Ein weiterer erzwungener Umbruch vor Anhang B wurde verworfen, weil er die Floats auf eine fast leere Folgeseite verschob. | `report/main.tex`, `scripts/verify_report.py`, PDF-Seiten 11 bis 13 |
| M5, unbeschriftete Referenzlinie und uneinheitliche Präzision | Kostenreferenz direkt erklärt, erweiterte Kapazitätsachse und drei Nachkommastellen in beiden Tabellen | `model/run_all.py`, `report/generated/sensitivity.tex`, `report/generated/flow_fractions.tex`, PDF-Seite 13 |
| M6, H2-Temperaturbeschreibung | Mit Kimis thermodynamischem Befund als Gegenstrommodell neu gefasst | `plant.evaporative_secondary_*`, `test_evaporative_pinch`, Bericht §3.3 |
| M7, Ausfallsequenz | 0,5 min Detektion, 5 min Generatorstart und weitere 5 min bis voller Kühlung; 10,5 min absolut und 4,5 min USV-Reserve | `data/parameters.yml`, `model/validation.py`, Bericht §4.2 |
| M8 und M9, Diesel- und Siedeschutzvergleich | Erwartungslast 89,4 MW im 95-%-Kostenfall und 234,336 MW für den 48-Stunden-Vorrat getrennt; Siedeschutz bei 2,3 m³/s und H1 bei 4,7 m³/s ausdrücklich nicht gleichgesetzt | Bericht §4.4, `availability_scenarios`, `boil_guard` |
| M10 und M11, unklare Alternativen und fehlendes Zitat | H4 bis H7 mit Namen im Paper genannt; 165 km² mit [2,3] belegt | Bericht §§1, 2.1 und 3.3 |
| M12, Fachbegriffe in der Zusammenfassung | Gerätestränge durch Kühlmodule ersetzt und die Temperaturrampe in Alltagssprache erklärt | PDF-Seite 2, `scripts/verify_report.py` |
| M13, unzureichender Leerseitentest | Jede Seite braucht mindestens 200 Textzeichen und 200 pt vertikale Textausdehnung; alle Seiten erneut gerendert und gesichtet | `scripts/verify_report.py`, `make verify`, `review/rendered/` |
| M14, fehlende Investitionsaufteilung | Wärmetauscher, Kältemaschinen, Trockenkühler, Ersatzstrom, Engineeringzuschlag und separate Festposten einzeln ausgewiesen | Bericht §3.3, generierte Kostenmakros |
| M15, optionale Satzverbesserung | Keine ungeprüfte globale Satzänderung. Die Zusammenfassung bleibt Gegenstand des separaten Design-Councils. | gerenderte PDF-Seite 2 |
| Reale Umsetzbarkeit und externe Reproduktion | Keine Standort-, Netz- oder Herstellerzusage erfunden. Die Archivprüfung gilt nur in der dokumentierten Referenzumgebung. | Bericht §§4.3, 5 und 6; neuer Archivnachweis für Runde 9 |

## Befunde aus Runde 8, Kimi

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, H2-Pinch am heißen Ende 0 K | Gegenstrom mit Quellstrom 100 bis 36 °C und Sekundärkreislauf 32 bis 96 °C. Beide Endabstände betragen 4 K. Der Sekundärstrom von 2,3 m³/s hat denselben Wärmekapazitätsstrom. | `plant.evaporative_secondary_*`, `test_evaporative_pinch` prüft beide Pinchstellen und die Energiebilanz; H2 617,3/260,4 MW und 8,32 Mio. m³/Jahr |
| M2, Kostenherkunft und Druckregister | HAW Tabelle 5.6 nennt für Kompressionskältemaschinen 75 bis 125, 125 bis 350 sowie 185 bis 236 €/kW, getrennt vom bewusst höheren Modellwert 500 €/kW. Trockenkühlung und Verdunstung sind eigene Szenariowerte. Hydrostatischer Druck auf 3,17080686 bar korrigiert. | `data/parameters.yml`, `sources/registry.yml`, Bericht §§2.2 und 3.1; HAW Tabelle 5.6 direkt geprüft |
| M3, Anhangslayout | Mit DeepSeek M2 bis M4 überarbeitet und anhand der gerenderten Seiten geprüft | PDF-Seiten 11 bis 13, `review/rendered/report_contact.png` |
| M4, 9-°C-Label | Mit DeepSeek M1 direkt an der Ziellinie beschriftet | PDF-Seite 5 |
| M5, menschliche Abgabevoraussetzungen | Keine offizielle Team-ID, Rechtefreigabe, menschliche Prüfung oder Einreichung behauptet. Diese Schritte bleiben offen. | `README.md`, `PROVENANCE.md`, Anhang A |

Die neue Revision enthält 19 bestandene Modelltests und 13 Seiten mit 8 Haupttext- und 4 Literatur-/Anhangsseiten. Frühere Punktzahlen werden nicht übernommen. Vor Runde 9 sind Modell, PDF, alle Seitenbilder und die Archivreproduktion erneut zu prüfen.

## Befunde aus Runde 9, DeepSeek

DeepSeek fand keinen materiellen Mangel. Die folgenden optionalen Hinweise wurden bei der nächsten Revision geprüft.

| Hinweis | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| NIST-URL im PDF | Die konkreten Abfragen stehen im Literaturtext und die vollständigen URLs im Quellenregister und den Modelleingaben. Keine neue externe Kurz-URL wird erfunden. | Quelle [4], `sources/registry.yml`, `data/parameters.yml` |
| Seitenzählung | Die Schlussfolgerung auf der ersten Literaturseite wird zum Haupttext gezählt, statt die ganze Seite auszunehmen. | `scripts/verification_summary.py`, `scripts/verify_report.py` |
| Ventilator und Pumpe | 1,5 % auf Trockenkühlung plus Kondensatorwärme sowie 12 m Förderhöhe und 80 % Wirkungsgrad sind im Paper genannt. | Bericht §3.2, `PFans`, `PPumps` |
| Tabelle 2 und H2-Wasser | Mittelbetrieb und p90-Auslegung sind getrennt. Die 8,32 Mio. m³ sind nur Verdunstung ohne Abschlämmung und Spülwasser. | Bericht §3.3 und Tabelle 2, Zusammenfassung |
| H1-Weiterentwicklung | Tiefenkreislauf mit Diffusor und Vollstromkühlung vor dem Becken werden als technische Weiterentwicklung statt bloßer Skalierung beschrieben. | Bericht §2.1, `docs/hypothesen.md` |
| Abbildung 1 | Szenariokurve, Abflussanteile und Stoffwerte werden getrennt zugeordnet. | Bericht, Abbildung 1 |
| Stufenplan | Die vorhandene Jahresreihe bleibt die Quelle der Ausbaustufen. Keine zusätzliche Tabelle ohne neuen Erkenntnisgewinn wird verlangt. | `output/model/hybrid_schedule.csv`, Bericht §3.3 |

## Befunde aus Runde 9, Kimi

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, wärmegetriebene Kühlung fehlt | H8 als einstufige Absorptionsvariante registriert. Heißwasser 96/82 °C, Quellstrom 100/86 °C, positive Pinchstellen von 4 K, Generator 135,0 MW, Verdampfer 94,5 MW, Absorptionsabwärme 229,6 MW. | `absorption_stage`, `test_absorption_stage_energy_and_pinch`, Bericht §3.3 |
| Elektrische und thermodynamische Prüfung | Hilfsstrom 5,56 % nach HAW 3/54 kW. H8 benötigt 94,6 MW im Mittelbetrieb und 245,1 MW im Min-COP-Fall, acht Aggregate plus Reserve und 3,001 Mio. Liter Diesel. Thermische COP-Werte 0,6 bis 1,3 und reversible Obergrenze 1,793 lassen den Quellstrom über 40 °C, die Kompressionsstufe bleibt unverändert. | `test_absorption_design_and_cost`, `test_absorption_temperature_limit_and_uncertainty`, Tabelle H8 |
| Kosten, Emissionen und Unsicherheit | Eigener Screeningwert 250 €/kW innerhalb der HAW-Spanne 80 bis 1800 €/kW plus 30 %, ansonsten dieselben Reserve- und Zuschlagsregeln. H8 kostet 1716,0 Mio. € Investition und 4,346 Mrd. € Barwert, verursacht 300,9 kt CO₂ pro Jahr und ist in allen 10.000 gekoppelten Ziehungen teurer als H1. | `variable_capex_eur`, `coupled_npv(..., technology="absorption")`, `output/model/results.json` |
| M2, reale Abgabe fehlt | Keine offizielle Team-ID, menschliche Freigabe, Rechteprüfung oder Einreichung wird erfunden. Kriterium 12a bezeichnet im nächsten Auftrag ausdrücklich die technische Testpaketbereitschaft; reale Abgabevoraussetzungen bleiben sichtbar. | `README.md`, `PROVENANCE.md`, Anhang A, `review/council_prompt.md` |

Die neue Revision enthält 22 bestandene Modelltests und 15 Seiten mit 10 Haupttext- und 5 Literatur-/Anhangsseiten. Die Spalten in Anhang A werden mit `\balance` ausgeglichen. Frühere Punktzahlen werden nicht übernommen. Vor Runde 10 ist die Archivreproduktion erneut zu prüfen.

DeepSeek legte in Runde 9 offen, versehentlich `review/README.md` mit früheren Übersichtspunktzahlen gelesen zu haben. Die Werte wurden nach dem Bericht nicht verwendet. Der nächste Prüfauftrag schließt diese Datei ausdrücklich aus.

## Befunde aus Runde 10, DeepSeek

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, schwach genutzte Anhangsseiten | Einspaltige Abbildung und Tabellen in Lesereihenfolge statt seitenbreiter Floats. Anhang B und alle vier Tabellen stehen auf Seite 14 mit Inhalt in beiden Spalten. Die Abbildung wurde für die Spaltenbreite neu gesetzt und ihre Beschriftung nach Sichtprüfung korrigiert. | `report/main.tex`, `model/run_all.py`, PDF-Seiten 13 und 14, mindestens 12,16 pt Diagrammglyphen |
| M2, falsches Seitenflag | Text vor der Überschrift Literaturverzeichnis entscheidet über die gemeinsame Seite. Das Flag ist jetzt true. Die zehn Haupttextseiten schließen das Deckblatt weiterhin aus. | `scripts/verification_summary.py`, `output/verification_summary.json` |
| M3, H2-Wasserbilanz unvollständig | Drei Konzentrationszyklen mit 4,16 Mio. m³ Abschlämmung und 0,02 % Drift ergänzen 8,32 Mio. m³ Verdunstung auf 12,48 Mio. m³ Zusatzwasser. Drei bis fünf Zyklen ergeben 10,40 bis 12,48 Mio. m³. Wasserkosten und Barwert 3,722 Mrd. € verwenden den vollständigen Bedarf. | `annual_operation`, `test_evaporative_makeup_water`, `evaporative_makeup_sensitivity`, Bericht §3.3 und Tabelle 2 |
| M4, Annahmen zu Hilfsantrieben und Servicefläche | Ventilatoranteil, 12 m Förderhöhe, 80 % Wirkungsgrad und Serviceflächenfaktor 1,5 werden ausdrücklich als eigene Annahmen ohne Herstellerkurven genannt. | Bericht §3.2, `data/parameters.yml` |
| M5, reversible H8-Grenze ohne feste Generatorwärme | Die 135,0 MW Generatorwärme und 96/82 °C stehen unmittelbar bei der reversiblen Obergrenze. | Bericht §3.3, `absorption_reversible_cop` |
| M6, historische Präsentation im Freeze-Nachweis | Der Freeze enthält separate Paperbefehle und kennzeichnet die historischen Präsentationsprüfungen als außerhalb des Lieferumfangs. | `scripts/freeze_revision.py`, `review/rounds/round11/reproduction.md` nach dem Lauf |

## Befund aus Runde 10, Kimi

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, 250 €/kW fälschlich als HAW-Unterwert | HAW Tabelle 5.6 wird mit dem vollständigen Spektrum 80 bis 1800 €/kW beschrieben. Der Wert 250 €/kW ist eine eigene günstige Szenarioannahme innerhalb dieses Spektrums, kein Unterwert und kein Angebot. | `data/parameters.yml`, `sources/registry.yml`, `docs/alternativenvergleich.md`, Bericht §3.3 |
| Robustheit der Auswahl | Selbst eine kostenlose Absorptionsmaschine ergibt 4,200 Mrd. € Barwert statt 4,136 Mrd. € bei H1. Die Auswahl hängt nicht am Preis der Absorptionsmaschine. | `zero_absorption_equipment_npv_eur`, `test_absorption_design_and_cost` |

Die neue Revision enthält 23 bestandene Modelltests und 14 Seiten mit 10 Haupttext- und 4 Literatur-/Anhangsseiten. Die Prüfung verlangt mindestens 40 % vertikale Textfläche und Inhalt in beiden Spalten nach dem Deckblatt. Frühere Punktzahlen werden nicht übernommen. Vor Runde 11 ist die Archivreproduktion erneut zu prüfen.

## Befunde aus Runde 11, DeepSeek

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| H2-Zyklen nicht eindeutig | Drei Zyklen werden ausdrücklich mit 12,48 und fünf Zyklen mit 10,40 Mio. m³ zugeordnet. Die Kosten verwenden den jeweiligen vollständigen Bedarf. | `evaporative_makeup_sensitivity`, Bericht §3.3 |
| H3-Fixkosten nicht beschrieben | H3 enthält als variable Ausrüstung nur Pumpen und keinen Notstromposten, aber dieselben 95 Mio. € für Tiefbau und Steuerung. | Bericht §3.3 und Tabelle 2, `docs/alternativenvergleich.md` |
| Teilstrom-Fixkosten fehlen | Die Unterschrift nennt \(80f^{0,65}+15f^{0,5}\) Mio. € für Tiefbau und Steuerung und die p90-Reserve der variablen Ausrüstung. | Tabelle 4, `civil_scale_exponent`, `controls_scale_exponent` |
| Vertikale Leerräume in Anhang A | `\raggedbottom` verhindert das Dehnen um die Displayformel. Die tatsächliche Seite wird erneut gesichtet. | `report/main.tex`, PDF-Seite 13 |
| COP- und Luftzeile in Tabelle 1 | Der COP ist als eigene Annahme und nur der Strompreis mit [16] belegt. Die Luftbezeichnung ist gekürzt und bleibt in einer Zeile. | Tabelle 1 auf PDF-Seite 4 |
| Gleiche MW-Header | Die Header \(Q\) und \(P_{el}\) unterscheiden Kühlung und elektrische Leistung ohne Spaltenüberlauf. Die Unterschrift definiert beide in MW. | `report/generated/flow_fractions.tex`, PDF-Seite 14 |
| Optionale Klarheitsbefunde | Die fünf Module im Mittelbetrieb werden mit etwa 98 % Last beschrieben. Die Quellkühlung ist gleichwertig, der Nasskühlturm bleibt unausgelegt. Der sekundäre Wärmekapazitätsstrom ist mit konstanten Stoffwerten gleich, mit temperaturabhängigen Werten nur eine Näherung. | Zusammenfassung, Bericht §§3.1 und 3.3 |

Die Revision enthält weiterhin 23 bestandene Modelltests und 14 Seiten mit 10 Haupttext- und 4 Literatur-/Anhangsseiten. Die Reproduktion wird für Runde 12 mit dem exakten Review-Commit geprüft.

## Befunde aus Runde 12, DeepSeek

| Befund | Konkrete Änderung oder begründete Grenze | Verifikation |
| --- | --- | --- |
| M1, Sensitivität ohne einheitliches Bezugsjahr | Alle Sensitivitätsgrößen werden im zehnten Jahr ausgewertet. Die 12-Jahres-Prognose ergibt dort 731,484 MW und -16,7 %. Die Barwerte folgen weiterhin der jeweiligen Prognose. | `sensitivity_rows`, `evaluation_year`, `test_sensitivity_uses_common_reference_year`, Tabelle 3 |
| M2, Ausfallgleichung ohne MW-Konversion | Die Gleichung verwendet \(10^6 Q_{\mathrm{Kuehl,MW}}\) im Zähler und definiert Sekunden, Volumen, Dichte, Wärmekapazität und die Einheit K/s. | `report/main.tex`, `scripts/verify_report.py`, PDF-Seite 8 |
| Optionale Klarheitsbefunde | Die Zusammenfassung beschreibt die Pufferwirkung als abhängig vom effektiven Volumen. Quelle [19] nennt Tabelle 5.11 für den Hilfsstrom. Die Spaltenbalance beginnt bereits bei Anhang A. | Zusammenfassung, Quelle [19], `sources/registry.yml`, `report/main.tex` |

Die Revision enthält 24 bestandene Modelltests und 14 Seiten mit 10 Haupttext- und 4 Literatur-/Anhangsseiten. Die Reproduktion wird für Runde 13 mit dem exakten Review-Commit geprüft.

## Aktueller Lieferumfang

Nach der Nutzerkorrektur ist nur der Research Paper Produkt. Die Kriterien 1 bis 6, 8 bis 11 und 12a bleiben Prüfgegenstand. Kriterium 12b und die Präsentationsartefakte werden nicht fortentwickelt. Nach den fachlichen Council-Runden folgt ein eigener Design-Council für den Research Paper.

## Offene physikalische und menschliche Grenzen

- Betroffener Stromanteil, Karsterfassung und Verhalten oberhalb 4,7 m³/s sind nicht feldkalibriert.
- COP, Teillast, Feuchtkugel, Wärmeübertragung, Luftführung, Schall und Plume benötigen Hersteller- oder Standortdaten.
- Netzanschluss, Flächeneigentum, Diesellogistik, Genehmigung und gemeinsame Ausfallursachen sind offen.
- Der Wiederanlauf ist ein Rechenszenario, keine durchgeführte Zuschaltprobe.
- Offizielle Team-ID, menschliche wissenschaftliche Prüfung, Rechtefreigabe und tatsächliche Einreichung fehlen.

Runde 2 wurde mit Commit `cc25cc903681ebbc4d6865309236885f729d6d77` bewertet und nicht bestanden. Der Runde-3-Kandidat `babe04c` wurde in einer frischen Archivkopie reproduziert. `review/rounds/round3/reproduction.md` dokumentiert ausdrücklich diesen Kandidaten, nicht den späteren Dokumentationscommit. Runde 3 wurde anschließend mit Commit `77c1f972df9c67a00354e395ce31f27fd0c1b95c` bewertet und nicht bestanden. Der Kandidat `85127420f90cc7fc742c5698e78fc1214e262a42` wurde für Runde 4 archivreproduziert; der Freeze-Commit `2fd9f3cd11e2f984f4fb8ce693b855529cabc580` ergänzte nur den Reproduktionsnachweis. Beide Runde-4-Reviewer bestanden die Stoppregel nicht. Ihre Befunde sind oben zugeordnet. Für Runde 5 wurde der Kandidat `9d8f4df4983335aed38bbd6cbd717d378ee3eba6` einschließlich Sprache und Video archivreproduziert. Alle 41 verglichenen Artefakte und 33 Renderbilder stimmen byteweise überein. `review/rounds/round5/reproduction.md` dokumentiert die Prüfung. Der folgende Freeze-Commit ergänzt nur Dokumentation und wird vor dem Council erneut geprüft. Diese Zuordnung behauptet keine neue Punktzahl.

Für den Paperkandidaten `a963e211813cb5bb4b34dd0e6c5b77bb6882d969` erzeugte eine frische Archivkopie Modell, PDF und Reviewbilder erneut. Alle 36 verglichenen Paperartefakte einschließlich der zwölf Seitenbilder stimmen byteweise überein. `review/rounds/round6/reproduction.md` dokumentiert diesen Lauf. Er bezieht sich nicht auf den späteren Dokumentations- und Freeze-Commit und behauptet keine neue Punktzahl.

Für den Paperkandidaten `1878af8f0a66802696b65243ea4db759fd40c919` nach den Runde-6-Korrekturen erzeugte eine frische Archivkopie Modell, PDF und Reviewbilder erneut. Alle 36 verglichenen Paperartefakte einschließlich der zwölf Seitenbilder stimmen byteweise überein. `review/rounds/round7/reproduction.md` dokumentiert diesen Lauf. Er bezieht sich nicht auf den späteren Dokumentations- und Freeze-Commit und behauptet keine neue Punktzahl.

Für den Paperkandidaten `2385effc1d03a39bdf3965222d4121030d7a6569` nach den Runde-7-Korrekturen erzeugte eine frische Archivkopie Modell, PDF und Reviewbilder erneut. Alle 37 verglichenen Paperartefakte einschließlich der dreizehn Seitenbilder stimmen byteweise überein. `review/rounds/round8/reproduction.md` dokumentiert diesen Lauf. Er bezieht sich nicht auf den späteren Dokumentations- und Freeze-Commit und behauptet keine neue Punktzahl.

Für den Paperkandidaten `becd50a0ddd77df4add7d03e8cb69866239f9b12` nach den Runde-8-Korrekturen erzeugte eine frische Archivkopie Modell, PDF und Reviewbilder erneut. Alle 37 verglichenen Paperartefakte einschließlich der dreizehn Seitenbilder stimmen byteweise überein. `review/rounds/round9/reproduction.md` dokumentiert diesen Lauf. Er bezieht sich nicht auf den späteren Dokumentations- und Freeze-Commit und behauptet keine neue Punktzahl.

Für den Paperkandidaten `3f2324cb7b7323f1a04fbbad82a87c6e48dd8f64` nach den Runde-9-Korrekturen erzeugte eine frische Archivkopie Modell, PDF und Reviewbilder erneut. Alle 40 verglichenen Paperartefakte einschließlich der fünfzehn Seitenbilder stimmen byteweise überein. `review/rounds/round10/reproduction.md` dokumentiert diesen Lauf. Er bezieht sich nicht auf den späteren Dokumentations- und Freeze-Commit und behauptet keine neue Punktzahl.

Für den Paperkandidaten `94736f771aea1db20d8c7eeca5ded11d7ff42389` nach den Runde-10-Korrekturen erzeugte eine frische Archivkopie Modell, PDF und Reviewbilder erneut. Alle 39 verglichenen Paperartefakte einschließlich der vierzehn Seitenbilder stimmen byteweise überein. `review/rounds/round11/reproduction.md` dokumentiert diesen Lauf. Er bezieht sich nicht auf den späteren Dokumentations- und Freeze-Commit und behauptet keine neue Punktzahl.

Für Runde 12 wird nicht nur der Ausgangskandidat `94927f986b015f4ab03cf151b97fc41f245cbdd0` archiviert, sondern der vollständige Review-Commit mit dem Reproduktionsnachweis und der Entscheidungsaufzeichnung. `review/rounds/round12/reproduction.md` beschreibt den Lauf und `revision.json` enthält den genauen Commit. Die Prüfung verlangt 39 bytegleiche Paperartefakte und bezieht sich nicht auf eine frühere Punktzahl.

Für Runde 13 wird der vollständige Review-Commit mit dem Reproduktionsnachweis und der Entscheidungsaufzeichnung archiviert. Ausgangskandidat ist `4d22546b9a146e63ece26ba38ffaac697e153d7e`. `review/rounds/round13/reproduction.md` beschreibt den Lauf und `revision.json` enthält den genauen Commit. Die Prüfung verlangt 39 bytegleiche Paperartefakte und bezieht sich nicht auf eine frühere Punktzahl.
