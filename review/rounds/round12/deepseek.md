# Prüfbericht Runde 12

**Geprüfte Revision:** `a4005b20d5c19efcba1755ce6bd7b82eb1ecfc84`  
**Prüfumfang:** `revision.json` mit 215 Dateien, davon 215/215 SHA-256-Hashes identisch; PDF-Hash `003804f9...c27c0aa`; 14 PDF-Seiten. Kontaktübersicht und alle 14 Seitenbilder gesichtet, dazu D4RT S. 1, 2 und 6 als visueller Maßstab. Keine früheren Rohberichte, Scorecards, `review/README.md` oder `decisions.tsv` gelesen. Keine Repository-Datei geändert, keine Builds oder `make`-Läufe ausgeführt. `git status` zeigt nur die bereits vorhandenen, nicht versionierten Dateien `review/rounds/round12/prompt.md` und `revision.json`.

**Stichprobenprüfung der Kernquellen:** Die Werte 9 °C und 22 m sind bei [Stadt Blaubeuren](https://www.blaubeuren.de/Geopoint-Blautopf) bestätigt; 165 km², 2,3 m³/s sowie 0,7/4,7 m³/s bei [Fan et al. 2023](https://doi.org/10.1007/s10040-023-02703-9); 32,7 m³/s HQ bei [LGRB](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele). Die [NIST-Abfrage](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Type=IsoBar&Digits=6&P=1.01325&TLow=0&THigh=100&TInc=10&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm) bestätigt 999,702 kg/m³ und 4,19514 kJ/(kg K) bei 10,01 °C. Die [LAWA-Empfehlung](https://www.laenderfinanzierungsprogramm.de/static/LFP/Dateien/LAWA/AO/O_10.20_211119_Endbericht_O10.20_TempEmpf_Fische.pdf) nennt auf S. 10 tatsächlich “±1 K / h”. Die Stadtseite nennt 160 km², der Bericht mit [2,3] 165 km²; bei “etwa 165” ist das kein materieller Widerspruch.

## 1. Bewertungstabelle

| Kriterium | Bewertung | Kurze Begründung | Beleg |
|---|---:|---|---|
| **1. Qualität der Argumentation** | **9** | Die Kette von der Wärmebilanz über die Zielhierarchie 9 °C/Siedeschutz zu H1, H2, H3 und H8 ist konsistent. Die Alternativen werden physikalisch ausgeschlossen, der H1-vs-H2-Zielkonflikt wird offen gelegt. Kein logischer Bruch gefunden. | PDF S. 2-3 (Abschn. 1-2), S. 5-7 (Abschn. 3), S. 10-11 (Abschn. 5-6); `docs/alternativenvergleich.md`. |
| **2. Vorgehen und Methodik** | **8** | Sehr systematisch, aber die Prognose-Sensitivität hat kein einheitliches Bezugsjahr: Die Wärmeleistung wird im Siedejahr ausgewertet, der Barwert dagegen im 10-Jahres-Horizont. Dadurch zeigt Tabelle 3 für “Sieden nach 12 Jahren” +0,0 %, obwohl im 10. Jahr 731,5 MW nötig wären. | PDF S. 14, Tab. 3; `output/model/sensitivity.csv` Z. 5; `model/run_all.py` Z. 239; `report/generated/sensitivity.tex` Z. 8. |
| **3. Qualität der vorgeschlagenen Lösung** | **9** | H1 ist als modulare Vollstromkühlung mit Trockenkühlung, Kältemaschinen, p90-Auslegung, zwölf Strängen und externer Luftsenke technisch schlüssig. Die Lösung ist ausdrücklich ein bedingter Szenarioentwurf, keine Baufreigabe. H2, H3 und H8 werden nachvollziehbar verglichen. | PDF S. 4-8 (Abschn. 3), S. 11 (Abschn. 6); Tab. 2 und Tab. 5; `docs/alternativenvergleich.md`. |
| **4. Mathematische und wissenschaftliche Modellierung** | **8** | Energie-, Kondensator-, Kosten- und Monte-Carlo-Bilanzen sind konsistent; NIST-Werte und Handrechnung stützen die Kernleistung. Gl. (10) ist jedoch ohne Einheitenangabe mehrdeutig, und Tab. 3 mischt Siedejahr und 10-Jahres-Auslegung. | PDF S. 5-8 (Gl. 5-10), S. 14 Tab. 3; `report/main.tex` Z. 188; `model/validation.py` Z. 46; `model/core.py`. |
| **5. Ableitung neuer Ansätze statt Wiederverwendung vorhandener Ergebnisse** | **9** | Sieben Ansätze, H8-Ergänzung nach dem Council-Hinweis, eigene Herleitung aus Aufgabe, Quellen und Rechnung. Keine früheren Lösungen; keine weltweite Neuheit behauptet. Die Unabhängigkeit ist über Provenienz und Ausschlussprotokoll dokumentiert. | PDF S. 3 (Abschn. 2.1), S. 5-7; `docs/hypothesen.md`; `PROVENANCE.md`; `EXCLUSION_LOG.md`. |
| **6. Wissenschaftliche Qualität** | **8** | Das Kernmodell ist reproduzierbar, 23 Tests sind vorhanden, `validation.all_checks_passed` ist gesetzt, NIST und Monte Carlo stützen die Aussagen. Die 12-Jahres-Zeile in Tab. 3 ist jedoch wissenschaftlich nicht sauber basisiert; externe Feldvalidierung fehlt und wird transparent gemacht. | PDF S. 9-10 (Abschn. 4.4/5), S. 14 Tab. 3; `output/model/results.json`; `model/test_model.py`; `review/rounds/round12/reproduction.md`. |
| **8. Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen** | **8** | Annahmen, Methode, Ergebnisse und Grenzen sind sehr klar, mit Tab. 1, Tab. 2 und den Anhängen. Ausnahme: Tab. 3 nennt den Bezugszeitpunkt nicht und suggeriert +0,0 %; Gl. (10) nennt keine Einheit. | PDF S. 3-4 (Tab. 1), S. 8 Gl. (10), S. 14 Tab. 3; `report/main.tex` Z. 188/305. |
| **9. Kritische Diskussion der Ergebnisse** | **9** | Die Diskussion ist stark: Datenlücken, Standort, Netz, FFH, Ausfall, Volumenabhängigkeit, 32,7-m³/s-Grenze, fehlende Feldvalidierung und fehlende menschliche Prüfung werden offen benannt. Der eigene Tabellenfehler wird allerdings nicht reflektiert. | PDF S. 8-11 (Abschn. 4.3-6); `docs/alternativenvergleich.md`, Abschnitt “Standort und Falsifikation”. |
| **10. Klare Berichtsstruktur und für die Jury nachvollziehbare Argumentation** | **9** | Pflichtstruktur vollständig: Zusammenfassung, Einführung, Methode, Ergebnisse, Diskussion, Schlussfolgerung, Literatur und Anhang. Die Haupttextseiten 1-10 und die vier Seiten Literatur/Anhang liegen im Budget. Tabellen- und Einheitenprobleme sind Inhalts-, keine Strukturfehler. | PDF S. 1-14; `compliance/checklist.md`; `scripts/verify_report.py`; `review/rounds/round12/reproduction.md`. |
| **11. Format, Zitation und Einreichungsanforderungen, visuelle Qualität gegenüber D4RT** | **9** | A4, 26 mm Rand, 12 pt, zehn Haupttextseiten, vier Seiten Literatur/Anhang, 25 Quellen mit Abrufdatum, anonyme Metadaten und KI-Offenlegung. Die D4RT-Prinzipien sind übernommen, ohne deren 10-pt-/20,7-mm-Verstöße zu kopieren. Visueller Rest: S. 13 hat eine leere linke Spalte. | PDF S. 1, S. 10-14; `compliance/regeln.md`; `compliance/layout_referenz.md`; `review/rendered/d4rt_page01/02/06.png`; `review/rendered/report_pages/page-13.png`. |
| **12a. Bereitschaft für die schriftliche Runde** | **8** | Das Testpaket ist technisch weitgehend bereit und reproduzierbar; die bekannte Tabellen-/Einheitenlücke verhindert aber eine abgabefertige Freigabe. Offizielle Team-ID, menschliche Prüfung, Rechte und Einreichung bleiben offen und werden nicht als erledigt behauptet. | `review/rounds/round12/reproduction.md`; `revision.json`; `README.md`; `PROVENANCE.md`; PDF S. 13 Anhang A. |

## 2. Behebung der vorangegangenen Befunde

- **H2-Sensitivität 12,48/10,40 Mio. m³:** In Tab. 2 (PDF S. 7) und im Text S. 5 korrekt getrennt; die Kosten verwenden den vollständigen Zusatzwasserbedarf.
- **H3-Ausrüstung/Notstrom/95-Mio.-Fixkosten:** In Tab. 2 und auf S. 6-7 korrekt: H3 nur Pumpen, kein Notstromposten, 95 Mio. € Fixkostenbasis.
- **`\raggedbottom`/Anhang A:** Überdehnte Leerräume sind nicht mehr sichtbar; auf S. 13 bleibt jedoch eine unausgeglichene linke Spalte.
- **Tab. 1 COP/Strompreis und Luftzeile:** Auf S. 4 korrekt getrennt; die Luftbezeichnung bleibt in einer Zeile.
- **Tab. 4 mit \(Q\) und \(P_{el}\):** Auf S. 14 korrekt definiert.
- **Fünf Module bei etwa 98 %:** Auf S. 2 korrekt beschrieben.
- **39 Paperartefakte:** Die Hashes der betroffenen Dateien und Seitenbilder stimmen mit `revision.json` überein. Die Archivreproduktion selbst habe ich nicht erneut ausgeführt; sie ist nur über `reproduction.md` und die Hashübereinstimmung belegt.

## 3. Materielle Mängel

### M1, hoch: Tabelle 3 mischt Siedejahr und 10-Jahres-Auslegung

**Beleg:** PDF S. 14, Tab. 3; `output/model/sensitivity.csv` Z. 5; `report/generated/sensitivity.tex` Z. 8; `model/run_all.py` Z. 239; `report/main.tex` Z. 304/305.

**Befund:** Die Zeile “Sieden nach 12 Jahren” nennt 877,8 MW und +0,0 %. Dieser Wert gilt im **Siedejahr 12**, nicht im zehnten Jahr. Mit den versionierten Parametern gilt im zehnten Jahr:

\[
T(10)=9+\frac{91}{12}\cdot 10=84{,}833\ ^\circ\text{C}
\]

\[
Q(10)=9{,}646\cdot(84{,}833-9)=731{,}484\ \text{MW}
\]

Das sind **-16,7 %** gegenüber 877,8 MW, nicht +0,0 %. Der Barwert 4,055 Mrd. € ist für die 12-Jahres-Trajektorie korrekt; die Q-Spalte und die Prozentänderung sind es für die 10-Jahres-Auslegung nicht. Die Tabellenunterschrift sagt nicht, dass die Q-Spalte “im Siedejahr” gemeint ist. Damit ist die zentrale Prognose-Sensitivität für die Jury irreführend.

**Korrektur:** In `model/run_all.py` die Sensitivitätsgröße auf `required_cooling_mw(10.0, varied)` umstellen, oder die Spalte ausdrücklich “Q im Siedejahr” nennen und zusätzlich Q im 10. Jahr ausgeben. `sensitivity.csv`, `sensitivity.tex` und PDF neu erzeugen; Regressionstest ergänzen: `forecast_years=12` muss für Jahr 10 \(Q=731,5\) MW und \(-16,7\%\) liefern. Anschließend `revision.json` und PDF-Hash neu einfrieren.

### M2, mittel: Gl. (10) ist ohne Einheitenangabe dimensionslos mehrdeutig

**Beleg:** PDF S. 8, Gl. (10); `report/main.tex` Z. 188; `model/validation.py` Z. 46.

**Befund:** Die Gleichung lautet

\[
\frac{dT}{dt}=\frac{100-T}{\tau}-\frac{Q_{Kuehl}(t)}{\rho Vc_p}.
\]

Der Nenner \(\rho Vc_p\) hat die Einheit J/K. Im Bericht werden Wärmeströme sonst in MW angegeben. Der Code verwendet `cooling_mw * 1e6 / (rho V cp)`, also Watt. Ohne ausdrückliche Einheit ist die gedruckte Gleichung um den Faktor \(10^6\) falsch, je nachdem, ob \(Q_{Kuehl}\) als MW oder W gelesen wird.

**Korrektur:** Entweder \(Q_{Kuehl}(t)\) ausdrücklich in W definieren oder

\[
\frac{dT}{dt}=\frac{100-T}{\tau}-\frac{10^6\,Q_{Kuehl,MW}(t)}{\rho Vc_p}
\]

schreiben und die Einheiten von \(\rho\), \(V\), \(c_p\) und \(Q\) in einer Zeile nennen. Die Änderung ist rein redaktionell, muss aber neu gerendert und geprüft werden.

## 4. Restrisiken und Dissens

- **Dissens zu M1:** Wenn die Tabelle bewusst “im Siedejahr” auswertet, ist die Zahl 877,8 MW für diese Definition korrekt. Dann ist nicht die Zahl, sondern die fehlende Bezugsjahr-Angabe der Mangel; die Spalte “+0,0 %” bleibt für die 10-Jahres-Auslegung irreführend. Ich bewerte diese Mehrdeutigkeit als materiell, bis sie ausdrücklich aufgelöst ist.
- **Dissens zu M2:** Wenn \(Q_{Kuehl}\) als W gemeint ist, ist Gl. (10) korrekt; der Bericht sagt es aber nicht, und alle anderen Q-Werte stehen in MW. Die Einheitenlücke ist damit mindestens ein Erklärungsmangel.
- **Visueller Restpunkt:** Auf PDF S. 13 endet die linke Spalte nach “Kimi K3.1 Pro ... Grafiken”, während die rechte Spalte weiterläuft. Das ist kein Formverstoß, aber ein sichtbarer Unterschied zur dichten D4RT-Referenz. Eine Verschiebung der Handrechnung oder eines Absatzes in die linke Spalte, verbunden mit einer erneuten `\balance`-/`\raggedbottom`-Prüfung, würde die Seite ausgleichen.
- **Testkennung:** Auf dem Deckblatt steht “Team-ID: TEST-K31pro-max”, ohne den Zusatz “Testkennung”. Anhang A und die Checkliste legen die Kennung als vorläufig offen; das ist ausreichend, aber ein Zusatz “(Testkennung)” auf dem Deckblatt wäre klarer. Die offizielle Team-ID bleibt eine menschliche Restaufgabe.
- **Quellen [4]:** In der Literaturliste ist die NIST-URL auf `webbook.nist.gov/cgi/fluid.cgi` verkürzt; die vollständige Abfrage steht im Quellenregister. Für die Reproduktion ist das ausreichend, für eine strenge Zitationsprüfung wäre die vollständige URL in der Literaturliste besser.
- **160 vs. 165 km²:** Die Stadtseite nennt 160 km², [2,3] nennen 165 km². Der Bericht schreibt “etwa 165” mit [2,3]; das ist kein materieller Widerspruch, aber eine offene Quellenunschärfe.
- **38-°C-Luft:** Das Modell enthält eine Wetter-Sensitivität bis 38 °C, der Bericht legt die Auslegung aber auf 35 °C aus und stellt die 38-°C-Variante nicht dar. Das ist eine optionale Ergänzung, kein Widerspruch, weil 35 °C als technische Annahme offengelegt ist.
- **Nicht erneut ausgeführt:** `make verify`, `make model test report` und die `git archive`-Reproduktion habe ich nicht ausgeführt; die Hashübereinstimmung und die gerenderten Seiten sind geprüft, der Build-Erfolg ist nur über `reproduction.md` belegt. Das ist eine Prüfgrenze, kein festgestellter Paketfehler.
- **Externe Validierung:** Es gibt keine Feldmessungen, Herstellerkurven, Standort-, Netz- oder Karstdaten. Das ist im Bericht durchgehend als Grenze sichtbar und wird nicht als erledigt behauptet.
- **H1-vs-H2-Entscheidung:** Der geringere H2-Barwert wird nicht monetär gegen Wasser, Hygiene und Aerosolrisiken aufgerechnet. Der Bericht behandelt das als qualitativen Zielkonflikt; eine andere Gewichtung könnte H2 bevorzugen. Das ist eine offene Bewertungsfrage, kein Rechenfehler.
- **Kosten:** 500 €/kW Kälte, 120/80 €/kW Trocken-/Verdunstungskühlung, 60 % Aufschlag, 95 Mio. € Fixkosten und 20 % Reserve sind Szenarioannahmen. Sie sind als solche gekennzeichnet; externe Angebote fehlen.

## 5. Prüfung der 10er-Hürde

Ich habe **keine 10** vergeben. Damit entfällt eine gesonderte “erfolglose substanzielle Fehlersuche” für eine 10. Die 9en in den Kriterien 1, 3, 5, 9, 10 und 11 sind bewusst keine 10, weil M1 und M2 offen sind und die externe Feldvalidierung fehlt. Ein 10er-Nachweis würde einen dokumentierten, vergeblichen Versuch verlangen, die zentrale Energie-, Kosten- und Sensitivitätskette einschließlich der 12-Jahres-Tabelle zu falsifizieren; dieser Versuch ist mit dem vorliegenden Paket nicht geführt.

## 6. Abschließendes Urteil zur Stoppregel

**Auf dieser Revision ist die Stoppregel aus meiner Sicht nicht erfüllt.** Meine Bewertung enthält fünf Zeilen mit 8 (Kriterien 2, 4, 6, 8 und 12a) und sechs Zeilen mit 9. Mit M1 und M2 bleiben zwei ungelöste substantielle Einwände gegen Korrektheit und wissenschaftliche Qualität. Die zweite Reviewer-Spalte ist mir nicht bekannt; die Stoppregel verlangt mindestens 9 in jeder Zeile von beiden Reviewern und keine ungelösten substantiellen Einwände.

Die beiden Mängel sind mit überschaubarem Aufwand korrigierbar: Q in Tab. 3 auf das 10. Jahr beziehen oder das Bezugsjahr ausdrücklich benennen und die Q-Spalte entsprechend definieren; Gl. (10) mit Einheiten versehen; danach `make model test report`, `make review-package`, PDF-Hash und `revision.json` neu einfrieren und die betroffenen Seiten erneut prüfen. Erst danach wäre eine erneute Bewertung sinnvoll, die auf meiner Seite die 8er auf 9 heben könnte.
