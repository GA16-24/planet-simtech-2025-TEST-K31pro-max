# Rohbericht Runde 8 — Commit `c76d40d3dabf894fb2475c714af5eed213f82c90`

## 0. Prüfgegenstand, Unabhängigkeit und Read-only-Status

Geprüft wurde ausschließlich der eingefrorene Commit `c76d40d3dabf894fb2475c714af5eed213f82c90` (HEAD). Die 181 in `review/rounds/round8/revision.json` gelisteten Dateien stimmen alle byteweise mit ihren SHA-256-Hashes überein (181/181, keine fehlende, keine abweichende Datei). Das PDF `output/pdf/TEST-K31pro-max.pdf` hat 13 Seiten, A4, und den SHA-256-Hash `4ffcbfb4fc9da8b23c2d57a4620c9b3c2bb6729971e38e08c569bd086ba1b854` — identisch mit `revision.json` und `review/rounds/round8/reproduction.md`.

Ich habe keine früheren Rohreviews oder Scorecards geöffnet und keine früheren Punktzahlen übernommen. Gelesen wurden nur der Prüfauftrag, `revision.json`, `reproduction.md`, `review/model_configuration.md` und die Befundzuordnung `review/revisions.md` (ohne Punktzahlen) sowie die Paketdateien. `review/rounds/round1` bis `round7` und `review/README.md`/`review/rubric.md` blieben ungelesen.

Read-only eingehalten: keine Repo-Datei verändert, kein Build, kein Git-Eingriff. Der Status ist unverändert (`?? review/rounds/round8/prompt.md`, `?? review/rounds/round8/revision.json` waren bereits vor der Prüfung untracked). Die 19 Modelltests habe ich mit `PYTHONDONTWRITEBYTECODE=1` und einem Cache außerhalb des Repos ausgeführt: `Ran 19 tests in 0.052s — OK`. Das Manifest `output/model/manifest.json` habe ich vollständig nachgerechnet: 43/43 Einträge stimmen. Die Archivreproduktion habe ich **nicht erneut gebaut** (kein Build); sie ist damit dokumentiert, aber von mir nicht nachgebaut (siehe Restrisiko R4). Die offiziellen PlaNeT-Vorgaben (Stand 10/2026) habe ich gegengeprüft; die Zusammenfassung in `compliance/regeln.md` ist inhaltlich korrekt.

---

## 1. Bewertungstabelle (elf Zeilen)

| Nr. | Kriterium | Pkt. | Kurzbegründung | Genauer Belegort |
|---|---|---:|---|---|
| **1** | Qualität der Argumentation | **9** | Die Argumentation trennt das literale Siedeverbot sauber vom ökologischen 9-°C-Ziel, leitet daraus den Vollstrombedarf ab und zeigt den Preis des Minimalziels (48,5 MW, 111,4 Mio. €) ausdrücklich. Sie behauptet keine Dauerlösung außerhalb der Auslegungshülle und benennt die Verwerfungsbedingungen. Der 9-°C-Anker ist eine offengelegte Wertentscheidung, kein verstecktes Faktum. | PDF S. 2 (Bericht S. 1), §§1–2; PDF S. 8–9 (Bericht S. 7–8), §§4.4, 6; Tab. 2, Tab. 3; `docs/hypothesen.md`; `docs/alternativenvergleich.md` |
| **2** | Vorgehen und Methodik | **9** | Systematisch und reproduzierbar: sieben Hypothesen, Screening, p90-Auslegung mit 20 % Reserve, gekoppelte Monte-Carlo-Rechnung, ODE-Ausfalltest, Sensitivitäten, Standort-/Genehmigungsprüfung, Falsifikationskriterien. Die 19 Tests und die Archivreproduktion sind dokumentiert. Vereinfachungen (konstante Stoffwerte, feste Trocken-/Kälteaufteilung) sind benannt oder als Szenario erkennbar; die Guard- und 95-%-Lastbasis sind Klarheitslücken (M8/M9), keine Methodenfehler. | PDF S. 3–4 (Gl. 1–4), S. 6–9 (§§4.1–4.4, 5); `model/core.py`; `model/validation.py`; `model/test_model.py`; `output/model/results.json`; `review/rounds/round8/reproduction.md` |
| **3** | Qualität der vorgeschlagenen Lösung | **8** | Physikalisch schlüssig, modular, mit Reserve, Stufenplan und Notkühlpfad. Aber: bedingter Szenarioentwurf ohne nachgewiesenen Karst-Eingriff, Standort, Netz und Genehmigung; die 2,15-GW-Anlage ist für das literale Siedeverbot stark überdimensioniert (48,5 MW genügen); die 9-°C-Zielsetzung ist eine Wertentscheidung. Die Offenheit ist dokumentiert, die Umsetzbarkeit bleibt aber ein materieller Vorbehalt. | PDF S. 2, 4–6, 8–9; Tab. 2; `boil_guard` in `output/model/results.json`; `docs/alternativenvergleich.md` |
| **4** | Mathematische und wissenschaftliche Modellierung | **9** | Die Kernmodelle sind korrekt und konsistent: `Q=ρV̇c_pΔT`, `T_q(t)`, `K_0`, `Q_Kond=Q_K+W_K`, ODE-Ausfall, Monte-Carlo, p90-/Reserve-Logik. Alle berichteten Werte stimmen mit `results.json` überein (877,781 MW; 967,2 MW; 89,4 MW; 234,3 MW; 2028,1 MW; 4,136 Mrd. € usw.). Die Validierung (19 Tests, Energiebilanzen, ODE-Fehler 8,0e-10 K, Konvergenz 1,79e-12 K) ist belastbar. Verbleibende Vereinfachungen sind als Näherung benannt. | PDF S. 3–4 (Gl. 1–10), S. 6–9; `model/core.py`; `model/validation.py`; `output/model/results.json`; `model/test_model.py` |
| **5** | Ableitung neuer Ansätze statt Wiederverwendung | **9** | Die Herleitung ist unabhängig dokumentiert: leeres Repository, keine früheren PlaNeT-Lösungen, nachvollziehbarer Hypothesen- und Entscheidungspfad, keine weltweite Neuheitsbehauptung. Der Ansatz (Trockenkühlung + Kältemaschine) ist fachlich konventionell, aber die Vollstrom-Skalierung, die p90-/Reserve-/Ausfallkette und die ökologische Zieltrennung sind eigenständig hergeleitet. | `PROVENANCE.md`; `EXCLUSION_LOG.md`; `decisions.tsv`; `docs/hypothesen.md`; PDF S. 3 (§2.1), S. 9 (§5), S. 11–12 (Anhang A) |
| **6** | Wissenschaftliche Qualität | **8** | Hohe Quellendisziplin, Annahmen/Unsicherheiten/Grenzen getrennt, KI-Offenlegung vorhanden, Zahlen reproduzierbar. Zwei konkrete Mängel verhindern die 9: (a) die H2-Beschreibung „Sekundärkreislauf von 100 auf 32 °C“ passt nicht zu 617,3 MW (das entspricht 100→36 °C; 100→32 wären 655,9 MW); (b) die 165 km² im Einführungssatz sind nicht direkt zitiert. | PDF S. 4 (H2-Absatz), S. 2 (165 km²); `model/core.py` (`evaporative_source_outlet_c=36`); `output/model/results.json` (`alternatives[1]`); `docs/alternativenvergleich.md` Z. 38; `sources/registry.yml` IDs 2/3 |
| **8** | Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen | **8** | Annahmen, Methode, Ergebnisse und Schluss sind klar getrennt (Tab. 1, Gl. 1–10, Tab. 2–4, Zusammenfassung/Schluss). Vier Klarheitsmängel: (a) „5 min Generatorstart und 10 min bis voller Kühlleistung“ ist mit den absoluten 5,5/10,5 min nur vereinbar, wenn die 10 min die 5 min einschließen; (b) H4–H7 werden im Paper nicht explizit benannt; (c) die 95-%-Dieselmenge 9,99 Mio. L basiert auf Erwartungslast 89,4 MW, der 48-h-Vorrat 2,869 Mio. L auf Auslegungslast 234,3 MW, ohne dass die Lastbasis genannt wird; (d) der Vergleich 48,5 MW/111,4 Mio. € (Mittelstrom) vs. 1595 Mio. € (p90) ist nicht like-for-like. | PDF S. 6 (§4.2), S. 6 (H4–H7), S. 8 (§4.4); `model/validation.py` Z. 36–37; `data/parameters.yml` (`failure.note`); `docs/alternativenvergleich.md` Z. 59 |
| **9** | Kritische Diskussion der Ergebnisse | **9** | Breite, ehrliche Diskussion: Alternativen, Ausfall, Standort, Netz, Wasserrecht/FFH, AwSV, Hochwasser, Teilstrom, Material-/Kostengrenzen, Falsifikation und „kein Baubescheid“. Die ökologische Begründung des 9-°C-Ziels bleibt qualitativ, und die H2-Wasserquelle (8,32 Mio. m³/Jahr) wird nicht auf Verfügbarkeit geprüft — Restrisiken, keine unkritische Überzeichnung. | PDF S. 4–9 (§§3.3, 4.1–4.4, 5, 6); Tab. 2/3; `docs/alternativenvergleich.md` |
| **10** | Klare Berichtsstruktur und Jury-Nachvollziehbarkeit | **8** | Die Hauptstruktur ist klar und jurytauglich (Zusammenfassung → Einführung → Methode → Ergebnisse → Diskussion → Nachweis → Schlussfolgerung). Der Anhang ist strukturell schwach: Anhang A beginnt am unteren Rand von PDF S. 11 und läuft als reiner Fließtextblock ohne Absatzabstand auf S. 12; Anhang B steht auf S. 13 in einer Spalte, die rechte Spalte und die untere Seitenhälfte bleiben leer. | PDF S. 11–13; `report/main.tex` Z. 262–278; `report/preamble.tex` Z. 17–18; `review/rendered/report_pages/page-12.png`, `page-13.png` |
| **11** | Format, Zitation, Einreichungsanforderungen, visuelle Qualität vs. D4RT | **7** | Weitgehend regelkonform: A4, mindestens 26 mm Rand (unten 34 mm), 12 pt Fließtext, 8 Haupttext-/4 Anhangseiten, Anonymität, 25 Quellen mit Abrufdaten, KI-Offenlegung. Visuell im Hauptteil nahe D4RT, im Anhang deutlich darunter: Legendenkollision in Abb. 1, halbleere Anhangsseite, 6,6-pt-Handrechnungsbruch, Tab.-4-Präzision, fehlendes 165-km²-Zitat, Fachbegriffe in der Zusammenfassung. | PDF S. 1, 2, 5, 9–10, 12–13; `compliance/regeln.md`; `compliance/checklist.md`; `compliance/layout_referenz.md`; D4RT S. 1/2/6 in `review/rendered/d4rt_page01.png`, `d4rt_page02.png`, `d4rt_page06.png`; `scripts/verify_report.py` Z. 109–119 |
| **12a** | Bereitschaft für die schriftliche Runde | **8** | Vollständig, anonymisiert, im Seitenbudget, mit 19 bestandenen Modelltests, 43/43 Manifest-Hashes und einem dokumentierten 37/37-Archivvergleich; KI-Offenlegung und menschliche Restaufgaben sind benannt. Noch nicht „abgabebereit ohne bekannten wesentlichen Mangel“: visuelle Anhangsfehler, H2-/5+10-/95-%-Klarheitsmängel, fehlende offizielle Team-ID und menschliche Prüfung. Die Archivreproduktion habe ich nicht erneut gebaut; der PDF-Hash stimmt mit dem dokumentierten Hash überein. | `README.md`; `PROVENANCE.md`; `review/rounds/round8/reproduction.md`; `review/rounds/round8/revision.json`; `output/model/manifest.json`; `scripts/verify_report.py`; eigener Testlauf „Ran 19 tests … OK“ |

---

## 2. Materielle Mängel mit konkreten Korrekturen

### A. Visuelle und strukturelle Mängel

**M1 — Legendenkollision in Abbildung 1.**
Beleg: PDF S. 5 (Bericht S. 4), Abb. 1; `model/run_all.py` Z. 283–286 (`axhline` mit Label „Regelziel 9 °C“, `axvline(10, color=GRAY)`, `legend(loc="upper left")`); `report/figures/fig01_prognose_last.pdf`.
Befund: Die Legende „Regelziel 9 °C“ reicht bis etwa Jahr 11 und wird von der grauen Jahreslinie bei Jahr 10 durchschnitten; die Textstelle „9 °C“ ist nicht sauber lesbar. Die Legende steht zudem weit von der eigentlichen 9-°C-Linie am unteren Rand entfernt, sodass der Bezug unklar ist.
Korrektur: Legende nach `lower right` verschieben **oder** die 9-°C-Linie direkt annotieren (z. B. `annotate("Regelziel 9 °C", xy=(0,9), xytext=(1.5,14), arrowprops=...)`); die Jahr-10-Linie entfernen oder mit „Jahr 10“ außerhalb der Legende beschriften; Panels mit „(a)“/„(b)“ labeln. Danach `make model`/`make report` und die gerenderte Seite 5 prüfen.

**M2 — Anhang A: Fließtextblock ohne Absatzabstand und 6,6-pt-Handrechnung.**
Beleg: PDF S. 12 (Bericht S. 11); `report/main.tex` Z. 262–275 (`\begingroup`, `\raggedright`, inline `\(\frac{...}{10^6}=...\)`); `report/preamble.tex` Z. 17–18 (`\parindent=1.25em`, `\parskip=0pt`); pdfplumber-Glyphengrößen 6,6/8,8/12,0 pt.
Befund: `\raggedright` setzt `\parindent=0`; bei `\parskip=0` sind die fünf Absätze visuell nicht unterscheidbar. Die Handrechnung ist als Inline-Bruch gesetzt; der Zähler fällt auf 6,6 pt und ist damit deutlich unter 12 pt.
Korrektur: Im Appendix-Group `\setlength{\parskip}{3pt}` und `\setlength{\parindent}{1.25em}` setzen; die Handrechnung als Display-Gleichung `\[ \frac{999{,}702\cdot2{,}3\cdot4195{,}14\cdot91}{10^6}=877{,}781\ \mathrm{MW} \]`; vor der Anhang-A-Überschrift `\needspace{5\baselineskip}` oder `\clearpage` einfügen. Danach PDF S. 12 prüfen.

**M3 — Anhang B: halbleere Seite 13.**
Beleg: PDF S. 13 (Bericht S. 12); `report/main.tex` Z. 277 (`\onecolumn`) und Z. 280–299 (`figure[H]`, `table[H]`); `review/rendered/report_pages/page-13.png`; `review/revisions.md` Z. 62 und Z. 168 (behaupten „keine fast leere Seite“ bzw. „Anhang A/B nutzt die freie zweite Spalte“).
Befund: Abb. 3 und Tab. 3/4 stehen nur in der linken Spalte; die rechte Spalte ist vollständig leer, die untere Seitenhälfte bleibt ungenutzt. Die Seite wirkt unfertig und ist der deutlichste visuelle Abfall gegenüber D4RT. Die Befundzuordnung behauptet die Behebung, der gerenderte Stand zeigt sie nicht.
Korrektur: `\onecolumn` entfernen; die Appendix-B-Inhalte als `figure*`/`table*` über die volle Breite setzen oder mit `\balance` auf zwei Spalten verteilen. Die Seite muss mindestens so gefüllt sein, dass keine freie Spalte/Halbseite bleibt. Danach PDF S. 13 und den Kontaktbogen erneut prüfen.

**M4 — Anhang-A-Überschrift am Seitenende.**
Beleg: PDF S. 11 (Bericht S. 10), rechte Spalte unten, und S. 12; `report/main.tex` Z. 262.
Befund: Die Überschrift „Anhang A: KI-Verwendung, Unabhängigkeit und Reproduktion“ steht am unteren Rand von S. 11, gefolgt von einer Zeile; der Rest läuft auf S. 12. Das ist ein unschöner Kopf-/Inhaltsbruch.
Korrektur: `\needspace{6\baselineskip}` oder `\clearpage` vor der Überschrift; die Überschrift mit mindestens 3–4 Zeilen Inhalt auf derselben Seite halten.

**M5 — Tab.-4-Präzision und unlabeled Referenzlinie in Abb. 3.**
Beleg: PDF S. 13; `model/run_all.py` Z. 336–339 (rechte `axvline` ohne Label; Legende nur mit den drei linken Handles) und Z. 641 (`flow_fractions` mit `4f`); `report/generated/sensitivity.tex` (`3f`); `report/generated/flow_fractions.tex`.
Befund: Tab. 4 zeigt „4,1365“, Tab. 3 „4,224“ — unterschiedliche Nachkommastellen. Im rechten Histogramm von Abb. 3 ist die rote Referenzlinie bei 4,14 Mrd. € unlabeled; die Legende beschreibt nur die linken Linien. Die p90-Linie bei 2152,5 MW liegt am äußersten rechten Rand und ist kaum von der Achse zu unterscheiden.
Korrektur: In Tab. 4 drei Nachkommastellen verwenden (4,136 / 0,434 / 0,048 / 0,006) oder die höhere Präzision in Tab. 3 angleichen; die rechte Referenzlinie mit `label="Referenz: 4,14"` in die Legende aufnehmen oder direkt annotieren; die x-Achse des linken Panels bis 2200 MW erweitern oder den p90-Eintrag aus der Legende entfernen.

### B. Wissenschaftliche und Klarheitsmängel

**M6 — H2: „100 auf 32 °C“ passt nicht zu 617,3 MW.**
Beleg: PDF S. 4 (Bericht S. 3), rechte Spalte, §3.2; `report/main.tex` Z. 168 (`\EvapSecondaryOutlet` = 32, `\EvapDry` = 617,3); `docs/alternativenvergleich.md` Z. 38; `data/parameters.yml` (`evaporative_source_outlet_c: 36`); `output/model/results.json` (`alternatives[1].external_air_rejection_mw = 957,37`, `annual_water_m3 = 8.3197e6`).
Befund: 617,3 MW entsprechen `C·(100−36)`; `C·(100−32)` wären 655,9 MW. Der Sekundärkreislauf wird bei 4 K Pinch real von 96 auf 32 °C gekühlt, nicht von 100 auf 32 °C. Die Energiebilanz ist mit 617,3 MW korrekt, die Temperaturbeschreibung nicht.
Korrektur: „Der Sekundärkreislauf wird auf 32 °C gekühlt; der Quellstrom verlässt den Wärmeübertrager bei 36 °C“ **oder** „von 96 auf 32 °C“ schreiben; die 617,3 MW und 263,7 kg/s beibehalten. `docs/alternativenvergleich.md` Z. 38 angleichen.

**M7 — Ausfallsequenz „5 min + 10 min“ widersprüchlich.**
Beleg: PDF S. 6 (Bericht S. 5), rechte Spalte, §4.2; `report/main.tex` Z. 184; `docs/alternativenvergleich.md` Z. 59; `data/parameters.yml` (`failure.note`); `model/validation.py` Z. 36–37 (`start_s = 0,5+5`, `full_s = 0,5+10`); `output/model/results.json` (`failure_p90.cooling_start_absolute_minutes = 5.5`, `full_cooling_absolute_minutes = 10.5`).
Befund: „Auf 0,5 min Detektion folgen angenommen 5 min Generatorstart und 10 min bis voller Kühlleistung. Absolute Zeitpunkte … 5,5 min für den Start und 10,5 min für die volle Kühlung.“ Das ist nur stimmig, wenn die 10 min die 5 min einschließen; liest man es sequenziell, wären es 15,5 min und die 15-min-USV wäre überschritten. Die Sicherheitsaussage hängt an dieser Zahl.
Korrektur: „0,5 min Detektion + 5 min bis zum Generatorstart + weitere 5 min bis zur vollen Kühlleistung = 10,5 min; die 15-min-USV hat 4,5 min Reserve“ **oder** „10 min ab Detektion inklusive 5 min Generatorstart“. `report/main.tex`, `docs/alternativenvergleich.md` und `data/parameters.yml` identisch fassen.

**M8 — 95-%-Dieselmenge ohne Lastbasis.**
Beleg: PDF S. 8 (Bericht S. 7), rechte Spalte, §4.4; `report/main.tex` Z. 202/206; `model/core.py` (`economic_schedule`, `backup_mwh = operation["electricity_mw"] * 8760 * (1-availability)`); `output/model/results.json` (`availability_scenarios[0].final_backup_fuel_liters = 9.987.125`, `baseline.backup_fuel_liters = 2.869.418`); `design_electrical_stage` = 234,3 MW.
Befund: 9,99 Mio. L gelten bei 5 % Ausfallzeit und Erwartungslast 89,4 MW; 2,869 Mio. L gelten für 48 h bei Auslegungslast 234,3 MW. Die beiden Werte stehen nebeneinander, ohne dass die unterschiedliche Lastbasis genannt wird; ein Leser kann die Zahlen nicht sauber vergleichen.
Korrektur: „Bei 95 % Netzverfügbarkeit und Erwartungslast 89,4 MW werden 9,99 Mio. L benötigt; der 48-h-Vorrat von 2,869 Mio. L ist dagegen für die Auslegungslast 234,3 MW bemessen.“ In `report/main.tex` §4.4 ergänzen.

**M9 — Guard-Vergleich nicht like-for-like.**
Beleg: PDF S. 8 (Bericht S. 7), linke Spalte, §4.4; `report/main.tex` Z. 198; `model/run_all.py` (`guard_p` mit `design_discharge_m3_s = 2,3`); `output/model/results.json` (`boil_guard.required_cooling_mw = 48,48`, `final_capex_eur = 111,38 Mio. €`, `npv = 0,1766 Mrd. €`); H1 `final_capex_eur = 1595,15 Mio. €` (p90 4,7 m³/s).
Befund: Der Siedeschutz ist auf den Erwartungsstrom 2,3 m³/s ausgelegt, H1 auf p90 4,7 m³/s. Der Kostenvergleich 111,4 Mio. € vs. 1595 Mio. € ist daher nicht auf derselben Auslegungsbasis; bei gleicher p90-Auslegung wäre der Siedeschutz größer (ca. 96–99 MW, deutlich mehr als 111 Mio. €).
Korrektur: Die Basis ausdrücklich nennen („Der Siedeschutz ist hier auf 2,3 m³/s ausgelegt; H1 auf 4,7 m³/s“) und entweder einen p90-Siedeschutz ergänzen oder den Vergleich auf den Erwartungsstrom beziehen.

**M10 — H4–H7 im Paper nicht aufgelöst.**
Beleg: PDF S. 6 (Bericht S. 5), linke Spalte, §3.3 Ende; `report/main.tex` Z. 170; `docs/hypothesen.md` H4–H7.
Befund: „H4 scheitert ohne genaue Karstwege … H5 kann nur zusammen mit H1 wirken. H6 erhöht lediglich den Siedepunkt. H7 benötigt 4,4 km² …“ — die Zuordnung zu „geologische Wärmeentnahme“, „Bypass“, „Druckverschiebung“ und „passive Wärmerohre“ muss der Leser aus der Reihenfolge der sieben Ansätze erraten.
Korrektur: Die Klammernamen ergänzen: „H4 (geologische Wärmeentnahme)“, „H5 (Bypass)“, „H6 (Druckverschiebung)“, „H7 (passive Wärmerohre)“; oder eine kleine Liste H1–H7 nach dem Sieben-Ansätze-Absatz.

**M11 — 165 km² ohne Zitat.**
Beleg: PDF S. 2 (Bericht S. 1), linke Spalte, §1 erster Absatz; `report/main.tex` Z. 42; `research_notes/Blautopf Wärmeschutz/physical_system.md` Z. 13; `sources/registry.yml` IDs 2/3.
Befund: „Der Blautopf entwässert einen Karstaquifer von etwa 165 km².“ ist eine externe Tatsache ohne numerischen Verweis; die Quelle existiert in den Recherchenotizen (LGRB/Fan), wird im Paper aber nicht genannt.
Korrektur: `[2,3]` nach „etwa 165 km²“ ergänzen; die Referenzen [2] und [3] sind vorhanden.

**M12 — Fachbegriffe in der Zusammenfassung.**
Beleg: PDF S. 2 (Bericht S. 1), linke Spalte, Zusammenfassung; `report/main.tex` Z. 32; offizielle PlaNeT-Vorgaben Stand 10/2026, §1 („ohne technische Fachbegriffe“); `scripts/verify_report.py` Z. 47 prüft nur `p90`, `H1`, `Barwert`.
Befund: „fünf Gerätestränge“ und „geregelte Rücklaufänderung von höchstens einem Grad pro Stunde“ sind technische Begriffe; die Zusammenfassung soll auch für Außenstehende verständlich sein.
Korrektur: „fünf Kühlmodule“ und „die Temperatur des zurückgeführten Wassers ändert sich höchstens um ein Grad pro Stunde“; die automatische Prüfung um diese Begriffe erweitern.

### C. Verifikation und Transparenz

**M13 — Befundzuordnung und Blank-Page-Check stimmen nicht mit dem PDF überein.**
Beleg: `review/revisions.md` Z. 62 („Fast leere Anhangsseite … keine fast leere Seite“), Z. 168 („Anhang A/B nutzt die freie zweite Spalte“), Z. 216 („Anhang A steht rechtsbündig“); `decisions.tsv` Z. 29 („alle Seiten visuell geprüft“); `scripts/verify_report.py` Z. 109–119 (`stat.stddev[0] > 5.0`); PDF S. 12–13; `review/rendered/report_pages/page-12.png`, `page-13.png`.
Befund: Anhang A/B nutzen die rechte Spalte nicht; Seite 13 ist halbleer; die Behauptung „keine fast leere Seite“ ist falsch. Der `stddev > 5.0`-Check erkennt eine halbleere Seite nicht, weil die linke Spalte genug Inhalt hat. Die Aussage „alle Seiten visuell geprüft“ ist mit dem gerenderten Stand nicht vereinbar.
Korrektur: Die Befundzuordnung auf den tatsächlichen Stand zurücksetzen (die Anhangkorrekturen als offen markieren); `verify_report.py` um eine Spaltenfüll-/Textbbox-Prüfung ergänzen (z. B. Füllgrad je Spalte oder Texthöhe je Spalte); Seite 13 erneut visuell prüfen.

**M14 — Kostenaufschlüsselung fehlt im Paper.**
Beleg: PDF S. 5–6 (Bericht S. 4–5), §3.3 und Tab. 2; `model/core.py` (`variable_capex_eur`); `output/model/results.json` (`baseline.final_capex_eur = 1.595.148.443,75`).
Befund: Das Paper nennt 1595 Mio. €, aber nicht die Anteile. Eine Leserin kann die Summe aus dem Paper allein nicht nachrechnen; die Einheitspreise und Zuschläge sind genannt, die Aufteilung fehlt.
Korrektur: Kleine Aufschlüsselung ergänzen: Wärmetauscher 32,3 Mio. €; Kältemaschinen 476,6; Trockenkühler 364,4; Notstrom 64,3; variable Summe 937,6; ×1,6 = 1500,1; + Tiefbau/Steuerung 95,0 = 1595,1 Mio. €. (Werte aus `variable_capex_eur(10, p)`.)

**M15 — kleinere Typografie/Lockerungen (optional, nicht stoprelevant).**
Beleg: PDF S. 2; `report/preamble.tex` (`\sloppy`, `\emergencystretch=5em`).
Befund: Die Zeile „Im zehnten Jahr wären dafür 877,8 Megawatt Kühlleistung nötig.“ hat sehr weite Wortabstände; das ist eine Folge des globalen `\sloppy`.
Korrektur: Die Zusammenfassung `\raggedright` setzen oder `\emergencystretch` auf 2–3em reduzieren; Sichtprüfung.

---

## 3. Restrisiken und Dissens

**R1 — Reale Machbarkeit bleibt offen.** Karst-Eingriff, Höhlenwege, Standort, Flächeneigentum, Netzzusage, Luftführung, Schall/Plume, AwSV-Lager und FFH-Prüfung sind nicht nachgewiesen. Das Paper sagt das ausdrücklich (PDF S. 6–9); eine Baufreigabe oder externe Machbarkeit darf nicht unterstellt werden. Die 2,15-GW-Anlage ist für das literale Siedeverbot stark überdimensioniert; die 9-°C-Zielsetzung ist eine Wertentscheidung, keine aus der Aufgabe zwingende Vorgabe.

**R2 — H2-Wasserquelle nicht geprüft.** H2 verbraucht 8,32 Mio. m³/Jahr (11,5 % des erwarteten Quellstroms); die Verfügbarkeit dieser Wassermenge, die ökologischen Folgen einer Entnahme und die Kosten der Wasserbereitstellung sind nicht untersucht. Die Aussage „H2 ist physikalisch gleichwertig“ gilt nur im Szenario 28 °C Feuchtkugel/4 K Pinch und bei gesicherter Wasserquelle.

**R3 — Modellannahmen sind Szenario, nicht Empirie.** Konstante Stoffwerte bei 10 °C für einen 100-°C-Prozess, feste Trocken-/Kälteaufteilung über alle Abflüsse, 100-°C-Deckel, 25.000 m³ Beckenvolumen, 35 °C Luft/28 °C Feuchtkugel, 3-Eingangs-Monte-Carlo und lognormaler Investitionsfaktor sind nicht empirisch kalibriert. Die Ergebnisse sind innerhalb dieser Hülle konsistent, aber keine Prognose.

**R4 — Archivreproduktion nicht erneut gebaut.** Ich habe keinen Build ausgeführt. Der PDF-Hash stimmt mit `reproduction.md`/`revision.json` überein; das Manifest ist 43/43; die 19 Tests bestehen. Die 37/37-byte-identisch-Aussage ist dokumentiert, aber von mir nicht nachgebaut; sie bezieht sich auf den Kandidaten `2385eff`, nicht auf den Dokumentationscommit `c76d40d` (der nur Doku ergänzt). Das ist eine Verifikationslücke, keine Widerlegung.

**R5 — Same-Model-Review und menschliche Restaufgaben.** Der Kimi-Reviewer ist same-model zum Autor; das Paper discloses das („Dieser Same-Model-Kontext ist keine externe oder menschliche Prüfung“). Der DeepSeek-Reviewer ist modellverschieden, aber die menschliche Fachprüfung, die offizielle Team-ID und die Einreichung fehlen. Das Paper behauptet sie nicht; für eine echte Abgabe bleiben es offene menschliche Aufgaben.

**R6 — KI-Offenlegung ist adequat, aber nicht granular.** Das Paper nennt Systeme, Rollen und „gesamten Bericht“; die offiziellen Vorgaben verlangen „wo, wie, welches“. Die Figure-Captions nennen das Tool; die PROVENANCE-Tabelle ist detaillierter. Für die PDF allein ist die Ortsangabe „gesamter Bericht“ breit, aber nachvollziehbar.

**R7 — 12-pt-Risiko in Anhang A.** Der Fließtext, die Tabellen, die Captions und die Figuren liegen bei 12 pt; der Inline-Bruch der Handrechnung fällt auf 6,6–8,8 pt. Mathematische Skripte sind üblicherweise ausgenommen, aber der Bruch ist ein textnahes Element. Wenn die Jury die 12-pt-Regel streng liest, ist das ein Compliance-Risiko; die Display-Gleichung aus M2 beseitigt es.

**R8 — D4RT-Vergleich nur teilweise erfüllt.** Der Hauptteil ist typografisch nahe an D4RT (zweispaltig, Serif, blaue Akzente, Captions unter Abbildungen, Tabellen mit horizontalen Linien). Der Anhang ist deutlich darunter; die Aussage in `compliance/layout_referenz.md` Z. 28, der Bericht übernehme die dichte Seitenintegration, gilt für die Anhänge nicht. Das ist der Kern von Kriterium 11.

**R9 — Prozessrisiko: Selbstprüfung übersieht sichtbare Layoutfehler.** `decisions.tsv` Z. 29 behauptet „alle Seiten visuell geprüft“; Seite 13 ist halbleer, Seite 12 ein Fließtextblock. Der `stddev`-Check in `verify_report.py` kann das nicht erkennen. Das ist ein Vertrauensproblem für die Prüfkette, nicht nur ein Layoutdetail: Wer „keine fast leere Seite“ behauptet, muss sie auch prüfen.

**Dissens.** Ich sehe die wissenschaftliche Kernsubstanz (Kriterien 1, 2, 4, 5, 9) auf 9-Niveau. Die Stoppregel scheitert an der Auslieferbarkeit/visuellen Qualität (Kriterium 11 = 7), an der Klarheit (8), an der Struktur (10 = 8) und an der Bereitschaft (12a = 8) sowie an zwei konkreten wissenschaftlichen Beschreibungsfehlern (H2, 5+10). Ein Reviewer, der Kriterium 11 als Kosmetik liest, könnte zu einem anderen Urteil kommen; die explizite D4RT-Vergleichsanforderung und die bereits in Runde 5/7 behauptete, aber nicht umgesetzte Anhangkorrektur sprechen dagegen.

---

## 4. 10er-Nachweis

**Keine Zeile erhält 10.** Die Bedingung für eine 10 — ein dokumentierter, erfolgloser Versuch, substanzielle Fehler zu finden, und eine Begründung, warum keiner verbleibt — ist nicht erfüllt, weil die Prüfung mehrere konkrete Mängel ergab (M1–M14). Es gibt daher keine „erfolglose Fehlersuche“, die als 10er-Nachweis dokumentiert werden könnte.

---

## 5. Abschließendes Urteil zur Stoppregel

**Die Stoppregel ist auf dieser Revision nicht erfüllt.**

Gründe:

1. **Punktzahlen:** Mit meinen Bewertungen liegen die Zeilen 3 (8), 6 (8), 8 (8), 10 (8), 11 (7) und 12a (8) unter 9. Die Stoppregel verlangt mindestens 9 in jeder Zeile von beiden Reviewern; meine Stimme allein erfüllt das nicht, unabhängig von der zweiten Stimme.
2. **Visuelle Auslieferbarkeit:** Die halbleere Seite 13, der Fließtextblock mit 6,6-pt-Bruch auf Seite 12 und die Legendenkollision in Abbildung 1 sind sichtbare, bekannte Mängel. Sie sind mit geringem Aufwand behebbar, aber im eingefrorenen Stand vorhanden.
3. **Klarheit/Korrektheit:** Die 5+10-min-Ausfallsequenz ist in einem sicherheitsrelevanten Absatz mehrdeutig; die H2-Temperaturbeschreibung passt nicht zur 617,3-MW-Bilanz; die 95-%-Lastbasis und der Guard-Vergleich sind nicht ausreichend gekennzeichnet; die 165 km² sind nicht zitiert.
4. **Verifikationsbehauptungen:** `review/revisions.md` und `decisions.tsv` behaupten Korrekturen („keine fast leere Seite“, „freie zweite Spalte“, „alle Seiten visuell geprüft“), die der gerenderte Stand nicht zeigt. Das ist ein zusätzlicher, nicht nur kosmetischer Mangel an Nachweisführung.
5. **Nicht nachgebaut:** Die Archivreproduktion habe ich nicht erneut ausgeführt; sie ist dokumentiert und der PDF-Hash stimmt, aber die 37/37-Aussage ist von mir nicht unabhängig bestätigt.

Die Revision ist **nahe** an einer Freigabe: Die wissenschaftliche Kernsubstanz ist stark, die Zahlen sind konsistent, die 19 Tests bestehen, das Manifest ist vollständig, und die Offenlegung ist ehrlich. Nach dem im Auftrag definierten 9/10-Maßstab („nachweisbar abgabebereit ohne bekannten wesentlichen Mangel“) wäre eine Freigabe auf diesem Stand jedoch nicht gerechtfertigt. Die konkret ausführbaren Korrekturen M1–M14 sind der Weg zu einer erneuten Bewertung.
