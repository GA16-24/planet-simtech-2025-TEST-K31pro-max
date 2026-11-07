# Rohbericht DeepSeek-V4.1-Flash, Runde 1

Revision: `9b3a83bcea1358184b14de6759af117a049114f5`
Prüfmodus: read-only, keine Datei geändert.

Der Reviewer erklärte, keine andere Bewertung, Scorecard oder Review dieser Aufgabe gelesen zu haben. Er prüfte alle 116 Dateihashes erfolgreich, den Bericht, die Präsentation, die MP4 mit `ffprobe`, vollständige Decodierung, Streams, fünf Frames und Audiopegel, Modellcode, Parameter, Ergebnisse, Validierung, Entscheidungs- und Quellenregister, Compliance, Provenienz und Ausschlussprotokoll. Er rechnete zentrale Werte und Kosten unabhängig nach und prüfte Quellen stichprobenartig einschließlich DOI-Metadaten. Nicht geprüft wurden das Hören der Audioaufnahme, alle 22 Quellen im Einzelnen, die Rechtsquellen im Volltext, ein erneuter Build und die Aussprache der Sprechstimme.

## Bewertungen

| Kriterium | Note | Begründung und Beleg |
| --- | ---: | --- |
| 1 Argumentation | 8 | Tragfähige Energiekette, aber falscher Vergleich „mehr als doppelt so viel wie installiert“ und keine 1-K/h-Rechnung. PDF S. 2 bis 11, `report/main.tex` Z. 279, `model/run_all.py`. |
| 2 Methodik | 8 | Systematische Trennung, sieben Ansätze, gemeinsame Kostenregeln, Sensitivität und Validierung. Kostenquantile koppeln Abfluss nicht an Lastreihen, COP Punktwert, Kostenskalierung Screening. PDF S. 3 bis 11, Modellcode. |
| 3 Lösung | 7 | Physikalisch und ökologisch schlüssig, aber Ansaugung und Rückführung, 952 MW Luftabgabe, 74,2 MW Netzanschluss und 1-K/h-Nachweis nicht technisch durchbildet. PDF S. 6 bis 7, 10, 14 und Folie 5. |
| 4 Modellierung | 8 | Bilanzen korrekt und nachvollziehbar. Näherungen sind konstante Stoffwerte, COP Punktwert und Potenzgesetze bei Kosten. PDF S. 4 bis 7, `report/generated/numbers.tex`, Ergebnisdateien und eigene Nachrechnung. |
| 5 Neue Ansätze | 9 | Eigenständige Herleitung mit sieben Hypothesen und Clean-Room-Spur. Technologie Standard, Systemführung und Vollstrom-/Speicherdiagnose eigenständig. `docs/hypothesen.md`, Provenienz, Ausschlussprotokoll. |
| 6 Wissenschaftliche Qualität | 8 | Reale Quellen, Abflussstatistik, Druckwerte, offene Unsicherheit und Falsifikation. Abzüge für 1-K/h ohne Modell, Verhältnisfehler, sichtbare Abbildungsfehler und fehlende menschliche Prüfung. |
| 8 Erklärungen | 8 | Annahmen, Methoden, Ergebnisse und Schlussfolgerungen klar. Missverständliche Formulierung „in kühleren Jahren“, 1-K/h als Eigenschaft im Abstract und wechselnde Dezimaltrennzeichen. PDF S. 2, 3, 4 bis 10. |
| 9 Kritische Diskussion | 9 | Modellstruktur, Feldvalidierung, Monte-Carlo-Grenzen, Hochwasser und Restaufgaben offen. CO2-/Primärenergiebilanz und Flächenbedarf der Luftsenke nicht quantifiziert. PDF S. 9 bis 11, 14, Folie 8. |
| 10 Struktur und Juryführung | 8 | Gute Gesamtstruktur und Seitenbudget. Anhangsfiguren ohne Textbezug, keine nummerierten Verweise im Fließtext, Gleichung (3) verliert Nummer, Captions wiederholen Labels. PDF S. 2 bis 16. |
| 11 Format und visuelle Qualität | 7 | Formale Pflichten weitgehend erfüllt. D4RT-Vergleich fällt ab: Legendenkollisionen, Gleichungsnummer auf eigener Zeile, Dezimaltrennzeichen, gerissene URLs, leere Anhangseiten, kleine Abbildungstexte, Seitenzahl im 13-mm-Rand. PDF und Figuren. |
| 12a Schriftliche Runde | 8 | Vollständig, anonym und im Seitenbudget. Für 9 müssen sichtbare Formfehler und der Verhältnisfehler behoben werden. |
| 12b Finalrunde | 7 | Alle Materialien vorhanden. Folie 8 läuft 33,4 pt unter die Seite und wird im Video abgeschnitten, Folie 5 hat Pfeil ins Leere. Q&A-Revisionen nicht an Commits oder `decisions.tsv` gebunden. |

## Materielle Mängel und verlangte Korrekturen

### M1, Folie 8 läuft unten aus dem Bild

Im Präsentations-PDF reicht der Text bis y = 288,5 pt bei einer Seitenhöhe von 255,1 pt. Das sind 33,4 pt über den Rand. Im Video fehlt die Zeile „erfordern einen neuen Entwurf“. Korrektur: Absatz kürzen oder auf 11,5 pt setzen, Abstände anpassen, PDF und MP4 neu rendern und alle Textboxen gegen die Seitenhöhe prüfen. Beleg: `output/presentation/Blautopf_Finale.pdf` S. 8, `presentation/main.tex`, MP4 03:30.86 bis 04:00.84.

### M2, Folie 5, Pfeil ins Leere

Der orangefarbene Pfeil von der Kältemaschine trifft die Box „Luft als externe Wärmesenke“ nicht. TikZ verwendet `(air.south -| chiller.north)`. Korrektur: Pfeil auf `air.south` führen oder ein horizontales Segment ergänzen und neu rendern. Beleg: `presentation/main.tex`, `review/rendered/presentation_pages/slide-05.png`.

### M3, Abbildung 1, Legendenkollision

Orange und grüne Kurve durchstreichen den Legendentext „1 % des Quellstroms“ und „0,1 % des Quellstroms“. Korrektur: Legende außerhalb der Achsen oder unter das Panel setzen, `model/run_all.py` anpassen und Abbildung und Seite 6 neu erzeugen.

### M4, Abbildung 3, Legendenkollision

Die gestrichelte Reserve Linie durchquert den Legendentext. Korrektur: Legende nach unten rechts oder außerhalb setzen, `model/run_all.py` anpassen und Seite 15 neu rendern.

### M5, Gleichung (3), Nummer auf eigener Zeile

Die Gleichung steht auf y = 349,0, die Nummer (3) auf y = 366,0. Korrektur: Gleichung mit `aligned` umbrechen oder Satz kürzen, Seite 4 neu rendern. Beleg: PDF S. 4, `report/main.tex` Z. 94 bis 96.

### M6, gemischte Dezimaltrennzeichen

Gl. (2) „9.646“, Gl. (6) „877.781“, Gl. (15) „52.3“, Gl. (16) „12.479,8 MW = 12.48 GW“, Tabellen „877,8“. Korrektur: alle Makros mit deutschem Komma erzeugen, zum Beispiel `siunitx` mit `output-decimal-marker={,}`, Gleichungen und Tabellen neu setzen und PDF nach `\d+\.\d+` durchsuchen. Beleg: PDF S. 4, 5, 7, 10, `report/generated/numbers.tex`.

### M7, falscher Vergleich „mehr als doppelt so viel wie installiert“

Installiert sind 1.053,3 MW. 1.793,7 / 1.053,3 = 1,70. Nur gegen die Referenzlast 877,8 MW sind es 2,04. Korrektur: „rund 1,7-mal so viel wie die installierte Reserveauslegung“ oder „mehr als doppelt so viel wie die Referenzlast“. Beleg: PDF S. 8, `report/main.tex` Z. 279, `\QReserve`, `\QFinal`.

### M8, 1 K/h nicht modelliert

`data/parameters.yml` setzt `maximum_return_rate_k_h: 1.0`, aber keine Rechnung verwendet den Wert. Der Abstract, Abschnitt 3.3 und Q&A 8 stellen die Rate als Eigenschaft dar. Korrektur: einfaches CSTR- oder Plug-Flow-Modell für den worst-case-Sprung ergänzen oder die Aussage überall als „Regelziel, im Betrieb nachzuweisen“ formulieren. Abstract, Folie 5 und Q&A 8 angleichen. Beleg: Parameterdatei, `model/run_all.py`, PDF S. 2, 6, 10, `presentation/jury_qa.md` Frage 8.

### M9, Seitenzahl außerhalb des 25-mm-Rands

Die Seitenzahl steht 13,1 mm über der Unterkante, y = 804,8 pt bei 841,89 pt Seitenhöhe. `scripts/verify_report.py` blendet Zeichen mit `top > 770` aus. Korrektur: Seitenzahl in den Satzspiegel holen oder Ausnahme mit der Wettbewerbsleitung schriftlich klären. Beleg: PDF S. 1 bis 15, `report/preamble.tex`, `scripts/verify_report.py`.

### M10, Quellenregister und Literaturverzeichnis widersprechen sich

[2] heißt im Register „Hydrological functioning of a karst system with multiple recharge pathways“, im Bericht und bei Crossref aber „Quantifying the historic and future response...“. [6] heißt im Register „River water temperature and heat exchange modelling“, im Bericht und bei Crossref aber „Towards a better understanding of the evaporative cooling of rivers...“. Korrektur: die zwei Titel im Register auf die DOI-Titel setzen. Beleg: `sources/registry.yml`, Crossref, PDF S. 11 bis 12.

## Weitere Befunde

- Folie 3 zeigt die Grafik nur 32 mm hoch, kleine Achsenbeschriftung und zweizeilige Zahl „0,0303 MW“. Der Vergleich mit 877,8 MW wird nicht visuell gezeigt.
- Folie 9 ist eng gesetzt, „Leis-tung“ und „Küh-ler“ werden ungünstig getrennt.
- Literatur-URLs sind teilweise mitten im Token gebrochen und gespreizt, Referenz [13] besonders auffällig, [4] belegt fünf Zeilen.
- Anhang C zeigt zwei Figuren pro Seite mit großen Leerflächen.
- Jede Caption wiederholt das Label, zum Beispiel „Abbildung 1. Abbildung 1 zeigt...“.
- Tabelle 3 ist nur 130 mm breit in einem 158-mm-Satzspiegel und bricht „Forschungsoption“ ungünstig.
- Folie 6 und Q&A 10 nennen „zwei Netzeinspeisungen“, die im Bericht nicht modelliert sind. Der Bericht kennt nur Ersatzstrom für 74,2 MW.
- Folie 6 nennt 20 °C eine „ökologische Alarmschwelle“, ohne ökologische Quelle.
- Folie 1 nennt „PlaNeT SimTech, Science Slam“, die vorliegenden Regeln sprechen vom „Finale“. Mit Finalisten-E-Mail abgleichen.
- VTT bei 03:41 sagt „32,7 Kubikmetern“ ohne „pro Sekunde“, bei 02:27 steht „unserem Modell nach“ statt „nach unserem Modell“.
- MP4 hat `sample_aspect_ratio=1215:1216` und `display_aspect_ratio=135:76`, also 1,7763 statt exakt 16:9. Die Folien lagen nur als 945 x 532 Pixel vor und wurden hochskaliert.
- README nennt die Präsentation „animiert“, das Video ist ein statischer Slidecast mit Sprecherton.
- Q&A-Revisionszeilen sind nicht an Commits oder `decisions.tsv` gebunden.
- `presentation/rights.md` nennt Arial nicht, obwohl `presentation/main.tex` Arial setzt und das PDF ArialMT einbettet.
- Abbildungen und Tabellen werden im Fließtext nicht mit Nummer zitiert.

## Restrisiken und Dissens

- Die 2,3-m³/s-Hülle ist das größte fachliche Risiko. Das 90-Prozent-Quantil verlangt 1.793,7 MW, Hochwasser 12,48 GW. Der Bericht sagt das offen, aber die Anlage ist keine Hochwasserlösung. Die entscheidende Messung fehlt.
- Die 952-MW-Luftsenke ist nicht standortbezogen. Fläche, Luftführung, Rückverwirbelung, Geräusche und lokale Erwärmung sind offen. Eine Größenordnung der Kühlfläche fehlt.
- Die 74,2 MW elektrische Leistung sind energiewirtschaftlich nicht bewertet. 650 GWh pro Jahr, Netzanschluss, CO2 und Primärenergie fehlen. H2 braucht 118 GWh, aber Wasser.
- Die 1-K/h-Kontrolle und der Diffusor sind nicht ausgelegt. Der Puffer ist eine Stunde Volumen, kein Regelungsnachweis.
- Kosten sind Szenarien. 719 Mio. € und 2,90 Mrd. € sind keine Angebote. Die Rangfolge kann sich mit realen Preisen ändern.
- Ansaugung und Rückführung im Karst sind hydraulisch nicht durchbildet. „Geschlossen und druckgehalten“ ist keine NPSH- oder Kavitationsrechnung und keine Ansauggeometrie.
- Die visuellen Mängel sind im Video sichtbar: Folie 8 abgeschnitten, Folie 5 Pfeil ins Leere, Folie 3 klein und schwach.
- Q&A-Revisionen sind nicht nachvollziehbar. Für 12b ist „mit nachvollziehbaren Revisionen“ nur teilweise erfüllt.
- Die Seitenzahl-Randfrage ist formal ungeklärt.
- `compliance/checklist.md` setzt alle Zeilen auf „erfüllt“, was nach der Prüfung zu optimistisch ist.
- `docs/alternativenvergleich.md` sagt H1 sei die kostengünstigste Variante ohne zusätzlichen Wasserverbrauch. H2 ist billiger, der Qualifier ist wichtig und leicht zu überlesen.
- Q&A sagt 25 mm Rand, der Bericht 26 mm.
- Für eine 10 wurde keine vergebene Note erforderlich. Der Prüfapparat ist blind für die gefundenen Fehler. `scripts/verify_report.py` prüft keine Overfull-Boxes, Legendenkollisionen oder Gleichungsnummern. `scripts/verify_presentation.py` prüft Standardabweichung, nicht Textüberlauf.

## Urteil zur Stoppregel

Nein. Nur Kriterien 5 und 9 erreichen mindestens 9. Kriterien 1, 2, 3, 4, 6, 8, 10, 11, 12a und 12b liegen darunter. Die Revision ist nicht abgabebereit. Die Mängel M1 bis M10 sind konkret korrigierbar. Nach der Korrektur ist eine neue Revision einzufrieren und erneut unabhängig zu prüfen. Ein Council-Konsens über diese Fassung wäre kein Freigabevermerk.
