## Prüfrahmen

Geprüft wurde ausschließlich Commit `77c1f972df9c67a00354e395ce31f27fd0c1b95c`. Alle 136 Dateien stimmen mit den SHA-256-Hashes in `review/rounds/round3/revision.json` überein. Seitenangaben bezeichnen physische PDF-Seiten.

Die Prüfung umfasste den vollständigen Quelltext und die Modellergebnisse, alle gerenderten Berichtsseiten und Folien, die D4RT-Referenzbilder, die MP4 samt Streams und Frames, Sprechtext, VTT, Zeitnachweise und alle 27 Juryfragen. Ich führte die zehn Modelltests mit deaktiviertem Bytecode-Schreiben aus, rechnete zentrale Größen unabhängig nach, prüfte die komplette Videodekodierung und gleichte zentrale Quellen sowie die aktuellen [Berichtsvorgaben](https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Vorgaben-Bericht.pdf), [Teilnahmebedingungen](https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Teilnahmebedingungen.pdf) und die [offizielle Startseite](https://www.planet-simtech.de/) ab.

## Bewertung

| Kriterium | Note | Begründung und genaue Belege | Erforderliche Korrektur |
|---|---:|---|---|
| 1. Qualität der Argumentation | 8 | Die Kette von vollständiger Wärmeerfassung über zweistufige Kühlung bis zur externen Senke ist schlüssig. Bericht PDF-S.4 bis 7, Gleichungen 1 bis 10, und die Trennung von Siedeschutz und 9-°C-Ziel sind überzeugend. Der Ausfall wird jedoch nur für den Mittelstrom gerechnet, und Abbildung 3 zeigt nicht die tatsächlich installierte Endkapazität. | M2 und M3. |
| 2. Vorgehen und Methodik | 8 | `docs/hypothesen.md` dokumentiert sieben Ansätze vor der quantitativen Auswahl. Modell, Sensitivität, Monte-Carlo-Rechnung und zehn erfolgreiche Tests sind nachvollziehbar. `model/core.py:60-81` schließt Kondensator- und Hilfsenergie korrekt ein. Der p90-Ausfall und eine Konvergenzprobe dieses Falls fehlen. | M2, einschließlich Zeitschritt- und Referenzprüfung. |
| 3. Qualität der vorgeschlagenen Lösung | 8 | H1 erfüllt die Energiebilanz innerhalb der erklärten Hülle und vermeidet offenen Wasserverbrauch. Reserve, Notstrom und Hochwassergrenze sind sichtbar. Die vollständige Karsterfassung, 8,19 ha Luftsenke, zweimal 182,7 MW Netzleistung und Genehmigung sind aber nicht nachgewiesen. Bericht PDF-S.6 und 7, Abschnitte 4.2 und 4.3. | M5. Die bedingte Szenariolösung ist brauchbar, aber noch keine nachweisbar realisierbare Dauerlösung. |
| 4. Mathematische und wissenschaftliche Modellierung | 8 | Meine Nachrechnung bestätigt 877,781145 MW, 1793,726688 MW, 2152,472026 MW installierte Kapazität, 967,163634 MW Wärmeabgabe, 2.236.544,98 Liter Diesel und die Barwerte. `output/model/results.json`, Schlüssel `baseline`, `design` und `validation`. Der dynamische Test verwendet in `model/validation.py:56-88` dagegen nur 2,3 m³/s und 877,8 MW. | M2. Zusätzlich temperaturabhängige Enthalpien nach IAPWS für die Endauslegung verwenden. |
| 5. Ableitung neuer Ansätze | 9 | `docs/hypothesen.md:3-59` enthält eine eigenständige Hypothesenbildung vor Recherche und Auswahl. H1 wird erst nach der Wärmebilanz vom Teilkreislauf zum Vollstrom skaliert. `PROVENANCE.md`, `EXCLUSION_LOG.md` und `decisions.tsv` dokumentieren Herkunft und Ausschlüsse. Weltweite Neuheit wird zutreffend nicht behauptet. Frühere Lösungsinhalte waren auch in meiner Prüfung nicht beteiligt. | Keine materielle Korrektur erforderlich. Die Unabhängigkeit beruht weiterhin auf Protokollen, nicht auf einem externen Clean-room-Audit. |
| 6. Wissenschaftliche Qualität | 8 | NIST, Fan et al., BDEW, UBA und die offiziellen Regeln bestätigen die zentralen Eingangswerte. Quellenregister und Trennung von Messwerten, Prämissen und Annahmen sind gut. Feldvalidierung, Herstellerkurven und ein empirisches Extremwertmodell fehlen. Die Dreiecksverteilung endet bei 4,7 m³/s, weshalb die null Überlastfälle keine unabhängige Sicherheitsaussage liefern. Bericht PDF-S.7 und 13. | M2 und M5. Die Verteilung durch gemessene Abflussdaten oder eine begründete Extremwertverteilung ersetzen. |
| 8. Klare Erklärung | 8 | Annahmen, Methoden und Schlussfolgerungen sind überwiegend gut getrennt. Die gerenderte Zusammenfassung verliert jedoch Text, und Folie 6 verbindet den Mittelstrom-Höchstwert unmittelbar mit p90-Notstrom, ohne die Fälle sauber zu markieren. PDF-S.2, `presentation/main.tex:122-138`, `presentation/jury_qa.md:63-67`. | M1, M2 und M3. |
| 9. Kritische Diskussion | 8 | Hochwasser, Wärmerückfluss, Standort, Genehmigung, COP, Kosten, CO₂, H2-Wasserverbrauch und reiner Siedeschutz werden offen diskutiert. Besonders klar sind Bericht PDF-S.7 und `presentation/jury_qa.md:83-165`. Der Auslegungsfall p90 fehlt aber gerade beim dynamischen Ausfall. | M2. Die Begriffe „Reserve“ und „begrenzte Stichprobe“ durch die konkreten p90-Ergebnisse ergänzen. |
| 10. Berichtsstruktur und Juryführung | 8 | Pflichtaufbau, Ergebnislogik und Schlussfolgerung sind vorhanden. Der Textverlust in der Zusammenfassung, die nicht eindeutige Kapazitätsgrafik und große ungenutzte Flächen erschweren die Juryführung dennoch. PDF-S.2, 8, 11, 12 und 13. | M1, M3 und M4. |
| 11. Format, Zitation und D4RT-Vergleich | 7 | A4, 13 Seiten, sieben Haupttextseiten, fünf Seiten für Literatur und Anhang, mindestens 26 mm Textrand, eingebettete Times-kompatible Schriften, numerische Verweise und KI-Offenlegung sind bestätigt. Die Zusammenfassung ist jedoch beschädigt und sehr fachsprachlich. Gegen `d4rt_page01.png`, `d4rt_page02.png` und `d4rt_page06.png` wirken Berichtsseiten 8, 11 und 13 schlecht genutzt; mehrere Diagrammbeschriftungen sind klein. | M1, M3 und M4. |
| 12a. Bereitschaft für die schriftliche Runde | 7 | Das PDF existiert und viele formale Prüfungen bestehen. Es ist aber keine fehlerfreie Abgabedatei: Ein Absatz der Zusammenfassung ist abgeschnitten, der p90-Ausfall fehlt, und die Kapazitätsgrafik ist mehrdeutig. Offizielle Team-ID und menschliche Fachprüfung fehlen weiterhin, siehe `README.md:44` und `PROVENANCE.md:41-43`. | M1 bis M6, danach PDF und Quelltext erneut gegen den tatsächlichen Renderabdruck prüfen. |
| 12b. Bereitschaft für die Finalrunde | 8 | Zehn fertige Folien, echte MP4, Sprechtext, 27 adversariale Fragen und Revisionszuordnung liegen vor. Die MP4 dauert 290,025458 s, hat H.264/AAC, 1920 x 1080, SAR 1:1, DAR 16:9 und 8.699 Frames; die vollständige Decodierung war fehlerfrei. Die Echtzeitprobe dokumentiert 289,46 s. Inhaltlicher p90-Fehler, nur wortproportional verteilte VTT-Zeiten und fehlende menschliche Probe verhindern eine 9. | M2 und M6. |

## Materielle Mängel und konkrete Korrekturen

### M1. Die Zusammenfassung ist im tatsächlichen PDF beschädigt

Auf PDF-S.2 endet der erste Absatz nach „mit weiteren 20“. Es fehlen „% Kapazitätsreserve ausgelegt.“ und der vollständige Satz zur Trennung von Jahresbetrieb und installierter Kapazität. Der Verlust ist sowohl im Renderbild als auch in der PDF-Textextraktion sichtbar.

Die Ursache steht in `report/main.tex:30`: Das Prozentzeichen ist nicht escaped und kommentiert den Rest der langen Quellzeile aus. Die automatische Prüfung in `scripts/verify_report.py` erkennt dies nicht, weil sie nur ausgewählte Begriffe und Geometrie kontrolliert.

Korrektur: `20 \%` schreiben, Bericht neu erzeugen und die vollständige Zusammenfassung per Textextraktion und Sichtprüfung bestätigen. Gleichzeitig die Zusammenfassung stärker in verständliche Sprache bringen, weil die offiziellen Vorgaben ausdrücklich eine für Außenstehende verständliche Kurzfassung verlangen.

### M2. Der dynamische Ausfalltest deckt den Auslegungsfall p90 nicht ab

`model/validation.py:56-88` verwendet den Mittelstrom von 2,3 m³/s und `final_q` mit 877,8 MW. Die Werte 12,6 °C, 23 Minuten und 13,3 Minuten in Bericht PDF-S.6, Folie 6 und Q&A 10 und 24 gelten daher nicht für 4,7 m³/s.

Meine unabhängige Rechnung mit derselben Differentialgleichung, 5 min Rampenbeginn und voller Kühlleistung nach 10 min ergibt für 4,7 m³/s und 1793,726688 MW:

- Höchstwert 16,2044656 °C statt 12,6447637 °C.
- Ungekühlte 20-°C-Zeit 11,4213539 min statt 23,3392884 min.
- Differenz bis zur vollen Kühlleistung 1,4213539 min statt 13,3392884 min.

Eine zweite Integration mit `solve_ivp`, RTOL und ATOL `1e-11`, bestätigte diese Werte. Die genannten 13,3 Minuten sollten zudem nicht als verbleibende dynamische Zeitreserve dargestellt werden. Sie sind nur die Differenz zwischen ungekühlter Alarmzeit und dem Zeitpunkt voller Kühlleistung.

Korrektur: Fluss und Kühlleistung im Ausfallmodell parametrisieren, Mittelstrom und p90 getrennt ausweisen, Folie 6 und Q&A entsprechend kennzeichnen und eine Zeitschrittstudie ergänzen. Die zeitliche Abfolge von Detektion, Generatorstart und Lastrampe muss ebenfalls eindeutig sein.

### M3. Abbildung 3 zeigt eine andere Kapazität als der Text

`model/run_all.py:278-286` zeichnet `stage.total_mw * 1.2` ohne den p90-Faktor `4,7/2,3`. Die Linie endet deshalb bei 1053,337 MW. Bericht und Zusammenfassung nennen dagegen 2152,472 MW installierte Endkapazität. Die Bildunterschrift in Anhang C, PDF-S.12, sagt lediglich, p90 werde „zusätzlich skaliert“, zeigt diese installierte Kapazität aber nicht.

Korrektur: Die Mittelstromlinie ausdrücklich „Mittelstrom plus 20 %“ nennen und eine zweite Linie „p90 plus 20 %, installiert“ bei 2152,5 MW einzeichnen. Alternativ nur die tatsächliche Auslegungskapazität darstellen. PDF und Zahlen müssen danach übereinstimmen.

### M4. Der direkte D4RT-Vergleich fällt nicht zugunsten des Berichts aus

D4RT Seiten 1, 2 und 6 integrieren große Abbildungen und Tabellen wesentlich dichter. Der Bericht lässt auf PDF-S.8, 11 und 13 jeweils etwa die halbe Seite oder mehr frei. Einzelne Diagrammbeschriftungen auf PDF-S.5, 12 und 13 sind zudem deutlich kleiner als der Fließtext. Das verletzt nicht das Seitenbudget, erreicht aber nicht den erklärten visuellen Qualitätsmaßstab.

Korrektur: Die freien Flächen für den p90-Ausfall, eine eindeutige Modul- und Kapazitätstabelle und größere Diagrammbeschriftungen nutzen. Anhang und Schlussbereich neu umbrechen, ohne die offiziellen 12-pt-Textanforderungen oder Seitenränder zu schwächen.

### M5. Zentrale Realisierungsnachweise bleiben offen

Das Paket nennt diese Grenzen ehrlich. Sie bleiben dennoch substanzielle Einwände gegen eine Bewertung von 9 für Lösung und Wissenschaftlichkeit:

- Vollständige Erfassung der betroffenen Karstströmung, Bericht PDF-S.5 und 7.
- Geeigneter Standort mit 8,19 ha, Luftführung, Schall und Rückverwirbelung, PDF-S.6.
- Zwei unabhängig nutzbare Netzeinspeisungen mit je 182,7 MW.
- COP 4 ohne Herstellerkurve, `data/parameters.yml:45-76`.
- Empirische Hochwasser- und Ausfallverteilung statt einer bei 4,7 m³/s abgeschnittenen Dreiecksverteilung.

Korrektur: Tracer- und Durchflussmessungen, Pilotkreislauf, Standort- und Netzprüfung sowie Herstellerdaten einholen und das Modell damit neu rechnen. Falls diese Nachweise nicht möglich sind, muss das Ergebnis ausdrücklich als begrenzte Szenariostudie statt als nachweisbar umsetzbare Dauerlösung bewertet werden.

### M6. Menschliche und technische Abgaberestaufgaben sind noch nicht erledigt

Die VTT-Zeiten sind nur proportional zur Wortzahl verteilt, `presentation/rehearsal.md:21-23`. Eine menschliche Live-Probe, verbindliche Medienfreigabe, offizielle Team-ID und Prüfung der Finalisten-E-Mail fehlen, `presentation/rights.md:26-28` und `PROVENANCE.md:41-43`.

Korrektur: VTT manuell oder durch Forced Alignment zeitlich prüfen, Sprechverständlichkeit mit Menschen testen, Rollen und Live-Technik proben, Rechte und synthetische Stimme freigeben, offizielle Team-ID einsetzen und die Finalisten-E-Mail auf Container, Codec, Dateiname und Abgabeweg prüfen.

## Restrisiken und Dissens

- Der 32,7-m³/s-Fall ist mit 12,48 GW ausdrücklich nicht abgedeckt. Auch ein später Anstieg über 100 °C oder ein anderer betroffener Stromanteil erfordert einen neuen Entwurf.
- Die Kosten bleiben Szenarien. Einzelhändlerpreis, Literatur aus 2012 und frei angesetzte Trockenkühler-, Tiefbau-, Notstrom- und Wasserpreise tragen keine belastbare Investitionszusage.
- Ideale Beckenmischung, konstante Stoffwerte und ein konstanter COP sind erste Näherungen, keine standortbezogene Validierung.
- `review/rounds/round3/reproduction.md` belegt eine Archivreproduktion durch den implementierenden Agenten. Ich habe wegen des Read-only-Verbots keinen Build ausgeführt und bestätige diese Reproduktion daher nicht unabhängig.
- `compliance/checklist.md` bewertet die schriftlichen Anforderungen als erfüllt. Dem widerspreche ich für die tatsächlich beschädigte Zusammenfassung und den visuellen D4RT-Vergleich.
- `review/revisions.md` dokumentiert viele wirksame Korrekturen, darunter COP, Tarif, H2-Kältestufe, Standort-Screening und Prozentformat. Die Behauptung behobener visueller Restfehler ist nach M1 und M3 nicht vollständig bestätigt.
- Eine menschliche Hörprüfung von Aussprache und Satzrhythmus fand nicht statt. Ich prüfte nur Streams, Frames, Sprechtext, Dauer und Pegel. Der Mittelpegel beträgt -17,3 dB, der Höchstpegel -1,2 dB; längere Pausen über 1,5 s bei -45 dB wurden nicht gemeldet.
- Frühere Rohbewertungen und Scorecards blieben ungelesen. Während der Prüfung erschienen `deepseek.md` und `deepseek_result.json` als neue unversionierte Dateien. Ich habe sie nicht geöffnet oder verwendet. Auf offiziellen Seiten waren lediglich Archivhinweise und frühere Aufgabenmottos sichtbar, keine Lösungsinhalte.
- Die Review-Unabhängigkeit bleibt auf getrennte Kontexte desselben Modells begrenzt. Sie ersetzt keine externe menschliche Fachprüfung.

## Vergabe von 10 Punkten

Keine Bewertung beträgt 10. Die substanzielle Fehlersuche war nicht erfolglos: Sie fand den PDF-Textverlust, den fehlenden p90-Ausfalltest und die abweichende Kapazitätsgrafik. Daher gibt es keine erfolglose Fehlersuche zu dokumentieren, die eine 10 rechtfertigen würde.

## Urteil zur Stoppregel

**Die Stoppregel ist auf dieser Revision nicht erfüllt.** Nur Kriterium 5 erreicht 9. Alle anderen Einzelbewertungen liegen darunter. Hinzu kommen substanzielle Einwände gegen die Ausgabeintegrität, die Vollständigkeit der Ausfallmodellierung und die tatsächliche Abgabebereitschaft.

Eine neue gemeinsame Revision muss mindestens M1 bis M3 schließen, die offenen Realisierungs- und Abgaberestaufgaben korrekt ausweisen und anschließend erneut von beiden Reviewern mit mindestens 9 in jedem Kriterium bestätigt werden.