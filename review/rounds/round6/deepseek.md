# Rohbericht Runde 6 — Commit 473e397c4d45a909cc024e1722d572cdbd73df7d

## 0. Prüfgegenstand, Prüfweise und Grenzen

Geprüft wurde ausschließlich die eingefrorene Revision `473e397c4d45a909cc024e1722d572cdbd73df7d` im Repository `planet-simtech-2025-TEST-K31pro-max`. Die 164 in `review/rounds/round6/revision.json` deklarierten Dateien stimmen vollständig mit den 164 getrackten Dateien des Commits überein; alle 164 SHA-256-Hashes wurden gegen `git show <commit>:<pfad>` geprüft, ohne Abweichung. Der Arbeitsbaum ist bis auf die beiden vom Prüfauftrag vorgegebenen, unversionierten Dateien `review/rounds/round6/prompt.md` und `review/rounds/round6/revision.json` sauber. Der Freeze-Commit `473e397` ändert gegenüber dem reproduzierten Kandidaten `a963e21` nur fünf Dokumentationsdateien (`decisions.tsv`, `review/README.md`, `review/council_prompt.md`, `review/revisions.md`, `review/rounds/round6/reproduction.md`); keine Paper-, Modell- oder Renderdatei ist betroffen.

Die PDF `output/pdf/TEST-K31pro-max.pdf` hat den SHA-256-Hash `c308a8facad232227c1cfaa83a562be4df9de81fc33fe263e7f287556a114d58` und 12 Seiten: Deckblatt plus 7 Haupttextseiten plus 4 Seiten Literatur/Anhang. Die Kontaktübersicht `review/rendered/report_contact.png` und alle zwölf Einzelseiten `review/rendered/report_pages/page-01.png` bis `page-12.png` wurden geöffnet; die Seitenbilder entsprechen dem gerenderten PDF. Zusätzlich wurden die D4RT-Referenzseiten 1, 2 und 6 geöffnet.

Unabhängig gemessen: Seitengröße A4 (595,28 × 841,89 pt), linker/rechter Rand 73,70 pt = 26,0 mm, unterster Text-/Seitenzahlabstand 73,94 pt = 26,1 mm, Median der Buchstabengröße 11,96 pt, keine Autorenmetadaten. Die Modellprüfung wurde an `model/core.py`, `model/run_all.py`, `model/validation.py`, `model/test_model.py`, `data/parameters.yml`, `output/model/results.json`, `output/model/hybrid_schedule.csv`, `output/model/sensitivity.csv` und `output/model/manifest.json` nachvollzogen. Alle 43 Manifest-Hashes stimmen. Die 13 Testmethoden sind vorhanden; ich habe sie wegen des ausdrücklichen Build-Verbots nicht ausgeführt, sondern den dokumentierten Reproduktionslauf und die Testlogik gelesen.

Die behauptete 36/36-Byte-Gleichheit der Archivreproduktion habe ich nicht unabhängig nachgebaut (read-only, keine Builds). Gestützt wird sie durch den übereinstimmenden PDF-Hash, die 43 übereinstimmenden Manifest-Hashes, die 164 übereinstimmenden Revisions-Hashes und die visuell identischen zwölf Seitenbilder; der letzte Byte-Vergleich bleibt ein Selbstbericht und wird als Restrisiko ausgewiesen.

Frühere Rohreviews oder Scorecards habe ich nicht geöffnet. `review/revisions.md` wurde nur als Befundzuordnung ohne Punktzahlen gelesen; `review/README.md` und die Runden 2–5 wurden nicht geöffnet. Der andere Reviewer wurde nicht kontaktiert. Es wurden keine Dateien im Repository verändert, keine Builds ausgeführt und keine Reviews geschrieben.

### Formale Regelprüfung

Die offiziellen [PlaNeT-Vorgaben für den Bericht, Stand 10/2026](https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Vorgaben-Bericht.pdf) verlangen unter anderem: höchstens 10 Seiten ohne Deckblatt und Anhang, Literatur und Anhang zusammen höchstens 5 Seiten, A4, mindestens 2,5 cm Rand, 12 pt, Deckblatt mit Team-ID/Datum/Aufgabenstellung/Wettbewerbsname, Zusammenfassung maximal eine Seite ohne technische Fachbegriffe, Schlussfolgerung mit einem Statement zu Verbesserungsmöglichkeiten bei mehr Bearbeitungszeit sowie klare KI-Transparenz. Der Bericht erfüllt Seitenbudget (7 + 4), Format, Ränder, Schriftgröße, Deckblatt, Zusammenfassung, Zitation, KI-Offenlegung und Anonymität. **Nicht erfüllt ist die ausdrücklich verlangte Aussage zu Verbesserungsmöglichkeiten bei mehr Bearbeitungszeit in der Schlussfolgerung** (dazu M9). Die Testkennung `TEST-K31pro-max` ist als Platzhalter offengelegt; eine reale Einreichung müsste die offizielle Team-ID einsetzen.

---

## 1. Bewertungstabelle

| Nr. | Kriterium | Punkte | Kurzbegründung | Belegorte |
|---|---|---:|---|---|
| 1 | Qualität der Argumentation | **9** | Saubere Trennung von Szenarioprämisse, Daten und Annahmen; klare Zielhierarchie „Sieden vs. 9 °C“; H1 wird aus der Wärmebilanz hergeleitet, Alternativen werden geprüft, die Schlussfolgerung bleibt innerhalb der erklärten Hülle. Kein wesentlicher Argumentationsbruch gefunden. | PDF S. 2–9, §§1–6; `docs/hypothesen.md`; `docs/alternativenvergleich.md`; `report/main.tex` |
| 2 | Vorgehen und Methodik | **9** | Vollständiges Vorgehen: sieben Hypothesen, Trennung von Messwerten und Annahmen, Wärmebilanz, NPV, Monte Carlo, ODE-Ausfallmodell, 13 Tests, Manifest und Archivreproduktion. Der lokale Kostenmodellfehler in Tabelle 4 ist ein Implementierungsfehler, den ich unter 4 und 6 abwerte; das Verfahren selbst ist nachvollziehbar und reproduzierbar. | PDF S. 3–8; `model/`; `model/test_model.py` (13 Testmethoden); `README.md`; `review/rounds/round6/reproduction.md` |
| 3 | Qualität der vorgeschlagenen Lösung | **9** | Technisch kohärente zweistufige Vollstromkühlung: Trockenkühlung 100→40 °C, Kältemaschinen 40→9 °C, p90-Auslegung 2152,5 MW, zwölf Stränge, Puffer, Notstrom, Mess- und Falsifikationsplan. Standort, Netz, Karst und Genehmigung bleiben offen und werden nicht als gelöst behauptet. | PDF S. 4–8, §§3–5; `output/model/results.json` (`baseline`, `design`); `docs/alternativenvergleich.md` |
| 4 | Mathematische und wissenschaftliche Modellierung | **8** | Gleichungen, Energiebilanz, NPV, Monte Carlo und ODE sind konsistent; die zentralen Werte (877,781 MW, 9,646 MW/K, 3,666 Mrd. €) sind nachrechenbar, die Validierung ist dokumentiert. **Aber:** Tabelle 4 skaliert den Notstrom in den Teilstromfällen nicht mit der Variante; der 0,1-%-Fall weist 103,83 Mio. € aus, davon 63,35 Mio. € Notstrom, bei 0,09 MW Elektrik. Bei skalenrichtiger Kopplung wären es rund 2,6 Mio. €. Zudem ist `condenser_temperature_c = 45` im Modell unbenutzt; die Kondensator-/Trockenkühlerfläche wird nicht als Pinch-/Flächenauslegung geprüft. | `model/core.py:104–148`; `model/run_all.py:194–207`; `output/model/results.json` (`flow_fraction_scenarios`); PDF S. 12 (gedruckte S. 11), Tabelle 4; `data/parameters.yml:54`; `model/validation.py` |
| 5 | Ableitung neuer Ansätze statt Wiederverwendung vorhandener Ergebnisse | **9** | Das Repository begann leer; die Hypothesen und die H1-Skalierung wurden aus der Wärmebilanz abgeleitet, nicht aus früheren Lösungen. Keine weltweite Neuheit wird behauptet; die Herleitung ist dokumentiert. Die Technik ist konventionell, die Quantifizierung und der Ausschlussweg sind eigenständig. | `PROVENANCE.md`; `EXCLUSION_LOG.md`; `docs/hypothesen.md`; PDF S. 3 §2.1, S. 8 Anhang A |
| 6 | Wissenschaftliche Qualität | **8** | Transparente Quellen, klare Trennung von Fakten und Szenarioannahmen, Unsicherheitsanalyse, Falsifikationskriterien und offengelegte Grenzen. **Aber:** Die fehlerhafte Notstromskalierung in Tabelle 4 ist ein bekannter materieller Modellfehler in einem berichteten Ergebnis; die wissenschaftliche Qualität ist dadurch nicht 9/10, auch wenn Darstellung und Offenheit sonst hoch sind. | PDF S. 2–9; `sources/registry.yml`; `PROVENANCE.md`; `EXCLUSION_LOG.md`; `compliance/regeln.md`; Tabelle 4 |
| 8 | Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen | **9** | Tabelle 1 trennt Quellenwerte, Szenarioprämissen und technische Annahmen; Gleichungen 1–10, Ergebnisgrößen und Schlussfolgerung sind nachvollziehbar. Kleine Unschärfe: Die Zusammenfassung spricht von „877,8 Megawatt Wärmeabfuhr“, während der Körper korrekt 877,8 MW Wärmeentzug und 967,2 MW Wärmeabgabe an die Luft trennt. Das ist eine optionale sprachliche Präzisierung, kein Verständnisbruch. | PDF S. 2 Zusammenfassung; S. 3 Tabelle 1; S. 4–7 §§2–5; `report/main.tex` |
| 9 | Kritische Diskussion der Ergebnisse | **9** | Sehr umfangreiche Diskussion: Standort, Netz, Diesel, AwSV/WHG/BNatSchG, Karst, Hochwasser, Ausfall, Kostenquantile, Tarif, Netzverfügbarkeit, fehlende Feldvalidierung und menschliche Restaufgaben. Die 60-%-Reserve und der 60-Mio.-€-Notstromblock werden allerdings nicht eigens kritisch hergeleitet; das bleibt ein Restrisiko. | PDF S. 6–9, §§4–6; `docs/alternativenvergleich.md`; `compliance/checklist.md` |
| 10 | Klare Berichtsstruktur und für die Jury nachvollziehbare Argumentation | **9** | Klassischer Aufbau: Zusammenfassung, Einführung, Methode, Ergebnisse, Diskussion, Schlussfolgerung, Literatur, Anhänge; numerische Verweise, Tabellen und Abbildungen sind konsistent. Der Übergang Literatur/Anhang A ist etwas eng, aber die Leserführung bleibt klar. | PDF S. 2–12; `report/main.tex`; `compliance/checklist.md` |
| 11 | Format, Zitation und Einreichungsanforderungen, einschließlich visueller Qualität im Vergleich zur D4RT-Referenz | **8** | Formal weitgehend erfüllt: A4, 26 mm Rand, 12 pt, 7 Haupttext- plus 4 Literatur-/Anhangseiten, numerische Zitate, Abrufdaten, KI-Offenlegung, Anonymität. Visuell nahe D4RT (zweispaltig, Times, Tabellenlinien, erklärende Unterschriften), aber **Abbildung 1 hat links „Tiefe in °C“ statt „Temperatur in °C“**, Referenz [19] bricht als „20. 500.12738“, das Deckblatt ist sehr leer, und die Schlussfolgerung enthält nicht das verlangte „mehr Bearbeitungszeit“-Statement. | PDF S. 5 (gedruckte S. 4), Abb. 1; `model/run_all.py:258`; PDF S. 10 (gedruckte S. 9), [19]; PDF S. 9 §6; `compliance/layout_referenz.md`; `review/rendered/d4rt_page01/02/06.png`; `scripts/verify_report.py` |
| 12a | Bereitschaft für die schriftliche Runde | **8** | Das Paket ist weitgehend abgabebereit, aber wegen M1 (Tabelle 4), M2 (Achsenlabel) und M9 (fehlendes Pflichtstatement) nicht ohne bekannten Mangel. Testkennung, fehlende menschliche Fachprüfung und ausstehende offizielle Einreichung sind ausdrücklich offengelegt. | `README.md`; `PROVENANCE.md`; PDF S. 1, S. 11 Anhang A/B; `compliance/checklist.md` |

**Summe der Einzelbewertungen:** 9 + 9 + 9 + 8 + 9 + 8 + 9 + 9 + 9 + 8 + 8 = **95 von 110** (falls eine Summe gewünscht ist; die Stoppregel wird nicht über die Summe entschieden).

---

## 2. Materielle Mängel und konkrete Korrekturen

### M1 (stopprelevant): Notstromskalierung in den Teilstromszenarien

**Beleg:** PDF S. 12 (gedruckte S. 11), Anhang C, Tabelle 4; `model/core.py:120–136` (`variable_capex_eur`); `model/run_all.py:194–207` (`flow_fraction_scenarios`); `output/model/results.json`, `flow_fraction_scenarios`; `model/test_model.py:68–77` (nur der Siedeschutzfall wird getestet); eigene read-only Nachrechnung mit `variable_capex_eur`.

**Befund:** `variable_capex_eur` berechnet `design_electricity_mw` und `reference_electricity_mw` beide mit dem festen Designstrom 4,7 m³/s. Für `scenario.affected_flow_fraction = 0,001` bleibt `electricity_ratio = 1`. Der Backup-Posten ist damit `(60 Mio. € + 3,35 Mio. € Kraftstoff) = 63,35 Mio. €` und dominiert die ausgewiesenen 103,83 Mio. € Gesamtinvestition. Die Tabelle nennt für 0,878 MW Kühlleistung und 0,089 MW Elektrik trotzdem 104 Mio. € Investition und 0,1731 Mrd. € Barwert. Bei skalenrichtiger Kopplung an die Design-Elektrik der Variante (ca. 0,182 MW p90 statt 182,65 MW Referenz) wären es ca. 0,063 Mio. € Backup und ca. 2,6 Mio. € Gesamtinvestition. Überschlägig ergäben sich für 10 %/1 %/0,1 % eher ca. 141/17/2,6 Mio. € statt 233/118/104 Mio. €. Die Aussage „ein bestätigter kleiner Teilstrom senkt Kosten“ bleibt qualitativ richtig; die absoluten Zahlen der Tabelle sind es nicht. Der gleiche Fehler trifft H2, weil `design_electricity_mw` ohne `technology` gerechnet wird; H2s Backup ist an H1s 182,7 MW statt an H2s ca. 142 MW gekoppelt (ca. 14–22 Mio. € zu hoch, für die H2/H1-Aussage nicht ausschlaggebend).

**Korrektur:**
1. In `variable_capex_eur` den Varianten-Designstrom verwenden:
   `design_flow = design_flow_ratio(p) * p["scenario"]["affected_flow_fraction"]`;
   `design_stage = cooling_stage(final_year, p, affected_fraction=design_flow, technology=technology)`;
   `reference_stage = cooling_stage(final_year, reference_p, affected_fraction=reference_flow, technology=technology)`;
   `electricity_ratio = design_stage.electricity_mw / reference_stage.electricity_mw`.
2. `backup_power` und `backup_fuel_cost` mit diesem `electricity_ratio` skalieren.
3. Regressionstests ergänzen: `affected_fraction = 0,001` → `backup_power < 1 Mio. €`, Gesamtinvestition `< 10 Mio. €`; `affected_fraction = 0,1` → Gesamtinvestition `< 30 Mio. €`. Zusätzlich H2-Backup gegen H2-Design-Elektrik testen.
4. `make model report review-package`; `results.json`, `flow_fractions.tex`, Tabelle 4 und `reproduction.md` neu erzeugen; den Satz in §5 („Ein bestätigter kleiner heißer Ast erlaubt dagegen eine kleinere Anlage“) mit den neuen Werten abgleichen.

**Nachweis nach Korrektur:** Tabelle 4 zeigt für 0,1 % eine plausible Größenordnung; der Test schlägt bei Rückfall auf den alten Zustand fehl; die PDF-Seite 12 und die Seitenbilder sind neu erzeugt.

### M2 (stopprelevant): Falsches Achsenlabel in Abbildung 1

**Beleg:** PDF S. 5 (gedruckte S. 4), Abbildung 1, linke y-Achse: „Tiefe in °C“; `model/run_all.py:258` (`axes[0].set(xlabel="Jahre", ylabel="Tiefe in °C")`); Bildunterschrift „Szenariotemperatur“; Werte 9–100 °C.

**Befund:** Die linke Achse zeigt die Wassertemperatur über die Jahre, nicht die Tiefe. „Tiefe in °C“ ist physikalisch sinnlos und widerspricht der eigenen Bildunterschrift. Der Fehler ist im gerenderten Paper sichtbar und wird von `scripts/verify_report.py` nicht erkannt, weil dort nur Schriftgrößen, Geometrie und Textphrasen geprüft werden.

**Korrektur:** In `model/run_all.py:258` `ylabel="Temperatur in °C"` (oder „Wassertemperatur in °C“) setzen; `make model report review-package`; in `scripts/verify_report.py` eine Prüfung ergänzen, dass der extrahierte Seitentext auf Seite 5 nicht „Tiefe in °C“ enthält bzw. „Temperatur in °C“ enthält; PDF-Hash in `review/rounds/round6/reproduction.md` aktualisieren.

**Nachweis nach Korrektur:** Seite 5 zeigt „Temperatur in °C“; die Prüfskripte laufen; die Seitenbilder sind neu gerendert.

### M3 (minor): H3 wird nicht mit derselben Kostenregel wie H1/H2 gerechnet

**Beleg:** PDF S. 5 (gedruckte S. 4), §3.3: „Tabelle 2 und Abbildung 2 vergleichen die Alternativen mit derselben Kapazitäts- und Kostenregel“; PDF S. 6 Tabelle 2, H3 Investition 145,3 Mio. €; `model/core.py:145–148`: H3 liefert nur `pumps`, keinen `backup_power`; H1/H2 in `core.py:130–144` enthalten Backup.

**Befund:** H3 wird ohne Notstrom gerechnet, H1/H2 mit. Für H3 ist der Unterschied wegen der dominierenden Wasserkosten nicht entscheidend, aber der Satz „derselben … Kostenregel“ ist zu stark. H3 wird ohnehin vor der Kostenfrage ausgeschieden; die Tabelle sollte das ausweisen.

**Korrektur:** Entweder H3 ebenfalls mit einem skalierten Backup-Posten versehen oder die H3-Zeile ausdrücklich als „Pumpen + Wasser, ohne Notstrom“ kennzeichnen und den Satz in §3.3 präzisieren („H1 und H2 mit derselben Kapazitäts- und Kostenregel; H3 ist eine reine Pumpenkosten-Schätzung“). Tabelle 2 neu erzeugen.

### M4 (minor, Reproduzierbarkeit): Manifest deckt PDF und Reviewseiten nicht ab

**Beleg:** `output/model/manifest.json` mit 43 Einträgen; keine Einträge für `output/pdf/TEST-K31pro-max.pdf`, `output/verification_summary.json`, `review/rendered/report_pages/*.png` oder `review/rendered/report_contact.png`; `model/run_all.py:588–608` (Manifestpfade); PDF S. 11 (gedruckte S. 10), Anhang B: „Das Manifest enthält SHA-256-Hashes der Eingaben, Programme und Ergebnisse“; `review/rounds/round6/reproduction.md` nennt den PDF-Hash separat; `review/rounds/round6/revision.json` hasht alle 164 Dateien.

**Befund:** Die 43 Manifest-Hashes stimmen; die zentrale PDF und die geprüften Seitenbilder sind aber nicht im Manifest. Die Reproduktionsbehauptung stützt sich für die PDF auf `reproduction.md`, für die Seiten auf den visuellen Vergleich. Das ist transparent, aber die Formulierung „Ergebnisse“ ist breiter als der Inhalt.

**Korrektur:** Entweder einen Post-Build-Artefaktmanifest `output/artifacts_manifest.json` mit PDF, `verification_summary.json`, allen `report_pages/page-*.png` und `report_contact.png` erzeugen und in `scripts/verify_repository.py` prüfen, oder die Anhang-B-Formulierung auf „Hashes der Modell-Eingaben, Programme und Modellergebnisse“ einschränken und den PDF-Hash ausschließlich in `reproduction.md` führen. Kein Stopp-Blocker, aber vor einer Reproduktionszusage zu schließen.

### M5 (minor, Klarheit): „Wärmeabfuhr“ in der Zusammenfassung

**Beleg:** PDF S. 2 (gedruckte S. 1), Zusammenfassung: „877,8 Megawatt Wärmeabfuhr nötig“; PDF S. 4 (gedruckte S. 3), §3.2: Wärmeentzug 877,8 MW, externe Wärmeabgabe 967,2 MW; `report/main.tex` Zusammenfassung vs. §3.2.

**Befund:** „Wärmeabfuhr“ kann als Abgabe an die Luft (967,2 MW) gelesen werden; die 877,8 MW sind der Wärmeentzug aus dem Wasser. Der Körper trennt korrekt, die Zusammenfassung nicht.

**Korrektur:** „Im zehnten Jahr wären dafür 877,8 MW Kühlleistung (Wärmeentzug) nötig; an die Luft abgegeben werden 967,2 MW.“ Kein Score-Abschlag über die bereits unter 11/8 erfasste Klarheitsunschärfe hinaus.

### M6 (Präzisionshinweis, kein Fehler): ODE-Abweichung „8,1 × 10⁻¹⁰ K“

**Beleg:** PDF S. 8 (gedruckte S. 7), §5: „höchstens 8,1 × 10⁻¹⁰ K“; `output/model/results.json`, `validation.ode_max_error_k = 8,031904030758596e-10`.

**Befund:** 8,1 × 10⁻¹⁰ ist als obere Schranke korrekt (8,03 ≤ 8,1), aber nicht der gerundete exakte Wert. Kein materieller Fehler; wer die Zahl nachrechnet, sieht eine kleine Differenz.

**Korrektur (optional):** „8,0 × 10⁻¹⁰ K“ oder einen Makro aus `validation.ode_max_error_k` verwenden. Kein Score-Abschlag.

### M7 (minor, visuell/Zitation): URL-Bruch bei Referenz [19]

**Beleg:** PDF S. 10 (gedruckte S. 9), Literaturverzeichnis [19]: „reposit.haw-hamburg.de/bitstream/20. 500.12738/…“; `report/main.tex`, `\def\UrlBreaks{\do/\do-\do_\do.\do=\do?\do\&}`; der Punkt ist als Umbruchstelle erlaubt.

**Befund:** Die URL wird nach „20.“ gebrochen und sieht wie „20. 500.12738“ aus; der Hyperlink ist vollständig, der gedruckte Pfad ist irreführend.

**Korrektur:** `\do.` aus den erlaubten Umbruchstellen entfernen oder für [19] eine kürzere Anzeige-URL mit `\href` auf die vollständige URL verwenden; alle Referenzen neu prüfen. Kein Stopp-Blocker, aber visuell und für die Zitierbarkeit relevant.

### M8 (optional): Deckblatt und 0,1-%-Tick

**Beleg:** PDF S. 1 (Deckblatt) ist sehr leer; PDF S. 5 Abb. 1, rechte y-Achse hat Ticks 0, 1, 10, 100, 1000, aber keinen 0,1-Tick, obwohl die 0,1-%-Linie nahe 0,03–0,9 MW liegt.

**Befund:** Kein materieller Fehler. Das Deckblatt erfüllt alle Pflichtangaben; die 0,1-%-Linie ist sichtbar, aber ohne 0,1-Tick schwerer abzulesen. Optionale Verbesserungen.

### M9 (stopprelevant, formal): Schlussfolgerung ohne „mehr Bearbeitungszeit“-Statement

**Beleg:** PDF S. 9 (gedruckte S. 8), §6 „Schlussfolgerung“; offizielle Vorgaben §1: „Die Schlussfolgerung enthält eine prägnante Zusammenfassung der wichtigsten Ergebnisse sowie ein kurzes Statement zu Verbesserungsmöglichkeiten bei mehr Bearbeitungszeit.“; `grep` nach „Bearbeitungszeit“/„Verbesserung“ in `report/main.tex`, `docs/`, `compliance/` ohne Treffer; `compliance/checklist.md` Zeile „Pflichtaufbau … erfüllt“ prüft dieses Unterkriterium nicht; `scripts/verify_report.py` prüft nur die Abschnittsnamen.

**Befund:** Die Schlussfolgerung fasst Ergebnisse und nächste Prüfungen zusammen, enthält aber kein explizites Statement, was mit mehr Bearbeitungszeit verbessert würde. Das ist eine formale Pflichtlücke, keine inhaltliche Katastrophe.

**Korrektur:** In §6 einen Satz ergänzen, z. B.: „Mit mehr Bearbeitungszeit würden wir die Karst- und Standortmessungen, eine herstellerbasierte Teillast- und Pinch-Auslegung sowie belastbare Angebote vorziehen; das würde Kosten- und Machbarkeitsaussage weiter schärfen.“ Zusätzlich in `scripts/verify_report.py` oder der Checkliste einen Check auf „Bearbeitungszeit“/„Verbesserungsmöglichkeit“ in der Schlussfolgerung ergänzen. Nach der Korrektur PDF und Seitenbilder neu erzeugen.

---

## 3. Restrisiken und Dissens

1. **Kostenbasis:** Die 60-%-Reserve, der 60-Mio.-€-Notstromblock, 500 €/kW Kältemaschine und 120 €/kW Trockenkühler sind Szenarioannahmen, keine Angebote. Die 60-%-Reserve ist der größte Einzelposten der 1283 Mio. € und wird nicht eigens begründet oder in einer 30/60/90-%-Sensitivität gezeigt. Die Monte-Carlo-Capex-Sigma von 0,30 ersetzt diese Basissensitivität nicht. Das ist ein Restrisiko für die zentrale Kostenaussage 3,666 Mrd. €.
2. **Teillast und COP:** Die Anlage ist auf 2152,5 MW ausgelegt, der Erwartungsbetrieb liegt bei 877,8 MW (ca. 41 %). Das Modell nutzt einen konstanten COP von 4,0 und keine Teillastkurven; die 783 GWh/Jahr und 108 Mio. €/Jahr Stromkosten sind Szenarioannahmen. Der Bericht sagt „Herstellerkurven fehlen weiterhin“; das bleibt eine externe Grenze.
3. **Kondensator und Trockenkühler:** `condenser_temperature_c = 45` ist in `data/parameters.yml:54` gesetzt, wird aber im Modell nicht verwendet. Die Trockenkühlerfläche wird pauschal aus 967,2 MW und 15 K Lufterwärmung berechnet; der Kondensator hat bei 45 °C und 35 °C Luft eine andere Annäherung als die 5 K der Trockenstufe. Eine Pinch-/Flächenauslegung fehlt; der Bericht nennt die Bilanzgrößen ausdrücklich „noch keine Hersteller- oder Standortauslegung“. Restrisiko, kein Widerspruch.
4. **Externe Machbarkeit:** Karstwege, betroffener Stromanteil, Standort, Netzanschluss, Diesel-Lagerlogistik, Schall/Plume, FFH/WHG/AwSV und die menschliche Fachprüfung bleiben offen. Der Bericht macht sie zu Zulassungsbedingungen und behauptet keine Baufreigabe. Die „dauerhaft“-Aussage gilt nur innerhalb der Hülle ≤4,7 m³/s und ≤100 °C; für 32,7 m³/s ist sie ausdrücklich nicht ausgelegt.
5. **Archivreproduktion:** Die 36/36-Byte-Gleichheit ist ein Selbstbericht; ich habe sie read-only nicht nachgebaut. PDF-Hash, 43 Manifest-Hashes, 164 Revisions-Hashes und die visuell identischen 12 Seitenbilder stützen sie. Eine frische Installation der Abhängigkeiten auf einem fremden Rechner ist nicht belegt; die `.venv` wurde als Referenzumgebung verknüpft. Das bleibt ein Restrisiko für die Auslieferbarkeit.
6. **Unabhängigkeit:** `PROVENANCE.md` und `EXCLUSION_LOG.md` dokumentieren den leeren Start und zwei unbeabsichtigte Expositionen (Thread-Metadaten, Round-3-Review-Fragmente). Die aktuelle Arbeit verwendet nach eigener Darstellung keine früheren Lösungen; ich habe keine früheren Rohreviews gelesen. Die Unabhängigkeit ist plausibel dokumentiert, aber letztlich eine Vertrauensfrage.
7. **D4RT-Vergleich:** Der Bericht ist zweispaltig, typografisch konsistent und nutzt Tabellenlinien/erklärende Unterschriften wie D4RT. D4RT ist dichter, hat mehr Abbildungen und eine aufwendigere erste Seite; der Bericht bleibt bewusst bei A4/26 mm/12 pt. Der Vergleich ist subjektiv; die sichtbaren Abweichungen (Achsenlabel, leereres Deckblatt, URL-Bruch) sprechen gegen 9/10, nicht gegen die grundsätzliche Vergleichbarkeit.
8. **Testkennung und Einreichung:** `TEST-K31pro-max` ist ein Platzhalter, keine offizielle Team-ID. Der Bericht sagt „Diese Fassung wurde nicht eingereicht“; eine reale Einreichung muss Dateiname, Deckblatt und Team-ID ersetzen. Das ist eine menschliche Restaufgabe, kein Paperfehler, aber für „Bereitschaft“ relevant.
9. **Dissens:** Ich gebe auf dieser Revision keine Freigabe. Die beiden Hauptgründe sind M1 (Tabelle 4, Notstromskalierung) und M2 (Achsenlabel); M9 ist eine formale Pflichtlücke. Die Arbeit ist inhaltlich nahe an der Schwelle, aber 9/10 in jeder Zeile ist mit diesen bekannten Mängeln nicht gerechtfertigt. Die Bewertung des anderen Reviewers kenne ich nicht; ich habe ihn nicht kontaktiert und keine früheren Punktzahlen übernommen.

---

## 4. Zu den 10en

Ich vergebe **keine 10**. Damit entfällt die geforderte Beschreibung einer erfolglosen substanziellen Fehlersuche für eine 10. Die 9en in den Zeilen 1, 2, 3, 5, 8, 9 und 10 sind keine 10, weil M1, M2 und M9 bekannte Mängel sind, die mindestens die Zeilen 4, 6, 11 und 12a unter 9 drücken. Für die 9en habe ich gezielt nach Gegenbeispielen gesucht (Energiebilanz, NPV, Monte Carlo, ODE, Zitate, Seitenbudget, Anonymität, KI-Offenlegung, D4RT-Layout); in ihrem jeweiligen Zuschnitt habe ich keinen weiteren wesentlichen Mangel gefunden. Eine 10 wäre erst nach Behebung von M1/M2/M9 und einer erneuten, dokumentierten Fehlersuche vertretbar.

---

## 5. Stoppregelurteil

**Die Stoppregel ist auf dieser Revision nicht erfüllt.**

Die Zeilen 4 (Modellierung, 8), 6 (Wissenschaftliche Qualität, 8), 11 (Format/visuelle Qualität, 8) und 12a (Bereitschaft, 8) liegen unter 9. Die Stoppregel verlangt mindestens 9 in jeder Zeile von beiden Reviewern und keine ungelösten substantiellen Einwände gegen Korrektheit, wissenschaftliche Qualität, Unabhängigkeit, Compliance oder Auslieferbarkeit. Mit M1 (Notstromskalierung in Tabelle 4), M2 (falsches Achsenlabel in Abbildung 1) und M9 (fehlendes Pflichtstatement in der Schlussfolgerung) sind solche Einwände offen.

Die Arbeit ist nahe an der Schwelle: Die Hauptargumentation, die Lösung, die Originalität, die Klarheit, die kritische Diskussion und die Struktur liegen bei 9; die formalen Anforderungen sind bis auf M9 erfüllt; die Archivreproduktion ist durch PDF- und Manifest-Hashes gestützt. Nach einer Korrektur von M1 und M2, idealerweise auch M3, M4, M5, M7 und M9, sowie einer erneuten Prüfung der dann erzeugten PDF/Seitenbilder halte ich eine 9/10-Freigabe für möglich. Auf der eingefrorenen Revision `473e397` ist sie aus meiner Sicht nicht gerechtfertigt.