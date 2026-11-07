## Prüfrahmen

Geprüft wurde Commit `cc25cc903681ebbc4d6865309236885f729d6d77`. Frühere Rohbewertungen und Scorecards wurden nicht gelesen.

- Alle 127 SHA-256-Hashes aus `review/rounds/round2/revision.json` stimmen mit den Arbeitsdateien überein. Die einzige Abweichung vom Commit betrifft `created_utc` in `output/verification_summary.json`. Hierfür wurde die committed Fassung gelesen. Die Dateien im Repository blieben unverändert.
- Geprüft wurden alle 16 Berichtsseiten, alle 10 Folien, die Kontaktübersichten, die MP4-Datei und einzelne Videoframes. D4RT wurde zusätzlich direkt aus dem Original im Speicher gerastert, Seiten 1, 2 und 6.
- Alle 7 Modelltests bestanden mit deaktiviertem Bytecode-Schreiben. Die gemessenen Mindest-Ränder des Berichts betragen links 25,85 mm, rechts 25,89 mm, oben 26,00 mm und unten 26,28 mm.
- Die MP4 hat H.264, AAC, 1920 x 1080, SAR 1:1 und 290,132 Sekunden Dauer. Meine unabhängige Echtzeitdecodierung endete fehlerfrei nach 289,58 Sekunden. Alle 65 Untertitel entsprechen exakt dem Sprechtext.

## Bewertung

| Kriterium | Punkte | Begründung und genaue Belege | Korrektur |
|---|---:|---|---|
| 1. Qualität der Argumentation | 8 | Die Unterscheidung von Vollstrom und Speicher sowie die externe Wärmesenke tragen die Argumentation. Bericht, PDF-S. 2, 4 bis 10. Überlastrisiko und nicht gleichwertige Alternativen schwächen sie. | M1, M2, M6 |
| 2. Vorgehen und Methodik | 7 | Parameter, Code und Tests sind nachvollziehbar. Die Auslegung verwendet den Mittelabfluss statt einer hydrologischen Belastungsreihe. H2 wird ohne Feuchtkugel- und Notfallnachweis verglichen. `model/core.py`, `model/run_all.py`, `output/model/results.json`. | M1, M2, M3, M4 |
| 3. Qualität der vorgeschlagenen Lösung | 7 | H1 ist innerhalb der angenommenen Hülle thermodynamisch stimmig. Für einen dauerhaften Betrieb fehlen jedoch eine ausreichende hydrologische Auslegung, der Standortnachweis der 952-MW-Senke und ein dynamischer Notfallnachweis. | M1, M3 |
| 4. Mathematische und wissenschaftliche Modellierung | 8 | Wärmebilanz, Kondensatorwärme und gekoppelte Monte-Carlo-Rechnung sind konsistent. Die Näherungen sind erklärt. H2 ist modellseitig unvollständig, und die Unsicherheitsrechnung wird nicht auf Überlast ausgewertet. `model/core.py:56-71`, `model/run_all.py:98-146`. | M1, M2, M4 |
| 5. Ableitung neuer Ansätze | 9 | Sieben Ansätze werden aus der Energiebilanz entwickelt und mit denselben Kriterien geprüft. `docs/hypothesen.md`, H1 bis H7, `docs/alternativenvergleich.md`, `PROVENANCE.md`, `EXCLUSION_LOG.md`. Kein Hinweis auf Wiederverwendung früherer Lösungen. | Kein materieller Mangel festgestellt. |
| 6. Wissenschaftliche Qualität | 8 | Quellenlage, Szenariotrennung und Falsifikationsplan sind gut. Tarifzuordnung, fehlende Feldvalidierung und offene technische Randbedingungen begrenzen die Beweiskraft. | M1, M2, M3, M4 |
| 8. Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen | 8 | Annahmen und Grenzen sind meist klar getrennt. Tabelle 3 enthält jedoch "0 %" statt 0,1 %. Folie 10 behauptet eine belegte Hülle und der Sprechtext bereits verwendete echte Messungen. | M5, M6, M7 |
| 9. Kritische Diskussion der Ergebnisse | 8 | Auslegungshülle, Hochwasser und Falsifikation sind ausdrücklich diskutiert. Bericht, PDF-S. 9 bis 11. Die konkrete Überlasthäufigkeit und die fehlende Vergleichbarkeit von H2 fehlen. | M1, M2, M3 |
| 10. Berichtsstruktur und jurygerechte Argumentation | 9 | Zusammenfassung, Einführung, Methode, Ergebnisse, Diskussion und Schlussfolgerung bilden eine klare Kette. Haupttext auf PDF-S. 2 bis 11, Literatur und Anhänge auf S. 12 bis 16. | Kein struktureller Mangel. Die Leerfläche auf S. 14 wird unter Kriterium 11 bewertet. |
| 11. Format, Zitation, Einreichungsanforderungen und D4RT-Vergleich | 8 | A4, Ränder, Schrift, Seitenbudget, Anonymität, numerische Verweise und KI-Offenlegung sind erfüllt. D4RT ist bei Abbildungsintegration und Flächennutzung besser. Tabellenfehler, Dezimalpunkte und die große Leerfläche auf PDF-S. 14 bleiben. | M5, M6, M7, M8 |
| 12a. Bereitschaft für die schriftliche Runde | 8 | Ein vollständiger, reproduzierbarer Bericht liegt vor. Vor einer Abgabe sind die fachlichen Fehler zu korrigieren und die offiziellen menschlichen Schritte auszuführen. | M1 bis M5, M8 |
| 12b. Bereitschaft für die Finalrunde | 8 | Folien, echte MP4, Sprechtext, VTT, technische Zeitprobe und 20 adversariale Fragen sind vorhanden. Inhaltliche Überbehauptungen, fehlende zentrale Q&A und menschliche Restaufgaben verhindern eine höhere Bewertung. | M1 bis M4, M6, M7, M8 |

## Materielle Mängel und konkrete Korrekturen

**M1. Die hydrologische Auslegung ist unter der eigenen Unsicherheitsannahme häufig überlastet.**

Die installierte Reserve beträgt 1.053,337 MW. In `output/model/uncertainty_samples.npz` überschreiten 3.857 von 10.000 Ziehungen diesen Wert, also 38,57 %. Der Abfluss 4,7 m³/s verlangt laut `output/model/sensitivity.csv` 1.793,727 MW, das 1,703-Fache der installierten Reserve. Der Bericht nennt auf PDF-S. 9 den Faktor 1,7, wertet die Überlasthäufigkeit aber nicht aus.

Korrektur: Entwurfsabfluss aus Messungen oder einer begründeten Risikovorgabe bestimmen. Ohne solche Messung ist mindestens der dokumentierte 90-Prozent-Fall zu prüfen. Anschließend Kühlung, Luftsenke, Strom, Notstrom und Kosten neu dimensionieren. Die Überlastwahrscheinlichkeit und die Abdeckung des Entwurfsabflusses in Bericht und Q&A aufnehmen.

**M2. H2 wird nicht unter denselben Betriebsbedingungen wie H1 ausgelegt.**

`model/core.py:153-158` berechnet H2 nur mit Ventilatoren und Pumpen. Eine Kältemaschine fehlt. Gleichzeitig räumt der Bericht auf PDF-S. 7 ein, dass 9 °C bei warmer, feuchter Luft ohne Feuchtkugeltemperatur nicht garantiert sind. Das widerspricht dem Auswahlkriterium auf PDF-S. 4, wonach jede Variante bei 35 °C Luft auf 9 °C kühlen muss. Auch `docs/alternativenvergleich.md:33` nennt H2 gleichzeitig physikalisch wirksam.

Korrektur: Feuchtkugeltemperatur und erforderliche Annäherung als Eingaben verwenden. Wenn 9 °C nicht erreichbar ist, eine Kältemaschine ergänzen oder H2 für diesen Betriebsfall als ungeeignet werten. Investition, Betrieb, Wasser und Emissionen neu vergleichen. Auf Folie 4 "ökologisch schlechter" durch eine sachliche Abwägung von Wasser, Hygiene und CO₂ ersetzen.

**M3. Wärmesenke, Erfassung und Notfallbetrieb sind noch kein betriebsfähiger Gesamtentwurf.**

Die 952 MW und 26.313 m² Face-Fläche sind nur Bilanzgrößen. Rückverwirbelung, Lärm, lokale Erwärmung und Standort sind laut Bericht, PDF-S. 5 und 7, offen. Die Ansaug- und Diffusorgeometrie bleibt nach `presentation/jury_qa.md:69-73` unbestimmt. Beim Ausfall bleiben im Beckenmodell nur 23 Minuten bis 20 °C, während Aggregatzahl, Anlaufzeit, Netzschutz und gemeinsame Fehler nicht ausgelegt sind.

Korrektur: Standortvariante mit Luftführung, Abständen, Rückverwirbelung und Lärm untersuchen. Die Erfassung der Karstäste durch Tracer und Durchflussnachweise absichern. Ein dynamisches Ausfallszenario mit Detektion, Aggregatanlauf, Lastzuschaltung und gemeinsamen Fehlern rechnen. Die 23 Minuten müssen als harte Zeitbedingung des Nachweises verwendet werden.

**M4. Der Stromtarif passt nicht zum Verbrauch und verändert den Barwert wesentlich.**

`data/parameters.yml:55` und `report/main.tex:116` verwenden 179 €/MWh für kleine und mittlere Industrie. H1 benötigt jedoch 650 GWh pro Jahr. Die [BDEW-Strompreisanalyse](https://www.bdew.de/service/daten-und-grafiken/bdew-strompreisanalyse/) nennt für 70 bis 150 GWh pro Jahr 138 €/MWh. Meine Rechnung mit dem vorhandenen Modell ergibt bei 138 €/MWh einen H1-Barwert von 2,519 statt 2,938 Mrd. €. Die Differenz beträgt rund 0,419 Mrd. €.

Korrektur: Einen Tarif für den tatsächlichen Abnahmefall verwenden oder zumindest 138 bis 179 €/MWh als Sensitivität rechnen. Alle Kosten, Tabellen, Folien und Q&A aktualisieren. Für 650 GWh pro Jahr ist ein konkretes Marktangebot erforderlich.

**M5. Tabelle 3 enthält einen falschen Prozentwert.**

`report/generated/flow_fractions.tex:9` zeigt "0 %" bei 0,9 MW. Ursache ist die Formatierung ohne Nachkommastelle in `model/run_all.py:456`. Auf Bericht, PDF-S. 10, Tabelle 3, ist der Fehler sichtbar.

Korrektur: Für gebrochene Prozentanteile eine Dezimalstelle ausgeben, also 0,1 %. Bericht neu rendern und den Wert direkt im PDF prüfen.

**M6. Die Schlusspräsentation überbehauptet den Nachweisstand.**

Folie 10 sagt "innerhalb ihrer belegten Hülle". `presentation/speaker_notes.md:106` beschreibt einen Ausbaupfad, "der auf echten Messungen beruht". Tatsächlich beruht der aktuelle Pfad auf Szenarioannahmen. Die Messungen sind erst geplant.

Korrektur: "Belegten Hülle" durch "angenommene" oder "ausgewiesene Hülle" ersetzen. Den Sprechtext in "der vor dem Bau durch echte Messungen festgelegt wird" ändern. Q&A zu Überlastwahrscheinlichkeit, Feuchtkugelgrenze, Tarifklasse und Notstromanlauf ergänzen und ihre Revisionen zuordnen.

**M7. Visuelle Restfehler verhindern Gleichzug mit der D4RT-Referenz.**

Die Diagramme auf Folie 3 und Folie 8 enthalten "0.030 MW" und "877.8 MW" statt deutscher Dezimalkommas. Ursachen stehen in `model/run_all.py:276` und `model/run_all.py:296`. Bericht, PDF-S. 14, nutzt nur eine Spalte und lässt große Flächen frei. D4RT Seiten 1, 2 und 6 integrieren Abbildungen und Tabellen deutlich dichter.

Korrektur: Dezimalformatierung der Matplotlib-Labels vereinheitlichen. Anhang A und B neu umbrechen, ohne das Seitenbudget zu überschreiten. Bericht und Folien erneut rendern und direkt mit D4RT vergleichen.

**M8. Die tatsächliche Auslieferung bleibt menschlich offen.**

Offizielle Team-ID, menschliche Fachprüfung, Medienfreigabe, Finalisten-E-Mail und eigene Live-Probe fehlen. Das ist in `README.md:44-56`, `presentation/rehearsal.md:21` und `presentation/rights.md:26-28` korrekt ausgewiesen, aber noch nicht erledigt.

Korrektur: Diese Schritte vor einer realen Abgabe dokumentiert ausführen. Die synthetische Vertonung nicht als menschliche Live-Probe oder abgeschlossene Rechteprüfung verwenden.

## Bewertung der Antworten auf Runde 1

Mehrere Antworten halten der erneuten Prüfung stand. Die Pfeile auf Folie 5 führen zur Luftsenke. Folien 7 und 8 laufen nicht über. Legenden, Gleichung 3, Seitenzahlen und Anhang C sind sauber gerendert. Ersatzinvestition, gekoppelte Monte-Carlo-Rechnung, Dieselbedarf, SAR 1:1, CO₂- und Luftkühlerflächenwerte stimmen mit Code und Ergebnissen überein. Auch die 127 Dateihashes einschließlich Umlautpfaden wurden erfolgreich geprüft.

Andere Einwände sind nur teilweise beantwortet. Die Rampe ist ein Sollwert-Stresstest, weiterhin kein Wiederanlauf- oder Notfallnachweis. Wärmesenke und Notstrom sind quantifiziert, aber nicht standort- und zuverlässigkeitsbezogen nachgewiesen. Die visuellen Dezimaltrennfehler und die Leerfläche auf PDF-S. 14 bestehen weiter. Die offenen physikalischen Grenzen bei Hochwasser, betroffenem Strom und Temperaturverlauf sind dokumentiert, nicht gelöst.

## Restrisiken und Dissens

- Der 12,48-GW-Hochwasserfall bleibt außerhalb der Auslegung. Ebenso ist ein Anstieg über 100 °C nach Jahr zehn nicht abgedeckt. Die Dauerhaftigkeitsaussage ist deshalb nur bedingt richtig.
- Ich teile die pauschale Bewertung "H2 ist ökologisch schlechter" nicht. H1 vermeidet Wasserverbrauch und offene Aerosole, verursacht im Modell aber 193,0 Kilotonnen mehr Stromemissionen pro Jahr. Das ist ein Zielkonflikt.
- N+1 deckt einen Modulausfall ab. Es ist keine Antwort auf hydrologische Überlast, gemeinsame Netzfehler oder eine unvollständige Erfassung des heißen Stroms.
- Die Rechenkontrollen sind keine Feldvalidierung. Die Unabhängigkeit ist durch Protokolle und nachvollziehbare Herleitung gestützt, kann als negative Tatsache aber nicht vollständig bewiesen werden.

## Prüfgrenzen

`make verify` wurde wegen der schreibenden Render- und Verifikationsschritte nicht ausgeführt. Stattdessen erfolgten direkte read-only Prüfungen der vorhandenen Artefakte und sieben Modelltests. D4RT wurde nur in reduzierter Rasterauflösung erneut betrachtet. Nicht jede der 23 externen Quellen wurde vollständig erneut gelesen. Eine subjektive Hörprobe, menschliche Live-Darbietung, Feldmessung und standortbezogene Ingenieurprüfung fanden nicht statt.

## Bewertungen von 10 und Fehlersuche

Es wurde keine 10 vergeben. Damit gibt es keine 10, zu der eine erfolglose substanzielle Fehlersuche beschrieben werden müsste. Die eigene Fehlersuche war nicht erfolglos. Sie hat insbesondere die 38,57-prozentige Überlasthäufigkeit, die Tarifabweichung, den falschen Tabellenwert und die Überbehauptungen in Folie 10 und Sprechtext gefunden.

## Abschließendes Urteil zur Stoppregel

Die Stoppregel ist nicht erfüllt. Zwei Kriterien erreichen 9, zehn bleiben darunter. Es bestehen offene materielle Einwände gegen Machbarkeit, wissenschaftliche Vergleichbarkeit, einzelne Angaben und Auslieferbarkeit. Bereits diese Bewertung verhindert den geforderten Mindestwert von 9 bei beiden Reviewern, unabhängig vom Ergebnis des anderen Reviewers. Eine weitere Revision mit den Korrekturen M1 bis M8 und erneuter Prüfung der tatsächlich gerenderten Ausgabedateien ist erforderlich.
