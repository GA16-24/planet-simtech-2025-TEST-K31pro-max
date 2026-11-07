# Sprechtext und Quellen

Die Vertonung verwendet eSpeak NG 1.52.0 mit deutscher Stimme. Der Tempofaktor nach der Laufzeitmessung beträgt 1.0783. Es handelt sich nicht um eine menschliche Live-Präsentation.

## Folie 1. Die 878-Megawatt-Aufgabe

Zeit 00:00:00.000 bis 00:00:17.396, effektive Dauer 17.40 s.

Der Blautopf soll in zehn Jahren kochen. Diese Zahl und die vulkanische Ursache sind die Prämissen unseres Szenarios, keine neuen Messungen von uns. Unsere Antwort beginnt mit einer unbequemen Energiebilanz. Wer das Becken dauerhaft kalt halten will, muss im Extremfall 878 Megawatt abführen.

Quellen und Belege:
- Aufgabenprämisse
- Modellergebnis baseline.final_cooling_mw

## Folie 2. Ein Kelvin entscheidet

Zeit 00:00:17.396 bis 00:00:46.199, effektive Dauer 28.80 s.

Im Mittel fließen jede Sekunde 2,3 Kubikmeter Wasser durch den Blautopf. Jedes Kilogramm speichert etwa 4,2 Kilojoule pro Kelvin. Deshalb transportiert der Strom 9,646 Megawatt pro Kelvin. Zwischen dem kalten Normalzustand und dem Sieden liegen hier 91 Kelvin. Multipliziert ergibt das 877,8 Megawatt. Das ist der zentrale Unterschied zwischen einer kleinen Kühlung am Beckenrand und einer Anlage, die den ganzen Quellstrom behandelt.

Quellen und Belege:
- Fan et al. [2]
- NIST [4]
- Gleichung in output/model/results.json

## Folie 3. Zwei Kontrollvolumen

Zeit 00:00:46.199 bis 00:01:14.545, effektive Dauer 28.35 s.

Man kann die Aufgabe mit 30 Kilowatt beantworten, wenn man nur das Beckenvolumen in zehn Jahren aufheizt und den Abfluss vergisst. Unsere Speicherrechnung zeigt genau diese 0,0303 Megawatt. Aber der Blautopf ist keine verschlossene Thermoskanne. Wenn der gesamte Zufluss warm wird, muss die gleiche Wärmemenge wieder aus dem Strom heraus. Erhitzt die Anomalie dagegen nur ein Prozent des Flusses, genügen 8,8 Megawatt. Die Messtechnik entscheidet also zuerst, welches Kontrollvolumen stimmt.

Quellen und Belege:
- Eigene Speicher- und Teilstromrechnung
- Fan et al. [2]

## Folie 4. Sieben physikalische Wege

Zeit 00:01:14.545 bis 00:01:41.771, effektive Dauer 27.23 s.

Wir haben sieben Wege mit derselben Last verglichen. Druck verschiebt nur das Sieden und schützt die Organismen nicht. Ein Bypass lässt das Becken weiter heiß werden. Passive Kühlflächen scheitern an Fläche und Sommerluft. Kaltwasserzumischung braucht mehr als das Zwanzigfache des natürlichen Abflusses. Verdunstung ist billig, entzieht der Blau aber elf Millionen Kubikmeter im Jahr. Ein Karsteingriff wäre ursächlich, kennt jedoch die Fließwege nicht sicher genug. Deshalb bleibt die trockene Hybridkühlung.

Quellen und Belege:
- Alternativenvergleich
- 42. BImSchV [13]
- Lauber et al. [11]

## Folie 5. Die zweistufige Kühlung

Zeit 00:01:41.771 bis 00:02:27.062, effektive Dauer 45.29 s.

Unsere Anlage nutzt die hohe Temperatur zuerst ohne Kältemaschine. Trockenkühler senken das Wasser von 100 auf 40 Grad und führen 579 Megawatt an die Luft ab. Danach kühlen Kältemaschinen auf 9 Grad und übernehmen 299 Megawatt. Ihre Kondensatoren geben zusätzlich die Antriebsenergie ab. Mit Ventilatoren und Pumpen muss die Luft 952 Megawatt aufnehmen. Sechs getrennte Stränge sind in jeder Ausbaustufe geplant, fünf arbeiten, einer ist Reserve. Bei der geplanten Inbetriebnahme senkt die Regelung den Kälteauslass mit höchstens einem Kelvin pro Stunde. Der Stresstest von 100 auf 9 Grad dauert deshalb 91 Stunden. Ein Puffer allein wäre dafür kein Nachweis. Nach einem Ausfall ist eine eigene sichere Wiederanlaufplanung erforderlich.

Quellen und Belege:
- OpenStax Kondensatorbilanz [8]
- LAWA [10]
- output/model/results.json

## Folie 6. Bei Ausfall zählen Minuten

Zeit 00:02:27.062 bis 00:02:55.801, effektive Dauer 28.74 s.

Ein Ausfall ist kein ferner Zufall. Im zehnten Jahr erreicht das ungekühlte Becken nach unserem Modell in etwa 23 Minuten die interne Alarmschwelle von 20 Grad. Diese Schwelle ist keine behördliche Blau-Grenze und keine Siedezeit. Deshalb gehören ein freier Strang, zwei Netzeinspeisungen und 48 Stunden Notstrom zum Entwurf. Unabhängige Sensoren messen Temperatur und Druck. Die Anlage gilt nur dann als erfolgreich, wenn auch Tiefe und Fluss kalt bleiben, nicht nur die sichtbare Oberfläche.

Quellen und Belege:
- Validierung failure_time_to_20c_h
- LAWA [10]
- OGewV [9]

## Folie 7. Der Preis des trockenen Weges

Zeit 00:02:55.801 bis 00:03:34.619, effektive Dauer 38.82 s.

Die trockene Lösung ist bewusst nicht die billigste. Wir schätzen 722 Millionen Euro Investition und 138 Millionen Euro jährlichen Betrieb im zehnten Jahr. Über 25 Jahre ergibt sich ein Barwert von 2,94 Milliarden Euro. Verdunstung käme mit 0,79 Milliarden aus. Diese Differenz kauft den Erhalt des Wasserhaushalts und vermeidet das offene Aerosolsystem am Blautopf. Der Emissionsunterschied beträgt 193 Kilotonnen CO2 pro Jahr. Alle Kosten sind Szenarien in Euro von 2026, keine Angebote. Ein belegter kleiner Teilstrom würde die Kosten drastisch senken.

Quellen und Belege:
- BDEW [16]
- Kostenannahmen in data/parameters.yml
- 42. BImSchV [13]

## Folie 8. Die Hülle begrenzt das Versprechen

Zeit 00:03:34.619 bis 00:04:04.021, effektive Dauer 29.40 s.

Dauerhaft heißt bei uns nicht grenzenlos. Unsere Auslegung gilt bis 100 Grad am tiefen Zufluss und bis 2,3 Kubikmeter pro Sekunde betroffenem Strom. Der gemessene Hochwasserwert liegt bei 32,7 Kubikmetern pro Sekunde. Wenn die Anomalie diesen gesamten Strom erfasst, wären 12,48 Gigawatt nötig. Das kann unsere Referenzanlage nicht. Auch ein Temperaturanstieg nach dem zehnten Jahr erfordert Nachrüstung. Diese Grenzen offen zu nennen ist Teil der Lösung, kein Fußnotenfehler.

Quellen und Belege:
- LGRB [3]
- Fan et al. [2]
- Sensitivitätsrechnung

## Folie 9. Messung und Kühlentscheidung

Zeit 00:04:04.021 bis 00:04:30.111, effektive Dauer 26.09 s.

Vor dem Bau messen verteilte Sonden Temperatur und Druck in beiden Karstästen und über die Tiefe. Tracer und Durchflussmessungen zeigen, welcher Ast die Wärme trägt. Abgestufte Kühlversuche prüfen die berechnete Leistung direkt. Wärme- und Stromzähler an der Luftseite verhindern, dass wir die abgegebene Energie nur scheinbar beseitigen. Erst diese Daten legen Modulzahl und Kosten fest. Ein kleiner betroffener Teilstrom ist die einzige ehrliche Abkürzung zur kleinen Anlage.

Quellen und Belege:
- Lauber et al. [11]
- US EPA [12]
- Falsifikationsprotokoll im Bericht

## Folie 10. Schlussfolgerung

Zeit 00:04:30.111 bis 00:04:50.065, effektive Dauer 19.95 s.

Die 878 Megawatt folgen zwingend aus dem Vollstromszenario. Unsere Antwort ist deshalb eine zweistufige Kühlung mit Reserve, externer Wärmesenke und einem Ausbaupfad, der auf echten Messungen beruht. Sie hält den Normalzustand innerhalb ihrer ausgewiesenen Hülle. Damit wird aus der Katastrophenprognose eine prüfbare Ingenieuraufgabe.

Quellen und Belege:
- Gesamtergebnis
- KI-Offenlegung auf der Folie
