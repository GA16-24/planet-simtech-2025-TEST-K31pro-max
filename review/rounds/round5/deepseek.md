# Rohbericht Runde 5 — Commit `e821bf60ef9fe637a5c5915a50d7748ab829c46c`

## 1. Prüfgegenstand, Umfang und Read-only-Status

Geprüft wurde ausschließlich der eingefrorene Commit `e821bf60ef9fe637a5c5915a50d7748ab829c46c`. Der Arbeitsbaum ist bis auf die vorgegebenen, nicht versionierten Dateien `review/rounds/round5/prompt.md` und `review/rounds/round5/revision.json` unverändert; der Git-Stand wurde nicht verändert.

Geprüft wurden: das tatsächlich gerenderte 12-seitige PDF (alle Seiten, Kontaktbogen und Einzelseiten), die 10 Folien, die MP4-Datei (Streams, Frames, vollständige Decodierung, Audio, VTT), Modell und Eingaben, `results.json`, `hybrid_schedule.csv`, `sensitivity.csv`, `manifest.json`, `revision.json`, die Reproduktions- und Compliance-Dokumente, Sprechtext, Zeitprotokoll, Jury-Q&A und Rechte.

Read-only-Vorgehen: keine Builds, keine Dateien geschrieben, keine Verzeichnisse angelegt; Python mit `PYTHONDONTWRITEBYTECODE=1`; PDF-Prüfung mit Poppler und pdfplumber; Video mit `ffprobe`, `ffmpeg -f null` und `volumedetect`; die 11 Modelltests liefen read-only und bestanden. **Die vollständige Archivreproduktion und `make verify` habe ich nicht selbst ausgeführt**, weil beide Dateien schreiben. Ich habe stattdessen die Hashes, den Kandidaten-/Freeze-Vergleich und die Dokumentation geprüft. Dieser Punkt bleibt ausdrücklich ungeprüft und wird unten als Restrisiko geführt.

Hash- und Revisionsprüfung: `revision.json` enthält 155 getrackte Dateien; alle SHA-256-Werte stimmen mit dem Arbeitsbaum überein. `output/model/manifest.json` enthält 42 Einträge; alle stimmen. Berichts-PDF (`af0883cd…`) und Video (`c80cd24c…`) stimmen mit `revision.json` überein. `git diff 9d8f4df e821bf6` zeigt nur `decisions.tsv`, `review/revisions.md` und `review/rounds/round5/reproduction.md`; die bewerteten Artefakte sind also die des reproduzierten Kandidaten. Die Reproduktion selbst ist jedoch ein Selbstbericht des implementierenden Agenten (`review/rounds/round5/reproduction.md:3`).

Die vorgegebene Kriterienliste enthält kein Kriterium 7 (Sprung von 6 zu 8). Ich erfinde keines; die zwölf bewerteten Zeilen sind 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12a und 12b.

## 2. Bewertungstabelle

| Nr. | Kriterium | Note | Kurze Begründung | Genaue Belegorte |
|---|---|---:|---|---|
| 1 | Qualität der Argumentation | **8** | Klare Vollstrom-These, saubere Alternativenprüfung, Grenzen und Falsifikation. Abzug für die rhetorische Gegenüberstellung 0,0303 MW vs. 877,8 MW („Fehler einer Auslegung“) und die schief formulierte 38,57-%-Aussage; der MC-Kostenwiderspruch bleibt argumentativ unaufgelöst. | PDF S. 2, 4, 7; `report/main.tex:30-36,106-116,198`; `model/run_all.py:104-152` |
| 2 | Vorgehen und Methodik | **8** | Parametrisiertes Modell, 11 Tests, ODE-Konvergenz, Sensitivität, MC, Alternativen. Abzug für den unentdeckten MC-Kostenfehler, die fehlende Prüfung am Auslegungspunkt und die nicht unabhängig nachgebaute Archivreproduktion. | `model/core.py`; `model/validation.py`; `model/run_all.py:129-165,223-237`; `review/rounds/round5/reproduction.md` |
| 3 | Qualität der vorgeschlagenen Lösung | **9** | Zweistufige Trocken-/Kältekühlung, p90 + 20 %, 12 Stränge (11 + 1), Notstrom, Puffer, 1-K/h-Rampe, Standort- und Genehmigungs-Screening. Technisch schlüssig und klar begrenzt; der Guard-Kostenfehler betrifft nur die Vergleichsvariante, nicht die Hauptlösung. | PDF S. 2, 5–6; `report/main.tex:30-36,125-146,180-192`; `results.design` |
| 4 | Mathematische und wissenschaftliche Modellierung | **8** | Kernphysik korrekt und validiert. Aber `coupled_npv` verdoppelt am Auslegungspunkt die variablen Capex (7,421 vs. 5,449 Mrd. €, +36 %), `boil_guard` trägt 60,0 Mio. € Backup für 1,07 MW, und die latente Wärme ist der 20-°C-Wert für einen 100→32-°C-Prozess. | `model/run_all.py:129-136`; `model/core.py:123`; `results.uncertainty.npv_p95_eur`, `results.design.npv_25y_eur`, `results.boil_guard.final_capex_eur`; `data/parameters.yml:16` |
| 5 | Ableitung neuer Ansätze statt Wiederverwendung | **9** | Sieben physikalisch verschiedene, selbst hergeleitete Ansätze; keine früheren Lösungen; keine weltweite Neuheit behauptet. Die Lösung ist konventionell, aber eigenständig dimensioniert. | `docs/hypothesen.md`; `docs/alternativenvergleich.md`; `PROVENANCE.md`; `EXCLUSION_LOG.md`; PDF S. 2–3 |
| 6 | Wissenschaftliche Qualität | **8** | Offenlegung, Quellen, Validierung, Falsifikation, Unsicherheit. Abzug für den MC-Kostenfehler, die nicht unabhängige Archivreproduktion und die fehlende externe oder menschliche Prüfung. | PDF S. 8; `model/test_model.py`; `output/model/results.json`; `review/rounds/round5/reproduction.md`; `review/model_configuration.md` |
| 8 | Klare Erklärung von Annahmen, Methoden, Ergebnissen, Schlussfolgerungen | **8** | Annahmentabelle, Modellgrenzen, Ergebnisgrößen, Schlussfolgerung. Abzug für die mehrdeutige 38,57-%-Aussage, die „benötigen“-Formulierung der Speicherrechnung, die fehlende Jährlichkeit zu 32,7 m³/s und die Satzfehler. | PDF S. 2–4, 7; `report/main.tex:50-71,106-116,198` |
| 9 | Kritische Diskussion der Ergebnisse | **9** | Sehr gute Diskussion von H2, H3, H4–H7, Hochwasser, Standort, Netz, FFH, Ausfall, 9 °C vs. Siedeschutz, 38,57 %, p90-Grenzen. Keine 10, weil der MC-Kostenfehler nicht diskutiert wird. | PDF S. 4–8; `docs/alternativenvergleich.md`; `presentation/jury_qa.md` Q1–Q27 |
| 10 | Klare Berichtsstruktur und für die Jury nachvollziehbare Argumentation | **8** | Pflichtaufbau, klare Kapitel, Zusammenfassung, Schlussfolgerung. Abzug für die unter Anhang B statt C platzierte Abbildung 3 und die fast leere Seite 10, die den Lesefluss der Unsicherheitsdiskussion bricht. | PDF S. 7, 10, 12; `report/main.tex:250,269-276` |
| 11 | Format, Zitation, Einreichungsanforderungen, visuelle Qualität vs. D4RT | **7** | Formalia weitgehend erfüllt, aber: fast leere Seite 10, geteilte Bibliothekseinträge [10]/[25], gequetschte Tabelle 1, „74, 756“, `‘data/parameters.yml‘`, Einheitenumbrüche, lange URL-Umbrüche, einspaltige Anhänge mit überlangen Zeilen. D4RT ist deutlich dichter und sauberer. | PDF S. 3, 4, 8, 9, 10, 11, 12; `report/main.tex:54,208,232,247,250`; `compliance/layout_referenz.md`; D4RT S. 1/2/6 |
| 12a | Bereitschaft für die schriftliche Runde | **8** | Bericht vollständig, anonym, im Seitenbudget, Quellen und KI-Offenlegung. Aber Modell- und Layoutmängel sowie Testkennung/fehlende offizielle Team-ID und die nicht unabhängig nachgebaute Archivreproduktion verhindern „abgabebereit ohne wesentlichen Mangel“. | PDF; `compliance/checklist.md`; `README.md`; `review/rounds/round5/reproduction.md` |
| 12b | Bereitschaft für die Finalrunde | **8** | Echte MP4 (290,232 s, 1920×1080, H.264/AAC), 10 Folien, Sprechtext, Zeitprotokoll, 27 Q&A, Rechte. Aber Folie 8 überlappt „1053,3“ mit der 500-Achsenmarke, die Folien sind aus 945×531-PNGs hochskaliert, die VTT ist wortproportional und nicht forced-aligned, die „Zeitprobe“ ist eine technische Wiedergabe. | `output/presentation/Blautopf_Finale.mp4` (ffprobe); `slide-08.png`; `presentation/figures/unsicherheit.png`; `presentation/timings.json`; `presentation/rehearsal.md`; `presentation/jury_qa.md` |

## 3. Materielle Mängel mit konkreten Korrekturen

### M1 — `coupled_npv` verdoppelt die variablen Capex am Auslegungspunkt (Hauptbefund)

**Befund.** `model/core.py:123` setzt in `variable_capex_eur` bereits

```text
capacity_scale = design_flow_ratio(p) * (1 + reserve_fraction)
```

also die p90-Skalierung plus 20 % Reserve. `model/run_all.py:129-136` multipliziert diese bereits skalierte Größe in `coupled_npv` erneut mit `flow_ratio` (Exchanger, Chiller) bzw. mit `(dry + condenser) * design_flow_ratio` (Dry Cooler) und `backup_ratio` (Backup). Am Auslegungspunkt `flow_ratio = 4,7/2,3 = 2,0435` wird dadurch jeder variable Posten ein zweites Mal mit dem Faktor 2,0435 skaliert.

**Reproduzierbare Ausgabe** (read-only Python-Sitzung, `PYTHONDONTWRITEBYTECODE=1`):

```text
coupled_npv(p, 4.7, 4.0, 1.0)            = 7.420.964.951 €
npv(economic_schedule(design_p))          = 5.448.799.139 €
Differenz                                 = 1.972.165.812 €  (+36,2 %)
```

Der Basispunkt 2,3 m³/s stimmt mit 3.666.015.955 € überein; genau dieser Punkt wird in `model/run_all.py:163-165` geprüft (`coupled_npv_error_eur = 0.0`). Der Auslegungspunkt 4,7 m³/s wird nicht geprüft. `model/validation.py` und `model/test_model.py` enthalten keinen Test dieser Konsistenz.

**Wirkung.** Die Monte-Carlo-NPV-Quantile (`results.uncertainty.npv_p05/p50/p95 = 1,829 / 3,729 / 6,491 Mrd. €`), Abbildung 3, die Folie-8-Grafik und die Aussage „Die gekoppelte Referenzkostenrechnung schließt mit Fehler null“ (`report/main.tex:208`) sind nicht mit der Auslegungsrechnung konsistent. Der zentrale NPV 3,666 Mrd. € und der Design-NPV 5,449 Mrd. € sind davon nicht betroffen; die Unsicherheitsaussage und die p95-Zahl sind es. Eine indikative Gegenrechnung mit linearer Skalierung auf den Auslegungspunkt ergab p95 ≈ 5,56 Mrd. €; eine Interpretation als feste p90-Anlage ergab ≈ 6,44 Mrd. €. Der exakte Wert hängt von der gewählten Skalierungsregel ab; der Widerspruch am Auslegungspunkt bleibt in beiden Fällen.

**Konkrete Korrektur.**
1. Eine einzige Skalierungsregel festlegen: Entweder ist die Anlage fest auf p90 ausgelegt (dann darf `coupled_npv` die Capex nicht mit dem Abfluss skalieren; nur Betrieb, COP und der explizite Capex-Multiplikator variieren), oder sie wird pro Ziehung dimensioniert (dann die bereits design-skalierte Größe mit `flow_ratio / design_flow_ratio` skalieren, nicht mit `flow_ratio`; den Fixkostenblock konsistent behandeln).
2. Regressionstest hinzufügen: `coupled_npv(p, design_discharge, 4.0, 1.0) == npv(economic_schedule(design_p))` auf 1 € genau, zusätzlich zum Basispunkt 2,3 m³/s.
3. `uncertainty.npv_p05/p50/p95`, Abbildung 3, Folie 8 und den Satz „Fehler null“ neu erzeugen; den Satz auf „am Basispunkt 2,3 m³/s null; am Auslegungspunkt 4,7 m³/s durch den neuen Test abgesichert“ präzisieren.

### M2 — `boil_guard` trägt 60,0 Mio. € Backup für 1,07 MW

**Befund.** `data/parameters.yml:111` setzt `backup_power_eur: 60.000.000`; `model/core.py:125` skaliert diesen Posten nur mit `fraction ** backup_scale_exponent`, nicht mit der elektrischen Leistung. `results.boil_guard.electricity_mw = 1,0655 MW` gegenüber `results.design.electricity_mw = 182,6512 MW`. Trotzdem enthält `boil_guard.final_capex_eur = 203.596.715,66 €` den Backup-Posten mit 60.019.570,57 €, also 29,5 % der Investition. Bei 1,07 MW wäre ein Backup-Posten von rund 0,35 Mio. € (lineare Skalierung auf 182,7 MW) plausibel; die Differenz beträgt rund 59,7 Mio. €.

**Wirkung.** Der Bericht nennt für den 48,5-MW-Siedeschutz 203,6 Mio. € Investition und 0,289 Mrd. € Barwert (`report/main.tex:196`; `docs/alternativenvergleich.md:51`; Q&A 25). Die qualitative Aussage „der reine Siedeschutz ist viel billiger als die 9-°C-Lösung“ bleibt richtig, aber die Zahl ist um rund 29 % überhöht und für eine Jury angreifbar.

**Konkrete Korrektur.** Den Backup-Posten mit der elektrischen Leistung skalieren (z. B. `backup_power_eur * stage.electricity_mw / design.electricity_mw`) oder für den Guard eine eigene kleine Backup-Schätzung verwenden; `boil_guard.final_capex_eur` und `npv_25y_eur` neu berechnen; Bericht, `docs/alternativenvergleich.md`, Q&A 25 und ggf. die Folien aktualisieren; einen Test ergänzen, der prüft, dass der Guard-Backup mit `boil_guard.electricity_mw` skaliert.

### M3 — Fast leere Seite 10, erzwungener Spaltenwechsel und geteilte Bibliothekseinträge

**Befund.** PDF-Seite 10 (gedruckte Seite 9): Die linke Spalte enthält 1.269 Zeichen bis y ≈ 740 pt, die rechte Spalte nur 99 Zeichen bis y ≈ 117 pt; der Rest der Seite ist leer. Ursache ist `\onecolumn` in `report/main.tex:250`, das vor Anhang A einen Seitenumbruch erzwingt, obwohl die Bibliothek bereits auf Seite 10 endet. Zusätzlich werden die Einträge [10] und [25] über den Spaltenbruch gerissen: Seite 9 endet links mit „[10] van Treeck, R.; Wolter, C. (2020):“, die rechte Spalte beginnt ohne [10] mit „Temperaturempfindlichkeiten der …“; Seite 10 endet links mit „Verordnung über Anlagen zum Umgang“, die rechte Spalte beginnt ohne [25] mit „mit wassergefährdenden Stoffen …“.

**Wirkung.** Eine fast leere Seite und zwei entwurzelte Literaturangaben sind sichtbare Layoutmängel; die Bibliothek ist nicht sauber lesbar, und die Seite ist weit von der Dichte der D4RT-Referenz entfernt.

**Konkrete Korrektur.** Den erzwungenen `\onecolumn`-Umbruch entfernen oder Anhang A/B direkt auf Seite 10 beginnen lassen; die Bibliothek mit `\balance` (das Paket `balance` ist bereits geladen) ausgleichen; jeden `\bibitem` in eine `\parbox`/`\samepage`-Umgebung setzen oder `\nopagebreak` verwenden, sodass ein Eintrag nicht über Spalten oder Seiten getrennt wird. Anhang A/B können zweispaltig bleiben; die breiten Tabellen 3/4 als `table*`. Das Seitenbudget (Haupttext ≤ 10, Literatur + Anhang ≤ 5) ist nach der Korrektur erneut zu prüfen.

### M4 — Tabelle 1 gequetscht; Satzfehler bei Dezimalkomma, Anführungszeichen und Einheiten

**Befund.**
- Tabelle 1 (`report/main.tex:54`) verwendet `p{28mm} p{16mm} p{22mm}`. In der gerenderten PDF-Seite 3 bricht die 16-mm-Spalte „Wert“ u. a. „25.000 m³“ in „25.000“ / „m³“, „9 bis 100 °C“ in „9 bis 100“ / „°C“, „35 °C, 28 °C“ in „35 °C, 28“ / „°C“ und „4,0; 138 €/MWh“ in zwei Zeilen.
- Gleichung (9) auf PDF-Seite 4 zeigt „299,024 + 74, 756“: Das Dezimalkomma wird im Mathematiksatz als Satzzeichen mit Leerraum behandelt. Betroffen sind alle Makros mit Dezimalkomma in `$...$`, z. B. `\PChiller` = „74,756“ (`report/main.tex:140`).
- PDF-Seite 8 zeigt „aus `‘data/parameters.yml‘`.“ Beide Backticks werden als öffnende einfache Anführungszeichen gesetzt; der Schluss ist kein schließendes „’“. Quelle: `report/main.tex:208`.
- Einheiten werden getrennt: PDF-Seite 2 „auf 9“ / „°C“; PDF-Seite 3 „100“ / „°C“ und „28“ / „°C“. Das Wort „Megawatt“ wird in der Zusammenfassung als „Me-“ / „gawatt“ getrennt (PDF-Seite 2).
- Die Anhänge A/B sind einspaltig (`report/main.tex:250`), die Zeilen laufen über die volle 170-mm-Satzbreite; das ist für 12 pt zu lang und visually deutlich schlechter als D4RT.
- Die Bibliothek bricht lange URLs mitten im Wort, z. B. „laenderfinanzierungsprogramm“ / „.de“, „bdew“ / „-strompreisanalyse“, „a“ / „wsv/__18.html“ (PDF-Seiten 9–10).

**Wirkung.** Diese Fehler sind auf den gerenderten Seiten sichtbar und summieren sich zu einem Satzbild, das unter dem D4RT-Maßstab liegt. Sie sind einzeln leicht behebbar, aber in der Summe materiell für Kriterium 11.

**Konkrete Korrektur.**
- Tabelle 1 als `table*` über beide Spalten setzen oder die Wert-Spalte auf mindestens 24 mm verbreitern; Werte mit `siunitx` (`\SI{25.000}{\cubic\metre}`, `\SI{9}{\celsius}`) und geschützten Leerzeichen setzen.
- Dezimalkommas im Mathematiksatz als `{,}` schreiben oder `\num{74.756}` verwenden; alle Makros in Gleichungen prüfen.
- Backticks durch `\texttt{data/parameters.yml}` ersetzen.
- Zahl und Einheit mit `~` oder `siunitx` binden; „Megawatt“ mit `\mbox{}` schützen.
- Anhang A/B zweispaltig setzen und breite Tabellen als `table*`; oder eine `minipage` mit kürzerer Satzbreite verwenden.
- URLs nur an „/“, „.“ und „-“ brechen oder kurze Anzeigetexte mit vollständigem `\href` verwenden; die vollständigen URLs stehen im Quellenregister.
- Nach der Korrektur alle 12 Seiten neu rendern und die Spaltenfüllung, Tabellenumbrüche und Bibliothekseinträge sichtprüfen.

### M5 — Abbildung 3 steht unter Anhang B statt unter Anhang C

**Befund.** `report/main.tex:269-276` platziert die `fig05_unsicherheit`-Abbildung nach dem Anhang-B-Text und vor `\section*{Anhang C: Ergänzende Ergebnisse}`. Auf PDF-Seite 12 erscheint Abbildung 3 daher vor der Anhang-C-Überschrift; der Text auf PDF-Seite 7 verweist für die Kostenquantile auf „Abbildung 3“ und für die Tabellen auf „Anhang C, Tabelle 3 und Tabelle 4“. Die Abbildung gehört inhaltlich zur Unsicherheitsdiskussion, nicht zur Reproduktions-/Layoutprüfung.

**Wirkung.** Die zentrale Unsicherheitsgrafik ist im falschen Anhang; die Jury sucht sie möglicherweise in Anhang C und findet dort nur die Tabellen. Das ist ein Struktur- und Auffindbarkeitsmangel.

**Konkrete Korrektur.** Den `figure`-Block entweder in Abschnitt 4.4 (Unsicherheit) verschieben oder unmittelbar nach der Anhang-C-Überschrift platzieren; den Textverweis auf „Abbildung 3“ und „Anhang C“ konsistent halten; Seite 12 neu rendern.

### M6 — Folie 8: „1053,3“ überlappt die 500-Achsenmarke

**Befund.** Die Projektgrafik `presentation/figures/unsicherheit.png` wird in `model/run_all.py:364-374` erzeugt. Die drei Textlabels werden bei `ylim=(0, 640)` auf y = 610, 500 und 610 gesetzt; „1053,3“ liegt damit exakt auf der 500-Achsenmarke. In `review/rendered/presentation_pages/slide-08.png` überdeckt „1053,3“ die „500“-Marke; die Zahl ist teilweise unleserlich. Die Folie wird in `presentation/main.tex:153` eingebunden; das MP4-Segment 8 verwendet dieselbe Folie und erbt den Fehler.

**Wirkung.** Ein zentraler Wert der Unsicherheitsfolie ist visuell verdeckt; das ist auf einer Finalfolie ein sichtbarer Qualitätsmangel und im Video vorhanden.

**Konkrete Korrektur.** In `model/run_all.py` den oberen Rand auf z. B. `ylim=(0, 800)` setzen und die Labels bei y = 700, 740, 780 mit versetzter Ausrichtung platzieren, oder eine Legende statt Überlagerung verwenden. `presentation/figures/unsicherheit.png`, das Folien-PDF und die MP4 neu erzeugen. Zusätzlich in `scripts/verify_presentation.py` eine Bounding-Box-Überlappungsprüfung für die Folientexte ergänzen; die aktuelle Prüfung (Zeile 55) kontrolliert nur, ob Text außerhalb der Seite liegt, nicht ob er sich überdeckt.

### M7 — Latente Wärme: 2,45 MJ/kg ist der 20-°C-Wert für einen 100→32-°C-Prozess

**Befund.** `data/parameters.yml:16` setzt `latent_heat_j_kg: 2.450.000`; `model/core.py:92` nutzt diesen konstanten Wert für die Verdunstung. Bei 100 °C beträgt die Verdampfungsenthalpie von Wasser etwa 2,257 MJ/kg, bei 32 °C etwa 2,42 MJ/kg; der mittlere Wert für 100→32 °C liegt bei etwa 2,34 MJ/kg. Der verwendete Wert 2,45 MJ/kg entspricht eher 20 °C.

**Wirkung.** `results.baseline.evaporation_kg_s = 267,7 kg/s`, `evaporation_m3_year = 8,45 Mio. m³` und `evaporation_flow_fraction = 11,6 %` sind um etwa 4–5 % zu niedrig; bei 2,34 MJ/kg ergeben sich rund 8,85 Mio. m³ und 12,2 %. Die qualitative Aussage „H2 ist wasserintensiv“ bleibt richtig; die Zahlen sind aber genauer zu belegen. Der Bericht nennt 2,45 MJ/kg einen „Screeningwert“ (`data/parameters.yml:16`), legt aber die Temperaturabhängigkeit nicht offen.

**Konkrete Korrektur.** `h_fg(T)` aus IAPWS/NIST verwenden oder einen mittleren Wert von etwa 2,34 MJ/kg für 100→32 °C ansetzen; `EvapRate`, `EvapAnnual`, `EvapFraction`, H2-Wasserkosten und Tabelle 2 neu berechnen; alternativ den Wert ausdrücklich als „20-°C-Screeningwert, unterschätzt den Wasserbedarf um ca. 5 %“ kennzeichnen und eine Sensitivität ausweisen. Q&A 22 und die Folien entsprechend aktualisieren.

### M8 — Weitere, für sich kleinere Mängel

- **38,57-%-Aussage** (`report/main.tex:198`): „Eine Auslegung … überschreitet in 38,57 % der Fälle die 9-°C-Kapazität“ ist grammatisch falsch herum. Richtig: „In 38,57 % der Fälle übersteigt der erforderliche Wärmestrom die Kapazität von 1053,3 MW.“ Q&A 21 formuliert es bereits korrekt.
- **Speicherrechnung** (`report/main.tex:111-116`): „würde … nur 0,0303 MW benötigen“ ist irreführend; 0,0303 MW ist die mittlere Heizleistung des isolierten Beckenvolumens, kein Kühlbedarf. Besser: „Die mittlere Heizleistung des isolierten Beckenvolumens beträgt 0,0303 MW; sie ist eine untere Grenze, kein Auslegungswert.“ Q&A 1 sagt das bereits.
- **32,7 m³/s** (`report/main.tex:50`, Tabelle 1): Die Jährlichkeit/Statistik des LGRB-Werts wird nicht genannt; „andere Hochwasserstatistik“ ist zu vage. Die konkrete LGRB-Bezeichnung (z. B. HQ100 oder der dortige Wert) ergänzen oder ausdrücklich „Jährlichkeit im LGRB nicht spezifiziert“ schreiben.
- **`u_T` im Guard** (`report/main.tex:91,196`): Der Bericht verlangt `T + u_T < T_sat − ΔT_S`, setzt in der Guard-Rechnung aber `u_T = 0` und nur 5 K Sicherheitsabstand. Das ist eine unausgewiesene Annahme; entweder `u_T = 0` explizit nennen oder eine Sensitivität mit z. B. `u_T = 0,5 K` rechnen.
- **`presentation/rehearsal.md:25`**: „Die zusätzliche Echtzeit-Wiedergabe und ihre Messung werden nach dem Export in diesem Dokument ergänzt.“ Der Abschnitt ist bereits vorhanden (Zeile 27 ff.); der Satz ist ein stehengebliebener Futur/Stale-Hinweis. Ändern in „sind unten dokumentiert“.
- **VTT-Cuezahl**: `review/revisions.md:107` nennt 62 Cues; die aktuelle `Blautopf_Finale.vtt` enthält 63. Das ist eine historische Angabe; entweder aktualisieren oder als Runde-3-Stand kennzeichnen. Die aktuelle VTT ist technisch gültig (63 Cues, 631 Wörter, keine Überlappungen, letzter Cue 289,793 s).

## 4. Restrisiken und Dissens

1. **Archivreproduktion nicht unabhängig nachgebaut.** `review/rounds/round5/reproduction.md` ist ein Selbstbericht des implementierenden Agenten; `make model`, `make report`, `make presentation` und `make verify` habe ich unter der Read-only-Vorgabe nicht ausgeführt. Die Hash-Evidenz ist konsistent (155/155 Revisionsdateien, 42/42 Manifesteinträge, PDF/Video-Hashes), und der Freeze-Commit `e821bf6` ergänzt gegenüber dem reproduzierten Kandidaten `9d8f4df` nur Dokumentation. Die Behauptung „41 Artefakte und 33 Renderbilder byteweise identisch“ bleibt dennoch ungeprüft. Das ist der wichtigste verbleibende Prüfvorbehalt.

2. **MC-Kostenfehler nur am Design-Punkt hart belegt.** Dass `coupled_npv` am Auslegungspunkt 7,421 statt 5,449 Mrd. € liefert, ist reproduzierbar. Wie stark die berichteten Quantile 1,83/3,73/6,49 Mrd. € dadurch verschoben sind, hängt von der gewählten Skalierungsregel ab; eine indikative per-Sample-Gegenrechnung ergab p95 ≈ 5,56 Mrd. €, eine feste-p90-Interpretation ≈ 6,44 Mrd. €. Der Design-Punkt-Widerspruch bleibt in beiden Fällen; die exakte Korrektur ist nach der Regelentscheidung neu zu rechnen.

3. **Latente Wärme und Guard-Backup sind sekundäre, aber reale Modellfehler.** Sie ändern die qualitative Rangfolge (H1 vs. H2, 9 °C vs. Siedeschutz) nicht, aber die Zahlen 8,45 Mio. m³, 11,6 %, 203,6 Mio. € und 0,289 Mrd. € sind angreifbar.

4. **Video ist ein hochskalierter Slidecast.** `scripts/build_presentation.sh` rendert die Folien mit `pdftoppm -r 150` (ca. 945×531 px); `scripts/build_video.py` skaliert auf 1920×1080. Die Frames sind lesbar, aber nicht native 1080p; auf einer großen Finalleinwand ist die Schrift weicher als nötig. Eine Ausgabe mit 300 dpi oder direkt 1920×1080 wäre besser.

5. **VTT und Zeitprobe sind technisch, nicht menschlich.** Die VTT-Satzzeiten sind wortproportional, nicht forced-aligned (`presentation/timings.json`: `subtitle_alignment: word-proportional, not forced alignment`); die „Echtzeitprobe“ ist eine `ffmpeg -re`-Decodierung (`playback.json`, real 289,67 s), keine menschliche Sprechprobe. Das ist im Paket offengelegt, aber für 12b ein Restpunkt.

6. **Unabhängigkeit des Councils.** Council B ist ein separates Kimi-K3.1-Pro-Exemplar, also ein Same-Model-Kontext, keine modellübergreifende oder menschliche Prüfung (`review/model_configuration.md`). Das ist offengelegt, begrenzt aber die Aussagekraft eines „Council-Konsenses“.

7. **Dissens zur Speicher-/Vollstrom-Gegenüberstellung.** Der Faktor 29.000 ist rhetorisch wirksam, aber kein like-for-like-Vergleich: 0,0303 MW ist die mittlere Heizleistung eines isolierten Beckenvolumens, 877,8 MW ist die stationäre Kühlleistung des durchströmten Systems. Der Bericht nennt die Speicherrechnung eine „untere Grenze“ (Q&A 1), der Haupttext spricht aber vom „Fehler einer Auslegung ohne Zu- und Abfluss“. Ich würde diesen Punkt nicht allein als Durchfallgrund werten, aber eine Jury kann ihn als Strohmann angreifen.

8. **Dissens zur 2,15-GW-Lösung.** Die Anlage ist mit 8,19 ha Luftfläche, 182,7 MW Netzleistung, 2,237 Mio. Litern Diesel und 1,283 Mrd. € eine sehr große Szenariolösung; Standort, Netz, FFH und Genehmigung sind nicht nachgewiesen. Der Bericht sagt das ausdrücklich und behandelt die Anlage als bedingten Szenarioentwurf, nicht als Baufreigabe. Das ist redlich, aber die Umsetzbarkeit bleibt ein erhebliches Restrisiko.

9. **9 °C als „Normalzustand“.** Die 9 °C sind ein Szenarioanker, keine gemessene historische Zeitreihe; der Bericht legt das offen (`data/parameters.yml`, PDF S. 2). Eine Jury kann die ökologische Zielsetzung dennoch anders bewerten.

10. **Formale Restaufgaben.** Testkennung statt offizieller Team-ID, menschliche Fachprüfung, Rechtefreigabe, Finalisten-E-Mail und echte Live-Probe sind offen und im Paket klar ausgewiesen. Sie sind keine erfundene Live-Darbietung, aber sie verhindern eine tatsächliche Einreichung ohne menschliche Nacharbeit.

## 5. Zu den 10er-Werten

Es gibt **keine 10**. Die Kandidaten 3, 5, 9 und 10 wurden gezielt auf substanzielle Fehler geprüft; die Prüfung ergab den MC-Kostenwiderspruch (M1), den Guard-Backup-Kostenfehler (M2), die Layoutmängel (M3–M5) und die Folienüberlappung (M6). Damit ist die 10er-Bedingung „dokumentierter Versuch, substanzielle Fehler zu finden, und Begründung, warum keiner verbleibt“ packageweit nicht erfüllt. Die drei 9er in 3, 5 und 9 sind stark, aber keine 10, weil der dokumentierte Fehlersuchversuch des Pakets (elf Tests, `make verify`) M1 nicht fand und die Layoutmängel nicht abdeckte.

## 6. Stoppregelurteil

**Die Stoppregel ist auf dieser Revision nicht erfüllt.**

`WORKFLOW.md:11` verlangt, dass beide vorgeschriebenen Council-Mitglieder unabhängig **jedes** Bewertungskriterium und beide Bereitschaftsteile mit mindestens 9/10 bewerten und alle Befunde geschlossen sind. Auf dieser Revision liegen neun der zwölf Kriterien unter 9 (1, 2, 4, 6, 8, 10, 11, 12a, 12b); nur 3, 5 und 9 erreichen 9. Die materiellen Mängel M1–M6 sind offen; M1 und M2 sind Modellfehler, M3–M6 sind sichtbare Layout-/Finalmängel. Die vollständige Archivreproduktion ist nicht unabhängig nachgebaut, und die menschlichen Restaufgaben (offizielle Team-ID, Rechte, Live-Probe, Finalisten-E-Mail) sind offen.

Damit ist die Revision **nicht abgabebereit im Sinne der Stoppregel**. Nach einer Korrektur von M1–M6, einer erneuten Hash-/Renderprüfung und einer unabhängigen Nachprüfung des Auslegungspunkts ist eine deutlich höhere Bewertung plausibel; auf dem aktuellen Stand bleibt sie aus.