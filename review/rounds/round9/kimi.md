## Prüfumfang

Geprüft wurde Commit `8e1b72d5235162172f31b00775cd1bb0c55d24ce`. Alle 189 SHA-256-Hashes stimmen mit `review/rounds/round9/revision.json` überein. Nach der Prüfung blieben nur die bereits vorhandenen unversionierten Dateien `review/rounds/round9/prompt.md` und `revision.json` unverändert. Ich habe keine Datei verändert.

Ich habe die Kontaktübersicht, alle 13 Berichtsseiten und die D4RT-Seiten 1, 2 und 6 gesichtet. Frühere Rohreviews und Scorecards habe ich nicht geöffnet.

Die 19 Modelltests und `make verify` habe ich wegen des Verbots von Builds und Dateiveränderungen nicht erneut ausgeführt. Ihr Erfolg ist ausschließlich durch `review/rounds/round9/reproduction.md` dokumentiert. Stattdessen habe ich die wichtigsten Bilanzen, die Jahresreihen, die Monte-Carlo-Auswertung, PDF-Geometrie, Metadaten und Schriftgrößen mit eigenen read-only Befehlen geprüft.

Externe Stichproben umfassten die [Berichtsvorgaben](https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Vorgaben-Bericht.pdf), [Teilnahmebedingungen](https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Teilnahmebedingungen.pdf), [FAQ](https://www.planet-simtech.de/faq/), [Fan et al.](https://publikationen.bibliothek.kit.edu/1000163518/151549041), [LGRB](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele), [Blaubeuren](https://www.blaubeuren.de/Geopoint-Blautopf), [NIST-Stoffwerte](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Type=IsoBar&Digits=6&P=1.01325&TLow=0&THigh=100&TInc=10&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm), [HAW Tabelle 5.6](https://reposit.haw-hamburg.de/bitstream/20.500.12738/5979/1/Bachelorthesis_Bez_Armin_20120618.pdf), [BDEW](https://www.bdew.de/service/daten-und-grafiken/bdew-strompreisanalyse/) und [UBA](https://www.umweltbundesamt.de/themen/co2-emissionen-pro-kilowattstunde-strom-2024).

## Bewertung

| Kriterium | Bewertung | Begründung und Belegorte |
|---|---:|---|
| 1. Qualität der Argumentation | 9 | Die Energiefrage führt schlüssig zur Vollstrombilanz und externen Wärmesenke. Ökologischer Normalzustand und reines Siedeverbot werden sauber getrennt. Die Begrenzung auf 4,7 m³/s und 100 °C ist Teil der Antwort statt einer versteckten Einschränkung. Belege: PDF-Seiten 2 bis 4, §§1 und 2, Gleichungen 1 bis 6, PDF-Seite 10, §6. |
| 2. Vorgehen und Methodik | 8 | Hypothesenbildung, Wärmebilanzen, Alternativen, Sensitivitäten, Ausfallrechnung und Messplan sind methodisch stark. Eine relevante wärmegetriebene Kältevariante fehlt jedoch vollständig, obwohl sie in den eigenen Recherchenotizen auftaucht. Belege: `docs/hypothesen.md:11-51`, `report/main.tex:51-52`, `research_notes/Blautopf Wärmeschutz/engineering_economics.md:79-80`. Korrektur unter Mangel 1. |
| 3. Qualität der vorgeschlagenen Lösung | 8 | H1 ist als bedingter Szenarioentwurf thermodynamisch schlüssig und berücksichtigt Reserve, Hilfsenergie, Wärmesenke, Notstrom und Standort. Die Wahl der Kompressionskühlung ist aber ohne Prüfung einer Absorptions- oder Adsorptionslösung unzureichend abgesichert, weil gerade Netz und Notstrom die zentralen Schwachstellen sind. Belege: PDF-Seiten 4 bis 8, §§3.2 bis 4.3, `output/model/results.json:190-218`. |
| 4. Mathematische und wissenschaftliche Modellierung | 9 | Die Gleichungen und gespeicherten Ergebnisse sind konsistent. Meine Nachrechnung ergab 877,781145 MW ohne Differenz, 2.152,472026 MW installierte Leistung und 234,335798 MW elektrische Auslegung. Die analytisch berechneten Ausfallspitzen weichen weniger als 0,0000033 K von den gespeicherten Werten ab. Alle 10.000 Stichproben und Quantile stimmen. Belege: `model/core.py:39-87`, `model/validation.py:28-72`, `output/model/results.json:151-218,2110-2194`. Konstante Stoffwerte und vereinfachte Verdampfungsenthalpie sind ausdrücklich als Näherungen benannt. |
| 5. Ableitung neuer Ansätze | 9 | Die Herleitung beginnt mit alternativen Erklärungen und sieben physikalisch verschiedenen Ansätzen vor der quantitativen Auswahl. Herkunft, KI-Beteiligung und Ausschlüsse sind dokumentiert. Ich fand keine Verwendung früherer Wettbewerbslösungen. Belege: `docs/hypothesen.md:3-59`, `PROVENANCE.md:3-24`, `EXCLUSION_LOG.md:1-13`, `decisions.tsv:2-4`. |
| 6. Wissenschaftliche Qualität | 9 | Zentrale empirische Eingaben und Rechenannahmen sind unterscheidbar, die geprüften Quellen decken die zitierten Werte. Die Arbeit überzeichnet interne Tests nicht als Feldvalidierung. Belege: Tabelle 1 auf PDF-Seite 4, §5 auf PDF-Seiten 9 und 10, `sources/registry.yml:1-164`, Anhang A auf PDF-Seite 12. Die externe wissenschaftliche und menschliche Validierung bleibt offen und wird nicht behauptet. |
| 8. Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen | 9 | Zusammenfassung, Annahmentabelle, Gleichungen, Ergebnisdarstellung und Schlussfolgerung bilden eine verständliche Kette. Die Zusammenfassung nennt Lösung, Größenordnung, Kosten und Grenzen ohne p90- oder COP-Kürzel. Belege: PDF-Seite 2, Tabelle 1 auf Seite 4, Gleichungen 1 bis 10 auf Seiten 3 bis 7, §6 auf Seite 10. |
| 9. Kritische Diskussion der Ergebnisse | 9 | Der Bericht diskutiert Hochwasser, kleines Beckenvolumen, COP, Stromtarif, Netzverfügbarkeit, Standort, Wasserbedarf, Emissionen und Gegenmaßnahmen. Besonders wirksam ist die Volumensensitivität mit 26,4 °C und negativer Zeitdifferenz im kleinen Fall. Belege: PDF-Seiten 7 bis 9, §§4.2 bis 4.4 und 5, `output/model/results.json:2014-2147`. |
| 10. Berichtsstruktur und jurygerechte Nachvollziehbarkeit | 9 | Der Aufbau folgt Problem, Annahmen, Methode, Ergebnissen, Betrieb, Diskussion, Nachweis und Schluss. Tabellen und Abbildungen stehen nahe am zugehörigen Text. Die Anhänge enthalten KI-Offenlegung, Handrechnung, Unsicherheit und Sensitivitätstabellen. Belege: PDF-Seiten 2 bis 13, besonders Abbildungen 1 bis 3 und Tabellen 1 bis 4. Ein zusätzliches Prozessschema wäre hilfreich, ist aber nicht für die Nachvollziehbarkeit erforderlich. |
| 11. Format, Zitation, Einreichungsanforderungen und D4RT-Vergleich | 9 | Das PDF hat 13 Seiten, davon 8 Haupttext- und 4 Literatur-/Anhangsseiten nach Deckblatt. A4, mindestens 26,0 mm gemessener Rand, nominale 12-pt-Schrift, numerische Verweise und eingebettete Schriften sind bestätigt. Autorenmetadaten fehlen. Im direkten Vergleich mit `d4rt_page01.png`, `d4rt_page02.png` und `d4rt_page06.png` ist der Bericht weniger dicht und besitzt weniger erklärende Grafiken. Satz, Tabellen, Diagramme und Gleichungen sind dennoch sauber, lesbar und ohne sichtbare Kollisionen. Belege: `report/preamble.tex:1-54`, PDF-Seiten 1 bis 13, `compliance/layout_referenz.md:15-28`. |
| 12a. Bereitschaft für die schriftliche Runde | 8 | Als technisches Testpaket ist das PDF vollständig. Für eine tatsächliche Abgabe fehlen die offizielle Team-ID und die menschliche inhaltliche und rechtliche Freigabe. Das Paket selbst erklärt diese Schritte ausdrücklich als offen. Belege: PDF-Seiten 1 und 2, Anhang A auf Seite 12, `README.md:43-45,55-59`, `PROVENANCE.md:42-44`. Korrektur unter Mangel 2. |

## Materielle Mängel und konkrete Korrekturen

### 1. Wärmegetriebene Kühlung fehlt im Alternativenvergleich

Der Bericht registriert sieben Ansätze, untersucht aber keine Absorptions- oder Adsorptionskühlung. Dabei liegt mit 100 °C eine mögliche Antriebstemperatur vor, und die Recherchenotizen enthalten bereits Kostenwerte für eine Absorptionskältemaschine. Die ausgewählte Lösung benötigt im Randfall 234,3 MW elektrische Leistung, zwei entsprechende Netzeinspeisungen und einen großen Dieselvorrat. Eine wärmegetriebene Variante könnte genau diese Schwachstellen verändern. Sie darf nicht ohne Prüfung als besser angenommen werden, aber ihr Fehlen schwächt die Auswahlmethodik.

Belegorte:

- `docs/hypothesen.md:11-51`
- `report/main.tex:51-52,137-146,190-196`
- `research_notes/Blautopf Wärmeschutz/engineering_economics.md:79-80`
- `sources/registry.yml:120-126`
- PDF-Seiten 3 bis 5 und 8, Quelle [19] auf PDF-Seite 11

Korrektur:

1. Eine zusätzliche Variante für heißwassergetriebene Absorptions- oder Adsorptionskühlung registrieren.
2. Für 100 °C Zufluss, 9 °C Rückführziel, 35 °C Sommerluft und 4,7 m³/s dieselbe Wärme- und Exergiebilanz rechnen.
3. Generator-, Verdampfer- und Kondensatorströme sowie Hilfsstrom, Temperaturabstände und Wärmeabgabe ausweisen.
4. Investition, 25-Jahres-Barwert, Notstrom, Emissionen und Unsicherheit nach denselben Regeln wie H1 und H2 vergleichen.
5. Falls die Variante technisch ungeeignet ist, die Ablehnung mit Temperaturgrenzen, Leistungszahlen und Hersteller- oder Literaturstellen quantitativ belegen.

### 2. Die reale Abgabe ist noch nicht vorbereitet

`TEST-K31pro-max` ist ausdrücklich nur eine Testkennung. Außerdem erklärt das Paket, dass keine menschliche Fachprüfung oder Einreichung stattgefunden hat. Diese offenen Schritte sind keine optionalen Verbesserungen, sondern Voraussetzungen für die tatsächliche schriftliche Runde.

Belegorte:

- Deckblatt auf PDF-Seite 1 und `report/main.tex:19`
- `README.md:43-45,55-59`
- `PROVENANCE.md:42-44`
- Anhang A auf PDF-Seite 12

Korrektur:

1. Offizielle Team-ID in Dateiname und Deckblatt einsetzen.
2. Berechtigte Teammitglieder müssen wissenschaftliche Inhalte, KI-Erklärung und Rechte prüfen und die erforderlichen Erklärungen abgeben.
3. Nach der Änderung PDF und alle Seitenbilder erneut erzeugen und prüfen.
4. Nur die finale PDF-Datei über den offiziell bestätigten Kanal und innerhalb der bestätigten Frist einreichen. Die FAQ schließt Extramaterial aus. Modell, README und Referenz-PDFs bleiben Reproduktionsunterlagen, keine Abgabebestandteile.

## Restrisiken und möglicher Dissens

- Die Lösung erfasst nur einen nachgewiesenen betroffenen Strom bis 4,7 m³/s und höchstens 100 °C. Für 32,7 m³/s wären 12,48 GW nötig. Karstwege und betroffener Anteil sind nicht feldkalibriert. Belege: PDF-Seiten 2, 8 und 9, `results.json:169,210-218`.
- Standort, Netz und Herstellerdaten fehlen weiterhin. Zwei Netzeinspeisungen mit je 234,3 MW, 8,41 ha Servicefläche, 112.110 m³/s Luft und 2.869 m³ Diesel sind Szenarioanforderungen, keine Zusagen. Rückverwirbelung, Schall, Plume, Teillast und gemeinsame Ausfallursachen bleiben offen.
- Der p90-Ausfallfall hat nur 0,921 Minuten Differenz bis zur vollen Kühlung. Bei 10.000 m³ effektivem Volumen werden 26,4 °C und eine negative Differenz berechnet. Das ist ein Rechenszenario, keine Zuschaltprobe. Belege: PDF-Seite 7, `results.json:2110-2127`.
- Die Kosten bleiben Szenarien. Der Tarifproxy stammt aus dem Bereich 70 bis 150 GWh, während das Modell etwa 783 GWh pro Jahr verbraucht. Netzanschlusskosten fehlen. Der pauschale Aufschlag von 30 % auf ältere Kostenwerte ersetzt keine Angebote. Belege: PDF-Seiten 3 und 5, `data/parameters.yml:60,106-126`.
- Die Monte-Carlo-Verteilungen sind unkalibrierte Annahmen. Null Überlastfälle gelten nur innerhalb der künstlich begrenzten Verteilungen. Sie sind keine Extremwert- oder Dauerzusage.
- Der zweite Reviewer ist ein Same-Model-Kontext, keine unabhängige menschliche oder externe Prüfung. Auch die Archivreproduktion gilt nur in derselben Referenzumgebung und belegt keine Neuinstallation auf einem fremden Rechner. Belege: `review/model_configuration.md:11-13`, `review/rounds/round9/reproduction.md:26-28`.
- D4RT nutzt die Seitenfläche dichter und erklärt sein Verfahren stärker durch Grafiken. Ich werte den geringeren grafischen Erklärungsreichtum des Berichts als optionale Verbesserung, nicht als wesentlichen Mangel. Ein Prozessschema von Zufluss, Trockenkühlung, Kältemaschine, Rückführung und Luftsenke wäre die sinnvollste Ergänzung.
- Möglicher Dissens besteht darüber, ob die fehlende Absorptionsvariante nur ein optionaler Zusatz ist. Ich halte sie wegen des dominanten Strom- und Netzrisikos für materiell. Ebenso kann man menschliche Restaufgaben als außerhalb des Papers liegend behandeln. Kriterium 12a verlangt jedoch tatsächliche Abgabebereitschaft, deshalb ziehen sie hier ab.

## Fehlersuche für Bewertungen von 10

Keine Zeile erhält eine 10. Die gezielte Suche nach Fehlern führte zu zwei materiellen Befunden. Weitere Angriffe auf Wärmebilanzen, Kostenreihen, Monte-Carlo-Auswertung, analytische Ausfallrechnung, Quellen, PDF-Geometrie, Anonymität und Seitenbudget ergaben keine zusätzlichen wesentlichen Fehler. Eine 10 wäre daher nicht begründbar.

## Stoppurteil

Die Stoppregel ist auf dieser Revision nicht erfüllt. Meine Bewertungen für Kriterium 2, 3 und 12a liegen jeweils bei 8. Der unvollständige Alternativenvergleich und die fehlende tatsächliche Abgabevorbereitung sind ungelöst. Damit scheitert die Regel bereits an meinem Votum, unabhängig von der Bewertung des anderen Reviewers.
