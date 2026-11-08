## Prüfumfang und Unabhängigkeit

Geprüft wurde ausschließlich die eingefrorene Revision `a8368ef77e14dcea7afb19c61b7f3b664c1344c9`. Alle **207/207** SHA-256-Hashes aus `review/rounds/round11/revision.json` stimmen; die PDF hat den dort verzeichneten Hash `38ff4f88…d09af`. Das Arbeitsverzeichnis blieb unverändert (nur die vom Prüfauftrag gelieferten, untracked Dateien `prompt.md` und `revision.json`). Ich habe keine Builds ausgeführt.

Geöffnet und geprüft: Kontaktübersicht `review/rendered/report_contact.png`, alle **14 Einzelseiten** `report_pages/page-01…14.png`, die Diagramme 1–3 und Tabellen 1–5 in den Renderbildern, die D4RT-Seiten 1, 2 und 6 sowie die Quellen zu HAW, LAWA, BDEW, LGRB und UBA. Frühere Rohberichte, Scorecards, `review/README.md` und `decisions.tsv` wurden nicht gelesen; `review/revisions.md` nur als erlaubte Befundzuordnung ohne Punktzahlen. Keine Exposition mit früheren Bewertungen.

---

## 1. Bewertungstabelle

| Kriterium | Bewertung | Kurze Begründung | Genauer Beleg |
|---|---:|---|---|
| **1. Qualität der Argumentation** | **9** | Die Argumentation trennt sauber zwischen Siedeverbot und ökologischem Normalziel, begründet die Vollstromkühlung, prüft H1–H8 und macht die Grenzen sichtbar. Die H2-/H3-Formulierungen und die 25-Jahres-Hülle sind Randschwächen, keine Bruchstellen. | PDF S. 2 (Zusammenfassung), S. 3–4 §2, S. 6–7 §3.3, S. 9–10 §4.3/4.4, S. 11 §6; `report/main.tex` Z. 40–52, 170–176, 226–230 |
| **2. Vorgehen und Methodik** | **9** | Systematisch: Prämissen und Quellen, Energie- und Kostenmodell, 10.000 Monte-Carlo-Ziehungen, deterministische Sensitivitäten, Ausfall-ODE, 23 Modelltests und Archivreproduktion. Die Fixkostenskalierung der Teilstromtabelle ist im Paper nicht ausgeschrieben, im Modell aber vorhanden. | PDF S. 3–4 §2, S. 8 §4.2, S. 10 §5; `model/core.py`; `output/model/results.json`; `review/rounds/round11/reproduction.md` |
| **3. Qualität der vorgeschlagenen Lösung** | **9** | H1 ist ein dokumentierter, modularer Vollstromentwurf mit p90-Reserve, Notstrom, Luftsenke, Standort-Screening und Messplan. Keine Baufreigabe; 8,41 ha, 234,3 MW Netzlast und 2,87 Mio. Liter Diesel bleiben offene Zulassungsbedingungen. | PDF S. 2; S. 4–6 §3; S. 9 §4.3; S. 11 §6; `results.json` `design`, `baseline` |
| **4. Mathematische und wissenschaftliche Modellierung** | **9** | Zentrale Bilanzen sind konsistent: \(Q=C\Delta T\), Kondensator-, Luftsenke- und H8-Bilanz, NPV, ODE und Monte-Carlo. NIST-Stoffwerte, 23 Tests, ODE-Fehler \(8{,}03\times10^{-10}\) K. Die H2-Sekundärkreis-Stoffwerte sind eine Näherung; die H2-Rückkühlung ist nicht ausgelegt. | Gl. (1)–(10), Tabellen 1–5; `results.json` `validation`; `model/test_model.py` |
| **5. Ableitung neuer Ansätze statt Wiederverwendung** | **9** | Eigene Herleitung aus Aufgabentext, Quellen und Rechnung; H1–H8-Screening, H8 nachträglich ergänzt; keine Übernahme früherer Lösungen; keine weltweite Neuheit behauptet. | PDF S. 3 §2.1; Anhang A S. 13; `PROVENANCE.md`; `EXCLUSION_LOG.md`; `docs/hypothesen.md` |
| **6. Wissenschaftliche Qualität** | **9** | Quellen, Einheiten, Unsicherheit, Alternativen, Falsifikation und Grenzen sind sauber; keine Feldvalidierung oder externe Prüfung behauptet. Die H2-Aussage „physikalisch gleichwertig“ ist quellseitig zu lesen; Rückkühlung und Wasserquelle bleiben offen. | PDF S. 3–11; §5 S. 10; Anhang A S. 13; `sources/registry.yml` |
| **8. Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen** | **8** | Überwiegend klar, aber drei konkrete Unschärfen: H2-Zyklen-Zuordnung, H3-„reine Pumpen-/Wasserkosten“ trotz 95 Mio. € Fixkosten und die nicht ausgeschriebene Fixkostenskalierung der Teilstromtabelle. Tabelle 1 bricht „Sommerluft/Feuchtkugel“ unschön. | PDF S. 6 §3.3 (H2), S. 7 §3.3 (H3), S. 14 Tab. 4, S. 4 Tab. 1; `main.tex` Z. 68, 150, 152, 170 |
| **9. Kritische Diskussion der Ergebnisse** | **9** | Starke Diskussion: Siedeschutz vs. 9 °C, H2-Wasser, H3-Quelle, H8-Screening, Ausfall, Volumensensitivität, Hochwasser, Standort, Genehmigung und menschliche Restaufgaben. Die Aussage „Modulausfall abgedeckt“ ist nicht transient modelliert. | PDF S. 7–10 §4; S. 11 §6; `results.json` `volume_sensitivity`, `failure_p90` |
| **10. Klare Berichtsstruktur und nachvollziehbare Argumentation** | **9** | Klare Gliederung: Zusammenfassung, Einführung, Methode, Ergebnisse, Betrieb/Diskussion, Nachweis, Schluss, Literatur, Anhänge; Querverweise stimmen. Der sichtbare Leerraum auf Anhang-A-Seite ist ein Layout-, kein Strukturproblem. | PDF S. 2–14; Abschnitte 1–6, Literatur, Anhänge A/B |
| **11. Format, Zitation, Einreichungsanforderungen und visuelle Qualität vs. D4RT** | **8** | Format und Regeln sind erfüllt: A4, 26 mm Rand, 12/14,4 pt, 10 Haupttext- plus 4 Rückseiten, anonym, Test-ID, 25 Quellen mit Abrufdatum, KI-Offenlegung. Abzug: zwei ca. 4–5 cm große Leerräume auf PDF S. 13, Tabelle-1-Zeilenumbruch und COP-4,0-Zuordnung zu [16]. D4RT ist dichter und glatter; der Bericht bleibt regelkonform. | PDF S. 1–14; `compliance/checklist.md`; `review/rendered/report_pages/page-13.png`; D4RT S. 1, 2, 6 |
| **12a. Bereitschaft für die schriftliche Runde** | **9** | Technisch abgabebereit: PDF, Quelle, Modell, Daten, Ergebnisse, Manifest, 23 Tests, 14 Renderbilder, 207/207 Hashes; `make verify` laut Revision bestanden. Die Archivreproduktion bezieht sich auf den Eltern-Commit `94736f7`, nicht auf den Freeze-Commit `a8368ef`; der Freeze ergänzt nur Dokumentation. Menschliche Restaufgaben bleiben offen. | `review/rounds/round11/revision.json`; `reproduction.md`; `output/pdf`; `review/rendered/`; `PROVENANCE.md` |

---

## 2. Materielle Mängel mit konkreten Korrekturen

1. **H2-Zyklen-Sensitivität ist nicht eindeutig zugeordnet.**  
   PDF S. 6 (gedruckte S. 5), §3.3: „Zwischen drei und fünf Zyklen liegt er bei 10,40 bis 12,48 Mio. m³.“ Tatsächlich gilt: **drei Zyklen → 12,48**, **fünf Zyklen → 10,40**. Der Satz nennt nur die Spanne und lässt die Zuordnung offen; der vorangehende Satz („Mit 3 Konzentrationszyklen … 12,48“) steht dazu in Spannung.  
   **Korrektur:** „Bei drei Zyklen beträgt der Zusatzwasserbedarf 12,48 Mio. m³, bei fünf Zyklen 10,40 Mio. m³.“  
   **Beleg:** `report/main.tex` Z. 170; `output/model/results.json` `evaporative_makeup_sensitivity`; PDF S. 6.

2. **H3 wird als „reine Pumpen- und Wasserkostenschätzung“ bezeichnet, enthält aber 95 Mio. € Fixkosten.**  
   PDF S. 7 (gedruckte S. 6), §3.3; Tabelle 2 weist für H3 **145,3 Mio. €** Investition aus. Die 95 Mio. € für Tiefbau und Steuerung sind in §3.3 (PDF S. 6) als separater All-in-Posten genannt; die H3-Summe enthält sie.  
   **Korrektur:** „H3 enthält als variable Ausrüstung nur Pumpen und keinen Notstromposten; die 95-Mio.-€-Fixkostenbasis bleibt wie bei H1.“  
   **Beleg:** `report/main.tex` Z. 150; PDF S. 6–7; `output/model/results.json` `alternatives`.

3. **Fixkostenskalierung der Teilstromtabelle ist im Paper nicht erklärt.**  
   Tabelle 4 (PDF S. 14) zeigt für 10 %, 1 % und 0,1 % Capex-Werte von 173, 21 und 3 Mio. €. Diese folgen aus `civil_scale_exponent: 0,65` und `controls_scale_exponent: 0,5` in `data/parameters.yml`; im Paper steht nur „95 Mio. € … separate All-in-Schätzposten“ (PDF S. 6). Ohne die Exponenten sind die Tabellenwerte aus dem Paper allein nicht nachvollziehbar.  
   **Korrektur:** In §3.3 oder der Tabellenunterschrift ergänzen: „Die 95 Mio. € Fixkosten skalieren mit dem betroffenen Anteil\(^{0,65}\) (Tiefbau) bzw. \(^{0,5}\) (Steuerung); die variable Ausrüstung folgt der p90-/Reserve-Regel.“  
   **Beleg:** `data/parameters.yml` `cost.civil_scale_exponent`, `cost.controls_scale_exponent`; `report/generated/flow_fractions.tex`; PDF S. 14.

4. **Anhang A enthält zwei große interne Leerräume.**  
   PDF S. 13 (gedruckte S. 12), rechte Spalte: Zwischen dem README-Absatz und der Handrechnung sowie zwischen Handrechnung und „Die Handrechnung bestätigt …“ stehen im 110-dpi-Render je ca. 170–190 px, also ca. **4–5 cm** Leerraum. Die Seite wirkt dadurch unruhig und deutlich weniger dicht als die D4RT-Seiten.  
   **Korrektur:** Die Displayformel in eine `minipage` oder `figure` ohne vertikale Streckung setzen bzw. `\raggedbottom` für Anhang A verwenden; alternativ die Gleichung in den linken Spaltenfluss integrieren und den Anhang kompakter setzen.  
   **Beleg:** `review/rendered/report_pages/page-13.png`; `report/main.tex` Z. 268–289; D4RT S. 1, 2, 6.

5. **Tabelle 1 ordnet den COP 4,0 der Quelle [16] zu.**  
   PDF S. 4 (gedruckte S. 3), Tabelle 1: „Kälte-COP, Strompreis 4,0; 138 €/MWh Szenarien [16]“. [16] ist die BDEW-Strompreisanalyse; der COP 4,0 ist eine eigene Szenarioannahme (so auch §2.2, PDF S. 3, und `data/parameters.yml`).  
   **Korrektur:** „Kälte-COP 4,0 (Szenario); Strompreis 138 €/MWh [16]“.  
   **Beleg:** `report/main.tex` Z. 68; PDF S. 3–4; `data/parameters.yml` `plant.chiller_cop`.

6. **Tabelle 1 bricht „Sommerluft, Feuchtkugel“ unschön.**  
   PDF S. 4: In der ersten Spalte steht „Sommerluft,“ mit dem Wert „35 °C, 28 °C“; in der nächsten Zeile steht „Feuchtkugel“ allein, die Wertespalte bleibt leer. Das ist lesbar, aber visuell unruhig und für die Jury unnötig irritierend.  
   **Korrektur:** Zwei getrennte Zeilen „Sommerluft 35 °C“ und „Feuchtkugel 28 °C“ oder eine gemeinsame Zeile „Luft 35 °C / Feuchtkugel 28 °C“ mit kürzerer erster Spalte.  
   **Beleg:** PDF S. 4; `report/main.tex` Z. 66.

7. **Kleinere, nicht materielle, aber sichtbare Punkte:**  
   - Tabelle 4 (PDF S. 14) hat zwei Spalten „MW“ ohne Kopfzeilenunterscheidung; die Caption erklärt „Kühlung und Elektrik“, der Leser muss die Reihenfolge erraten. Korrektur: „Kühlung MW | Elektrik MW“.  
   - Die Zusammenfassung sagt „fünf Kühlmodule“, ohne den Lastgrad zu nennen; bei 877,8 MW und 179,4 MW installiert je Modul sind es fünf Module bei ca. 98 % Last (nicht 5 × 163,1 MW). Korrektur: „fünf Module bei etwa 98 % ihrer installierten Leistung“ oder „sechs Module“.  
   - Die H2-Aussage „physikalisch gleichwertig“ ist quellseitig richtig, aber die Nassrückkühlung (Turmfläche, Plume, Wasserquelle) ist nicht ausgelegt. Korrektur: „quellseitig gleichwertig; die Rückkühlung ist ein separater, hier nicht ausgelegter Nasskühlturm.“  
   - Der Sekundärkreis „hat denselben Wärmekapazitätsstrom“ ist eine Näherung: bei 32–100 °C sinkt die Dichte von 994,985 auf 958,349 kg/m³, während \(c_p\) von 4,17975 auf 4,21567 kJ/(kg K) steigt; der Wärmekapazitätsstrom liegt bei 100 °C ca. 3–4 % unter dem bei 10 °C. Korrektur: „näherungsweise derselbe Wärmekapazitätsstrom; die Detailauslegung verwendet temperaturabhängige Stoffwerte.“  
   **Beleg:** `report/generated/flow_fractions.tex`; PDF S. 2, 6; `data/nist_saturation_32_100.tsv`.

---

## 3. Restrisiken und Dissens

Auch nach einer hohen Bewertung bleiben sichtbar:

- **Standort und Karst:** Kein konkreter Standort, keine belegten Höhlenwege, 8,41 ha Servicefläche, 234,3 MW Netzanbindung, 2,87 Mio. Liter Diesel und AwSV-Rückhaltung. Das Paper macht diese Punkte zu Zulassungsbedingungen; sie sind nicht gelöst.
- **H2:** 12,48 Mio. m³ Zusatzwasser pro Jahr, Wasserquelle, Wasserchemie, Aerosole, Plume und Turmfläche sind nicht ausgelegt. H2 ist deshalb eine **Screening-Alternative**, keine vollständige Anlage.
- **H3:** 52,3 m³/s Wasser bei 5 °C sind nicht belegt; 1,65 Mrd. m³ pro Jahr und 11,45 Mrd. € Barwert machen H3 zu keiner realistischen Lösung.
- **H8:** Der Absorptionswert 250 €/kW, COP 0,70 und 5,56 % Hilfsstrom sind Screening-Annahmen; die echte Maschine kann teurer oder anders sein. Die Aussage „in allen 10.000 Ziehungen teurer“ gilt nur für dieses Screening.
- **Dauerhaftigkeit:** Die Wirtschaftlichkeitsrechnung endet nach 25 Jahren, mit Ersatz im Jahr 15. Die Lösung ist an die 100-°C-Hülle gebunden; oberhalb 100 °C oder bei mehr als 4,7 m³/s ist ein neuer Entwurf erforderlich. Das ist im Paper und in `README.md` offenlegt, bleibt aber eine Grenze des Begriffs „dauerhaft“.
- **Lokaler Siedepunkt:** Die Schutzmarke 94,97 °C verwendet 1,01325 bar; der Blautopf liegt höher, der lokale Siedepunkt ist niedriger. Das Paper sagt, der höhenabhängige Luftdruck müsse vor Ort gemessen werden; die 5-K-Marge ist damit eine Standarddruck-Marge, keine Standortgarantie.
- **Modellnäherungen:** Konstante Stoffwerte, arithmetisches Mittel der Verdampfungsenthalpie, ideal gemischtes Becken, nicht modellierter Modulausfall, nicht ausgeschriebene Teilstrom-Fixkostenskalierung. Diese Punkte sind im Modell oder in den Grenzen genannt, aber nicht extern validiert.
- **Unabhängigkeit:** `EXCLUSION_LOG.md` dokumentiert eine T3-Thread-Listen-Exposition sowie zwei frühere Review-Expositionen; eine inhaltliche Verwendung wird verneint. Das ist nachvollziehbar dokumentiert, aber nicht vollständig unabhängig überprüfbar. Der Kimi-Zweitreviewer ist ein Same-Model-Kontext, keine externe Prüfung; das Paper sagt das ausdrücklich.
- **Reproduktion:** Die Archivreproduktion bezieht sich auf `94736f7` (Eltern-Commit); der Freeze-Commit `a8368ef` ergänzt nur Dokumentation. Die Paperartefakte sind byteweise identisch, aber eine Reproduktion des exakten Freeze-Commits in einer frischen Umgebung liegt nicht vor.
- **Quellenprüfung:** LGRB (32,7 m³/s HQ, MQ 2,33 m³/s, 165 km²), HAW (Tabelle 5.6: AKM 80–1800 €/kW; 3 kW/54 kW), LAWA (±1 K/h, S. 11), BDEW (13,8 ct/kWh für 70–150 Mio. kWh/a) und UBA (363 g/kWh) habe ich direkt gegengeprüft. Die p10/p90-Werte 0,7/4,7 m³/s aus Fan et al. (2023) konnte ich nicht separat am Primärartikel verifizieren (Springer-Zugriff blockiert); der LGRB-Mittelwert 2,33 m³/s stützt zumindest den Mittelwert 2,3 m³/s. Dieser Punkt bleibt als **unvollständig geprüft** markiert.
- **Visueller Dissens:** Die Seite 13 mit den zwei Leerräumen und der Tabelle-1-Umbruch sind keine Regelverstöße, aber sie liegen sichtbar unter der D4RT-Glätte. Ich werte das als materiellen Layoutmangel, nicht als K.-o.-Kriterium.

---

## 4. Zu jeder 10 eine erfolglose substanzielle Fehlersuche

**Es wurde keine 10 vergeben.** Daher entfällt die 10er-Dokumentation. Die 9er-Bewertungen stützen sich auf die oben dokumentierte Prüfung: Hashkontrolle, alle 14 Seiten, Kontaktübersicht, Diagramme, Tabellen, D4RT-Seiten, Quellenabgleich, Modell- und Ergebnisprüfung. Die verbleibenden Abzüge betreffen Klarheit und Layout, nicht die substanzielle Korrektheit.

---

## 5. Abschließendes Urteil zur Stoppregel

**Die Stoppregel ist auf dieser Revision aus meiner Sicht nicht erfüllt.** Kriterium 8 und Kriterium 11 liegen bei **8**, alle übrigen Kriterien bei **9**. Damit fehlt die von der Stoppregel verlangte Mindestbewertung von 9 in jeder Zeile bereits auf meiner Seite; selbst wenn der zweite Reviewer überall ≥9 vergäbe, wäre die gemeinsame Bedingung wegen meiner beiden 8er nicht erfüllt.

Das ist **kein** Urteil über einen substanziellen Korrektheits-, Unabhängigkeits-, Compliance- oder Auslieferungsfehler. Die wissenschaftliche Grundlinie ist tragfähig; die beiden Abzüge betreffen eine **konkrete, kleine Nacharbeit**:

- H2-Zyklen-Satz eindeutig zuordnen,
- H3-Fixkosten richtig beschreiben,
- Teilstrom-Fixkostenskalierung im Paper nennen,
- Anhang-A-Leerräume beseitigen,
- Tabelle-1-Zuordnung [16] und Zeilenumbruch korrigieren,
- optional Tabelle 4 und die Modulllast klarstellen.

Nach diesen Korrekturen ist in Kriterium 8 und 11 jeweils eine **9** erreichbar. Erst dann kann die Stoppregel – bei ebenfalls ≥9 beim zweiten Reviewer – erfüllt werden.
