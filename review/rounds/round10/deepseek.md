## Prüfumfang und Methode

Geprüft wurde ausschließlich Commit `2c8deecf575e3c837a505be00f1e170348d28a27`. Alle 200 Hashes in `review/rounds/round10/revision.json` stimmen; die PDF hat 15 Seiten. Ich habe alle 15 Seitenbilder (`review/rendered/report_pages/page-01.png` bis `page-15.png`), die Kontaktübersicht `report_contact.png` sowie die D4RT-Referenzseiten 1, 2 und 6 geöffnet. Die zentralen Zahlen habe ich mit eigenen Rechnungen aus `data/parameters.yml` nachvollzogen; es wurden keine Builds ausgeführt und keine Dateien verändert.

Gelesen wurden nur erlaubte Dateien: `review/revisions.md`, `review/model_configuration.md`, `review/rounds/round10/revision.json` und `review/rounds/round10/reproduction.md`. `review/README.md`, `decisions.tsv` und frühere Runden habe ich nicht geöffnet; eine unerlaubte Exposition trat nicht auf.

Nicht unabhängig online nachprüfbar waren die externen Ausgangswerte [2] und [3] (LGRB-Seite HTTP 401, Springer-PDF nicht abrufbar). Sie sind unten als ungeprüft markiert. Die NIST-Sättigungstabelle liegt versioniert vor und ist in sich konsistent.

---

## 1. Bewertungstabelle

| Kriterium | Bewertung | Kurze Begründung | Genauer Beleg |
|---|---:|---|---|
| **1. Qualität der Argumentation** | **9** | Der Bericht argumentiert konsistent von der Wärmebilanz über die Alternativenprüfung und Unsicherheit bis zur begrenzten Schlussfolgerung. Die H1/H2/H8-Abwägung ist nachvollziehbar; die H8-Aussage wird ausdrücklich auf die untersuchte Temperaturführung begrenzt. | `report/main.tex` §§1–6; PDF-S. 2–10 (gedruckte S. 1–9); `docs/alternativenvergleich.md`; `report/main.tex` Z. 174 (H8-Grenze), Z. 228 (Schlussfolgerung) |
| **2. Vorgehen und Methodik** | **9** | Daten, Prämissen und technische Annahmen sind getrennt; Wärmebilanz, Kostenmodell, p90-Auslegung, Monte-Carlo, Ausfallmodell und Sensitivitäten sind nachvollziehbar. Die Tests sind ausdrücklich interne Konsistenzprüfungen, keine Feldvalidierung. | `report/main.tex` §§2–5; `data/parameters.yml`; `model/core.py`; `model/validation.py`; `model/test_model.py` (22 Tests); `output/model/results.json`; `review/rounds/round10/reproduction.md` |
| **3. Qualität der vorgeschlagenen Lösung** | **9** | Die zweistufige Vollstromkühlung mit Trockenkühlung, Kältemaschinen, zwölf Strängen, Redundanz, Stufenplan und Ausfallmodell ist als Szenarioentwurf technisch kohärent. Die Größenordnung und die offenen Standort-/Karstfragen werden nicht als Baufreigabe ausgegeben. | `report/main.tex` §§3.1–3.3; PDF-S. 4–7 (gedruckte S. 3–6); `report/generated/alternatives.tex`; `report/generated/absorption.tex`; `docs/alternativenvergleich.md` |
| **4. Mathematische und wissenschaftliche Modellierung** | **9** | Die zentralen Bilanzgleichungen (1)–(10) sind korrekt und die berichteten Werte stimmen mit unabhängigen Nachrechnungen überein (u. a. 877,781 MW; 1793,727 MW; 234,336 MW; 2028,062 MW; 56.055,8 m²; H8 135,043/94,530/229,574 MW). Die konstante Stoffwertnäherung, die COP-Szenarien und die H8-Grenzen sind benannt. | `report/main.tex` Gl. (1)–(10), §§2.2, 3.1–3.2, 4.2, 4.4; `model/core.py`; `model/validation.py`; `output/model/results.json`; eigene Nachrechnung aus `data/parameters.yml` |
| **5. Ableitung neuer Ansätze statt Wiederverwendung vorhandener Ergebnisse** | **9** | Das Repository begann leer; H1–H7 wurden vor der quantitativen Auswahl registriert, H8 nach dem Council-Hinweis transparent ergänzt. Die H1-Weiterentwicklung vom Tiefenkreislauf mit Diffusor zur Vollstromkühlung ist als technische Änderung, nicht als bloße Skalierung begründet. | `report/main.tex` §2.1, Z. 52; `docs/hypothesen.md`; `PROVENANCE.md`; `EXCLUSION_LOG.md`; `review/revisions.md` (H1-Weiterentwicklung) |
| **6. Wissenschaftliche Qualität** | **9** | Quellen, Stoffwerte, Unsicherheit, Falsifikation und Grenzen sind sauber dokumentiert; die Schlussfolgerung bleibt innerhalb der erklärten Hülle. Die externen Werte [2]/[3] konnte ich nicht online nachprüfen; der Bericht zitiert sie aber nachvollziehbar und die Abflusssensitivität deckt 0,7–4,7 m³/s ab. | `report/main.tex` §§4.3–5; `sources/registry.yml`; `data/nist_saturation_32_100.tsv`; `report/main.tex` Anhang A; PDF-S. 9–10 (gedruckte S. 8–9) |
| **8. Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen** | **9** | Tabelle 1 trennt Messwerte, Szenarioprämissen und technische Annahmen; Methodik, Ergebnisse und Grenzen sind systematisch erklärt. Kleinere Unschärfen bleiben: die Ventilator-/Pumpenbasis und der Serviceflächenfaktor 1,5 stehen nicht in Tabelle 1; die H8-Formulierung „Damit werden 94,6 MW … benötigt“ ist als Gesamtstrom, nicht als Hilfsstrom zu lesen. | `report/main.tex` Tabelle 1, §§2.1–2.2, 3.2, 3.3; PDF-S. 4 und 6 (gedruckte S. 3 und 5); `data/parameters.yml` (`dry_auxiliary_fraction`, `pump_head_m`, `pump_efficiency`, `air.service_area_factor`) |
| **9. Kritische Diskussion der Ergebnisse** | **9** | Der Bericht diskutiert Volumensensitivität, Ausfallverhalten, H2-Wasser-/Hygieneproblem, H8-Grenzen, Standort- und Genehmigungsrisiken sowie den Hochwasserfall. Die offenen Punkte werden als Zulassungs- oder Messbedingungen formuliert, nicht als erledigt behauptet. | `report/main.tex` §§4.2–4.4, 5; PDF-S. 7–10 (gedruckte S. 6–9); `report/main.tex` Z. 190–214; `docs/alternativenvergleich.md` §§Auswahl, Standort |
| **10. Klare Berichtsstruktur und für die Jury nachvollziehbare Argumentation** | **9** | Zusammenfassung, Einführung, Methode, Ergebnisse, Diskussion, Schlussfolgerung, Literatur und Anhänge sind klar getrennt; alle Abbildungen und Tabellen sind im Text referenziert. Die Anhang-B-Floats stehen allerdings weit von ihrem Textbezug entfernt. | `report/main.tex` Struktur; PDF-S. 2–11 (gedruckte S. 1–10); Querverweise `Tabelle 1–5`, `Abbildung 1–3`; `report/main.tex` Z. 116, 150, 174, 208, 214 |
| **11. Format, Zitation und Einreichungsanforderungen, einschließlich visueller Qualität im Vergleich zur D4RT-Referenz** | **8** | Formal ist der Bericht weitgehend konform: A4, 26 mm Rand, 12 pt, 15 Seiten (10 Haupttext-/5 Literatur-/Anhangseiten), Deutsch, anonym, 25 Quellen mit Abrufdatum, KI-Offenlegung. Die Hauptseiten sind dicht und D4RT-nah; die Anhangsseiten sind es nicht: PDF-S. 15 (gedruckte S. 14) enthält nur Tabelle 5 und ist zu ca. drei Vierteln leer, PDF-S. 13 (gedruckte S. 12) ist zur Hälfte leer. Das ist ein sichtbarer, reproduzierbarer Layoutmangel gegenüber der D4RT-Dichte. Zusätzlich ist `main_bibliography_shared_page: false` in `verification_summary.json` sachlich falsch. | `review/rendered/report_pages/page-13.png`, `page-15.png`; `review/rendered/report_contact.png`; `report/main.tex` Z. 291–320 (`\balance`, `figure*`/`table*` mit `[!t]`); `output/verification_summary.json`; `scripts/verification_summary.py` Z. 34–36; D4RT-Vergleich `review/rendered/d4rt_page01.png`, `d4rt_page02.png`, `d4rt_page06.png`; `compliance/checklist.md` |
| **12a. Bereitschaft für die schriftliche Runde** | **9** | Das Testpaket ist technisch erzeugt und reproduziert: PDF, LaTeX-Quelle, Modell, 22 Tests, Manifest, 40/40 Paperartefakte byteweise identisch. Offizielle Team-ID, menschliche Fachprüfung, Rechtefreigabe und Einreichung sind offen und korrekt als menschliche Restaufgaben ausgewiesen; sie werden nicht als erledigt behauptet. Der Layoutmangel aus Kriterium 11 bleibt als formaler Mangel sichtbar, blockiert die technische Erzeugung aber nicht. | `README.md`; `PROVENANCE.md`; `review/rounds/round10/reproduction.md`; `output/verification_summary.json`; `report/main.tex` Anhang A; `compliance/checklist.md` |

**Summenbild:** Zehn Zeilen mit 9, eine Zeile (11) mit 8. Keine 10.

---

## 2. Materielle Mängel und konkrete Korrekturen

### M1 — Fast leere Anhangsseite und schwach genutzte Seite 13 (punktesenkend, Kriterium 11)

**Befund:** PDF-S. 15 (gedruckte S. 14) enthält ausschließlich Tabelle 5; darunter ist die Seite weitgehend leer. PDF-S. 13 (gedruckte S. 12) enthält den Schluss von Anhang A und die Überschrift „Anhang B“, danach sind beide Spalten über weite Strecken leer. Die Kontaktübersicht `review/rendered/report_contact.png` zeigt das deutlich. Die Hauptseiten 2–11 sind dicht; die Anhangsseiten 13–15 sind es nicht. Das widerspricht dem D4RT-Maßstab, den der Bericht in `compliance/layout_referenz.md` selbst beansprucht, und der früheren Revision, die eine „fast leere Anhangsseite“ bereits als Befund hatte.

**Beleg:** `review/rendered/report_pages/page-13.png`, `page-15.png`; `review/rendered/report_contact.png`; `report/main.tex` Z. 291–320 (insbesondere `\balance` vor `\section*{Anhang B}`, `figure*`/`table*` mit `[!t]`); `review/revisions.md` (Befunde „fast leere Seite“ und „Anhang A/B nutzt die freie zweite Spalte“).

**Korrektur:**
1. `\balance` vor `\section*{Anhang B}` entfernen oder erst nach dem Anhang setzen.
2. Vor Anhang B `\clearpage` verwenden und die Anhang-B-Floats als einspaltige `figure`/`table` in die freie Spalte setzen; alternativ Tabelle 5 auf PDF-S. 14 verschieben oder in Abschnitt 3.3 integrieren.
3. In `scripts/verify_report.py` eine echte Seitenfüllprüfung ergänzen (z. B. mindestens 40 % der Textfläche oder eine Mindestzahl Textzeilen pro Spalte), damit eine Seite mit nur einer Tabelle nicht wieder als „bestanden“ durchgeht.
4. Alle 15 Seiten neu rendern und die Kontaktübersicht erneut prüfen.

### M2 — `main_bibliography_shared_page: false` ist sachlich falsch (Buchhaltung/Compliance, nicht punktesenkend)

**Befund:** PDF-S. 11 (gedruckte S. 10) enthält den letzten Absatz der Schlussfolgerung („Mit mehr Bearbeitungszeit …“) und unmittelbar danach die Überschrift „Literaturverzeichnis“. Die Literatur beginnt also auf derselben Seite wie das Ende des Haupttexts. `output/verification_summary.json` behauptet `"main_bibliography_shared_page": false`. Ursache: `scripts/verification_summary.py` prüft nur, ob das Wort „Schlussfolgerung“ auf der Literaturseite steht; die Überschrift steht aber auf der vorherigen Seite, der Schlussabsatz auf der Literaturseite. Zusätzlich zählt `main_pages: 10` das Deckblatt mit; die gedruckte Haupttextzählung ist davon zu unterscheiden.

**Beleg:** `output/verification_summary.json`; `scripts/verification_summary.py` Z. 34–36; PDF-S. 11 (gedruckte S. 10); `pypdf`-Text von PDF-S. 11 enthält „Literaturverzeichnis“, aber nicht „Schlussfolgerung“; `scripts/verify_report.py` Z. 65–72.

**Korrektur:** In `verification_summary.py` den Text **vor** dem `Literaturverzeichnis`-Heading auf Haupttextinhalt prüfen (z. B. den letzten Absatz „Mit mehr Bearbeitungszeit“ oder die letzte Haupttext-Sektion) und `main_bibliography_shared_page: true` setzen. Die gemeinsame Seite in beiden Budgets ausweisen; das Deckblatt bei `main_pages` abziehen oder die gedruckte Seitenzahl verwenden. `verify_report.py` entsprechend nachziehen. Der Seitenrahmen (10 Haupttext + 5 Literatur/Anhang) bleibt auch mit der gemeinsamen Seite eingehalten.

### M3 — H2-Abschlämmung und Spülwasser nur als Grenze, nicht quantifiziert (Grenze, nicht punktesenkend)

**Befund:** Der Bericht sagt korrekt: „Abschlämmung und Spülwasser sind nicht enthalten, deshalb ist dies kein vollständiger Zusatzwasserbedarf“ (PDF-S. 6, gedruckte S. 5; Tabellenunterschrift Tabelle 2). Die H2-Wasserkosten enthalten aber nur die Verdunstung (8,32 Mio. m³/a), nicht die Abschlämmung. Die H2-Aussage „H2 bleibt billiger“ ist damit auf eine unvollständige Wasserbilanz gestützt. Die Offenlegung ist vorhanden; die Quantifizierung fehlt.

**Beleg:** `report/main.tex` Z. 170 und Tabellenunterschrift Tabelle 2; `docs/alternativenvergleich.md` §H2; `data/parameters.yml` (kein `blowdown_cycles`/`drift_fraction`); `report/generated/alternatives.tex` (8,32 Mio. m³, 141,8 Mio. €).

**Korrektur:** `blowdown_cycles` (z. B. 3, Spanne 3–5) und `drift_fraction` in `data/parameters.yml` ergänzen; `blowdown = evaporation/(cycles-1)`, `makeup = evaporation + blowdown + drift`; H2-Wasserkosten und NPV neu berechnen und die Spanne ausweisen. Bei 3 Cycles steigen die H2-Wasserkosten um ca. 2 Mio. €/a; die Rangfolge H2 < H1 dürfte erhalten bleiben, ist aber zu belegen. Die bestehende Offenlegung bleibt zusätzlich stehen.

### M4 — Ventilator-, Pumpen- und Serviceflächenbasis nicht als Annahme gekennzeichnet (Dokumentation, nicht punktesenkend)

**Befund:** §3.2 nennt „1,5 % der Summe aus Trockenkühlung und Kondensatorwärme“ und „12 m Förderhöhe und 80 % Wirkungsgrad“; der Serviceflächenfaktor 1,5 für die 8,41 ha steht nur in `data/parameters.yml`. Tabelle 1 führt diese Werte nicht als technische Annahmen. Die Werte sind plausibel, aber ihre Herkunft/Unsicherheit ist nicht sichtbar; der Ventilatoranteil ist mit 14,3 MW rund 16 % der elektrischen Leistung.

**Beleg:** `report/main.tex` Z. 144 und Tabelle 1; `data/parameters.yml` (`dry_auxiliary_fraction: 0.015`, `pump_head_m: 12`, `pump_efficiency: 0.8`, `air.service_area_factor: 1.5`); PDF-S. 5 (gedruckte S. 4).

**Korrektur:** In Tabelle 1 oder einem Satz in §3.2 ergänzen: „Ventilatoranteil 1,5 %, Pumpenförderhöhe 12 m bei 80 %, Serviceflächenfaktor 1,5 sind eigene technische Annahmen; Herstellerkurven fehlen.“ Eine einfache Sensitivität (z. B. Ventilatoranteil 1,0/2,0 %) würde die Robustheit der Kostenaussage zeigen.

### M5 — H8-„reversible Obergrenze“ ohne Nennung der festen Generatorwärme (Klarheit, nicht punktesenkend)

**Befund:** Der Satz „Die reversible Obergrenze … beträgt … 1,79; selbst sie lässt den Quellstrom nur auf 60,9 °C sinken“ ist rechnerisch korrekt, gilt aber nur bei der dokumentierten Generatorwärme von 135 MW und 96/82 °C Heißwasser. Ohne diese Bedingung liest er sich wie eine allgemeine thermodynamische Schranke für jede wärmegetriebene Maschine. Die anschließende Einschränkung („Andere Maschinen und Temperaturführungen …“) relativiert das bereits, aber die Bedingung sollte direkt am Satz stehen.

**Beleg:** `report/main.tex` Z. 174; `model/validation.py` Z. 173–178 (`absorption.generator_mw` fest); `output/model/results.json` (`reversible_cop: 1.793`, `reversible_source_after_evaporator_c: 60.895`); `report/main.tex` Z. 174 letzter Satz.

**Korrektur:** Ergänzen: „bei der dokumentierten Generatorwärme von 135 MW und 96/82 °C Heißwasser“. Keine Zahlenänderung; die bestehende Grenze „andere Maschinen/Temperaturführungen nicht allgemein ausgeschlossen“ bleibt.

### M6 — Verifikationsbefehl in `revision.json` umfasst historische Präsentationsprüfungen (Prozessdokumentation, nicht punktesenkend)

**Befund:** `review/rounds/round10/revision.json` nennt `verification_command: make verify` und `verification_result: passed`. `README.md` Z. 45 sagt dagegen, `make verify` beziehe sich auf den historischen Gesamtbestand und sei für das aktuelle Produkt nicht erforderlich. Die Präsentationsdateien sind laut Nutzerauftrag nicht Lieferumfang. Der `reproduction.md` trennt das zwar ausdrücklich, der Freeze-Record tut es nicht.

**Beleg:** `review/rounds/round10/revision.json`; `README.md` Z. 45; `review/rounds/round10/reproduction.md`; `output/verification_summary.json` (enthält `presentation` und `playback`).

**Korrektur:** Für die gefrorene Paper-Revision den Paper-Chain `make model test report && make review-package` als `verification_command` verwenden oder im Record ausdrücklich vermerken, dass `make verify` die historischen Präsentationsprüfungen einschließt und die Paper-Prüfungen eine Teilmenge sind. Die Paper-Artefakte sind nach `reproduction.md` 40/40 byteweise identisch; das bleibt der maßgebliche Nachweis.

---

## 3. Restrisiken und Dissens

Auch nach einer hohen Bewertung bleiben folgende Punkte sichtbar:

1. **H8 ist ein Screening, kein Absorptionskreislauf-Nachweis.** Die gewählte Temperaturführung nutzt die Absorption oberhalb 40 °C, wo Trockenkühlung ausreicht; der Quellstrom nach dem Verdampfer bleibt bei COP 1,3 bei 67,8 °C und selbst bei der reversiblen Grenze bei 60,9 °C. Ein Dissens bleibt möglich: Ein Reviewer könnte dies als Strohmann ansehen, weil eine andere Temperaturführung (z. B. eine mehrstufige Absorptions- oder Resorptionsmaschine mit anderem Heißwasserrücklauf) nicht ausgeschlossen ist. Der Bericht sagt das selbst („Das Screening schließt sie nicht allgemein aus“); die Aussage „H8 ersetzt Trockenkühlung statt Kompressionskälte“ ist auf die dokumentierte Führung begrenzt. Das ist ein Restrisiko, kein Rechenfehler.

2. **H2-Wasserbilanz ohne Abschlämmung/Spülwasser.** Die 8,32 Mio. m³/a sind nur Verdunstung. Die H2-Kosten sind deshalb eine Untergrenze; die Rangfolge H2 < H1 ist plausibel, aber nicht mit vollständiger Wasserbilanz belegt. Die Offenlegung ist vorhanden; die Quantifizierung fehlt (M3).

3. **Externe Quellenwerte [2]/[3] nicht unabhängig nachgeprüft.** Die Werte 2,3 m³/s (Mittel), 0,7/4,7 m³/s (p10/p90) und 32,7 m³/s (HQ) sind plausibel und im Quellenregister verankert; die LGRB-Seite war nicht abrufbar (HTTP 401), das Springer-PDF nicht lesbar. Eine menschliche Prüfung sollte die Originale abgleichen. Die Abflusssensitivität des Berichts deckt den Bereich 0,7–4,7 m³/s ab, sodass die zentrale Aussage nicht an der exakten Zahl hängt.

4. **H1 ist hydraulisch/standörtlich nicht nachgewiesen.** Die Vollstromfassung des Karstzuflusses vor dem Becken, die Höhlenwege, die 8,41 ha Luftkühlerfläche, die zwei 234,3-MW-Netzeinspeisungen und die 2.869 m³ Diesel sind Screening-Annahmen. Der Bericht sagt ausdrücklich „keine Baufreigabe“ und „Höhlenwege … prüfen“; das ist korrekt, bleibt aber das größte reale Umsetzungsrisiko.

5. **Siedeschutz vs. H1 ist kein kostengleicher Vergleich.** Der Siedeschutz ist auf 2,3 m³/s und 94,97 °C ausgelegt, H1 auf 4,7 m³/s und 9 °C; der Bericht sagt „Diese Auslegungsbasen sind nicht direkt gleichwertig. Eine p90-Variante des Siedeschutzes wird nicht kostengleich verglichen.“ Die Aussage „Der reine Siedeschutz wäre kleiner“ ist dennoch richtig; die Kosten 0,177 vs. 4,136 Mrd. € sind indikativ, nicht symmetrisch.

6. **Seitenzähl-/Verifikationsmetadaten.** Die gemeinsame Literaturseite ist real; `main_bibliography_shared_page: false` ist falsch (M2). Der Seitenrahmen bleibt eingehalten, aber ein formaler Reviewer könnte die Zählung anders interpretieren. Die Korrektur ist eine reine Buchhaltungsfrage.

7. **`make verify` und historische Präsentation.** Der Freeze-Record vermischt Paper- und Präsentationsprüfungen (M6). Für die Paper-Bewertung ist der `reproduction.md`-Nachweis (40/40 Paperartefakte) maßgeblich; die Präsentationsprüfungen sind nicht Teil des Lieferumfangs.

8. **D4RT-Vergleich.** Die Hauptseiten 2–11 sind dicht, typografisch konsistent und D4RT-nah; die Anhangsseiten 13–15 sind es nicht. Das ist der punktesenkende Mangel M1. D4RTs US-Letter-/10-pt-/20,7-mm-Werte werden zu Recht nicht übernommen; der Vergleich betrifft Ordnung, Dichte und Integration, nicht die Übernahme von Regelverstößen.

---

## 4. Fehlersuche für die 10er

**Keine 10 vergeben.** Eine 10 verlangt einen dokumentierten, erfolglosen Angriff auf die Substanz und die Begründung, dass kein wesentlicher Fehler verbleibt. Meine Fehlersuche war teilweise erfolgreich: Sie fand M1 (fast leere Seite 15, halbleere Seite 13) und die kleineren Punkte M2–M6. Damit ist eine 10 in Kriterium 11 und im Gesamtbild nicht vertretbar.

Was ich für die 9er geprüft habe:

- **Zentrale Zahlen unabhängig nachgerechnet:** \(Q_{10}=877{,}781145\) MW; Design \(1793{,}726688\) MW; Elektrik \(89{,}382489\)/\(234{,}335798\) MW; Luft \(967{,}163634\)/\(2028{,}062486\) MW; Face-Fläche \(56.055{,}8\) m²; H2 \(617{,}34\)/\(260{,}44\) MW und \(8{,}32\) Mio. m³/a; H8 \(135{,}043\)/\(94{,}530\)/\(229{,}574\) MW, \(1716{,}0\) Mio. €, \(4{,}346\) Mrd. €. Alle Werte stimmen mit `output/model/results.json` und den Berichtsseiten überein.
- **H8-Energie- und Temperaturbilanz:** Generator 135,0 MW, Verdampfer 94,5 MW, Abwärme 229,6 MW, Trockenkühlung 349,2 MW, Kompression 299,0 MW; Summe 877,7 MW; die 10.000 Ziehungen zeigen ein minimales H8-NPV-Delta von 87,9 Mio. €, also H8 ist in allen Ziehungen teurer. Die Aussage ist innerhalb der dokumentierten Temperaturführung korrekt.
- **H2-Pinch und Wasser:** 100→36 °C, Sekundär 32→96 °C, beide Endabstände 4 K; 617,3/260,4 MW; 263,7 kg/s; 8,32 Mio. m³/a. Die Rechnung stimmt; die Abschlämmung fehlt (M3).
- **Seitenzählung, Zitate, Anonymität:** 15 PDF-Seiten, 10 gedruckte Haupttextseiten, 5 Literatur-/Anhangseiten; 25 Quellen, alle mit Autor/Institution, Titel, URL/DOI und Abrufdatum; PDF-Text und Metadaten ohne Namen/Schulangaben; Testkennung nur als `TEST-K31pro-max`. Der Seitenzähl-Flag ist falsch (M2).
- **Renderprüfung:** Alle 15 Seiten und die Kontaktübersicht geöffnet; Figuren 1–3 und Tabellen 1–5 in den gerenderten Seiten geprüft. Die Hauptseiten sind dicht und lesbar; die Anhangsseiten sind der gefundene Mangel.
- **Externe Quellen:** [2]/[3] nicht online nachprüfbar; als ungeprüft markiert. Die NIST-Tabelle ist lokal versioniert und in sich konsistent; die Handrechnung in Anhang A bestätigt die zentrale Leistung.

Die 9er sind daher „abgabebereit ohne bekannten wesentlichen Mangel“ **innerhalb der jeweiligen Zeile**; die Gesamtabgabe ist es wegen M1 (Kriterium 11 = 8) nicht.

---

## 5. Abschließendes Urteil zur Stoppregel

**Die Stoppregel ist auf dieser Revision nicht erfüllt.**

Sie verlangt mindestens 9 in jeder Zeile von beiden Reviewern und keine ungelöste substantielle Einwendung gegen Korrektheit, wissenschaftliche Qualität, Unabhängigkeit, Compliance oder Auslieferbarkeit. Meine Bewertung enthält mit **Kriterium 11 = 8** eine Zeile unter 9. Der Grund ist kein fachlicher oder rechnerischer Fehler, sondern der sichtbare Layoutmangel im Anhang: PDF-S. 15 (gedruckte S. 14) ist fast leer, PDF-S. 13 (gedruckte S. 12) zur Hälfte leer; das widerspricht dem D4RT-Dichtemaßstab und dem eigenen früheren Befund „fast leere Anhangsseite“. Zusätzlich ist der `main_bibliography_shared_page`-Flag falsch, was die Compliance-Dokumentation angreifbar macht.

**Was die Stoppregel erreichbar macht:** M1 ist lokal und konkret behebbar (M1-Korrektur: `\balance` entfernen, `\clearpage`/einspaltige Anhang-B-Floats, Tabelle 5 auf PDF-S. 14 oder in §3.3, Seitenfüllprüfung in `verify_report.py`). Nach der Korrektur und einer erneuten Sichtprüfung aller 15 Seiten kann Kriterium 11 auf 9 steigen; die übrigen zehn Zeilen liegen bereits bei 9. Die Punkte M2–M6 sind vor einer Abgabe zu schließen, senken die übrigen Kriterien aber nicht unter 9.

**Menschliche Restaufgaben:** Offizielle Team-ID, menschliche wissenschaftliche Prüfung, Rechtefreigabe und tatsächliche Einreichung sind weiterhin offen. Der Bericht behauptet sie nicht als erledigt; sie sind korrekt in `PROVENANCE.md`, `README.md` und Anhang A offengelegt. Ihr Fehlen allein ist kein Papermangel. Der vorliegende Testcharakter (`TEST-K31pro-max`) ist sichtbar; die Endkennung muss vor einer realen Abgabe ersetzt werden.

**Gesamtbild:** Ein fachlich starkes, transparentes und reproduzierbares Paperpaket mit einer belastbaren Szenarioargumentation, sauberer H8-Ergänzung und guter Haupttypografie. Der einzige punktesenkende Mangel ist die Anhang- und Seitenzählpräsentation; er ist vor der Abgabe zu beheben. Ohne diese Korrektur ist die Stoppregel nicht erfüllt.
