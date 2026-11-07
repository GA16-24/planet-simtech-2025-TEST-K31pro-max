# Quantitativer Alternativenvergleich

## Einheitliche Auslegungsbasis

Alle Varianten müssen den mittleren betroffenen Quellstrom von 2,3 m³/s im zehnten Jahr von 100 °C auf 9 °C bringen und diese Temperatur danach halten. Die erforderliche Wärmeabfuhr beträgt 877,8 MW. Die Rechnung verwendet 999,702 kg/m³ und 4195,14 J/(kg K) aus der NIST-Tabelle bei etwa 10 °C. Der konstante Stoffwert ist eine Näherung über den Temperaturpfad. Die Unsicherheit des Wärmeeintrags ist wesentlich größer.

Alle Geldbeträge sind Szenario-Schätzungen in Euro von 2026, keine Angebote. Der Barwert umfasst 25 Jahre, 3 % Diskontsatz, Investitionen, 20 % Reserve, Wartung, Ersatz, Strom und soweit anwendbar Wasser und Hygiene. Die Investitions- und Betriebskosten stammen aus `output/model/results.json`. Die vollständigen Jahresreihen stehen in `output/model/hybrid_schedule.csv`.

## Harte Auswahlkriterien vor der Wirtschaftlichkeit

1. Der Ansatz muss die gesamte Wärmebilanz schließen. Eine bloße Verschiebung des Siedepunkts oder eine Umleitung am Becken vorbei genügt nicht.
2. Die Kühlung muss auch bei sommerlicher Auslegungsluft von 35 °C auf 9 °C wirken. Passive Wärmeabgabe an diese Luft ist dafür nicht ausreichend.
3. Die Wärme senke muss außerhalb des verbundenen Grund- und Oberflächenwassers liegen. Rückkehr der Kondensatorwärme in denselben Kreislauf würde die Bilanz aufheben.
4. Ein Ansatz ohne belastbare Wasserquelle, Standort- oder Wirkungsnachweise wird nicht als Dauerlösung dargestellt.
5. Erst nach diesen physikalischen und ökologischen Filtern entscheiden Kosten und Umsetzbarkeit.

## Vergleich der rechnerisch dimensionierten Varianten

| Größe im zehnten Jahr | H1 Hybride Vollstromkühlung | H2 Geschlossene Verdunstungskühlung | H3 Kaltwasserzumischung |
| --- | ---: | ---: | ---: |
| Wärmeabfuhr | 877,8 MW | 877,8 MW | 877,8 MW |
| Investition einschließlich Reserve | 719 Mio. € | 284 Mio. € | 120 Mio. € |
| Strombedarf | 74,2 MW | 13,5 MW | 12,8 MW |
| Strom pro Jahr | 650 GWh | 118 GWh | 112 GWh |
| Wasserbedarf pro Jahr | 0 m³ | 11,30 Mio. m³ | 1650 Mio. m³ |
| Betriebskosten im zehnten Jahr | 137,9 Mio. € | 35,8 Mio. € | 848,8 Mio. € |
| Barwert über 25 Jahre | 2,90 Mrd. € | 0,78 Mrd. € | 11,48 Mrd. € |

H1 verteilt die Wärmeabfuhr auf 578,8 MW direkte Trockenkühlung und 299,0 MW Kältemaschinen. Die Kondensatoren geben 358,8 MW ab. Zusammen mit Hilfsantrieben müssen die Luftkühler und Kondensatoren 952,0 MW an die Umgebung abgeben. Diese Summe entspricht der entzogenen Wärme plus sämtlicher elektrischer Antriebsleistung.

H2 ist die günstigste physikalisch wirksame Variante. Sie verdunstet jedoch 358 kg/s beziehungsweise 15,6 % des mittleren Quellstroms. Die fehlende Wassermenge wirkt direkt auf die Blau. Hinzu kommen Aerosol- und Legionellenrisiken, die Kontroll-, Labor-, Protokoll- und Prüfpflichten der 42. BImSchV sowie Schaum- und Sichtwirkungen an einem touristisch sichtbaren Ort. H2 bleibt als Notfall- oder Spitzenlastoption denkbar, ist aber nicht die bevorzugte Dauerlösung.

H3 verlangt bei 5 °C kaltem Zusatzwasser 52,3 m³/s. Das ist das 22,75-fache des natürlichen mittleren Quellstroms. Eine solche ganzjährig kalte und ökologisch verträgliche Reserve ist nicht belegt. Die Wasserkosten dominieren den Barwert. H3 scheidet trotz einfacher Technik aus.

## Nicht dimensionierbare oder physikalisch unzureichende Ansätze

| Ansatz | Quantitativer oder physikalischer Befund | Entscheidung |
| --- | --- | --- |
| H4 Geologische Wärmeabschirmung oder Wärmeentnahme im Karst | Dieselbe Wärmemenge müsste im Gestein erfasst werden. Zwei Karstäste, unbekannte Gesamtlänge und stark unterschiedliche Fließgeschwindigkeiten verhindern eine belastbare Erfassungsgarantie ohne Feldversuche. | Forschungsoption, keine aktuelle Dauerlösung. Erst Tracer, Druck- und Temperaturmessungen können sie falsifizieren oder tragen. |
| H5 Bypass am Blautopf vorbei | Schützt allenfalls die Blau. Das verbleibende Becken erhält weiterhin Wärme. Die geschlossene Beckenbilanz fehlt. | Als alleinige Antwort abgelehnt. |
| H6 Druckbeaufschlagung | Der hydrostatische Siedepunkt in 22 m Tiefe liegt bei etwa 135,4 °C. Höherer Druck verschiebt nur die Schwelle, entzieht aber keine Wärme und verschärft die ökologische Belastung. | Aus Prinzip abgelehnt. |
| H7 Passive Wärmerohre und Strahlungskühlung | Bei 10 W/(m² K) und 20 K treibender Differenz wären 4,39 km² aktive Fläche nötig. Bei 35 °C Luft kann ein passiver Kühlkörper nicht auf 9 °C kühlen. | Allenfalls Hilfskühlung in kalten Perioden, keine Hauptlösung. |

## Auswahl und Reserve

H1 ist die kostengünstigste der geprüften Varianten, die ohne zusätzlichen Wasserverbrauch und ohne offenes Verdunstungssystem den Normalzustand dauerhaft halten kann. Der höhere Strom- und Kapitalaufwand ist der Preis für den Erhalt des Wasserhaushalts und die geringere hygienische und ökologische Belastung.

Der Referenzentwurf hat sechs Module. Fünf Module zu je 175,6 MW decken die Last, das sechste bildet die Reserve. Jedes betriebsbereite Modul führt etwa 0,46 m³/s. Bei 1,2 m/s ergibt sich ein rechnerischer Rohrdurchmesser von 0,70 m. Ein 8280 m³ großer Misch- und Pufferspeicher entspricht einer Stunde mittleren Quellstroms. Dort wird die Rückführung so geregelt, dass die Temperaturänderung am ökologischen Kontrollpunkt 1 K/h nicht überschreitet.

Die Trockenkühler arbeiten bei heißem Quellwasser zuerst. Kältemaschinen senken danach die Temperatur auf 9 °C. Die Leistung wird erst mit gemessener Temperatur und erfasstem Durchfluss ausgebaut. Gegenüber dem sofortigen Bau der Endstufe spart dieser Stufenplan im Modell 112 Mio. € Barwert. Die Einsparung ist keine Freigabe für verzögerten Sicherheitsbau. Jedes Modul muss vor dem prognostizierten Lastjahr betriebsbereit und getestet sein.

## Sensitivität des Anlagenmaßstabs

| Erfasster Anteil des mittleren Quellstroms | Kühlleistung | Strombedarf | Investition | Barwert 25 Jahre |
| --- | ---: | ---: | ---: | ---: |
| 100 % | 877,8 MW | 74,2 MW | 719 Mio. € | 2,90 Mrd. € |
| 10 % | 87,8 MW | 7,4 MW | 85 Mio. € | 0,31 Mrd. € |
| 1 % | 8,8 MW | 0,74 MW | 12 Mio. € | 0,036 Mrd. € |
| 0,1 % | 0,88 MW | 0,074 MW | 2,0 Mio. € | 0,0049 Mrd. € |

Die kleinen Investitionswerte skalieren Tiefbau und Leitungen mit Potenzgesetzen, Antrieb und Wärmeübertragung dagegen direkt mit dem betroffenen Strom. Sie sind Szenarien, keine Zusicherung von Baukosten.

Die untere Speichergrenze beträgt bei einem angenommenen Beckenvolumen von 25.000 m³ nur 0,0303 MW. Sie ignoriert den Wärmeabtransport durch den Quellabfluss und ist deshalb keine geeignete alleinige Auslegungsgrundlage. Umgekehrt führt der dokumentierte Hochwasserwert von 32,7 m³/s im unrealistisch konservativen Fall einer vollständig erwärmten Hochwasserströmung zu 12,48 GW. Diese Hülle deckt der Referenzentwurf nicht ab. Die Zuordnung der Anomalie zu Karstast, Abflussregime und betroffenem Volumenstrom ist deshalb die wichtigste Messaufgabe vor dem Bau.

## Dauerhaftigkeit und Falsifikation

Dauerhaft bedeutet hier unbegrenzter Betrieb mit Wartung innerhalb einer ausdrücklich begrenzten Hülle: linearer Anstieg der tiefen Quelltemperatur von 9 auf 100 °C in zehn Jahren, danach höchstens 100 °C, höchstens 2,3 m³/s betroffener Volumenstrom und ausreichende Luftkühlung bei 35 °C. Eine endliche Anlage kann keine unbegrenzt wachsende vulkanische Leistung garantieren.

Die Auslegung ist zu verwerfen oder zu vergrößern, wenn Tracer- und Durchflussmessungen einen größeren betroffenen Strom zeigen, die Temperatur nach Jahr zehn weiter ansteigt oder Hochwasser die Anomalie trägt. Sie kann verkleinert werden, wenn nur ein begrenzter Karstast betroffen ist. Jede Überschreitung der Sicherheitsmarge unter dem lokalen Siedepunkt, jedes Nichterreichen des 9-°C-Ziels und jede nachgewiesene Rückströmung der abgegebenen Wärme in denselben Wasserkreislauf falsifiziert den Erfolg der Anlage.
