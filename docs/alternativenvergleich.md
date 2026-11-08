# Quantitativer Alternativenvergleich

## Einheitliche Auslegungsbasis

Der erwartete betroffene Quellstrom beträgt 2,3 m³/s. Für die Kapazität wird das historische 90-Prozent-Quantil von 4,7 m³/s mit 20 % Reserve gewählt. Diese Risikovorgabe ist kein Extremwertnachweis. Alle Varianten müssen im zehnten Jahr von 100 °C auf 9 °C kühlen und die Temperatur danach halten. Der erwartete Wärmeentzug beträgt 877,8 MW, der p90-Bedarf 1793,7 MW. Die Rechnung verwendet 999,702 kg/m³ und 4195,14 J/(kg K) aus der NIST-Tabelle bei etwa 10 °C. Konstante Stoffwerte sind eine Näherung.

Alle Geldbeträge sind Szenarioschätzungen in Euro von 2026, keine Angebote. Der Barwert umfasst 25 Jahre, 3 % Diskontsatz, Investitionen, p90-Kapazität und 20 % Reserve, Wartung, Ersatz, Strom und soweit anwendbar Wasser und Hygiene. Die Werte stammen aus `output/model/results.json`. Jahresreihen stehen in `output/model/hybrid_schedule.csv` und `design_schedule`.

## Physikalische und ökologische Auswahlkriterien

1. Der Ansatz muss die gesamte Wärmebilanz schließen. Eine Verschiebung des Siedepunkts oder eine Umleitung am Becken vorbei genügt nicht.
2. Auch bei sommerlicher Auslegungsluft muss 9 °C erreichbar sein. Passive Wärmeabgabe an 35 °C Luft genügt dafür nicht.
3. Die Wärme inklusive Kondensator- und Hilfsenergie muss außerhalb des verbundenen Grund- und Oberflächenwassers bleiben.
4. Fehlende Wasserquellen, Standortnachweise oder Wirkungsnachweise werden nicht als Dauerzusage dargestellt.
5. Erst danach entscheiden Kosten und Umsetzbarkeit. Der Normalzustand um 9 °C wird vom reinen Siedeschutz getrennt.

## Rechnerisch dimensionierte Varianten

| Größe im zehnten Jahr | H1 Trockene Hybridkühlung | H2 Verdunstung mit Kältestufe | H3 Kaltwasserzumischung |
| --- | ---: | ---: | ---: |
| Wärmeentzug | 877,8 MW | 877,8 MW | 877,8 MW |
| Wärmeabgabe an Luft | 967,2 MW | 947,6 MW | 0,0 MW |
| Investition mit p90-Reserve | 1283,1 Mio. € | 1018,5 Mio. € | 145,3 Mio. € |
| Elektrische Leistung im Erwartungsfall | 89,4 MW | 69,8 MW | 12,8 MW |
| Strom pro Jahr | 783,0 GWh | 611,5 GWh | 112,4 GWh |
| Wasserbedarf pro Jahr | 0 m³ | 8,84 Mio. m³ | 1650 Mio. m³ |
| Betriebskosten im zehnten Jahr | 146,5 Mio. € | 119,9 Mio. € | 844,9 Mio. € |
| Barwert über 25 Jahre | 3,663 Mrd. € | 2,985 Mrd. € | 11,452 Mrd. € |

Die Kapazität wird mit p90 bemessen, der Verbrauch mit dem erwarteten Abfluss. Ein dauerhafter p90-Betrieb kostet H1 259,3 Mio. € im zehnten Jahr und 5,446 Mrd. € über 25 Jahre. Diese beiden Betrachtungen dürfen nicht vermischt werden. Für die Unsicherheit wird dieselbe p90-Anlage mit Reserve verwendet; nur Betrieb und expliziter Investitionsfaktor variieren.

H1 verteilt den Wärmeentzug auf 578,8 MW direkte Trockenkühlung und 299,0 MW Kältemaschinen. Die Kondensatoren geben 373,8 MW ab. Zusammen mit Hilfsantrieben müssen 967,2 MW an die Umgebung abgegeben werden. Im p90-Spitzenfall sind 182,7 MW Antriebsleistung und 1976,4 MW Wärmeabgabe angesetzt.

Für die Luftsenke werden 2 m/s Face-Geschwindigkeit und 15 K Lufterwärmung angesetzt. Im p90-Fall folgen 54.626 m² Face-Fläche, 8,19 ha Betriebs- und Servicefläche und 109.253 m³/s Luftvolumenstrom. Diese Werte sind Bilanzannahmen, keine Standort- oder Herstellernachweise. Die Stromemissionen betragen im Erwartungsjahr 284,2 Kilotonnen CO₂ gegenüber 222,0 Kilotonnen bei H2, nach dem UBA-Faktor 363 g/kWh für 2024 [23].

H2 nutzt im Szenario 28 °C Feuchtkugeltemperatur und 4 K Annäherung. Verdunstung kühlt von 100 auf 32 °C mit 655,9 MW. Eine Kältemaschine übernimmt 221,9 MW bis 9 °C. Die Verdunstung findet in einem separaten Sekundärkreislauf statt. Der Quellstrom bleibt geschlossen und wird nach dieser Stufe vollständig weitergekühlt, der Dampfstrom gehört nicht zum Quellabfluss. Der Dampfstrom beträgt 280,2 kg/s, der jährliche Ersatzwasserbedarf 8,84 Mio. m³. Die Verdampfungsenthalpie wird mit 2340,730 kJ/kg als Mittel der NIST-Werte 2425,056 kJ/kg bei 32 °C und 2256,404 kJ/kg bei 100 °C angesetzt [4]. Damit ist H2 physikalisch gleichwertig, verursacht aber Wasserverlust, Hygieneaufwand und Aerosolrisiken nach der 42. BImSchV. H1 verursacht mehr Stromemissionen. Die Wahl ist ein Zielkonflikt, kein pauschaler Vorteil einer Variante in jeder Umweltkategorie.

H3 verlangt bei 5 °C kaltem Zusatzwasser 52,3 m³/s. Das ist das 22,75-fache des mittleren Quellstroms. Eine ganzjährig kalte und ökologisch verträgliche Reserve ist nicht belegt. Die Wasserkosten dominieren den Barwert. H3 scheidet trotz einfacher Technik aus und wird als reine Pumpen- und Wasserkostenschätzung ohne Notstromposten ausgewiesen.

## Verworfene Ansätze

| Ansatz | Quantitativer oder physikalischer Befund | Entscheidung |
| --- | --- | --- |
| H4 Geologische Wärmeabschirmung oder Wärmeentnahme im Karst | Dieselbe Wärmemenge müsste im Gestein erfasst werden. Zwei Karstäste und unterschiedliche Fließgeschwindigkeiten verhindern eine belastbare Erfassungsgarantie ohne Feldversuche. | Forschungsoption, erst Tracer, Druck- und Temperaturmessungen können sie tragen. |
| H5 Bypass am Blautopf vorbei | Schützt allenfalls die Blau. Das verbleibende Becken erhält weiterhin Wärme. | Als alleinige Antwort abgelehnt. |
| H6 Druckbeaufschlagung | Höherer Druck verschiebt nur den Siedepunkt, entzieht aber keine Wärme und verschärft die ökologische Belastung. | Aus Prinzip abgelehnt. |
| H7 Passive Wärmerohre und Strahlungskühlung | Bei 10 W/(m² K) und 20 K treibender Differenz wären 4,39 km² aktive Fläche nötig. Bei 35 °C Luft kann ein passiver Kühlkörper nicht auf 9 °C kühlen. | Allenfalls Hilfskühlung in kalten Perioden. |

## Auswahl, Reserve und dynamischer Nachweis

H1 ist die günstigste geprüfte Variante ohne zusätzlichen Wasserverbrauch und ohne offenes Verdunstungssystem. Der höhere Strom- und Kapitalaufwand ist der Preis für geschlossene Wasserführung und trockene Wärmeabgabe. Der reine Siedeschutz auf 94,97 °C benötigt beim Mittelstrom nur 48,5 MW Kühlleistung und 1,07 MW Antriebsleistung. Er kostet 108,2 Mio. € Investition und 0,173 Mrd. € Barwert, wahrt aber nicht das Ökosystem und wird nicht als Normalzustand gewählt. Sein Notstromposten wird mit der elektrischen Leistung dieser kleinen Variante statt mit der vollen Referenzanlage skaliert.

Der Endausbau besitzt zwölf Stränge mit je 179,4 MW installierter Leistung, zusammen 2152,5 MW. Im p90-Fall liefern elf davon je 163,1 MW bei etwa 91 % Auslastung, einer ist Reserve. Im Mittelbetrieb modulieren fünf. Jede Ausbaustufe muss ihre Reserve vor dem Lastjahr prüfen. Der Stufenplan spart 189 Mio. € Barwert gegenüber sofortigem Endausbau, darf aber keine Sicherheitsstufe verzögern.

Ein Puffer von 8280 m³ entspricht einer Stunde Erwartungsstrom und erzwingt keine Temperaturrampe. Die geplante Inbetriebnahme senkt den Kälteauslass mit höchstens 1 K/h. Der Stresstest von 100 auf 9 °C dauert 91 Stunden und ist kein Wiederanlauf- oder Notfallnachweis. Sensoren stoppen die Rampe bei Überschreitung am Kontrollpunkt.

Ohne Kühlung erreicht das Beckenmodell im Mittelstrom nach 23,34 Minuten 20 °C, im p90-Fall bereits nach 11,42 Minuten. Die Detektion dauert 0,5 min. Danach folgen 5 min Generatorstart und 10 min bis voller Kühlleistung, also absolute Zeitpunkte 5,5 und 10,5 Minuten nach dem Ausfall. Der Höchstwert beträgt 12,88 °C im Mittelstrom und 16,66 °C im p90-Fall. Die Differenz zwischen ungekühlter 20-°C-Zeit und voller Kühlleistung beträgt 12,84 beziehungsweise 0,92 Minuten. Sie ist keine freie Wartezeit. Zwei Toleranz- und Zeitschrittstufen bestätigen den p90-Verlauf. Sechs Aggregate liefern die p90-Leistung, ein siebtes ist Reserve. Für 48 Stunden ergibt sich bei 40 % Wirkungsgrad und 9,8 kWh/L ein Dieselvorrat von 2,237 Mio. Litern, also 2.237 m³. Diese Werte sind Szenarioannahmen, keine Hersteller- oder Zuschaltnachweise.

## Standort und Falsifikation

Das Standort-Screening verlangt 8,19 ha, zweimal 182,7 MW unabhängig nutzbare Netzleistung und 2.237 m³ Diesellager. Luftführung, Rückverwirbelung, Schall und Plume sind zu untersuchen. Die Rückhaltung und Leckkontrolle folgt der AwSV [25]. Wasserrecht und FFH-Vorprüfung nach § 34 BNatSchG bleiben Zulassungsbedingungen [14,15,24]. Ein geeigneter Standort ist nicht nachgewiesen.

Dauerhaft bedeutet unbegrenzter Betrieb mit Wartung innerhalb der Hülle: höchstens 4,7 m³/s betroffener Volumenstrom, höchstens 100 °C am tiefen Zufluss, nachgewiesene Erfassung und externe Wärmesenke. Für 32,7 m³/s wären 12,48 GW für 9 °C erforderlich. Dieser Fall ist nicht abgedeckt. Eine endliche Anlage kann keine unbegrenzt wachsende Wärmezufuhr beherrschen.

Bei der alten Auslegung nur auf den Mittelstrom übersteigt der erforderliche Wärmestrom in 38,57 % der vorhandenen 10.000 Ziehungen die 9-°C-Kapazität. Die p90-Reserve deckt die begrenzte Verteilung vollständig ab. Das ist keine Garantie für Extremhochwasser oder andere Wärmequellen. Jede Ziehung verwendet dieselbe p90-Anlage; Abfluss und COP verändern den Betrieb, der Investitionsfaktor verändert die Investition. Auch ein Tarifwechsel von 138 auf 179 €/MWh erhöht den Barwert von 3,663 auf 4,171 Mrd. €. Bei 95 % Netzverfügbarkeit steigt er mit vollständigem Dieselersatz auf 3,815 Mrd. €.

Die Auslegung ist zu verwerfen oder zu vergrößern, wenn Tracer- und Durchflussmessungen einen größeren betroffenen Strom zeigen, die Temperatur nach Jahr zehn weiter ansteigt oder Hochwasser die Anomalie trägt. Sie darf verkleinert werden, wenn nur ein begrenzter Karstast betroffen ist. Jede Überschreitung der Siedemarge, jedes Nichterreichen des 9-°C-Ziels, jede Überschreitung von 1 K/h und jede Rückströmung der Abwärme in denselben Wasserkreislauf falsifiziert den Erfolg.
