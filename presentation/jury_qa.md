# Adversariale Juryfragen und Antworten

Diese Fragen sind simulierte Prüffragen, keine Aussagen einer realen Jury. Jede Antwort verweist auf Belege und eine konkrete Revision oder eine begründete offene Grenze. Ein Council-Review ist keine menschliche Fachprüfung.

## Thermodynamik und Modell

### 1. Warum reichen nicht etwa 30 kW aus dem Energiebedarf des Beckenvolumens?

Die 0,0303 MW gelten nur für ein isoliertes Speichervolumen von 25.000 m³ über zehn Jahre. Der Blautopf hat im Mittel 2,3 m³/s Abfluss. Wenn der gesamte Zufluss von 9 auf 100 °C ansteigt, muss die Anlage die eingebrachte Enthalpie wieder abführen. Dann sind 877,8 MW erforderlich. Die Speicherrechnung ist eine untere Grenze, keine Auslegung.

Beleg: `baseline.storage_lower_bound_mw` und `baseline.final_cooling_mw`, Folien 2 und 3.

### 2. Ist die 100-°C-Annahme in 22 m Tiefe nicht physikalisch falsch?

Hydrostatisch liegt der Siedepunkt dort bei etwa 135,4 °C. Die Aufgabe prognostiziert Sieden am Blautopf, deshalb dient der Oberflächenwert von etwa 100 °C als Szenarioanker. Heißes Wasser kann beim Aufstieg und Druckabfall in die Sättigungslinie eintreten. Die Anlage hält 9 °C und bleibt dadurch weit unter beiden Grenzen. Ein Druckprofil ist dennoch erforderlich.

Beleg: NIST und IAPWS [4,5], `data/parameters.yml`. Revision: Druckgrenze und Entspannungskochen ausdrücklich getrennt.

### 3. Wie kann trockene Luft bei 35 °C Wasser auf 9 °C kühlen?

Mit direkter Trockenkühlung allein geht das nicht. Die erste Stufe kühlt nur von 100 auf 40 °C. Erst Kältemaschinen senken danach auf 9 °C. Die Stufen sind getrennt dimensioniert.

Beleg: `cooling_stage` in `model/core.py`, Folie 5.

### 4. Wo bleibt die Wärme der Kältemaschinen?

Die direkte Trockenkühlung gibt 578,8 MW ab. Die Kondensatoren geben 373,8 MW ab, darin sind 299,0 MW Entzug und 74,8 MW Antriebsleistung. Mit Ventilator- und Pumpenarbeit beträgt die externe Wärmeabgabe 967,2 MW. Im p90-Spitzenfall steigt sie auf 1976,4 MW. Sie muss außerhalb des verbundenen Gewässersystems nachgewiesen werden.

Beleg: `baseline.air_rejection_mw`, `design.air_rejection_mw`, `validation.heat_sink_balance_error_mw`. Revision: Kondensator- und Hilfsenergie sind in Bilanz, Kosten und Folien enthalten.

### 5. Ist COP 4 belegt?

Nein. COP 4 ist eine Szenarioannahme, keine Herstellerkurve. Die Referenz wurde von 5 auf 4 gesenkt, damit sie nicht von einem Heizungs-Feldwert abhängt. Die gekoppelte Unsicherheitsrechnung variiert COP zwischen 3 und 6,5. Vor einer Beschaffung sind Herstellerkurven mit Teillast, Pumpen, Ventilatoren und tatsächlichen Quell- und Senkentemperaturen erforderlich.

Beleg: `data/parameters.yml`, `uncertainty` und Abbildung `fig:unsicherheit` im Bericht. Revision: COP als unsichere Variable, nicht als Zusicherung.

### 6. Warum ändern 8 oder 12 Jahre die Endleistung nicht?

Die Endtemperatur beträgt in beiden Fällen 100 °C. Deshalb bleibt die stationäre Kühlleistung gleich. Der kürzere Zeitraum verlangt jedoch einen früheren Ausbau und verändert den Kostenpfad. Die Jahresreihen erfassen diesen Unterschied.

Beleg: `output/model/sensitivity.csv` und `hybrid_schedule.csv`.

## Lösung und Betrieb

### 7. Warum nicht die günstigere Verdunstungskühlung?

H2 kostet im Modell 2,988 statt 3,666 Mrd. € Barwert, verbraucht aber 8,45 Mio. m³ Wasser pro Jahr. Das sind 11,6 % des mittleren Quellstroms. Hinzu kommen Aerosol- und Legionellenmanagement nach der 42. BImSchV. H1 verursacht um 62,3 Kilotonnen pro Jahr mehr Stromemissionen. Die Wahl ist ein Zielkonflikt, kein pauschaler Sieg der ökologisch besseren Technik.

Beleg: `alternatives` in `output/model/results.json`, `fig03_kostenpfad`, Folie 7. Revision: H2 wurde um eine Kältestufe und dieselbe p90-Reserve ergänzt.

### 8. Ist 9 °C Rücklauf nicht selbst ein Kälteschock?

Der Normalzustand liegt bei etwa 9 °C. Bei geplanter Inbetriebnahme senkt die Regelung den Kälteauslass vom gemessenen Ausgangswert mit höchstens 1 K/h. Für den Stresstest von 100 auf 9 °C dauert die Sollwertrampe 91 Stunden. Sensoren stoppen die Rampe bei Überschreitung am Kontrollpunkt. Der Puffer allein und ein linear geöffnetes Ventil wären dafür kein Nachweis. Die Rampe wird vor kritischen Temperaturen eingefahren und ist kein Wiederanlauf- oder Notfallnachweis.

Beleg: LAWA [10], `return_ramp_hours` und `return_ramp_max_rate_k_h`. Revision: Geregelter Sollwert statt Pufferbehauptung, Pilotversuch weiterhin erforderlich.

### 9. Deckt N+1 nur das letzte Jahr ab?

Nein. Jede Ausbaustufe muss ihre erforderliche Reserve vor dem Lastjahr nachweisen. Im Endausbau sind zwölf Stränge geplant, elf tragen den p90-Bedarf und einer ist Reserve. Im Mittelbetrieb modulieren fünf. Die Kostenrechnung enthält p90-Skalierung und 20 % Reserve. N+1 deckt trotzdem nur einen Einzelfehler, keine hydrologische Überlast oder gemeinsame Ursachen.

Beleg: `module_count`, `required_modules`, `reserve_fraction` und `design` in `output/model/results.json`. Revision: Auslegung von Mittelwert auf p90 geändert.

### 10. Was passiert bei einem Stromausfall?

Ohne Kühlung erreicht das angenommene Becken im Mittelstrom nach 23 Minuten 20 °C, im p90-Fall bereits nach 11,4 Minuten. Diese Schwelle ist intern, keine behördliche Blau-Grenze und keine Siedezeit. Das dynamische Modell nutzt 0,5 min Detektion, 5 min Generatorstart und 10 min bis voller Kühlleistung. Der Höchstwert beträgt 12,6 °C im Mittelstrom und 16,2 °C im p90-Fall. Die Differenz zur vollen Leistung beträgt dort 1,4 Minuten und ist keine freie Wartezeit. Zwei Netzeinspeisungen, sechs Aggregate und eine Reserve gehören zum Szenario, nicht zu einem erfolgten Feldtest.

Beleg: `validation.failure_mean` und `failure_p90`, Folie 6. Revision: Beide Abflussfälle und eine Konvergenzprüfung ergänzt.

### 11. Wie wird sichergestellt, dass wirklich der gesamte betroffene Strom erfasst wird?

Das Konzept soll das betroffene Tiefenwasser vor dem Austritt erfassen und nach der Kühlung zurückführen. Leitungen, Ansaug- und Diffusorgeometrie sind noch nicht konstruiert. Sie müssen nach Tracer-, Durchfluss- und Druckmessungen entworfen werden. Erst Messungen an Zufluss, Rücklauf und Blau können die vollständige Erfassung bestätigen. Gestufte Versuche müssen auch einen thermischen Kurzschluss zwischen Entnahme und Rückführung ausschließen. Der Messplan ist ein Prüfkonzept, kein Nachweis der Erfassung.

Beleg: Messplan in Bericht und Folie 9. Revision: Die nicht konstruierte Geometrie wird nicht mehr als fertige Anlagenplanung dargestellt.

### 12. Warum ist keine Wärmevermarktung eingerechnet?

Das Altstadtnetz existiert, aber Abnahmekapazität, Temperatur und Jahresgang sind unbekannt. Der Referenzfall setzt deshalb null Erlös. Wärmenutzung darf die Bilanz nur verbessern, wenn ein gemessener Abnehmer zeitgleich Wärme annimmt. Die Kühlung bleibt auch ohne Käufer erforderlich.

Beleg: Stadt Blaubeuren [20], `heat_recovery_mw: 0.0`.

## Grenzen, Kosten und Nachweise

### 13. Ist die Anlage auch beim dokumentierten Hochwasser sicher?

Nicht im vollständig erwärmten Hochwasserfall. Für 32,7 m³/s wären 12,48 GW für die Rückkehr auf 9 °C erforderlich. Der Entwurf umfasst höchstens 4,7 m³/s betroffenen Strom. Tracer und Hochwassermessungen müssen vor dem Bau zeigen, ob das Ereignis die Anomalie trägt. Falls ja, ist ein neuer Entwurf nötig. Diese Grenze wird im Bericht und auf Folie 8 ausdrücklich genannt.

Beleg: `baseline.flood_stress_cooling_mw`. Revision: Hochwasser bleibt Stresstest, nicht versteckte Kapazitätszusage.

### 14. Wie kann von dauerhaft gesprochen werden?

Dauerhaft bedeutet unbegrenzter Betrieb mit Wartung innerhalb der erklärten Hülle, nicht beliebig wachsende Vulkanleistung. Nach Jahr zehn wird die Zuflusstemperatur konservativ bei 100 °C begrenzt. Steigt sie weiter oder wächst der betroffene Strom über 4,7 m³/s, muss die Anlage erweitert oder das Konzept verworfen werden.

Beleg: `scenario.premise`, `docs/alternativenvergleich.md`.

### 15. Sind 1.283 Mio. € nicht völlig unbelegt?

Der Wert ist eine Szenarioschätzung, kein Angebot. Ein Händlerpreis für Plattenwärmetauscher und Literatur zu Kältemaschinen dienen nur als Anker. Trockenkühler, Tiefbau, Notstrom und Zuschläge sind ausdrücklich eigene Annahmen. Die 95 Mio. € für Tiefbau und Steuerung sind All-in-Posten einschließlich Reserve; die 60 % gelten nur für variable Ausrüstung. Monte-Carlo-Läufe variieren COP, Abfluss und Investitionskosten gekoppelt.

Beleg: `data/parameters.yml`, `sources/registry.yml`, `fig:unsicherheit`. Revision: Kostenlabels, Tarifproxy und Zuschlagsgrenzen konkretisiert.

### 16. Welche Beobachtung würde die Lösung falsifizieren?

Mehr als 4,7 m³/s betroffener Strom, ein weiterer Temperaturanstieg über 100 °C, Wärmerückfluss in dasselbe Gewässer oder ein Verstoß gegen Temperatur- und Druckkriterien trotz Betrieb genügen jeweils. Auch Standort oder Genehmigung können den Entwurf scheitern lassen. Ein bestätigter kleiner Teilstrom widerlegt dagegen die Notwendigkeit der großen Referenzanlage.

Beleg: `docs/alternativenvergleich.md`, Folien 8 und 9.

### 17. Ist die Umsetzung in einem Schutzgebiet genehmigt?

Nein, eine Genehmigung wird nicht behauptet. Entnahme und Rückführung sind wasserrechtlich zu prüfen, außerdem FFH- und Artenschutz. Die Vorprüfung nach § 34 BNatSchG kann erhebliche Beeinträchtigungen untersagen. Erst Feldversuche, konkrete Unterlagen und die zuständige Behörde können die Umsetzbarkeit bestätigen.

Beleg: WHG [14], Stadt Blaubeuren [15], BNatSchG [24]. Diese Einschränkung ist eine menschliche Restaufgabe.

### 18. Warum soll eine synthetische Präsentation finaltauglich sein?

Das Paket enthält echte Folien, ein echtes Video, gemessene Audiodauer und dokumentierte Fragen. Es behauptet keine menschliche Live-Darbietung. Untertitel entstehen aus dem Sprechtext; ihre Satzzeiten sind proportional zur Audiodauer verteilt und nicht durch Forced Alignment verifiziert. Vor dem Finale müssen die Teilnehmenden Rechte, Vertonung, Rollen und ihre eigene Live-Probe freigeben.

Beleg: `presentation/timings.json`, `presentation/rehearsal.md`, `output/presentation/verification.json`.

### 19. Entspricht das Layout nicht D4RT nur oberflächlich?

Der Vergleich betrifft messbare Gestaltungsmerkmale: Zweispaltigkeit, Times-Hierarchie, Tabellenlinien, Bildunterschriften und numerische Verweise. A4, mindestens 25 mm Rand und 12 pt bleiben übergeordnet. Die lokale D4RT-PDF und gerasterte Seiten 1, 2 und 6 liegen dem Reviewpaket bei, sodass der Bildvergleich direkt möglich ist.

Beleg: `compliance/layout_referenz.md`, `sources/D4RT_paper.pdf`, `review/rendered/d4rt_page01.png`, `d4rt_page02.png`, `d4rt_page06.png`. Revision: Referenzbilder statt bloßer Textbeschreibung.

### 20. Welche Arbeit bleibt trotz Council-Konsens menschlich?

Berechtigte Teammitglieder müssen Annahmen und Quellen prüfen, die offizielle Team-ID einsetzen, Feld- und Behördenkontakte klären, Medienrechte freigeben, die Finalisten-E-Mail lesen und ihre eigene Darbietung proben. Der Council bewertet nur interne Bereitschaft. Er garantiert keine Jurypunkte oder Qualifikation.

Beleg: `PROVENANCE.md`, `README.md`, `review/README.md`.

### 21. Wie hoch ist das Überlastrisiko der alten Mittelwertauslegung?

In der vorhandenen Stichprobe überschreiten 3.857 von 10.000 Fällen die alte Kapazität von 1053,3 MW, also 38,57 %. Die neue p90-Auslegung installiert 2152,5 MW. Damit bleibt kein Fall der auf 0,7 bis 4,7 m³/s begrenzten Verteilung oberhalb der Kapazität. Das ist keine Wahrscheinlichkeitsaussage für höhere Abflüsse oder andere Wärmequellen.

Beleg: `uncertainty.mean_capacity_overload_fraction`, `design_overload_fraction` und `coverage_scope`. Revision: Kapazität auf historisches p90 mit 20 % Reserve erhöht.

### 22. Ist H2 bei warmer, feuchter Luft physikalisch gleichwertig?

Im Szenario beträgt die Feuchtkugeltemperatur 28 °C, die Annäherung 4 K. Verdunstung kühlt damit zunächst von 100 auf 32 °C mit 655,8 MW. Eine Kältemaschine übernimmt 221,9 MW bis 9 °C. Ohne diese Stufe wäre H2 nicht gleichwertig. Die 28 °C sind eine technische Annahme, keine gemessene standortbezogene Extremfeuchte. Feuchtemessungen können die Auslegung verändern.

Beleg: `plant.wet_bulb_design_c`, `evaporative_approach_k`, `alternatives[1]` und `test_evaporative_has_summer_chiller`. Revision: Feuchtkugelgrenze und Kältestufe ergänzt.

### 23. Warum kostet der Strom 138 €/MWh?

Der BDEW nennt diesen Wert für 70 bis 150 GWh pro Jahr. H1 benötigt im Erwartungsjahr 783 GWh, deshalb ist der Wert nur ein Tarifproxy und kein Angebot für diesen Abnahmefall. Das Alternativszenario mit 179 €/MWh ergibt 4,174 statt 3,666 Mrd. € Barwert. Ein konkretes Marktangebot bleibt erforderlich.

Beleg: BDEW [16], `tariff_scenarios`. Revision: Tarifklasse und Sensitivität korrigiert.

### 24. Ist der Wiederanlauf nach zehn Minuten bewiesen?

Nein. Es ist ein dynamisches Rechenszenario mit expliziten Annahmen. Detektion, Generatorstart und Lastzuschaltung werden gegen das Beckenaufheizen gerechnet. Im Mittelstrom liegt der Höchstwert bei 12,6 °C, im p90-Fall bei 16,2 °C. Ohne Kühlung wären 20 °C dort nach 11,4 Minuten erreicht. Die Differenz zur vollen Leistung beträgt dort 1,4 Minuten und ist keine freie Wartezeit. Zwei Toleranz- und Zeitschrittstufen bestätigen den Verlauf. Herstellerdaten, Netzschutz, Aggregatanlauf, gemeinsame Fehler und ein realer Lastabwurf- und Zuschaltversuch fehlen weiterhin.

Beleg: `failure` in `data/parameters.yml`, `validation.failure_mean`, `failure_p90` und `failure_p90_convergence_error_k`. Revision: Auslegungsfall und Konvergenzprüfung ergänzt, keine Feldvalidierung behauptet.

### 25. Warum nicht nur das Sieden statt des 9-°C-Zustands verhindern?

Mit 5 K Abstand zum Oberflächensiedepunkt liegt die Schutzmarke bei 94,97 °C. Beim Mittelstrom genügen dafür 48,5 MW Kühlleistung und 1,07 MW Antriebsleistung. Die Szenariokosten betragen 203,6 Mio. € Investition und 0,289 Mrd. € Barwert. Das bewahrt aber nicht das Ökosystem. Deshalb ist es eine getrennte Betriebs- und Sensitivitätsoption, kein Ersatz für den Normalbetrieb.

Beleg: `boil_guard` in `output/model/results.json`. Revision: Reine Siedeverhinderung und ökologisches Ziel quantitativ getrennt.

### 26. Ist die Anlage am Blautopf überhaupt platzierbar?

Das Screening verlangt 8,19 ha für Kühlung und Service, zweimal 182,7 MW unabhängig nutzbare Netzleistung und 2.237 m³ Diesellager. Ein konkreter Platz ist nicht ausgewählt. Luftführung, Rückverwirbelung, Schall und Plume fehlen als Messdaten. Rückhaltung und Leckkontrolle sind nach AwSV auszulegen, FFH und Wasserrecht gesondert zu prüfen. Ohne geeigneten Standort darf die Vollstromanlage nicht gebaut werden.

Beleg: `design.air_service_area_m2`, `design.electricity_mw`, `design.backup_fuel_m3`, AwSV [25], BNatSchG [24]. Revision: Standort-Screening als Zulassungsbedingung ergänzt.

### 27. Ist Council B wirklich unabhängig, wenn es dasselbe Modell nutzt?

Der Nutzer schreibt Kimi K3.1 Pro für Implementierung und einen Reviewer vor. Ein Modellwechsel wäre ein Verstoß gegen diese Vorgabe. Deshalb ist Council B ein unabhängiger Same-Model-Kontext mit getrenntem Auftrag und ohne Kenntnis der Implementierungshistorie oder der anderen Bewertung. Er ist keine externe, menschliche oder modellübergreifende Prüfung. Diese Einschränkung wird offengelegt und nicht durch Durchschnittsnoten oder nachträgliche Absprachen überdeckt.

Beleg: `review/model_configuration.md`, `PROVENANCE.md`, getrennte `clientRequestId`-Werte. Entscheidung: Vorgeschriebene Modelle beibehalten, Unabhängigkeitsgrenze präzise benannt.
