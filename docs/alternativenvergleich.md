# Quantitativer Alternativenvergleich

## Einheitliche Auslegungsbasis

Der erwartete betroffene Quellstrom beträgt 2,3 m³/s. Für die thermische Kapazität wird das historische 90-Prozent-Quantil von 4,7 m³/s mit 20 % Reserve gewählt. Diese Risikovorgabe ist kein Extremwertnachweis. Alle Varianten müssen im zehnten Jahr von 100 °C auf 9 °C kühlen und die Temperatur danach halten. Der erwartete Wärmeentzug beträgt 877,8 MW, der p90-Bedarf 1793,7 MW. Die Rechnung verwendet 999,702 kg/m³ und 4195,14 J/(kg K) aus der NIST-Tabelle bei etwa 10 °C. Konstante Stoffwerte sind eine Näherung.

Für Netz, Ersatzstrom und die Luftsenke wird zusätzlich der ungünstigste deklarierte COP von 3,0 angesetzt. Dadurch werden elektrische Leistung und Wärmeabgabe nicht nur am Erwartungs-COP 4,0 bemessen. Die Betriebskosten verwenden weiterhin den Erwartungs-COP.

Alle Geldbeträge sind Szenarioschätzungen in Euro von 2026, keine Angebote. Die HAW-Arbeit nennt in Tabelle 5.6 für Kompressionskältemaschinen Bereiche von 75 bis 125, 125 bis 350 sowie 185 bis 236 €/kW [19]. Der Modellwert von 500 €/kW liegt bewusst darüber. Trockenkühlung mit 120 €/kW und Verdunstung mit 80 €/kW sind eigene Szenariowerte, keine HAW-Beschaffungsangebote. Auf alle drei Werte wird ein pauschaler Aufschlag von 30 % angesetzt, ohne amtlichen Baupreisindex zu unterstellen. Der Barwert umfasst 25 Jahre, 3 % Diskontsatz, Investitionen, p90-Kapazität und 20 % Reserve, Wartung, Ersatz, Strom und soweit anwendbar Wasser und Hygiene. Die Werte stammen aus `output/model/results.json`. Jahresreihen stehen in `output/model/hybrid_schedule.csv` und `design_schedule`.

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
| Wärmeabgabe an Luft | 967,2 MW | 957,4 MW | 0,0 MW |
| Investition mit p90-Reserve | 1595,1 Mio. € | 1364,1 Mio. € | 145,3 Mio. € |
| Elektrische Leistung im Erwartungsfall | 89,4 MW | 79,6 MW | 12,8 MW |
| Strom pro Jahr | 783,0 GWh | 697,2 GWh | 112,4 GWh |
| Wasserbedarf pro Jahr | 0 m³ | 12,48 Mio. m³ | 1650 Mio. m³ |
| Betriebskosten im zehnten Jahr | 155,9 Mio. € | 143,9 Mio. € | 844,9 Mio. € |
| Barwert über 25 Jahre | 4,136 Mrd. € | 3,722 Mrd. € | 11,452 Mrd. € |

Die Kapazität wird mit p90 bemessen, der Verbrauch mit dem erwarteten Abfluss. Ein dauerhafter p90-Betrieb kostet H1 268,7 Mio. € im zehnten Jahr und 5,919 Mrd. € über 25 Jahre. Diese beiden Betrachtungen dürfen nicht vermischt werden. Für die Unsicherheit wird dieselbe p90-Anlage mit Reserve verwendet; nur Betrieb und expliziter Investitionsfaktor variieren.

H1 verteilt den Wärmeentzug auf 578,8 MW direkte Trockenkühlung und 299,0 MW Kältemaschinen. Die Kondensatoren geben 373,8 MW ab. Zusammen mit Hilfsantrieben müssen 967,2 MW an die Umgebung abgegeben werden. Im Randfall mit p90-Abfluss und COP 3,0 sind 234,3 MW Antriebsleistung und 2028,1 MW Wärmeabgabe erforderlich.

Für die Luftsenke werden 2 m/s Face-Geschwindigkeit und 15 K Lufterwärmung angesetzt. Im Randfall folgen 56.055 m² Face-Fläche, 8,41 ha Betriebs- und Servicefläche und 112.110 m³/s Luftvolumenstrom. Diese Werte sind Bilanzannahmen, keine Standort- oder Herstellernachweise. Die Stromemissionen betragen im Erwartungsjahr 284,2 Kilotonnen CO₂ gegenüber 253,1 Kilotonnen bei H2, nach dem UBA-Faktor 363 g/kWh für 2024 [23].

H2 kühlt den Quellstrom im Gegenstrom von 100 auf 36 °C. Der separate Sekundärkreislauf wird dabei von 32 auf 96 °C erwärmt. Am heißen Ende beträgt der Abstand 100 - 96 = 4 K, am kalten Ende 36 - 32 = 4 K. Der Sekundärstrom von 2,3 m³/s hat im Modell denselben Wärmekapazitätsstrom wie der Quellstrom, mit temperaturabhängigen Stoffwerten nur näherungsweise. Die Verdunstung übernimmt 617,3 MW, eine Kältemaschine weitere 260,4 MW bis 9 °C. Der Quellstrom bleibt geschlossen und wird vollständig weitergekühlt, der Dampfstrom gehört zum Sekundärkreislauf und nicht zum Quellabfluss. Der Dampfstrom beträgt 263,7 kg/s, die jährliche Verdunstungsmenge 8,32 Mio. m³. Mit drei Konzentrationszyklen kommen 4,16 Mio. m³ Abschlämmung und 0,02 % Drift hinzu. Der Zusatzwasserbedarf beträgt 12,48 Mio. m³ pro Jahr oder 17,2 % des erwarteten Quellstroms. Bei drei Zyklen sind es 12,48 Mio. m³, bei fünf Zyklen 10,40 Mio. m³. Diese Annahmen ersetzen keine Wasserchemie- oder Herstellerdaten. Die Verdampfungsenthalpie wird mit 2340,730 kJ/kg als Mittel der NIST-Werte 2425,056 kJ/kg bei 32 °C und 2256,404 kJ/kg bei 100 °C angesetzt [4]. Die Quellkühlung ist physikalisch gleichwertig, der separate Nasskühlturm ist nicht ausgelegt. H2 verursacht Wasserverlust, Hygieneaufwand und Aerosolrisiken nach der 42. BImSchV. Die Kosten und der Barwert verwenden den vollständigen Zusatzwasserbedarf. H1 verursacht mehr Stromemissionen. Die Wahl ist ein Zielkonflikt, kein pauschaler Vorteil einer Variante in jeder Umweltkategorie.

H8 wurde nach dem Council-Befund als wärmegetriebene Variante ergänzt. Die einstufige Absorptionsstufe verwendet Heißwasser von 96 auf 82 °C und einen thermischen COP von 0,70 im HAW-Bereich 0,6 bis 0,8 [19]. Der Quellstrom kühlt sich im Gegenstrom von 100 auf 86 °C ab, beide Endabstände betragen 4 K. Die Generatorwärme beträgt 135,0 MW, die Verdampferkälte 94,5 MW und die Absorptionsabwärme 229,6 MW. Der Sekundärstrom beträgt 2,3 m³/s. Nach dem Verdampfer verbleiben 76,2 °C. Trockenkühler liefern 349,2 MW und die nachfolgende Kompressionsstufe weiterhin 299,0 MW mit 373,8 MW Kondensatorwärme.

Der Hilfsstrom beträgt 5,56 % der Verdampferleistung nach dem HAW-Beispiel 3/54 kW. Im Erwartungsbetrieb sind es 94,6 MW elektrische Leistung und 972,4 MW Wärmeabgabe, im Min-COP-Auslegungsfall 245,1 MW und 2038,8 MW. Acht Aggregate plus Reserve und 3,001 Mio. Liter Diesel sind erforderlich. Der Wert 250 €/kW ist ein eigener günstiger Screeningwert innerhalb der HAW-Spanne 80 bis 1800 €/kW und wird um 30 % erhöht. Damit betragen Investition und Barwert 1716,0 Mio. € und 4,346 Mrd. €. Selbst eine kostenlose Absorptionsmaschine ließe den Barwert bei 4,200 Mrd. € und damit über H1. Die Emissionen steigen auf 300,9 kt CO₂ pro Jahr. Thermische COP-Werte bis 1,3 senken den Quellstrom nicht unter 40 °C; die reversible Obergrenze 1,793 ergibt 60,9 °C. H8 ersetzt damit Trockenkühlung statt Kompressionskälte und ist in allen 10.000 gekoppelten Ziehungen teurer. Es wird nicht gewählt. Diese Begrenzung gilt für die dokumentierte Temperaturführung, nicht als allgemeiner Ausschluss anderer wärmegetriebener Maschinen.

H3 verlangt bei 5 °C kaltem Zusatzwasser 52,3 m³/s. Das ist das 22,75-fache des mittleren Quellstroms. Eine ganzjährig kalte und ökologisch verträgliche Reserve ist nicht belegt. Die Wasserkosten dominieren den Barwert. H3 scheidet trotz einfacher Technik aus. Es enthält als variable Ausrüstung nur Pumpen und keinen Notstromposten; die 95 Mio. € für Tiefbau und Steuerung bleiben als Fixkostenbasis erhalten.

## Verworfene Ansätze

| Ansatz | Quantitativer oder physikalischer Befund | Entscheidung |
| --- | --- | --- |
| H4 Geologische Wärmeabschirmung oder Wärmeentnahme im Karst | Dieselbe Wärmemenge müsste im Gestein erfasst werden. Zwei Karstäste und unterschiedliche Fließgeschwindigkeiten verhindern eine belastbare Erfassungsgarantie ohne Feldversuche. | Forschungsoption, erst Tracer, Druck- und Temperaturmessungen können sie tragen. |
| H5 Bypass am Blautopf vorbei | Schützt allenfalls die Blau. Das verbleibende Becken erhält weiterhin Wärme. | Als alleinige Antwort abgelehnt. |
| H6 Druckbeaufschlagung | Höherer Druck verschiebt nur den Siedepunkt, entzieht aber keine Wärme und verschärft die ökologische Belastung. | Aus Prinzip abgelehnt. |
| H7 Passive Wärmerohre und Strahlungskühlung | Bei 10 W/(m² K) und 20 K treibender Differenz wären 4,39 km² aktive Fläche nötig. Bei 35 °C Luft kann ein passiver Kühlkörper nicht auf 9 °C kühlen. | Allenfalls Hilfskühlung in kalten Perioden. |

## Auswahl, Reserve und dynamischer Nachweis

H1 ist die günstigste geprüfte Variante ohne zusätzlichen Wasserverbrauch und ohne offenes Verdunstungssystem. Der höhere Strom- und Kapitalaufwand ist der Preis für geschlossene Wasserführung und trockene Wärmeabgabe. Der reine Siedeschutz auf 94,97 °C benötigt beim Mittelstrom nur 48,5 MW Kühlleistung und 1,07 MW Antriebsleistung. Er kostet 111,4 Mio. € Investition und 0,177 Mrd. € Barwert, wahrt aber nicht das Ökosystem und wird nicht als Normalzustand gewählt. Der Siedeschutz ist auf den Erwartungsstrom von 2,3 m³/s ausgelegt, H1 auf 4,7 m³/s. Diese Auslegungsbasen sind nicht direkt gleichwertig, eine p90-Variante wird nicht kostengleich verglichen. Die Schutzmarke verwendet Standarddruck, der lokale Luftdruck ist noch zu messen. Sein Notstromposten wird mit der elektrischen Leistung dieser kleinen Variante statt mit der vollen Referenzanlage skaliert.

Der Endausbau besitzt zwölf Stränge mit je 179,4 MW installierter Leistung, zusammen 2152,5 MW. Im p90-Fall liefern elf davon je 163,1 MW bei etwa 91 % Auslastung, einer ist Reserve. Im Mittelbetrieb modulieren fünf. Jede Ausbaustufe muss ihre Reserve vor dem Lastjahr prüfen. Der Stufenplan spart 241 Mio. € Barwert gegenüber sofortigem Endausbau, darf aber keine Sicherheitsstufe verzögern.

Ein Puffer von 8280 m³ entspricht einer Stunde Erwartungsstrom und erzwingt keine Temperaturrampe. Die geplante Inbetriebnahme senkt den Kälteauslass mit höchstens 1 K/h. Der Stresstest von 100 auf 9 °C dauert 91 Stunden und ist kein Wiederanlauf- oder Notfallnachweis. Sensoren stoppen die Rampe bei Überschreitung am Kontrollpunkt.

Ohne Kühlung erreicht das Beckenmodell im Mittelstrom nach 23,34 Minuten 20 °C, im p90-Fall bereits nach 11,42 Minuten. Nach 0,5 min Detektion vergehen 5 min bis zum Generatorstart und weitere 5 min bis zur vollen Kühlleistung, also absolute Zeitpunkte 5,5 und 10,5 Minuten nach dem Ausfall. Die 15-min-USV hat damit 4,5 min Reserve. Der Höchstwert beträgt 12,88 °C im Mittelstrom und 16,66 °C im p90-Fall. Die Differenz zwischen ungekühlter 20-°C-Zeit und voller Kühlleistung beträgt 12,84 beziehungsweise 0,92 Minuten. Sie ist keine freie Wartezeit. Bei nur 10.000 m³ effektivem Volumen liegt der Höchstwert trotz Wiederanlauf bei 26,43 °C und die Differenz bei -5,93 Minuten, die Alarmschwelle wird also verfehlt. Bei 50.000 m³ beträgt sie 12,34 Minuten. Zwei Toleranz- und Zeitschrittstufen bestätigen den p90-Verlauf. Sieben Aggregate mit je 35 MW sind für 234,3 MW im Randfall erforderlich, das achte ist Reserve. Für 48 Stunden ergibt sich bei 40 % Wirkungsgrad und 9,8 kWh/L ein Dieselvorrat von 2,869 Mio. Litern, also 2.869 m³. Diese Werte sind Szenarioannahmen, keine Hersteller- oder Zuschaltnachweise.

## Standort und Falsifikation

Das Standort-Screening verlangt 8,41 ha, zweimal 234,3 MW unabhängig nutzbare Netzleistung und 2.869 m³ Diesellager. Luftführung, Rückverwirbelung, Schall und Plume sind zu untersuchen. Die Rückhaltung und Leckkontrolle folgt der AwSV [25]. Wasserrecht und FFH-Vorprüfung nach § 34 BNatSchG bleiben Zulassungsbedingungen [14,15,24]. Ein geeigneter Standort ist nicht nachgewiesen.

Dauerhaft bedeutet unbegrenzter Betrieb mit Wartung innerhalb der Hülle: höchstens 4,7 m³/s betroffener Volumenstrom, höchstens 100 °C am tiefen Zufluss, nachgewiesene Erfassung und externe Wärmesenke. Für 32,7 m³/s wären 12,48 GW für 9 °C erforderlich. Dieser Fall ist nicht abgedeckt. Eine endliche Anlage kann keine unbegrenzt wachsende Wärmezufuhr beherrschen.

Bei der alten Auslegung nur auf den Mittelstrom übersteigt der erforderliche Wärmestrom in 38,57 % der vorhandenen 10.000 Ziehungen die 9-°C-Kapazität. Die p90-Reserve deckt die begrenzte Verteilung vollständig ab. Auch elektrische Leistung und Wärmeabgabe werden separat am minimalen COP begrenzt; die Überlastanteile liegen bei null. Das ist keine Garantie für Extremhochwasser oder andere Wärmequellen. Jede Ziehung verwendet dieselbe p90-Anlage; Abfluss und COP verändern den Betrieb, der Investitionsfaktor verändert die Investition. Auch ein Tarifwechsel von 138 auf 179 €/MWh erhöht den Barwert von 4,136 auf 4,644 Mrd. €. Bei 95 % Netzverfügbarkeit steigt er mit vollständigem Dieselersatz auf 4,288 Mrd. €. Diese Kostensensitivität verwendet die Erwartungslast von 89,4 MW und erfordert 9,99 Mio. Liter Diesel bei unbegrenzter Verfügbarkeit. Der 48-Stunden-Vorrat von 2,869 Mio. Litern ist dagegen für die Auslegungslast von 234,3 MW bemessen. Unbegrenzte Dieselverfügbarkeit ist keine Lagerplanung.

Die Auslegung ist zu verwerfen oder zu vergrößern, wenn Tracer- und Durchflussmessungen einen größeren betroffenen Strom zeigen, die Temperatur nach Jahr zehn weiter ansteigt oder Hochwasser die Anomalie trägt. Sie darf verkleinert werden, wenn nur ein begrenzter Karstast betroffen ist. Jede Überschreitung der Siedemarge, jedes Nichterreichen des 9-°C-Ziels, jede Überschreitung von 1 K/h und jede Rückströmung der Abwärme in denselben Wasserkreislauf falsifiziert den Erfolg.
