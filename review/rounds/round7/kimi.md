# Rohbericht zu Runde 7

**Commit:** `a405cd19f187e2e6c80b51453617a6b6d883ae2a`
**Bewertungsgegenstand:** ausschließlich das Research-Paper-Paket.
**Seitenangaben:** physische PDF-Seiten einschließlich Deckblatt. Die gedruckte Foliennummerierung beginnt auf PDF-Seite 2 mit Seite 1.

Geprüft wurde :codex-file-citation{path="/Users/macbook_air_m1/.t3/scratch/2026-11-07-create-a-new-separate-github-162aa05c/planet-simtech-2025-TEST-K31pro-max/output/pdf/TEST-K31pro-max.pdf" purpose="source"} mit allen zwölf gerenderten Einzelseiten und der Kontaktübersicht. Zum direkten Layoutvergleich dienten die D4RT-Seiten 1, 2 und 6 sowie :codex-file-citation{path="/Users/macbook_air_m1/.t3/scratch/2026-11-07-create-a-new-separate-github-162aa05c/planet-simtech-2025-TEST-K31pro-max/sources/D4RT_paper.pdf" purpose="source"}.

Frühere Rohreviews und Scorecards habe ich nicht gelesen. Der andere Reviewer wurde nicht kontaktiert. Im Repository wurden keine Dateien verändert, keine Builds ausgeführt und kein Git-Zustand verändert.

## Einzelbewertungen

| Kriterium | Bewertung | Begründung und genaue Belegorte |
|---|---:|---|
| 1. Qualität der Argumentation | **9** | Die Argumentation folgt konsequent der Energiebilanz. Durchströmung und Speicherung, ökologischer Normalzustand und reiner Siedeschutz sowie Lösung und Auslegungsgrenzen werden sauber getrennt. Belege: PDF 2 bis 4, §§1 bis 3, Gleichungen 1, 5 und 6; PDF 8 bis 9, §§5 und 6. Der neue COP-Einwand betrifft die Dimensionierung, nicht diese Grundlogik. |
| 2. Vorgehen und Methodik | **8** | Quellenwahl, Alternativenvergleich, Deterministik, Monte-Carlo-Analyse und Falsifikationsplan sind methodisch stark. Die Unsicherheitsprüfung kontrolliert jedoch nur die thermische Kühlleistung, nicht die bei niedrigem COP ebenfalls begrenzte elektrische Leistung und Wärmesenke. Belege: PDF 8, §4.4; `model/run_all.py:104-137`, `model/run_all.py:208-222`, `model/run_all.py:441-452`; `output/model/results.json:2104-2115`. |
| 3. Qualität der vorgeschlagenen Lösung | **8** | Die zweistufige geschlossene Kühlung mit externer Wärmeabgabe beantwortet die Aufgabe physikalisch passend. Netz und Ersatzstrom sind aber am deklarierten Rand von Abfluss und COP nicht ausreichend dimensioniert. Bei 4,7 m³/s und COP 3,0 sind 234,336 MW statt der ausgelegten 182,651 MW erforderlich. Belege: PDF 4, §3.2; PDF 7, §4.2; `output/model/results.json:184-202`; `data/parameters.yml:126-136`. |
| 4. Mathematische und wissenschaftliche Modellierung | **8** | Die geprüften Wärme-, Kosten-, Mischungs- und Ausfallbilanzen sind rechnerisch korrekt. Das Modell enthält jedoch keine Begrenzung oder Überlastauswertung für elektrische Leistung und Wärmesenke über die COP-Ziehungen. `design_overload_fraction = 0` gilt ausschließlich für `cooling_mw`. Belege: `model/core.py:60-81`; `model/run_all.py:104-137`, `model/run_all.py:216-222`, `model/run_all.py:449-452`. |
| 5. Ableitung neuer Ansätze | **9** | Sieben physikalisch verschiedene Ansätze wurden vor der quantitativen Auswahl registriert, anschließend mit einheitlicher Wärmebilanz bewertet. H1 wird aus einem Teilkreislauf erst nach der Vollstrombilanz skaliert. Eine weltweite Neuheit wird zutreffend nicht behauptet. Belege: `docs/hypothesen.md:3-59`; `docs/alternativenvergleich.md:9-67`; PDF 3, §2.1; `PROVENANCE.md:3-24`. |
| 6. Wissenschaftliche Qualität | **8** | Zentrale externe Angaben und die Rechenkette ließen sich bestätigen. Die ungeprüfte elektrische Kapazität innerhalb der eigenen Unsicherheitshülle bleibt jedoch ein wissenschaftlicher Modellierungsmangel. Belege: PDF 3, Tabelle 1; PDF 8, §4.4; `output/model/results.json:2104-2162`; unabhängige Rand- und Stichprobenrechnung unten. |
| 8. Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen | **9** | Messwerte, Szenarioprämissen und technische Annahmen werden ausdrücklich unterschieden. Zusammenfassung, Methodik, Ergebnisse und Schlussfolgerung sind verständlich und decken die wesentlichen Grenzen auf. Der COP-Bereich und die Referenzauslegung sind dokumentiert; ihr nicht ausgewerteter Zusammenhang ist ein fachlicher Mangel, keine allgemeine Unverständlichkeit. Belege: PDF 2, Zusammenfassung; PDF 3, Tabelle 1; PDF 5, §3.3; PDF 9, §6. |
| 9. Kritische Diskussion der Ergebnisse | **8** | Hochwasser, Standort, Netz, Karst, Kosten, Wasserbedarf, Emissionen, Notstrom und externe Validierung werden kritisch behandelt. Gerade bei der eigenen Unsicherheitsanalyse fehlt aber die Diskussion elektrischer Überlastungen bei niedrigem COP. Belege: PDF 7 bis 9, §§4.3 bis 6; `output/model/results.json:2112-2115`. |
| 10. Berichtsstruktur und Nachvollziehbarkeit | **9** | Der Pflichtaufbau ist eingehalten. Gleichungen, Tabellen und Abbildungen haben Textverweise, und die Argumentation bleibt für die Jury nachvollziehbar. Alle zwölf Seiten sind geordnet und lesbar. Belege: PDF 2 bis 9; Abbildungen 1 bis 3 auf PDF 5, 7 und 12; Tabellen 1 bis 4 auf PDF 3, 6 und 12; `report/main.tex:27-290`. |
| 11. Format, Zitation, Einreichungsanforderungen und D4RT-Vergleich | **9** | Für das definierte Testpaket sind Form und Zitation abgabereif: A4, 12 Seiten, Haupttext unter 10 Seiten, Literatur und Anhang auf PDF 9 bis 12, Zusammenfassung unter einer Seite, numerische Verweise, KI-Anhang und anonyme Metadaten. Der direkte D4RT-Vergleich bestätigt eine klare Typografie und Figurenintegration. D4RT bleibt bei großen Schaubildern dichter und gestalterisch ausgefeilter, ohne dass hieraus ein Regelverstoß entsteht. Belege: `report/preamble.tex:1-50`; PDF 9 bis 12; `compliance/layout_referenz.md:5-28`; unabhängige PDF-Geometrie unten. |
| 12a. Bereitschaft für die schriftliche Runde | **8** | Artefakte und Archivreproduktion sind überzeugend dokumentiert. Der offene Kapazitätsbefund verhindert jedoch die fachliche Stoppbereitschaft. Für eine reale Abgabe fehlen zusätzlich offizielle Team-ID, menschliche Fachprüfung und die abschließenden Erklärungen. Belege: `review/rounds/round7/reproduction.md:3-28`; PDF 2, Zusammenfassung; PDF 11, Anhang A; `README.md:43-59`. |

## Materielle Mängel und konkrete Korrekturen

### M1: Elektrische Leistung und Wärmesenke werden nicht über den deklarierten COP-Bereich ausgelegt

Der Bericht deklariert eine COP-Dreiecksverteilung von 3,0 bis 6,5. Gleichzeitig bleiben Netzanschluss, sechs erforderliche Aggregate, Dieselvorrat und Luftsenke auf den Referenzfall COP 4,0 ausgelegt.

**Belege:**

- COP-Bereich: PDF 8, §4.4; `data/parameters.yml:133-136`.
- Elektrische Referenzauslegung mit 182,651 MW: `output/model/results.json:184-202`.
- Sechs Aggregate plus Reserve und zwei Netzeinspeisungen: PDF 7, §4.2; `data/parameters.yml:73-88`.
- Die Monte-Carlo-Auswertung bildet nur `q_samples` und deren thermische Überlast ab: `model/run_all.py:208-222`, `model/run_all.py:441-452`.
- `coupled_npv()` berechnet den Strombedarf für die Kosten, prüft aber keine Kapazitätsgrenze: `model/run_all.py:104-137`.

Meine read-only Auswertung mit dem vorhandenen Seed `20261107` ergab:

- **62 von 10.000 Ziehungen**, also **0,62 %**, überschreiten die elektrische Auslegung von 182,651 MW.
- Das Stichprobenmaximum beträgt **211,546 MW**. Sieben Aggregate kämen rechnerisch auf **213,093 MW**, dann aber ohne Ersatzaggregat.
- Am ausdrücklich zugelassenen Rand **4,7 m³/s und COP 3,0** werden **234,336 MW** benötigt. Das sind **128,3 %** der Netzauslegung und mehr als die rechnerische Leistung aller sieben Aggregate.
- Die erforderliche Wärmeabgabe beträgt dort **2028,062 MW** statt der ausgelegten **1976,378 MW**.
- Auch bei der Wärmesenke überschreiten drei Stichproben die Referenzauslegung.

Die vorhandene Kennzahl `design_overload_fraction = 0` ist dabei nicht falsch berechnet. Sie bezieht sich nur auf die thermische Kühlleistung. Der Mangel ist die fehlende zweite Kapazitätsprüfung.

**Korrektur:**

1. Für elektrische Leistung und Wärmesenke einen eigenen Auslegungspunkt bei 4,7 m³/s und dem deklarierten minimalen COP 3,0 berechnen. Alternativ muss der zulässige Betriebsbereich ausdrücklich auf COP-Werte begrenzt werden, bei denen die vorhandene Auslegung ausreicht.
2. Netzanschlüsse, Aggregatzahl und -leistung, Dieselbedarf, Face- und Servicefläche auf diesen Rand auslegen.
3. In der Monte-Carlo-Auswertung `electricity_mw` und `air_rejection_mw` gegen die installierten Grenzen prüfen und getrennte Überlastanteile ausweisen.
4. Modelltests für den Rand 4,7 m³/s und COP 3,0 sowie für die Reserveanforderung ergänzen.
5. Ergebnisse, PDF §§3.2, 4.2 und 4.4 sowie gegebenenfalls Investition, Betriebskosten und Zusammenfassung aktualisieren.

### M2: Reale Wettbewerbsabgabe ist noch nicht durchgeführt oder freigegeben

Dieser Punkt betrifft die tatsächliche Einreichung, nicht die Qualität des Testpakets.

**Belege:**

- Testkennung statt offizieller Team-ID: PDF 1 und Dateiname; `README.md:45`.
- Keine menschliche Fachprüfung: PDF 2, Zusammenfassung; PDF 11, Anhang A; `PROVENANCE.md:42-44`.
- Vor Abgabe offene Inhalts-, Rechte- und Erklärungsprüfungen: PDF 11, Anhang A; `README.md:55-59`.
- Die [offiziellen Berichtsvorgaben](https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Vorgaben-Bericht.pdf) verlangen Team-ID und Verantwortung für die KI-Ausgaben. Die [Teilnahmebedingungen](https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Teilnahmebedingungen.pdf) verlangen ein registriertes Team und die eigenständige Abgabe durch dieses Team.

**Korrektur:**

Nach Behebung von M1 muss ein berechtigtes Team den vollständigen Bericht fachlich prüfen, die Testkennung in Deckblatt und Dateiname durch die offizielle ID ersetzen, Rechte und Erklärungen bestätigen und den aktualisierten menschlichen Prüfstatus wahrheitsgemäß dokumentieren. Anschließend sind Abgabefrist und Kanal anhand der Team-E-Mail zu prüfen. Die KI-Offenlegung muss erhalten bleiben.

## Durchgeführte Gegenprüfungen

### Revision und Archivreproduktion

- HEAD entspricht dem Zielcommit.
- 128 Dateien außerhalb früherer Reviewrunden stimmen byteweise mit den SHA-256-Hashes der eingefrorenen `revision.json` überein.
- Alle 43 Einträge des Modellmanifests stimmen mit den vorhandenen Dateien überein.
- Zwischen dem reproduzierten Kandidaten `1878af8f0a66802696b65243ea4db759fd40c919` und dem Zielcommit bestehen keine Änderungen am bewerteten Paperpaket.
- Der Reproduktionsnachweis dokumentiert 36 von 36 byteweise identischen Paperartefakten und 16 bestandene Modelltests: `review/rounds/round7/reproduction.md:3-28`.
- Der PDF-Hash ist `44a5751389b6ae580ba9d560ed6292867a78f188f035fb4e66705efa7bd80da7`.

Build, `make verify`, neue Archivkopie und die vollständige Unittest-Datei wurden wegen des Schreibverbots nicht erneut ausgeführt. Die Archivreproduktion wurde deshalb dokumentarisch und durch Hashvergleich geprüft, nicht neu aufgebaut. Sie belegt zudem nur dieselbe Referenzumgebung, keine Neuinstallation auf einem fremden Rechner.

### Unabhängige Modell- und Ergebnisprüfung

Ohne Schreibzugriffe wurden bestätigt:

- `877,781145 MW` Erwartungslast, `1793,726688 MW` p90-Last und `2152,472026 MW` installierte thermische Leistung.
- Trockenkühlung, Kältemaschinen, Kondensatorwärme, Hilfsenergie und externe Wärmeabgabe schließen die Energiebilanz.
- Dieselbedarf, Speichergrenze, Verdunstung, Zumischung, passive Fläche, Rohrdurchmesser und Hochwasserlast stimmen mit direkten Rechnungen überein.
- Eine frische Ausführung von `run_validation()` reproduziert die archivierten Werte, darunter `ode_max_error_k = 8,031904 × 10⁻¹⁰`, p90-Höchstwert `16,66377598 °C` und Konvergenzfehler `1,790568 × 10⁻¹² K`.
- Die unabhängige Diskontierung aller drei Alternativen stimmt mit den JSON-Barwerten überein.
- CSV und JSON enthalten 26 Jahreszeilen mit 25 tatsächlichen Betriebsjahren.
- Alle 10.000 archivierten Ziehungen und die ausgewiesenen Quantile lassen sich aus Seed und Verteilungen reproduzieren.

### PDF, Quellen und visuelle Prüfung

- Zwölf A4-Seiten, keine verschlüsselte oder beschädigte PDF.
- Kein Autorenmetadatum und keine Namens- oder Schulangabe im sichtbaren Paper.
- Kleinster gemessener Textabstand zu den Seitenrändern: etwa **25,997 mm**.
- Median der PDF-Textschrift: **11,955 pt**, entsprechend LaTeX 12 pt.
- Kleinste gemessene Diagrammglyphendimension: **12,685 pt**.
- Keine sichtbaren Kollisionen, abgeschnittenen Tabellen, fehlerhaften Glyphen oder unlesbaren Diagramme auf den zwölf Einzelseiten.
- 57 URI-Annotationen mit 26 unterschiedlichen HTTP-Zielen. Die Quellen 1 bis 25 werden einschließlich der Anhänge verwendet und sind dem Literaturverzeichnis zugeordnet.

Inhaltlich stichprobenartig bestätigt wurden:

- Fan et al.: Mittel 2,3 m³/s und tägliche 10-/90-Prozent-Quantile 0,7 und 4,7 m³/s, [KIT-Volltext](https://publikationen.bibliothek.kit.edu/1000163518/151549041).
- LGRB: HQ 32,7 m³/s für 1951 bis 2007 und Karststruktur, [LGRB-Fallbeispiele](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele).
- NIST: 999,702 kg/m³ und 4195,14 J/(kg K) bei etwa 10 °C; Sättigungspunkt 135,413 °C bei 3,17007 bar; Verdampfungsenthalpien 2425,056 und 2256,404 kJ/kg.
- BDEW: 138 €/MWh für 70 bis 150 GWh und 179 €/MWh für kleine bis mittlere Industrie, [BDEW-Strompreisanalyse](https://www.bdew.de/service/daten-und-grafiken/bdew-strompreisanalyse/).
- UBA: 363 g CO₂/kWh für 2024, [UBA-Datengrundlage](https://www.umweltbundesamt.de/themen/co2-emissionen-pro-kilowattstunde-strom-2024).
- LAWA: Temperaturänderungen sollten ±1 K/h nicht überschreiten, [LAWA-Bericht](https://www.laenderfinanzierungsprogramm.de/static/LFP/Dateien/LAWA/AO/O_10.20_211119_Endbericht_O10.20_TempEmpf_Fische.pdf).
- Die Produktseite des Wärmetauschers weist 6418,18 € Verkaufspreis und 8952,68 € regulären Preis bei 601 bis 700 kW aus. Der Ansatz von 15 €/kW ist als grober Listenpreisanker plausibel, nicht als Projektangebot.

## Nebenbefund ohne wesentliche Auswirkung

Das hydrostatische Beispiel ist geringfügig gerundet beziehungsweise nicht aus den deklarierten Konstanten reproduziert:

- Direkte Rechnung mit 999,702 kg/m³, 9,81 m/s² und 22 m: **3,17080686 bar**.
- Modellparameter und PDF 4, §3.1: **3,17007 bar**.
- Differenz: **0,00073686 bar**.

Fundorte: `data/parameters.yml:32-36`, `data/parameters.yml:72`; `model/run_all.py:382-383`.

Optional sollte der Druck aus denselben Konstanten neu berechnet und die zugehörige NIST-Abfrage aktualisiert werden. Auf die zentrale Kühlleistung oder den COP-Befund hat diese Differenz keine Auswirkung.

## Restrisiken und möglicher Dissens

- **Karst und Wärmeeintrag:** Betroffener Stromanteil, unterirdische Wege, Bathymetrie und lokale Wärmebilanz sind nicht feldkalibriert. Die Vollstromanlage ist deshalb ein Szenarioentwurf, keine bestätigte Standortlösung. Belege: PDF 2 bis 3, §2.1; PDF 8 bis 9, §5.
- **Technische Auslegung:** Herstellerkurven, Teillast, Pinch-Auslegung, Feuchtkugelstatistik, Rückverwirbelung, Schall und Plume fehlen weiterhin. Belege: PDF 4, §3.2; PDF 7, §4.3; PDF 9, §6.
- **Ausfallverhalten:** Beckenvolumen, Detektion, Generatorstart und Wiederanlauf sind Annahmen. Der p90-Spitzenwert von 16,66 °C ist kein realer Zuschaltversuch. Gemeinsame Ausfallursachen bleiben offen. Belege: PDF 6 bis 7, §§4.1 und 4.2.
- **Hochwasser:** Für 32,7 m³/s wären 12,48 GW nötig. Dieser Fall ist ausdrücklich nicht abgedeckt. Temperaturen über 100 °C und zusätzliche Wärmequellen verlangen einen neuen Entwurf. Beleg: PDF 8, §4.4.
- **Kosten:** Tarif, Investitionen, Ersatz, Wartung und Verfügbarkeit sind Szenarien ohne Angebote. Netzanschlusskosten fehlen. Die Zahlen sind keine Wirtschaftlichkeitszusage.
- **Reproduktion:** Der Nachweis verwendet eine verknüpfte Referenzumgebung. Neuinstallation, fremde Plattform und externe wissenschaftliche Validierung bleiben ungeprüft.
- **Unabhängigkeit:** Die Dokumentation ist konsistent und das Ausschlussprotokoll benennt frühere Expositionen. Die Nichtverwendung früherer Lösungen kann aus Dateien jedoch nicht abschließend bewiesen werden. Der Same-Model-Review ist keine menschliche oder externe Prüfung.
- **Möglicher Dissens zu M1:** Die ausgewiesene thermische Abdeckung ist korrekt. Man könnte COP 4,0 als getrennten Auslegungspunkt und niedrigere COP-Werte nur als Kostensensitivität lesen. Ich bewerte die fehlende Kapazitätsprüfung dennoch als wesentlich, weil der Bericht denselben fixen Anlagenverbund über den deklarierten COP-Bereich verwendet und die Dauerlösung auf Reserve und Notstrom stützt.
- **D4RT:** Die Referenz ist visuell dichter und bei komplexen Abbildungen ausgefeilter. Der Bericht erreicht mit seinen strengeren Rand- und Schriftvorgaben eine gute, aber schlichtere Ordnung. Das ist für mich kein wesentlicher Mangel.

## Fehlersuche bei Bewertungen von 10

Keine Zeile erhält eine 10. Die substanzielle Fehlersuche war erfolgreich und führte zu M1. Damit fehlt die für eine 10 erforderliche Begründung, warum kein wesentlicher Fehler verbleibt.

## Stoppregelurteil

**Die Stoppregel ist auf dieser Revision aus meiner Sicht nicht erfüllt.**

Die Kriterien 2, 3, 4, 6, 9 und 12a liegen unter 9. Mit M1 bleibt ein substanzieller Einwand gegen die vollständige Dimensionierung und die wissenschaftliche Unsicherheitsprüfung offen. Für die reale Auslieferung kommen mit M2 offene Team- und Freigabeschritte hinzu. Ein Gesamtstopp ist daher unabhängig vom unbekannten Urteil des anderen Reviewers nicht möglich.