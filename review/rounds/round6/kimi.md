# Rohbericht zu Commit `473e397c4d45a909cc024e1722d572cdbd73df7d`

## Prüfumfang und Nachweislage

- `HEAD` entspricht exakt dem Zielcommit. Alle 164 SHA-256-Hashes aus `review/rounds/round6/revision.json` stimmen. Nur `prompt.md` und `revision.json` sind unversioniert.
- Gegenüber dem archivreproduzierten Elterncommit `a963e211813cb5bb4b34dd0e6c5b77bb6882d969` ändert der Zielcommit nur Dokumentation und Reviewkonfiguration. PDF, Modell, Eingaben, Ergebnisse und Renderbilder bleiben unverändert.
- Ich habe die Kontaktübersicht, alle zwölf gerenderten Berichtsseiten und die D4RT-Seiten 1, 2 und 6 geöffnet und geprüft. Seitenzahlen im Bericht bezeichnen nachfolgend die physischen PDF-Seiten einschließlich Deckblatt.
- Die PDF hat zwölf A4-Seiten, eingebettete Schriften und keine Autorenmetadaten. Gemessen wurden 26 mm Mindestseitenrand, sieben Haupttextseiten und vier gemeinsame Seiten für Literatur und Anhang.
- Ich habe keine Builds oder Tests ausgeführt. Die Archivreproduktion wurde anhand `review/rounds/round6/reproduction.md` geprüft. Darin sind 36 von 36 byteweise identischen Paperartefakten und 13 erfolgreiche Modelltests belegt. Der Nachweis gilt in derselben Referenzumgebung, nicht für eine fremde Neuinstallation.
- Unabhängig davon habe ich read-only die 43 Manifest-Hashes, CSV gegen JSON, die Monte-Carlo-Auswertungen und zentrale thermodynamische und hydraulische Werte nachgerechnet. Die gespeicherten Ergebnisse stimmen mit diesen Nachrechnungen überein.
- Frühere Rohreviews und Scorecards wurden nicht gelesen. Frühere Punktzahlen wurden nicht übernommen.
- Die zentralen Primärquellen und die aktuellen offiziellen Regeln wurden direkt gegengeprüft.

## Einzelbewertungen

| Kriterium | Note | Begründung und genaue Belegorte |
|---|---:|---|
| 1. Qualität der Argumentation | 9 | Die Argumentation folgt schlüssig aus der Energiebilanz: Vollstromkühlung statt Speicherrechnung, externe Wärmesenke einschließlich Antriebsenergie, Trennung von ökologischem Normalziel und reinem Siedeschutz. Die Schlussfolgerung bleibt ausdrücklich bedingt und falsifizierbar. PDF-S. 2, §1; PDF-S. 4, Gleichungen 5 bis 9; PDF-S. 9, §6; `report/main.tex:38-44,210-214`. |
| 2. Vorgehen und Methodik | 8 | Stoffwerte, Volllast, Teillast, p90-Auslegung, Sommerfall, Ausfallintegration, Alternativen und Sensitivitäten werden methodisch verbunden. Die unabhängigen Nachrechnungen bestätigen die Kernergebnisse. Zwei methodische Mängel bleiben: Die 25-Jahres-Rechnung enthält 26 Betriebsjahresposten, und die Monte-Carlo-Verteilungen fehlen im Paper. PDF-S. 3, Gleichung 4; PDF-S. 5, §3.3; `model/core.py:195-238`; `output/model/hybrid_schedule.csv:2-27`; Korrekturen M1 und M2. |
| 3. Qualität der vorgeschlagenen Lösung | 9 | H1 verbindet direkte Trockenkühlung und Kältemaschinen, führt Wärme an Luft statt an das Gewässer ab und dimensioniert Reserve, Notstrom, Rücklauframpe und Standortbedarf. Fehlende Karst-, Netz-, Hersteller- und Standortdaten werden als Zulassungsbedingungen statt als erledigte Machbarkeit behandelt. PDF-S. 4, §3.1 und 3.2; PDF-S. 6, Tabelle 2 und §4.2; PDF-S. 7, §4.3; `output/model/results.json`, `baseline` und `design`. |
| 4. Mathematische und wissenschaftliche Modellierung | 8 | Wärme-, Kondensator-, Mischungs-, Speicher- und Ausfallmodelle sind konsistent implementiert. Unabhängig bestätigt wurden unter anderem 877,781145245 MW Endlast, 1793,726688109 MW p90-Bedarf, 2152,472025731 MW installierte Leistung, 182,651173513 MW Antriebsleistung und 2.236.544,982 l Diesel. `model/core.py:39-113`; `model/validation.py:27-71`; `output/model/results.json`, `baseline`, `design`, `validation`. Der Zeitfehler im Barwert und die unvollständig dokumentierte Unsicherheitsmodellierung verhindern eine 9. |
| 5. Ableitung neuer Ansätze statt Wiederverwendung | 9 | Vor der quantitativen Auswahl wurden sieben physikalisch verschiedene Ansätze registriert. H1 wurde vom begrenzten Teilkreislauf zur Vollstromlösung skaliert, ohne weltweite Neuheit zu behaupten. `docs/hypothesen.md:3-59`; `docs/alternativenvergleich.md:9-53`; `PROVENANCE.md:3-24`; `EXCLUSION_LOG.md`. Die Dokumentation belegt eine eigenständige Herleitung aus Aufgabe, Bilanzen und allgemeinen Quellen. |
| 6. Wissenschaftliche Qualität | 8 | Die zentralen Quellen tragen die verwendeten Werte: [Fan et al., „Discharge and climate trends“, Fig. 4h](https://publikationen.bibliothek.kit.edu/1000163518/151549041) bestätigt 2,3, 0,7 und 4,7 m³/s; [LGRB, „Schüttungsverhalten“](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele) bestätigt HQ 32,7 m³/s für 1951 bis 2007; [NIST](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Type=IsoBar&Digits=6&P=1.01325&TLow=0&THigh=100&TInc=10&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm) bestätigt Dichte und Wärmekapazität; [BDEW](https://www.bdew.de/service/daten-und-grafiken/bdew-strompreisanalyse/) bestätigt 13,8 und 17,9 ct/kWh; [UBA](https://www.umweltbundesamt.de/themen/co2-emissionen-pro-kilowattstunde-strom-2024) bestätigt 363 g/kWh; [LAWA, S. 10](https://www.laenderfinanzierungsprogramm.de/static/LFP/Dateien/LAWA/AO/O_10.20_211119_Endbericht_O10.20_TempEmpf_Fische.pdf) bestätigt die Empfehlung von höchstens ±1 K/h. Die verbleibenden Modell- und Dokumentationsfehler senken die Note. |
| 8. Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen | 8 | Zusammenfassung, Annahmentabelle, Ergebnisdarstellung und Schlussfolgerung sind gut verständlich. Vulkanik und Zehnjahresprognose werden wiederholt als Prämissen markiert. PDF-S. 1 bis 3 und PDF-S. 9. Zwei konkrete Erklärungsmängel bleiben: die falsche Achsenbezeichnung „Tiefe in °C“ auf PDF-S. 5 und die fehlenden Angaben zu Verteilungsform und Parametern der Monte-Carlo-Ziehungen auf PDF-S. 8. Korrekturen M2 und M3. |
| 9. Kritische Diskussion der Ergebnisse | 9 | Der Bericht diskutiert Hochwasser, Temperaturen oberhalb der Auslegungshülle, natürliche Wärmeverluste, COP, Strompreis, Netzverfügbarkeit, Standort, Genehmigung, Teilstrom, reines Siedeschutzziel und gemeinsame Ausfallursachen. Die Falsifikationskriterien sind konkret. PDF-S. 7 und 8, §4.4 und §5; PDF-S. 12, Tabellen 3 und 4; `docs/alternativenvergleich.md:59-67`. |
| 10. Berichtsstruktur und jurygerechte Nachvollziehbarkeit | 9 | Zusammenfassung, Einführung, Methode, Ergebnisse, Diskussion und Schlussfolgerung sind vorhanden und logisch angeordnet. Zahlen werden in Text, Gleichungen, Tabellen und Diagrammen weitgehend konsistent verwendet. Literatur und Anhänge bleiben im zulässigen Umfang. PDF-S. 2 bis 12; `report/main.tex:27-295`. |
| 11. Format, Zitation, Einreichungsanforderungen und visuelle Qualität | 8 | A4, 26 mm Rand, nominell 12 pt, eingebettete Schriften, numerische Quellenverweise, KI-Anhang und anonyme Metadaten sind erfüllt. Die aktuellen [Berichtsvorgaben](https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Vorgaben-Bericht.pdf), [Teilnahmebedingungen](https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Teilnahmebedingungen.pdf) und [FAQ](https://www.planet-simtech.de/faq/) bestätigen diese Anforderungen. Im direkten Vergleich mit D4RT-Seiten 1, 2 und 6 ist der Bericht weniger dicht, aber sauber gesetzt, mit konsistenten Tabellenlinien, Legenden und Bildunterschriften. D4RTs US Letter, kleinere Ränder und kleinere Schriften wurden nicht übernommen. Die falsche Achsenbezeichnung in Abbildung 1 ist jedoch ein sichtbarer fachlicher Satzfehler. `report/preamble.tex:1-54`; PDF-S. 5; Korrektur M3. |
| 12a. Bereitschaft für die schriftliche Runde | 8 | Die dokumentierte Archivreproduktion umfasst 36 identische Paperartefakte und alle zwölf Renderseiten. `review/rounds/round6/reproduction.md:3-28`. Hashprüfung, PDF-Geometrie und Quellenlage sind gut. Vor einer Auslieferung müssen jedoch M1 bis M3 behoben und die Artefakte erneut erzeugt werden. Offizielle Team-ID, menschliche Fachprüfung und tatsächliche Einreichung sind weiterhin offen und werden im Paper nicht als erfolgt behauptet. PDF-S. 11, Anhang A; `README.md:43-59`. |

## Materielle Mängel und konkrete Korrekturen

### M1. Die 25-Jahres-Rechnung enthält 26 Betriebsjahresposten

**Beleg.** `scenario.horizon_years` ist 25. `model/core.py:199-203` iteriert mit `range(horizon + 1)` über die Jahre 0 bis 25 und ruft `annual_operation` für jedes Jahr auf. `output/model/hybrid_schedule.csv:2-27` enthält daher 26 Jahreszeilen und 26 Betriebsposten. PDF-S. 3, Gleichung 4 summiert ebenfalls von 0 bis 25. PDF-S. 5, §3.3 erklärt ausdrücklich einen ersten Betriebsposten in Jahr 0 und danach 25 weitere.

Jahr 0 enthält allein 2,85 Mio. € Wartung. Der gespeicherte H1-Barwert beträgt 3.666.015.955,38 €. Ohne den zusätzlichen Betriebsposten in Jahr 0 ergeben sich 3.663.165.955,38 €. Der Fehler verändert die Technologiewahl nicht, ist aber systematisch und widerspricht der ausgewiesenen Laufzeit.

**Korrektur.** Jahr 0 ausschließlich als Investitionszeitpunkt behandeln und dort keine Betriebskosten oder Wartung ansetzen. Die 25 Betriebsjahre 1 bis 25 beibehalten. Alternativ müssten Zeithorizont, Überschriften und Text durchgehend auf 26 Betriebsjahre geändert werden. Anschließend Modell, Alternativen, Sensitivitäten, Stichproben, Tabellen und PDF neu erzeugen. Ein Test sollte neben der Anzahl der Zeilen auch die Zahl der tatsächlich berechneten Betriebsjahre prüfen.

### M2. Die Monte-Carlo-Annahmen fehlen im Paper

**Beleg.** PDF-S. 8, §4.4 nennt 10.000 Ziehungen für Abfluss, COP und Investitionsfaktor, erklärt deren zeitliche Kopplung und die feste Anlagenkapazität. Dort fehlen Verteilungsfamilien und Parameter. `data/parameters.yml:127-139` und `model/run_all.py:209-223` enthalten sie dagegen: Dreiecksverteilungen für Abfluss und COP, ein lognormaler Investitionsfaktor und der Seed 20261107.

Ohne diese Angaben sind insbesondere die 38,57 % Überlastfälle und die Kostenquantile aus dem Paper allein nicht reproduzierbar. Ein Verweis auf externe Modelldateien genügt nicht, weil der Wettbewerb das gesamte Ergebnis im Bericht verlangt.

**Korrektur.** In §4.4 eine kompakte Parameterangabe ergänzen:

- Abfluss: dreiecksverteilt mit 0,7, 2,3 und 4,7 m³/s als Minimum, Modalwert und Maximum.
- COP: dreiecksverteilt mit 3,0, 4,0 und 6,5.
- Investitionsfaktor: lognormal mit `sigma = 0,30` und `mean = -sigma²/2` im Logarithmus, damit der Erwartungsfaktor 1 beträgt.
- Seed 20261107, unabhängige Ziehungen der drei Eingangsgrößen, jeweils konstante Werte über alle Jahresreihen einer Ziehung.
- Ausdrücklicher Hinweis, dass diese Verteilungen Szenarioannahmen und keine empirisch kalibrierten Häufigkeitsmodelle sind.

### M3. Abbildung 1 bezeichnet die Temperaturachse als Tiefe

**Beleg.** Auf PDF-S. 5 steht links in Abbildung 1 „Tiefe in °C“. Dargestellt ist die Szenariotemperatur nach Gleichung 3. Der Fehler ist direkt in `model/run_all.py:258` enthalten und kommt dadurch auch in die gerenderte PDF.

**Korrektur.** Die Achsenbeschriftung zu „Szenariotemperatur in °C“ ändern. Abbildung, PDF und Renderseiten neu erzeugen und PDF-S. 5 erneut sichtprüfen. Die Berichtsprüfung sollte diese Achsenbeschriftung als erlaubten Wert vorgeben, damit ein semantisch falscher, aber formal lesbarer Text nicht erneut unentdeckt bleibt.

## Restrisiken und möglicher Dissens

- **H2-Kreislauf.** Der konsistente Lesart zufolge verdunstet ein separater Sekundärkreislauf, während der Quellstrom geschlossen bleibt. Das Paper sagt dies nicht ausdrücklich. `model/core.py:70-81` kühlt nach der Verdunstungsstufe weiterhin den vollen Volumenstrom. Bei direkter Verdunstung von Quellwasser müssten nach 280,222 kg/s Dampf nur noch 2019,092 statt 2299,315 kg/s gekühlt werden. Die Kältestufe läge dann bei 194,819 statt 221,857 MW. Sollte kein Sekundärkreislauf gemeint sein, ist das H2-Modell zu korrigieren. Ein Fließbild und ein eindeutiger Satz zur Topologie wären hier sinnvoll.
- **Reale Machbarkeit.** Karstwege, betroffener Stromanteil, Bathymetrie, vertikale Temperaturprofile, Netzanschluss, Flächeneigentum, Herstellerkurven und Genehmigungen fehlen weiterhin. Das Paper behandelt sie korrekt als offene Zulassungsbedingungen, nicht als erledigte Nachweise.
- **Auslegungshülle.** Der p90-Wert ist ein historisches Quantil und kein Extremwertnachweis. Für 32,7 m³/s wären 12,48 GW erforderlich. Auch Temperaturen über 100 °C und zusätzliche Wärmequellen sind nicht abgedeckt. Die Monte-Carlo-Überdeckung von 100 % gilt nur innerhalb der gewählten, bei 4,7 m³/s abgeschnittenen Verteilung.
- **Stoffwerte und Verdunstung.** Konstante Werte bei etwa 10 °C sind für die Szenariorechnung brauchbar, ersetzen aber keine IAPWS-Auslegung über Temperatur und Druck. Das arithmetische Mittel der Verdampfungsenthalpien bei 32 und 100 °C ist keine vollständige Temperaturintegration. Beide Grenzen sind im Paper ausgewiesen.
- **Notbetrieb.** Detektion, Generatorstart, Anfahrrampe, zwei Netzeinspeisungen und sechs Aggregate plus Reserve sind Szenarioannahmen. Gemeinsame Ausfallursachen, Kraftstofflogistik, Brandereignisse und reale Zuschaltversuche bleiben ungeprüft.
- **Kosten.** Der Jahresstrombedarf von rund 783 GWh liegt weit außerhalb des BDEW-Tarifbereichs von 70 bis 150 GWh. Der Bericht nennt 138 €/MWh daher nur einen Tarifproxy. Netzanschlusskosten fehlen. Die Beträge sind Szenarioschätzungen, keine Angebote.
- **Zielkonflikt.** H2 bleibt im Modell günstiger, verbraucht aber Wasser und benötigt Hygienemaßnahmen. H1 verursacht höhere Stromemissionen. Der reine Siedeschutz wäre wesentlich kleiner und billiger, bewahrt aber nicht den ökologischen Normalzustand. Diese Abwägung kann unterschiedlich bewertet werden, ohne dass die Energiebilanz davon abhängt.
- **Unabhängigkeit und Prüftiefe.** Die Clean-room-Dokumentation ist schlüssig, aber selbstreferenziell. Ein Same-Model-Review ist keine externe oder menschliche Prüfung. Die Archivreproduktion belegt Wiederholbarkeit in derselben Referenzumgebung, keine fremde Neuinstallation oder Feldvalidierung.

## Bewertungen von 10 und Fehlersuche

Es gibt keine Bewertung von 10. Die eigenen substanziellen Fehlersuchen waren nicht erfolglos: Sie führten zu M1, M2 und M3. Die zentralen physikalischen Werte, Manifest-Hashes, CSV- und JSON-Daten sowie die geprüften Primärquellen zeigten dagegen keine Abweichung von den abgelegten Ergebnissen.

## Stoppregelurteil

**Die Stoppregel ist auf dieser Revision nicht erfüllt.**

Sechs Zeilen liegen unter 9: Kriterien 2, 4, 6, 8, 11 und 12a. Zusätzlich bleiben mit dem systematischen Zeitfehler im Barwert, der unvollständig dokumentierten Unsicherheitsanalyse und der falschen Achsenbezeichnung konkrete Einwände gegen Korrektheit, Reproduzierbarkeit und Auslieferbarkeit.

Nach den Korrekturen müssen Modellergebnisse, PDF und alle Renderseiten erneut erzeugt und die Archivreproduktion wiederholt werden. Erst danach ist eine neue unabhängige Bewertung sinnvoll. Das Urteil des anderen Reviewers ist mir nicht bekannt und wurde nicht verwendet.

**Prozesshinweis.** Das Repository und der Git-Stand blieben unverändert. Bei zwei großen externen PDF-Abrufen legte das Fetch-Werkzeug automatisch Sitzungslogs außerhalb des Repositories an. Diese Logs wurden nicht ausgewertet und nicht gelöscht.