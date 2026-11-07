# Revisions- und Befundzuordnung

Diese Datei verbindet adversariale Juryfragen und Council-Befunde mit nachweisbaren Änderungen. Sie erhebt nicht den Anspruch, dass jede Antwort durch einen Commit beweist die technische Machbarkeit. Offene Restaufgaben bleiben ausgewiesen.

## Fragen 1 bis 20

| Frage | Nachweis der Herleitung und späteren Änderung | Status |
| --- | --- | --- |
| 1, Speicher statt Vollstrom | Commit `49eb33fb652215a09fd154042d3df922edadded2`, `model/core.py`, `docs/hypothesen.md` | Vollstrom- und Speicherfall getrennt |
| 2, Siedepunkt im Tiefendruck | Dasselbe Ausgangsmodell, NIST und IAPWS [4,5] | Hydrostatisches Beispiel dokumentiert |
| 3, Kühlung bei 35 °C Luft | Commit `49eb33f`, `model/core.py` | Zwei Stufen ausdrücklich getrennt |
| 4, Kondensatorwärme | Commit `65f218b4d5e57f9ad565231dc7b8fb41b4e46c69` und spätere Kostenrevision | Kondensator- und Hilfsenergie in Senke und Kosten |
| 5, COP als Annahme | `data/parameters.yml`, `model/run_all.py` | COP variiert, keine Herstellerkurve |
| 6, 8 oder 12 Jahre | Commit `65f218b`, `output/model/sensitivity.csv` | Endlast und Ausbau getrennt |
| 7, Verdunstungsalternative | Commit `65f218b`, Runde 2 Kostenrevision | Wasserhaushalt und Emissionen offengelegt |
| 8, Kälteschock | Commit `9b3a83bcea1358184b14de6759af117a049114f5` und Runde 2 Rampenmodell | Aktive 91-Stunden-Rampe und Sensorabschaltung |
| 9, N+1 in jeder Stufe | Commit `65f218b`, `reserve_fraction` | Sechs Stränge in jeder Stufe |
| 10, Stromausfall | Commit `65f218b`, `model/validation.py`, Runde 2 Notstromszenario | Interne Alarmschwelle und 48 Stunden Reserve |
| 11, Vollständige Stromerfassung | Commit `49eb33f`, Messplan in Bericht und Folie 9 | Tracer und Durchfluss vor Detailauslegung |
| 12, Wärmevermarktung | Commit `65f218b`, `heat_recovery_mw: 0.0` | Kein Erlös ohne Abnehmer |
| 13, Hochwasser | Commit `65f218b`, `baseline.flood_stress_cooling_mw` | 12,48-GW-Grenze nicht abgedeckt |
| 14, Dauerhaftigkeit | Commit `65f218b`, `scenario.premise` | Gültigkeit nur innerhalb der Hülle |
| 15, Kosten | Commit `65f218b`, Runde 2 Ersatzinvestition und Notstrom | Szenarien mit gekoppelter Unsicherheit |
| 16, Falsifikation | Commit `65f218b`, `docs/alternativenvergleich.md` | Explizite Abbruchkriterien |
| 17, Genehmigung | Commit `65f218b`, WHG und Naturschutzquellen | Keine Genehmigung behauptet |
| 18, Synthetische Präsentation | Commit `9b3a83b`, `presentation/rehearsal.md`, `output/presentation/playback.json` | Slidecast und Echtzeitprobe, keine Live-Darbietung |
| 19, D4RT-Layout | Commit `65f218b`, Runde 2 Layoutkorrekturen | D4RT-Prinzipien ohne Verstoß gegen Vorgaben |
| 20, Menschliche Restaufgaben | `PROVENANCE.md`, `README.md`, `presentation/rights.md` | Weiterhin offen |

## Council-Befunde aus Runde 1

| Befund | Konkrete Änderung | Verifikation |
| --- | --- | --- |
| Folie 8 läuft über die Seite | Grafik und Text kompakt, Fußzeile gekürzt | `scripts/verify_presentation.py` prüft alle Textzeichen gegen Seitenfläche, MP4-Frames zusätzlich visuell |
| Pfeil ins Leere in Folie 5 | Beide Wärmepfeile führen direkt auf `air.south` | Folie 5 im Renderbild |
| Legendenkollisionen in Abbildungen 1 und 3 | Legenden außerhalb der Datenfläche | Abbildungen neu rendern und Sichtprüfung |
| Gleichung 3 mit eigener Nummernzeile | Szenariogleichung gekürzt und Einheiten in Prosa | PDF-Geometrie und Sichtprüfung |
| Gemischte Dezimaltrennzeichen | Makros erzeugen deutsches Komma | `report/generated/numbers.tex` und PDF-Text |
| „Mehr als doppelt“ falsch | Auf rund 1,7-fache Reserveauslegung korrigiert | `report/main.tex`, Modellwerte |
| 1-K/h-Aussage unmodelliert | Sollwert rampe am Kälteauslass statt Pufferbehauptung | `return_ramp_hours` und `return_ramp_max_rate_k_h` in Modell und Tests |
| Zwischenkorrektur der Ventil rampe | Linearer Ventilhub verworfen, weil er in einem Mischbehälter die Rate nicht generell begrenzt. Kälteauslass wird geregelt, Wiederanlauf bleibt gesondert offen | Sollwert funktion `planned_return_temperature_c`, Intervalltest mit 921 Stützstellen |
| Seitenzahl außerhalb des Randbereichs | Unterer Satzspiegel 28 mm, `footskip=6mm`, Fußzeile um 7 mm angehoben | Vertikale Prüfung aller Textzeichen einschließlich Fußzeilen, gemessen mindestens 26,50 mm |
| Quellenregisterfehler | Drei DOI-Titel und zweite NIST-Tabelle korrigiert, UBA ergänzt | `sources/registry.yml`, `report/main.tex` |
| Ersatzinvestition ohne 60-%-Zuschlag | Multiplikator auch auf Ersatz angewandt | `test_replacement_uses_engineering_multiplier` |
| Monte-Carlo-Kopplung unzureichend | Jede Ziehung rechnet alle 25 Jahre mit Abfluss, COP und Investitionsfaktor | `coupled_npv_error_eur = 0.0` |
| Manifest ignoriert Umlautpfade | `git ls-files -z`, NUL-Verarbeitung und Mengenabgleich mit `git ls-tree -r -z` | Exakte Dateimenge des neuen Manifests |
| Wärmesenke und Notstrom offen | Fläche, Rückverwirbelung, NPSH, zwei Einspeisungen, 48 Stunden und Diesel vorrat quantifiziert | `air_face_area_m2`, `npsh_design_margin_m`, `backup_fuel_liters` |
| Visuelle Qualität unter D4RT | Doppelte Labels entfernt, Verweise ergänzt, Figuren und Tabellen neu angeordnet | Marken- und Referenzprüfung in `scripts/verify_report.py` |
| URLs und Zitierweise | Links umbrechbar, linksbündig, zweite Drucktabelle, Klammern `[n]` sichtbar | PDF-Text und Sichtprüfung |
| SAR 1215:1216 statt 1:1 | `setsar=1` und verlustfreie Einpassung | `ffprobe` verlangt SAR 1:1 und DAR 16:9 |
| Q&A-Revisionen ohne Commitbezug | Diese Datei verbindet Fragen und Befunde mit Commits | `review/revisions.md` |
| CO2 und Luftkühlerfläche fehlen | UBA-Faktor 363 g/kWh, Face- und Servicefläche ergänzt | `emissions_tco2_year`, `air_face_area_m2` |
| Zwischenkorrektur Diesel einheit | MWh mit 1000 in kWh umgerechnet, Brennstoffkosten neu berechnet | Exakter Test auf 908657,186903 Liter, NPV 2,938 Mrd. € |
| Zwischenkorrektur Folie 7 | Kürzere Kennzahlenbeschreibungen, Mathematiksatz für CO2, geringere Abstände | Alle Textzeichen innerhalb der Folie, Sichtprüfung und Videoexport |
| Zwischenkorrektur Anhang | Einspaltiger Ergebnis anhang, Überschrift vor den Inhalten, größere Diagrammtexte | Gerenderte Seiten 15 und 16, keine fast leere Zwischenseite |

Der neue Runde-2-Commit wird nach dem vollständigen Build eingetragen. `decisions.tsv` enthält die zusätzlichen Befunde aus der Selbstprüfung. Die Council-Bewertungen der neuen Revision folgen erst nach erneuter unabhängiger Prüfung.
