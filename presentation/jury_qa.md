# Adversariale Juryfragen und Antworten

Diese Fragen sind simulierte Prüffragen, keine Aussagen einer realen Jury. Die Antworten beziehen sich auf die aktuelle Paketrevision. Jede Zeile zur Revision nennt eine konkrete Änderung oder eine begründete Entscheidung, warum keine Änderung erfolgt.

## Thermodynamik und Modell

### 1. Warum reichen nicht etwa 30 kW aus dem Energiebedarf des Beckenvolumens?

Die 0,0303 MW gelten nur für ein isoliertes Speichervolumen von 25.000 m³ über zehn Jahre. Der Blautopf hat im Mittel 2,3 m³/s Abfluss. Wenn der gesamte Zufluss von 9 auf 100 °C ansteigt, muss die Anlage die eingebrachte Enthalpie wieder abführen. Dann sind 877,8 MW erforderlich. Die Speicherrechnung ist eine untere Grenze, keine Auslegung.

Beleg: `output/model/results.json`, `baseline.storage_lower_bound_mw` und `baseline.final_cooling_mw`, Folien 2 und 3.

### 2. Ist die 100-°C-Annahme in 22 m Tiefe nicht physikalisch falsch?

Hydrostatisch liegt der Siedepunkt dort bei etwa 135,4 °C. Die Aufgabe prognostiziert Sieden am Blautopf, weshalb der Bericht den Oberflächenwert von etwa 100 °C als Szenarioanker verwendet. Das Modell prüft zusätzlich Druck und Siedepunkt örtlich. Heißes Wasser kann beim Aufstieg und Druckabfall in die Sättigungslinie eintreten. Die Anlage hält 9 °C und bleibt dadurch weit unter beiden Grenzen.

Beleg: NIST und IAPWS [4,5], `data/parameters.yml`, Abschnitt Hydrologie. Revision: Druckgrenze und Entspannungskochen ergänzt.

### 3. Wie kann trockene Luft bei 35 °C Wasser auf 9 °C kühlen?

Mit direkter Trockenkühlung allein geht das nicht. Die erste Stufe kühlt nur von 100 auf 40 °C. Erst Kältemaschinen senken danach auf 9 °C. Die Stufen sind getrennt dimensioniert.

Beleg: `cooling_stage` in `model/core.py`, Folie 5. Revision: Die Stufenfiguren nennen beide Temperaturbereiche ausdrücklich.

### 4. Wo bleibt die Wärme der Kältemaschinen?

Die direkte Trockenkühlung gibt 578,8 MW ab. Die Kondensatoren geben 358,8 MW ab, darin sind 299,0 MW Entzug und 59,8 MW Antriebsleistung. Mit Ventilator- und Pumpenarbeit beträgt die externe Wärmeabgabe 952,0 MW. Sie erfolgt an Luft außerhalb des verbundenen Gewässersystems.

Beleg: `baseline.air_rejection_mw`, Validierung `heat_sink_balance_error_mw`. Revision: Kondensatorwärme wurde nachträglich in Leistung, Kosten und Folien aufgenommen.

### 5. Ist COP 5 nicht einfach gewünscht?

COP 5 ist eine Szenarioannahme, kein Herstellerversprechen. Der Bericht variiert COP zwischen 3 und 6,5 in 10.000 Zufalls läufen. Vor einer Beschaffung sind Herstellerkurven mit Teillast, Pumpen, Ventilatoren und tatsächlichen Quell- und Senkentemperaturen erforderlich.

Beleg: `data/parameters.yml`, `fig05_unsicherheit`, `uncertainty.npv_p05_eur` bis `npv_p95_eur`.

### 6. Warum ändern 8 oder 12 Jahre die Endleistung nicht?

Die Endtemperatur beträgt in beiden Fällen 100 °C. Deshalb bleibt die stationäre Kühlleistung gleich. Der kürzere Zeitraum erhöht jedoch den erforderlichen Ausbau und die Kosten früher. Die Jahresreihen und Barwerte erfassen diesen Unterschied.

Beleg: `output/model/sensitivity.csv` und `hybrid_schedule.csv`.

## Lösung und Betrieb

### 7. Warum nicht die deutlich günstigere Verdunstungskühlung?

H2 kostet im Modell 0,792 statt 2,938 Mrd. € Barwert, verbraucht aber 11,3 Mio. m³ Wasser pro Jahr. Das sind 15,6 % des mittleren Quellstroms. Hinzu kommen Aerosol- und Legionellenmanagement nach der 42. BImSchV. H1 kauft mit höheren Kosten den Erhalt des Wasserhaushalts und weniger hygienische und ökologische Risiken. Die Stromemissionen von H1 sind um 193,0 Kilotonnen pro Jahr höher [23].

Beleg: `docs/alternativenvergleich.md`, `fig03_kostenpfad`, Folie 7. Entscheidung: Der höhere Preis wird bewusst akzeptiert, H2 bleibt als mögliche Notfalloption dokumentiert.

### 8. Ist 9 °C Rücklauf nicht selbst ein Kälteschock?

Der Normalzustand liegt bei etwa 9 °C. Bei geplanter Inbetriebnahme senkt die Regelung den Auslass der Kältemaschinen vom gemessenen Ausgangswert mit höchstens 1 K/h. Der volle betroffene Strom bleibt dabei erfasst. Für den rechnerischen Stresstest von 100 auf 9 °C dauert die Sollwert rampe 91 Stunden. Unabhängige Sensoren stoppen die Rampe, wenn die gemessene Änderung am ökologischen Kontrollpunkt den Grenzwert überschreitet. Der 8280-m³-Puffer allein und ein linear geöffnetes Zulaufventil wären dafür kein Nachweis. Die Rampe wird vor kritischen Temperaturen eingefahren und ist kein Wiederanlauf- oder Notfallnachweis. LAWA behandelt schnelle Abkühlung als mögliche Belastung. Die konkrete Gewässertyp- und Artenschutzprüfung bleibt behördliche Restaufgabe.

Beleg: LAWA [10], `return_ramp_hours` und `return_ramp_max_rate_k_h`. Revision: Die Sollwert rampe am Kälteauslass ersetzt die physikalisch unzureichende Ventil rampe. Ein eigener Wiederanlaufplan bleibt erforderlich.

### 9. Deckt N+1 nur das letzte Jahr ab?

Nein. Die sechs getrennten Stränge werden in jeder Ausbaustufe so dimensioniert, dass fünf die Last tragen und der sechste frei ist. In frühen Stufen sind die Module kleiner und werden erweitert oder ersetzt. Die Kostenrechnung enthält in jedem Jahr 20 % Reserve.

Beleg: `reserve_fraction` in `data/parameters.yml`, Folie 6. Revision: Formulierung von Reserve nur im Auslegungsjahr auf Reserve in jeder Ausbaustufe geändert.

### 10. Was passiert bei einem Stromausfall?

Zwei unabhängige Netzeinspeisungen und 48 Stunden Notstromreserve sind Teil des Entwurfs. Nach einem vollständigen Kühlungsausfall erreicht das angenommene Becken im zehnten Jahr in etwa 23 Minuten 20 °C. Diese Schwelle ist intern und ökologisch motiviert, keine behördliche Blau-Grenze und nicht der Siedepunkt. Die Notfallplanung muss diesen Zeitraum für Alarm und Lastzuschaltung nutzen.

Beleg: `validation.failure_time_to_20c_h`, `backup_duration_hours`, Folie 6. Revision: Interne Alarmschwelle und Notstromdauer präzisiert.

### 11. Wie wird sichergestellt, dass wirklich der gesamte betroffene Strom erfasst wird?

Das Tiefenwasser wird vor dem Austritt durch getrennte Leitungen gefasst und nach der Kühlung über Puffer und Diffusor zurückgeführt. Tracer und Durchflussmessungen an Zufluss, Rücklauf und Blau prüfen die Vollständigkeit. Ein thermischer Kurzschluss zwischen Entnahme und Rückführung wird durch gestufte Versuche erkannt.

Beleg: Messplan in Bericht und Folie 9. Offene technische Detailplanung: endgültige Ansaug- und Diffusorgeometrie nach Feldversuch.

### 12. Warum ist keine Wärmevermarktung eingerechnet?

Das Altstadtnetz existiert, aber Abnahmekapazität, Temperatur und Jahresgang sind unbekannt. Der Referenzfall setzt deshalb null Erlös. Wärmenutzung darf die Bilanz nur verbessern, wenn ein gemessener Abnehmer zeitgleich Wärme annimmt. Die Kühlung bleibt auch ohne Käufer erforderlich.

Beleg: Stadt Blaubeuren [20], `heat_recovery_mw: 0.0`.

## Grenzen, Kosten und Nachweise

### 13. Ist die Anlage auch beim dokumentierten Hochwasser sicher?

Nicht im vollständig erwärmten Hochwasserfall. 32,7 m³/s führen rechnerisch zu 12,48 GW. Der Referenzentwurf umfasst höchstens 2,3 m³/s betroffenen Strom. Tracer und Hochwassermessungen müssen vor dem Bau zeigen, ob das Ereignis die Anomalie trägt. Falls ja, ist ein neuer Entwurf nötig. Diese Grenze wird im Bericht und auf Folie 8 ausdrücklich genannt.

Beleg: `baseline.flood_stress_cooling_mw`. Revision: Hochwasserfall als nicht abgedeckten Stresstest ergänzt.

### 14. Wie kann von dauerhaft gesprochen werden?

Dauerhaft bedeutet unbegrenzter Betrieb mit Wartung innerhalb der erklärten Hülle, nicht beliebig wachsende Vulkanleistung. Nach Jahr zehn wird die Zufluss temperatur konservativ bei 100 °C begrenzt. Steigt sie weiter oder wächst der betroffene Strom, muss die Anlage erweitert oder das Konzept verworfen werden.

Beleg: `scenario.premise`, `docs/alternativenvergleich.md`.

### 15. Sind 722 Mio. € nicht völlig unbelegt?

Der Wert ist eine Szenario-Schätzung, kein Angebot. Ein Händlerpreis für Plattenwärmetauscher und Literatur zu Kältemaschinen dienen nur als Anker. Trockenkühler, Tiefbau, Notstrom und Zuschläge sind ausdrücklich eigene Annahmen. Monte-Carlo-Läufe variieren COP und Investitionskosten. Die Entscheidung zwischen H1 und H2 wird zusätzlich anhand physischer Größen geführt, damit sie nicht nur auf unsicheren Eurobeträgen beruht.

Beleg: `data/parameters.yml`, `sources/registry.yml`, `fig05_unsicherheit`. Revision: Kostenlabels und Unsicherheitsband ergänzt.

### 16. Welche Beobachtung würde die Lösung falsifizieren?

Vier Befunde genügen jeweils: ein größerer betroffener Volumenstrom als ausgelegt, ein weiterer Temperaturanstieg über 100 °C, nachgewiesener Wärmerückfluss in dasselbe Gewässer oder ein Verstoß gegen Temperatur- und Druckkriterien trotz Betrieb. Ein bestätigter kleiner betroffener Teilstrom widerlegt dagegen die Notwendigkeit der großen Referenzanlage.

Beleg: `docs/alternativenvergleich.md`, Folien 8 und 9.

### 17. Ist die Umsetzung in einem Schutzgebiet genehmigt?

Nein, eine Genehmigung wird nicht behauptet. Entnahme und Rückführung sind wasserrechtlich zu prüfen, außerdem FFH- und Artenschutz. Die Anlage liegt außerhalb des Beckens und vermeidet Tiefbohrungen im Karst. Erst Feldversuche und die zuständige Behörde können die Umsetzbarkeit bestätigen.

Beleg: WHG [14], Stadt Blaubeuren [15]. Diese Einschränkung ist eine menschliche Restaufgabe, kein behaupteter Erledigungsvermerk.

### 18. Warum soll eine synthetische Präsentation finaltauglich sein?

Das Paket enthält echte Folien, ein echtes Video, gemessene Audiodauer und dokumentierte Fragen. Es behauptet keine menschliche Live-Darbietung. Vor dem Finale müssen die Teilnehmenden Rechte, Vertonung, Rollen und ihre eigene Live-Probe freigeben. Der synthetische Slidecast ist eine fertige Alternative, kein Ersatznachweis für menschliche Proben.

Beleg: `presentation/timings.json`, `presentation/rehearsal.md`, `output/presentation/verification.json`.

### 19. Entspricht das Layout nicht D4RT nur oberflächlich?

Der Vergleich betrifft gezielt messbare Gestaltungsmerkmale: Zweispaltigkeit, Times-Hierarchie, Tabellenlinien, Bildunterschriften und numerische Verweise. Abweichende Vorgaben bleiben übergeordnet. Der Bericht verwendet A4, mindestens 25 mm Rand und 12 pt statt D4RTs Letterformat und kleineren Schriftgraden.

Beleg: `compliance/layout_referenz.md`, gerenderter Bericht.

### 20. Welche Arbeit bleibt trotz Council-Konsens menschlich?

Berechtigte Teammitglieder müssen Annahmen und Quellen prüfen, die offizielle Team-ID einsetzen, Feld- und Behördenkontakte klären, Medienrechte freigeben, die Finalisten-E-Mail lesen und ihre eigene Darbietung proben. Der Council bewertet nur interne Bereitschaft. Er garantiert keine Jury punkte oder Qualifikation.

Beleg: `PROVENANCE.md`, `README.md`, `review/README.md`.
