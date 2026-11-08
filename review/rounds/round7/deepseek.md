# Rohbericht Runde 7 — unabhängige Prüfung

**Prüfgegenstand:** Commit `a405cd19f187e2e6c80b51453617a6b6d883ae2a`, ausschließlich diese Revision.  
**Modus:** read-only; keine Datei geändert, erzeugt oder gelöscht; kein Build, kein `git`-Eingriff. Geprüft wurden alle zwölf PDF-Seiten, die Kontaktübersicht, das Modell, `results.json`, die Archivreproduktion, Quellen, Compliance und die D4RT-Seiten 1, 2 und 6.  
**Revision:** `HEAD` steht auf `a405cd1`; 172 von 172 in `review/rounds/round7/revision.json` gelisteten Dateien stimmen byteweise. Die PDF hat den dort angegebenen Hash `44a5751389b6ae580ba9d560ed6292867a78f188f035fb4e66705efa7bd80da7`. Einzige unversionierte Dateien sind `review/rounds/round7/prompt.md` und `revision.json` (Prüfauftrag), nicht von mir verändert. Frühere Rohreviews oder Scorecards habe ich nicht gelesen; Kenntnis früherer Befunde nur aus `review/revisions.md` ohne Punktzahlen.

## 1. Bewertungen

| Nr. | Kriterium | Note | Kurze Begründung | Genauer Belegort |
|---|---|---:|---|---|
| 1 | Qualität der Argumentation | **9** | Der Bericht trennt sauber zwischen ökologischem 9-°C-Normalziel und reinem Siedeschutz, begründet den Vollstromansatz mit der nicht vermessenen Karststruktur und macht die Gültigkeitsgrenzen (4,7 m³/s, 100 °C) explizit. Die H2-Aussage „physikalisch gleichwertig“ ist etwas stärker als das unmodellierte Wärmeübertrager-Pinch (Restrisiko R1), trägt aber die Hauptargumentation nicht. | PDF S. 2–3 (§1), S. 3 (§2.1), S. 3–5 (§3.1–3.3), S. 6 (§4.3), S. 8 (§6); `docs/hypothesen.md`; `docs/alternativenvergleich.md` |
| 2 | Vorgehen und Methodik | **9** | Transparente Eingaben, Gleichungen, Modell, 16 Tests, Validierungsfehler, Monte-Carlo, Sensitivitäten, Manifest und dokumentierte Archivreproduktion. Die Reproduktion ist nachvollziehbar dokumentiert, aber von mir nicht erneut gebaut (read-only); der Freeze-Commit ergänzt nur Dokumentation, die 36 Paperartefakte sind als byte-identisch belegt. | `data/parameters.yml`; `model/core.py`; `model/validation.py`; `model/test_model.py` (16 Testmethoden); `output/model/results.json` (`coupled_npv_error_eur=0.0`, `ode_max_error_k=8,03e-10`, `failure_p90_convergence_error_k=1,79e-12`); `output/model/manifest.json`; `review/rounds/round7/reproduction.md`; `review/rounds/round7/revision.json` |
| 3 | Qualität der vorgeschlagenen Lösung | **9** | Zweistufige Vollstromkühlung, 12 Stränge à 179,4 MW, p90 + 20 % Reserve, sechs plus ein Reserveaggregat, 48-h-Dieselvorrat, Mess- und Falsifikationsplan, Standort- und Genehmigungsbedingungen. Die Lösung ist ausdrücklich ein bedingter Szenarioentwurf, keine Baufreigabe; die offenen Standort-, Netz- und Herstellerdaten bleiben sichtbar. | PDF S. 3–5 (§3.1–3.3), Tabelle 2 S. 5, Abbildung 2 S. 6, S. 5–6 (§4.2–4.3), S. 8 (§6); `model/core.py`; `docs/alternativenvergleich.md` |
| 4 | Mathematische und wissenschaftliche Modellierung | **9** | Gleichungen (1)–(10) sind dimensions- und vorzeichenkorrekt; Wärme-, Kondensator-, Mischungs- und Speicherbilanzen stimmen; die zentrale Handrechnung ergibt 877,781 MW; die p90-Kopplung ist bis auf 9,5 × 10⁻⁷ € (Rundung) null. Restrisiken: H2-Pinch, lokaler Siedepunkt, Kostenbasis 2012, Beckenvolumen (R1–R4); sie sind begrenzt und betreffen den Hauptpfad H1 nicht. | PDF S. 3–5 (Gl. 1–10), S. 5–7 (§4.2–4.4), S. 10 (Handrechnung); `model/core.py:39–246`; `model/validation.py:27–173`; `output/model/results.json`; eigene Read-only-Nachrechnung von `run_validation` und der p90-Kopplung |
| 5 | Ableitung neuer Ansätze statt Wiederverwendung | **9** | Das Repository begann leer; sieben physikalisch verschiedene Ansätze sind vor der Quantifizierung registriert; H1 wird erst nach der Wärmebilanz vom Teilkreislauf auf den Vollstrom skaliert. Keine früheren PlaNeT-Lösungen; D4RT dient nur dem Layout. Die Same-Model-Review ist offengelegt, nicht als externe Prüfung ausgegeben. | `PROVENANCE.md`; `EXCLUSION_LOG.md`; `docs/hypothesen.md`; `sources/registry.yml`; PDF S. 3 (§2.1), S. 10–11 (Anhang A); `review/model_configuration.md` |
| 6 | Wissenschaftliche Qualität | **9** | Klare Frage, quantitatives Szenario, Quellen, Unsicherheitsanalyse, Falsifikationskriterien und offene Grenzen. Die zentralen Hydrologiewerte sind textlich bestätigt: Fan et al. nennen Mittel 2,3 m³/s sowie 10-/90-Perzentil 0,7/4,7 m³/s; das LGRB nennt NQ 0,251, MQ 2,330 und HQ 32,700 m³/s. Keine Feldvalidierung wird behauptet. Restrisiken: fehlende Standort-, Netz-, Hersteller- und Karstdaten (R7). | PDF S. 2–8; `sources/registry.yml` [2], [3]; Fan et al.-PDF (via KIT, Textstelle „Mean = 2.3“ und „10th and 90th percentiles … 0.7 and 4.7“); LGRB-Seite (NQ/MQ/HQ); `PROVENANCE.md`; `docs/alternativenvergleich.md` |
| 8 | Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen | **9** | Annahmentabelle, Gleichungen, generierte Zahlen, erklärende Bildunterschriften, Abschnittsführung und Grenzen sind nachvollziehbar; die Zusammenfassung ist vollständig und ohne unerklärte Kürzel. Die formalen Auffälligkeiten (Anhang C, Tabellenfloat, Appendixtypografie) sind Layout-, keine Erklärungsmängel. | PDF S. 2–3 (Zusammenfassung, Tabelle 1), S. 3–5 (Gl. 1–10), S. 5 (Tabelle 2), S. 5–8 (Abb. 1–3), S. 10–12 (Anhang A/C); `report/generated/numbers.tex` |
| 9 | Kritische Diskussion der Ergebnisse | **9** | Breite Diskussion: Standort und Genehmigung (§4.3), Unsicherheit und Hochwasser (§4.4), Nachweis und Falsifikation (§5), Grenzen und menschliche Restaufgaben (§6); H2-Wasser/Hygiene, H3-Quelle, H7-Fläche; p90 ist kein Extremwertnachweis; der Ausfalltest ist kein Feldversuch. Die Kostenbasis 2012, der H2-Pinch, der lokale Siedepunkt, das Beckenvolumen und das 48-h-Diesel-/95-%-Verfügbarkeitsverhältnis bleiben als Restrisiken sichtbar. | PDF S. 5–8 (§4.2–§6); `docs/alternativenvergleich.md`; `README.md`; `PROVENANCE.md` |
| 10 | Klare Berichtsstruktur und jury-nachvollziehbare Argumentation | **9** | Pflichtaufbau vollständig: Deckblatt, Zusammenfassung, Einführung, Methode, Ergebnisse, Diskussion, Schlussfolgerung, Literatur, Anhang; 7 Haupttextseiten plus 4 Seiten Literatur/Anhang, innerhalb des Budgets. Der Anhang-C-Sprung und der Tabellenfloat sind sichtbare Layout-/Nummerierungsfehler, beeinträchtigen aber die Argumentationskette nicht. | PDF S. 1–12; `review/verification_summary.json` (`main_pages=7`, `bibliography_and_appendix_pages=4`); `scripts/verify_report.py`; `compliance/checklist.md` |
| 11 | Format, Zitation und Einreichungsanforderungen, einschließlich D4RT-Vergleich | **8** | Formal erfüllt: A4, 26 mm Rand, 12 pt, 1,2 Zeilenabstand, Deutsch, anonym, Deckblatt, Zusammenfassung, Seitenbudget, numerische Verweise, URLs/DOIs, Abrufdaten, KI-Offenlegung. Abwertung wegen sichtbarer Formfehler: „Anhang C“ ohne „Anhang B“ (PDF S. 12; §4.4 S. 8), Tabelle 1 zerschneidet „Wärmeentnahme“ (PDF S. 2/3), Appendix A mit weit gespreizten Wortabständen (PDF S. 11), [6] ohne Untertitel sowie [5]/[7]/[8] ohne Jahr. D4RT ist visuell dichter/aufwändiger; der Bericht bleibt bewusst bei A4/12 pt/26 mm und kopiert D4RTs 10-pt-/20,7-mm-/US-Letter-Verstöße nicht. | PDF S. 1–12; `report/main.tex:52–74, 202, 233–236, 258–269`; `report/preamble.tex:1,5,26,31,37–43`; `pdfinfo` (12 Seiten, A4 595,28 × 841,89); `pdftohtml`-Schriftgrößen (Median 12 pt); `compliance/checklist.md`; `compliance/layout_referenz.md`; `review/rendered/d4rt_page01/02/06.png` |
| 12a | Bereitschaft für die schriftliche Runde | **9** | PDF, LaTeX-Quelle, Modell, Ergebnisse, Manifest, Reproduktionsnachweis und Compliance-Checkliste liegen vor; die Testkennung, die fehlende offizielle Team-ID und die fehlende menschliche Fachprüfung sind ausdrücklich als Restaufgaben benannt, keine Einreichung wird behauptet. | `README.md`; `compliance/checklist.md`; `PROVENANCE.md`; `review/rounds/round7/reproduction.md`; PDF S. 1, 10–11; `review/model_configuration.md` |

## 2. Mängel und konkrete Korrekturen

### A. Formale Mängel, die die 8 in Kriterium 11 tragen

1. **„Anhang C“ ohne „Anhang B“.**  
   **Beleg:** PDF S. 12 (Druckseite 11) beginnt mit „Anhang C: Ergänzende Ergebnisse“; §4.4 verweist auf PDF S. 8 (Druckseite 7) auf „Anhang C, Tabelle 3 und Tabelle 4“. In `report/main.tex` fehlt jede Anhang-B-Überschrift; die Handrechnung liegt in Anhang A (Zeile 264). `review/revisions.md` (Runde 3, M12) spricht noch von „Anhang B“.  
   **Korrektur:** In `report/main.tex` Zeile 269 „Anhang C“ → „Anhang B“ und Zeile 202 „Anhang C“ → „Anhang B“; neu bauen; PDF S. 8 und S. 12 prüfen. Alternativ einen kurzen „Anhang B: Handrechnung“ wieder einfügen und C beibehalten — dann beide Verweise konsistent halten.

2. **Tabelle 1 zerschneidet den Absatz und das Wort „Wärmeentnahme“.**  
   **Beleg:** PDF S. 2 endet unten mit „geologische Wärmeent-“; PDF S. 3 beginnt mit Tabelle 1, darunter setzt der Absatz mit „nahme, Bypass, Druckverschiebung …“ fort. Ursache: `table*` mit `[!t]` in `report/main.tex:52–71` vor dem Absatz `:73–74`.  
   **Korrektur:** Den `table*`-Block hinter den Absatz Zeile 73–74 verschieben oder als nicht schwebende Vollbreitentabelle am Seitenanfang setzen; alternativ die Tabelle in den Anhang verschieben und im Text auf „Tabelle 1“ verweisen. Neu rendern und prüfen, dass „Wärmeentnahme“ nicht über die Tabelle getrennt wird (PDF S. 2–3).

3. **Appendix A mit weit gespreizten Wortabständen.**  
   **Beleg:** PDF S. 11, erster Absatz „Kimi K3.1 Pro bei thinking=max erstellte Recherche, Code, Text und Grafiken.“; die unumbrechbaren `\texttt`-Token und `\sloppy` (`report/preamble.tex:31`) erzeugen große Lücken.  
   **Korrektur:** Die Appendix-A-Absätze in `\raggedright` setzen oder in `\texttt{thinking=max}` / `\texttt{reasoning\_effort=max}` Umbruchstellen (`\allowbreak`, `\-`) zulassen; `\sloppy` gezielt für diese Passage entschärfen. Neu rendern; PDF S. 11 prüfen.

4. **Zitationsdetails.**  
   **Beleg:** [6] auf PDF S. 9 nennt nur „Towards a better understanding of the evaporative cooling of rivers“; der vollständige Titel lautet laut Crossref „…: case study for the Little Southwest Miramichi River (New Brunswick, Canada)“. [5], [7] und [8] (PDF S. 10) nennen kein Jahr.  
   **Korrektur:** [6] um den Untertitel ergänzen; [5] IAPWS IF97-Rev. (2007), [7] Bergman et al. (2011) und [8] OpenStax (2016/2023) mit Jahr versehen; `report/main.tex:233–236` anpassen und PDF S. 9–10 prüfen.

### B. Technische Restrisiken (nicht der Grund für die 8, aber sichtbar)

1. **H2-Wärmeübertrager-Pinch.**  
   **Beleg:** `model/core.py:60–81` setzt für H2 den Prozessaustritt auf `wet_bulb + approach = 32 °C`; der Bericht beschreibt zugleich einen separaten Sekundärkreislauf (PDF S. 4–5, §3.3). Wenn die 4 K die Kühlturmannäherung sind, liegt der Sekundärkreis bei 32 °C und der Quellstrom kann nicht ebenfalls auf 32 °C abgekühlt werden; die 655,9/221,9-MW-Aufteilung wäre optimistisch.  
   **Korrektur:** Den Wärmeübertrager-Pinch separat ansetzen (z. B. Quellaustritt 36 °C bei 4 K Pinch) oder ausdrücklich sagen, dass die 4 K den gesamten Wärmeübergang einschließen; H2-Zahlen und Tabelle 2 neu rechnen. Die qualitative Aussage „H2 billiger, aber Wasserrisiko“ bleibt voraussichtlich erhalten.

2. **Lokaler Siedepunkt am Standort.**  
   **Beleg:** `data/parameters.yml:34–39` und PDF S. 3/7 verwenden 3,17007 bar und 99,9743 °C bei 1,01325 bar. Der Blautopf liegt bei etwa 520 m ü. NN; der lokale Atmosphärendruck liegt bei ca. 0,95 bar, die Sättigungstemperatur bei ca. 98,7 °C, die 5-K-Schutzmarke bei ca. 93,7 °C.  
   **Korrektur:** Den lokalen Atmosphärendruck ansetzen oder die 1,01325-bar-Annahme ausdrücklich als Standardbedingung nennen und die Standortdaten als offene Grenze führen; `GuardTarget`, `GuardCooling`, `GuardCapex` und `GuardNpv` für den lokalen Druck neu berechnen. Der Hauptpfad H1 (9 °C) ist davon nicht betroffen.

3. **Kostenbasis 2012 vs. „Euro von 2026“.**  
   **Beleg:** `data/parameters.yml:103–120` und PDF S. 3 (§2.2) nennen 500 €/kW Kältemaschine und 120 €/kW Trockenkühler nach [19]; [19] ist eine HAW-Arbeit von 2012. Der Bericht bezeichnet die Kosten als „Euro von 2026“, ohne Baupreisindex/Eskalation; die 60 % sind Engineering-Contingency, nicht Inflation.  
   **Korrektur:** Preisbasis 2012 offenlegen und mit einem Baupreisindex auf 2026 eskalieren oder eine Sensitivität ±30 % zeigen; die 1283 Mio. € und 3,663 Mrd. € als Bandbreite kennzeichnen.

4. **Beckenvolumen und 0,9-min-Marge.**  
   **Beleg:** `data/parameters.yml:9–10` (25.000 m³, „Rechenannahme“), `model/validation.py:27–71`; PDF S. 5 (§4.2) berichtet 12,9 °C bzw. 16,7 °C und 0,9 min p90-Marge. Die Marge hängt direkt an Volumen und „ideal gemischt“; eine Volumen-/Mischungssensitivität fehlt.  
   **Korrektur:** Die 20-°C-Zeit und die p90-Marge für z. B. 10.000/25.000/50.000 m³ und für einen Mischungsgrad < 1 zeigen; die 0,9 min ausdrücklich als nicht frei verfügbare Wartezeit und als Annahme kennzeichnen (der Bericht tut Letzteres bereits).

5. **48-h-Dieselvorrat vs. 95-%-Verfügbarkeitsszenario.**  
   **Beleg:** `data/parameters.yml:74–78` (48 h, 2,237 Mio. Liter), `output/model/results.json` `availability_scenarios` (bei 95 %: 9,99 Mio. Liter), PDF S. 5–7. Der 95-%-Fall unterstellt „vollständigem Dieselersatz“ und übersteigt den 48-h-Vorrat um Faktor 4,5.  
   **Korrektur:** Im Text ausdrücklich sagen, dass der 95-%-Fall eine Kostensensitivität mit unbegrenzter Dieselverfügbarkeit ist und der 48-h-Vorrat nur den Kurzausfall deckt; alternativ den Vorrat für die 5-%-Ausfallzeit dimensionieren.

6. **Archivreproduktion nicht unabhängig nachgebaut.**  
   **Beleg:** `review/rounds/round7/reproduction.md` dokumentiert `git archive 1878af8`, `make model test report`, `make review-package`, `make verify`, 16 Tests und 36/36 byte-identische Paperartefakte. Der Freeze-Commit `a405cd1` ändert nur `decisions.tsv`, `review/README.md`, `review/revisions.md` und `review/rounds/round7/reproduction.md`; die 172 Hashes und der PDF-Hash stimmen. Ich habe keinen Build ausgeführt (read-only).  
   **Korrektur:** Keine in dieser Runde; im nächsten Umlauf einen unabhängigen Archivbuild mit Hashvergleich wiederholen oder die 36/36-Dokumentation als akzeptierte Grenze führen.

7. **Same-Model-Review, keine menschliche Prüfung, keine Felddaten.**  
   **Beleg:** `review/model_configuration.md`; PDF S. 11 (Anhang A); `PROVENANCE.md`; `EXCLUSION_LOG.md`; §4.3/§6. Council B ist ein separates Kimi-Exemplar, kein externer/menschlicher Reviewer; Standort, Netz, Herstellerkurven und Karstmessungen fehlen.  
   **Korrektur:** Keine Erfindung; die Offenlegung ist korrekt. Vor einer echten Einreichung menschliche Fachprüfung, offizielle Team-ID und Rechteklärung nachholen.

8. **D4RT-Visualvergleich.**  
   **Beleg:** `review/rendered/d4rt_page01/02/06.png`; `sources/D4RT_paper.pdf` (17 Seiten, US Letter, 10-pt-Umfeld); `compliance/layout_referenz.md`. Der Bericht ist typografisch konsistent und formal sauberer (A4, 12 pt, 26 mm), aber weniger dicht/illustrativ als D4RT.  
   **Korrektur:** Keine Übernahme der D4RT-Verstöße; die 8 in Kriterium 11 folgt aus den konkreten Formfehlern A1–A4, nicht aus geringerer Dichte. Optional: eine der beiden Berichtsabbildungen stärker als D4RT-integrative Grafik aufbauen (z. B. Prozessschema mit Wärmepfaden), ohne die 12-pt-Regel zu verletzen.

## 3. Restrisiken und Dissens

- **Die 8 in Kriterium 11 ist der einzige Punktabzug.** Sie ist keine Aussage über die wissenschaftliche Qualität; die Kriterien 1–6, 8–10 und 12a liegen bei 9. Ein Reviewer, der „Anhang C“, den Tabellenfloat und die Appendixtypografie als rein kosmetisch einstuft, könnte 11 mit 9 bewerten. Ich bewerte sie strenger, weil die 9-Definition „nur optionale Verbesserungen“ verlangt und diese Punkte vor einer Abgabe sichtbar zu korrigieren sind.
- **H2-Pinch und lokaler Siedepunkt** sind die wahrscheinlichsten fachlichen Juryfragen. Der Bericht sagt „Pinch-Auslegung … future“ (§6) und „Standort … prüfen“ (§4.3), aber die konkreten H2-Zahlen und die 5-K-Schutzmarke sind ohne diese Annahmen etwas zu optimistisch. Der Hauptpfad H1 (9 °C, 877,8 MW, 2152,5 MW installiert) ist davon nicht abhängig.
- **Kostenbasis 2012:** Die 60-%-Contingency kann die Preissteigerung teilweise auffangen, ist aber nicht als Eskalation deklariert. Die Aussage „Euro von 2026“ ist daher eine offene Setzung; die Rangfolge H2 < H1 und die Aussage „wirtschaftlich anspruchsvoll“ bleiben robust.
- **0,9-min-Marge:** Sie ist ein Rechenergebnis aus 25.000 m³ und idealer Mischung, keine Zuschaltprobe. Der Bericht sagt das; eine Volumensensitivität fehlt.
- **Archivreproduktion:** Die 36/36-Identität ist dokumentiert und über Hashes/Freeze-Commit gestützt, aber nicht von mir nachgebaut. Ich markiere das ausdrücklich als **ungeprüft im engeren Sinne**; die Revision selbst ist hashkonsistent.
- **Quellen:** [2] und [3] sind textlich bestätigt (2,3/0,7/4,7 m³/s; HQ 32,7 m³/s), [6] und [22] über Crossref/PDF-Metadaten; [4] NIST-Werte sind über die Daten und die Handrechnung konsistent. [16], [19] und [23] habe ich nicht extern nachgerechnet; sie sind als Szenario-/Proxy-Quellen gekennzeichnet. Das ist ein Restrisiko, kein bekannter Fehler.
- **Anonymität und KI-Offenlegung** sind sauber: PDF-Autorenmetadaten leer, kein Personenname, Testkennung und fehlende menschliche Prüfung offengelegt; die KI-Systeme, Rollen und Einstellungen stehen in Anhang A und `PROVENANCE.md`.
- **D4RT** wird nur als Layoutmaßstab verwendet; die D4RT-Seiten 1/2/6 sind visuell verglichen, die Inhalte nicht übernommen. Die D4RT-Formatverstöße (US Letter, 10 pt, 20,7 mm) werden bewusst nicht kopiert.

## 4. Zehner

**Keine 10 vergeben.** Für keine Zeile blieb nach der Fehlersuche ein Zustand „nur optionale Verbesserungen“ ohne sichtbare Restpunkte. Die Fehlersuche ist in den Begründungen zu 4, 6, 9 und 11 dokumentiert; sie hat die formalen Mängel A1–A4 und die technischen Restrisiken B1–B8 gefunden. Deshalb 9/8 statt 10.

## 5. Stoppregelurteil

**Auf dieser Revision nicht erfüllt.**  
Zehn Kriterien liegen bei 9, **Kriterium 11 bei 8**. Die Stoppregel verlangt mindestens 9 in jeder Zeile; 8 < 9. Der Grund ist formal/visuell (Anhang C, Tabellenfloat, Appendixtypografie, Zitationsdetails), nicht ein wissenschaftlicher Kernfehler. Nach den Korrekturen A1–A4 ist eine 9 in Kriterium 11 und damit die Stoppregel aus meiner Sicht erreichbar; die technischen Restrisiken B1–B8 sind dann weiter sichtbar zu halten und, soweit sie die Jury betrifft, zu schließen oder ausdrücklich als akzeptierte Grenzen zu dokumentieren.

Die zweite Reviewerstimme lag mir nicht vor; ich habe keinen Kontakt aufgenommen und keine früheren Rohreviews oder Scorecards gelesen. Mein Urteil beruht ausschließlich auf der eingefrorenen Revision `a405cd1`, den zwölf gerenderten Seiten, dem Modell, den Quellen und den Reproduktions-/Compliance-Nachweisen.