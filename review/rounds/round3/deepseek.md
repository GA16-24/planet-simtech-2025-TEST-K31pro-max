# Prüfbericht Runde 3, eingefrorener Commit `77c1f972df9c67a00354e395ce31f27fd0c1b95c`

## 1. Prüfumfang, Unabhängigkeit und Grenzen

Geprüft wurden der eingefrorene Commit, alle 136 in `review/rounds/round3/revision.json` gelisteten Dateien, der tatsächlich gerenderte Bericht (13 PDF-Seiten), alle 10 Folien, die MP4-Datei mit Streams und Frames, die VTT, der Sprechtext, die Zeitprobe, die 27 Q&A, die Rechte, das Modell, die Ergebnisse, die Sensitivität, das Manifest und die Revisionszuordnung. PDF-Seiten sind inklusive Deckblatt gezählt; die gedruckte Seitenzahl ist jeweils um eins kleiner.

Read-only eingehalten: keine Datei geändert, keine Prüfdatei erzeugt, kein Build und kein `make verify` ausgeführt. Python lief mit deaktiviertem Bytecode-Schreiben. `pdftotext`, `pdfplumber`, `pdffonts`, `pdfinfo`, `ffprobe`, `ffmpeg` und `curl` wurden nur lesend beziehungsweise auf stdout verwendet. `git status` zeigt nur die beiden vorgegebenen untracked Dateien `review/rounds/round3/prompt.md` und `revision.json`; der Arbeitsbaum der versionierten Dateien ist sauber.

Die 136 Hashes in `revision.json` stimmen alle mit dem Arbeitsbaum überein; `HEAD` ist exakt `77c1f972df9c67a00354e395ce31f27fd0c1b95c`. Anders als in einer früheren Runde gibt es keine Hashabweichung durch Zeitstempel. Das ist ein belastbarer Freeze.

Zentrale positive Befunde vorab: Die Modellwerte sind unabhängig nachgerechnet und stimmen (C = 9,646 MW/K, Q10 = 877,781 MW, Design 1793,727 MW, Reserve 2152,472 MW, Luftabgabe 967,164 beziehungsweise 1976,378 MW, 1.283 Mio. €, 3,666 Mrd. €). Die MP4 ist eine echte, vollständig decodierbare Datei mit 1920 × 1080, H.264/AAC, SAR 1:1, DAR 16:9 und 290,025 s. Die eigene Echtzeitwiedergabe endete mit `real 289.47`, Exit 0. Die harten Formalien A4, 26 mm Rand, 12 pt, 7 Haupttext- und 5 Anhangseiten, 25 numerierte Quellen, Anonymität und KI-Offenlegung sind erfüllt. Die kritische Diskussion und die Q&A sind die stärksten Teile des Pakets.

Grenzen, die die Bewertung nachvollziehbar begrenzen:

- `make test`, `make report`, `make presentation` und `make verify` habe ich nicht ausgeführt. Ich habe Code, Hashes, Ergebnisse und die tatsächlichen Artefakte geprüft und zentrale Zahlen unabhängig nachgerechnet; die Testbehauptungen sind nicht von mir ausgeführt.
- Die Audiodateien habe ich nicht angehört. Ich habe Dauer, Pegel, Kanäle, Clip-Grenzen und vollständige Decodierung geprüft; die Verständlichkeit der synthetischen Stimme ist ungeprüft.
- Die VTT habe ich nicht in einem Browser getestet, aber mit `ffmpeg` gegen den WebVTT-Parser geprüft; das Ergebnis ist eindeutig.
- Die externen Quellen habe ich stichprobenartig geprüft: offizielle PlaNeT-Vorgaben, Fan et al. 2023 und BDEW 2026. Die übrigen Quellen habe ich nicht vollständig gegengelesen.
- Die D4RT-Seiten 1, 2 und 6 habe ich als Bild verglichen; nicht alle D4RT-Seiten.
- Den exakten Commit habe ich nicht neu gebaut. `review/rounds/round3/reproduction.md` ist ein Nachweis des implementierenden Agenten, keine unabhängige Prüfung; die Hashes und Zahlen sind damit konsistent, aber nicht von mir reproduziert.
- Standort, Baurecht, Wasserrecht, FFH und Genehmigungsfähigkeit habe ich nicht geprüft; es gab keinen Ortstermin und keinen Behördendialog.
- Eine menschliche Live-Probe hat nicht stattgefunden; die Echtzeitmessung ist eine synthetische Wiedergabe, keine menschliche Darbietung.

**Exposition:** Bei einer rekursiven Suche nach „Handrechnung“ wurden Teile von `review/rounds/round2/deepseek.md` und `review/rounds/round2/deepseek_result.json` in die Tool-Ausgabe gespült. Ich habe diese Dateien nicht gezielt geöffnet und keine dortigen Punktzahlen oder Bewertungen übernommen. Die hier genannten Befunde sind an der eingefrorenen Revision selbst nachgeprüft. Die Exposition wird hiermit dokumentiert.

## 2. Bewertungstabelle

| Nr. | Kriterium | Bewertung | Kurzbegründung | Belege |
|---|---|---:|---|---|
| 1 | Qualität der Argumentation | 8 | Energiebilanz, Vollstrom/Speicher, Alternativen, p90, Kosten, Standort und Falsifikation sind stringent. Die Zusammenfassung ist aber mitten im Satz abgeschnitten („mit weiteren 20“, dann neuer Absatz), und die 38,57-%-Aussage ist ohne die 1053,3-MW-Bezugsgröße nicht mit Abbildung 4 (Linie bei 877,8 MW) vereinbar. | PDF S. 2, 4–8; `report/main.tex:30,106–116,192–198`; `output/model/results.json` (`uncertainty`); `model/run_all.py:312,415`; `presentation/jury_qa.md:131–135` |
| 2 | Vorgehen und Methodik | 8 | Systematisch und reproduzierbar: versionierte Eingaben, Modell, Tests, Manifest, Sensitivität, Monte Carlo, Alternativen, Falsifikation; `make verify` ist als bestanden dokumentiert. Die Prüfkette hat aber Lücken: `verify_report.py` prüft die Zusammenfassung nur auf die Überschrift, `verify_presentation.py` die VTT nur auf Existenz. Dadurch passieren der abgeschnittene Satz und die ungültige VTT. `reproduction.md` ist Implementierer-Nachweis, keine unabhängige Prüfung. | `Makefile:15–19`; `scripts/verify_report.py:37,63`; `scripts/verify_presentation.py:25`; `review/rounds/round3/reproduction.md:3,7`; `output/model/manifest.json` |
| 3 | Qualität der vorgeschlagenen Lösung | 8 | Die zweistufige Vollstromkühlung ist physikalisch schlüssig, mit 20 % Reserve, N+1, Notstrom, Puffer, Sollwertrampe und externer Luftsenke. Sie bleibt aber ein bedingter Szenarioentwurf: 8,19 ha Luftsenke, 182,7 MW Netz, 2.237 m³ Diesel, 1.283 Mio. € und kein Standort- oder Genehmigungsnachweis. Das 9-°C-Ziel ist strenger als die Frage; der reine Siedeschutz (48,5 MW) wird nur als Alternative gezeigt. | PDF S. 4–7; `results.json` (`design`, `boil_guard`); `report/main.tex:186–190`; `docs/alternativenvergleich.md:51–63` |
| 4 | Mathematische und wissenschaftliche Modellierung | 8 | Die zentralen Werte stimmen mit meiner unabhängigen Rechnung. Die ODE-Kontrolle ist jedoch ein numerischer Solver-Test mit 40 °C, die „gekoppelte Referenzkostenrechnung“ eine Selbstkonsistenz, und die 38,57-%-Kennzahl bezieht sich auf 1053,3 MW, während Abbildung 4 die Linie bei 877,8 MW zieht. | `model/core.py:60–81`; `model/validation.py:27–111`; `results.json`; eigene Rechnung; `model/run_all.py:310–318,415`; PDF S. 4, 7, 13 |
| 5 | Ableitung neuer Ansätze statt Wiederverwendung | 9 | Leeres Repository, dokumentierte Hypothesen H1–H7, Ausschlussprotokoll, keine früheren Lösungen; H1 wird ausdrücklich vom Teilkreislauf auf den Vollstrom skaliert und als nicht weltweit neu bezeichnet. Der Same-Model-Review ist offengelegt. Keine 10, weil die Lösung technisch konventionell bleibt und die Herleitung nicht frei von den übrigen Paketmängeln ist. | `PROVENANCE.md:5–9`; `EXCLUSION_LOG.md:5–9`; `docs/hypothesen.md:11–59`; `report/main.tex:48–50,73`; `review/model_configuration.md` |
| 6 | Wissenschaftliche Qualität | 8 | Quellen, Einheiten, NIST-Werte, Fan-Abflussstatistik und BDEW-Tarif sind nachvollziehbar; Grenzen, fehlende Feldvalidierung und Kostenunsicherheit werden offen benannt. Es fehlt eine externe Validierung; „unabhängige Handrechnungen“ sind nur in einer Recherchenotiz angedeutet, nicht im Bericht belegt; die 38,57-%-Darstellung ist inkonsistent. | `sources/registry.yml`; PDF S. 3–7; `report/main.tex:206`; `research_notes/Blautopf Wärmeschutz/physical_system.md:53`; `model/validation.py`; `jury_qa.md:131–135` |
| 8 | Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen | 8 | Tabelle 1 trennt Quellen, Szenario und Annahmen; Methode, Gleichungen und Ergebnisse sind klar; die Diskussion ist strukturiert. Die Zusammenfassung ist aber abgeschnitten und mit „p90“, „Barwert“, „H1“ und „90-Prozent-Abflussquantil“ nicht fachbegriffsfrei; die 38,57-%-Aussage bleibt ohne 1053,3 MW unklar. | PDF S. 2–8; `report/main.tex:30,50–71,192–198`; `report/generated/numbers.tex`; `jury_qa.md:131–135` |
| 9 | Kritische Diskussion der Ergebnisse | 9 | Die Diskussion ist die stärkste Passage: 9-°C-Ziel gegen Siedeschutz, p90-Grenze, Hochwasser 32,7 m³/s, Standort, COP, Kosten, Ausfall, fehlende Feldvalidierung und menschliche Restaufgaben werden offen behandelt; Q13–Q27 sind adversarial und belegt. Die 38,57-%-Unschärfe ist ein Klarheitsmangel, kein verschwiegener Einwand. | PDF S. 6–8; `report/main.tex:186–206`; `jury_qa.md:83–171`; `docs/alternativenvergleich.md:59–67`; `PROVENANCE.md:41–43` |
| 10 | Klare Berichtsstruktur und nachvollziehbare Argumentation | 8 | Pflichtaufbau und Abschnittslogik stimmen; Abbildungen und Tabellen sind referenziert. Die halbleere Seite 8 (rechte Spalte leer), die abgeschnittene Zusammenfassung, die gespreizten beziehungsweise getrennten Überschriften und die weit entfernten Anhangstabellen stören die Nachvollziehbarkeit. | PDF S. 2–13; `review/rendered/report_pages/page-08.png`; `page-04.png`, `page-07.png`; `report/main.tex:214`; `pdfplumber`: max. x 300,6 pt, rechter Rand 103,9 mm |
| 11 | Format, Zitation und Einreichungsanforderungen, einschließlich D4RT | 6 | A4, 26 mm Rand, 12 pt, 7 Haupttext- und 5 Anhangseiten, 25 numerierte Quellen mit Abrufdatum, Anonymität und KI-Offenlegung sind erfüllt. Dagegen: abgeschnittene Zusammenfassung; Verstoß gegen „ohne technische Fachbegriffe“; URL-Umbruch nach „https:“; Dezimalpunkte in Abbildung 4; halbleere Seite 8; Überschriften-Trennungen; VTT ungültig; Testkennung. Der D4RT-Vergleich zeigt ähnliche Zweispaltigkeit, aber geringere Dichte und Politur. | [PlaNeT-Vorgaben Bericht](https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Vorgaben-Bericht.pdf), S. 1–2; PDF S. 2–13; `review/rendered/d4rt_page01.png`, `d4rt_page02.png`, `d4rt_page06.png`; `report/preamble.tex:19,30`; `output/presentation/Blautopf_Finale.vtt`; `compliance/checklist.md:13` |
| 12a | Bereitschaft für die schriftliche Runde | 7 | Der Bericht ist inhaltlich vollständig und formal weitgehend konform, aber wegen der abgeschnittenen Zusammenfassung, des Verstoßes gegen die Fachbegriffsregel, der Testkennung und der sichtbaren Satzfehler nicht abgabebereit. Menschliche Prüfung und offizielle Team-ID fehlen. | PDF S. 2; `report/main.tex:19,30`; `README.md:44`; `PROVENANCE.md:41–43`; offizielle Vorgaben S. 1–2 |
| 12b | Bereitschaft für die Finalrunde | 8 | 10 Folien, echte MP4 (1920 × 1080, H.264/AAC, 290,025 s, SAR 1:1, DAR 16:9, 8699 Frames), vollständige Decodierung, eigene Echtzeitmessung 289,47 s, Sprechtext, Zeitprobe, 27 Q&A und Rechte liegen vor. Die VTT ist wegen Komma-Zeitstempeln unbrauchbar; Folie 8 zeigt zur 38,57-%-Aussage ein deterministisches Sensitivitätsbild; menschliche Live-Probe und Rechtefreigabe fehlen. | `ffprobe`; `output/presentation/verification.json`; `playback.json`; `presentation/rehearsal.md:18–31`; `presentation/jury_qa.md`; `presentation/main.tex:157`; `slide-08.png`; `presentation/rights.md:26–28` |

## 3. Materielle Mängel mit konkreten Korrekturen

### M1. Die Zusammenfassung ist abgeschnitten, weil ein Prozentzeichen nicht escaped ist

**Befund:** In der PDF endet der erste Zusammenfassungsabsatz mit „wird für das historische 90-Prozent-Abflussquantil von 4,7 m³/s mit weiteren 20“, danach beginnt ohne Satzende der nächste Absatz „Im zehnten Jahr beträgt die erwartete Kühlleistung 877,8 MW“. Es fehlt der Rest: „% Kapazitätsreserve ausgelegt. Diese Trennung von Jahresbetrieb und installierter Kapazität verhindert, dass eine Mittelwertrechnung als Hochwassernachweis missverstanden wird.“

**Ursache:** `report/main.tex:30` enthält `20 %` statt `20 \%`. Das Prozentzeichen kommentiert den Rest der Zeile in LaTeX aus. Der Fehler ist mit dem Commit `ddff8c2` („Strengthen p90 design and verification package“) entstanden, also in der p90-Überarbeitung, und wurde beim Freeze nicht bemerkt.

**Beleg:** `report/main.tex:30`; `review/rendered/report_pages/page-02.png`; `pdftotext -layout output/pdf/TEST-K31pro-max.pdf` (der Text „Kapazitätsreserve“ fehlt vollständig); PDF S. 2.

**Korrektur:** `20 \%` setzen, Bericht neu bauen, PDF S. 2 visuell prüfen und in `scripts/verify_report.py` einen Test auf den vollständigen Satz „Kapazitätsreserve ausgelegt“ aufnehmen. Das ist die wichtigste Einzelkorrektur.

### M2. Die Zusammenfassung verstößt gegen die Regel „ohne technische Fachbegriffe“

**Befund:** Die offiziellen Vorgaben verlangen: „Die Zusammenfassung fasst die erarbeiteten Ergebnisse kurz und ohne technische Fachbegriffe zusammen. Sie muss so verfasst sein, dass auch eine außenstehende Person die Ergebnisse und Methoden versteht.“ Die Zusammenfassung verwendet „90-Prozent-Abflussquantil“, „p90-Fall“, „Barwert“, „H1“ und „Mittelwertrechnung“. Das ist für eine außenstehende Person nicht verständlich.

**Beleg:** [PlaNeT-Vorgaben Bericht](https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Vorgaben-Bericht.pdf), S. 1; `report/main.tex:30–36`; PDF S. 2; `compliance/checklist.md:13` prüft nur die Ein-Seiten-Grenze, nicht die Fachbegriffsregel; `scripts/verify_report.py:37,63` prüft nur die Überschrift.

**Korrektur:** Die Zusammenfassung vollständig in Alltagssprache neu schreiben, etwa: „Im angenommenen stärksten Fall müsste man 878 Megawatt Wärme abführen. Für den stärksten erwarteten Wasserfluss wird die Anlage größer ausgelegt. Sie kostet schätzungsweise 1,28 Milliarden Euro und verbraucht keinen zusätzlichen Wasserdurchfluss.“ Fachbegriffe wie „p90“, „Barwert“ und „H1“ entfernen oder im Satz erklären.

### M3. Die VTT ist ungültig: Komma statt Punkt in den Zeitstempeln

**Befund:** Die Datei `output/presentation/Blautopf_Finale.vtt` verwendet Zeitstempel der Form `00:00:00,000 --> 00:00:03,200`. WebVTT verlangt einen Punkt als Millisekundentrenner; das Komma ist das SRT-Format. `ffmpeg` parst die Datei mit 0 Cues. Ersetzt man die Kommas testweise durch Punkte, parst `ffmpeg` 62 Cues. Die Untertitel sind damit in Standardbrowsern und Playern nicht funktionsfähig.

**Ursache:** `scripts/build_video.py:38` setzt `separator = "," if vtt else "."`; die Bedingung ist invertiert. `scripts/verify_presentation.py:25` prüft die VTT nur auf Existenz, nicht auf Parsebarkeit.

**Beleg:** `output/presentation/Blautopf_Finale.vtt:3` und alle 62 Cues; `scripts/build_video.py:33–39`; `scripts/verify_presentation.py:25`; `ffmpeg -v info -i output/presentation/Blautopf_Finale.vtt -f webvtt -` liefert 0 Cues; mit Punkt-Korrektur 62 Cues.

**Korrektur:** `separator = "." if vtt else ","` setzen, VTT neu erzeugen (die MP4 selbst muss dafür nicht neu kodiert werden) und in `verify_presentation.py` einen echten VTT-Parse-Test aufnehmen, der mindestens 60 Cues und den Punkt als Trenner verlangt. Die VTT ist in `revision.json` enthalten und damit Teil des eingefrorenen Pakets.

### M4. 38,57 % Überlast ist nicht mit Abbildung 4 vereinbar

**Befund:** Der Berichtstext sagt: „Eine Auslegung nur auf den Mittelstrom überschreitet in 38,57 % der Fälle die 9-°C-Kapazität.“ Die Zahl 38,57 % gehört im Modell zur Kapazität 1053,3 MW, also Mittelstrom plus 20 % Reserve. Abbildung 4 zeichnet die rote Linie jedoch bei 877,8 MW, dem Mittelstrom ohne Reserve. Über 877,8 MW liegen in der Stichprobe 59,89 %, über 1053,3 MW 38,57 %. Die Q&A Q21 nennt immerhin die 1053,3 MW; der Haupttext und die Abbildung tun es nicht. Ein Leser kann die Zahl daher nicht mit dem Bild verbinden.

**Beleg:** `model/run_all.py:312` (`axvline(final_q)`), `model/run_all.py:415` (`q_samples > final_q * 1.2`), `output/model/results.json` (`mean_capacity_overload_fraction = 0.3857`), PDF S. 7 und S. 13, `presentation/jury_qa.md:131–135`; eigene Rechnung mit `uncertainty_samples.npz`: 59,89 % über 877,8 MW, 38,57 % über 1053,3 MW.

**Korrektur:** In Abbildung 4 beide Linien zeichnen und beschriften: „Mittelstrom 877,8 MW“ und „Mittelstrom + 20 % Reserve 1053,3 MW“. Den Text präzisieren: „Eine Auslegung auf den Mittelstrom mit 20 % Reserve (1053,3 MW) überschreitet in 38,57 % der Fälle die 9-°C-Kapazität.“ Dasselbe auf Folie 8 und in der Narration.

### M5. Seite 8 hat eine vollständig leere rechte Spalte

**Befund:** PDF S. 8 (Druck S. 7) enthält den Schluss der Arbeit nur in der linken Spalte; die rechte Spalte ist leer. Der Text endet nach etwa 30 Zeilen, obwohl die Seite 47 Zeilen pro Spalte fasst. `pdfplumber` misst max. x = 300,6 pt, während der rechte Rand bei 521,6 pt liegt; der rechte Rand ist 103,9 mm breit. Das ist eine sichtbar unfertige Seite und widerspricht dem Qualitätsanspruch „keine fast leere Seite“.

**Ursache:** `\clearpage` vor dem Literaturverzeichnis (`report/main.tex:214`) beendet die zweispaltige Seite, ohne die Spalten zu balancieren.

**Beleg:** `review/rendered/report_pages/page-08.png`; `report/main.tex:214`; `report/preamble.tex:1` (`twocolumn`); `pdfplumber`-Messung.

**Korrektur:** `\usepackage{balance}` und `\balance` vor dem `\clearpage` setzen oder die Seite mit einem kurzen Absatz „Grenzen und Ausblick“ füllen. Anschließend PDF S. 8 erneut rendern und die rechte Spalte prüfen.

### M6. URLs brechen nach „https:“

**Befund:** In der Bibliographie stehen bei [5] und [11] Zeilen wie `https:` am Zeilenende und `//iapws.org/...` beziehungsweise `//doi.org/...` in der nächsten Zeile. Das ist typografisch schlecht und macht das Kopieren der URL fehleranfällig. Die Hyperlink-Ziele können korrekt sein, der gedruckte Text ist es nicht.

**Beleg:** PDF S. 9 (Druck S. 8), Quellen [5] und [11]; `report/main.tex:226,232`; `report/preamble.tex:19` (`xurl`).

**Korrektur:** `xurl` so konfigurieren, dass nach `https:` nicht gebrochen wird, oder die Lang-URLs auf eine kurze Anzeige mit `\href` und eine Parameter-Fußnote verkürzen. Die NIST-Abfrage [4] zusätzlich auf eine kürzere URL plus erklärende Parameterzeile reduzieren.

### M7. Abbildung 4 verwendet Dezimalpunkte statt Deutschkommas

**Befund:** Die rechte Achse von Abbildung 4 zeigt `2.5`, `5.0`, `7.5`, `10.0`, `12.5`, `15.0`. Der Bericht verwendet sonst deutsche Kommas, und `review/revisions.md:45` behauptet, Diagrammlabels seien auf Deutschkomma umgestellt. Das ist im gerenderten PDF nicht der Fall.

**Beleg:** `review/rendered/report_pages/page-13.png`; `model/run_all.py:310–318`; `review/revisions.md:45`.

**Korrektur:** Für die NPV-Achse einen `FuncFormatter` verwenden, der `"."` durch `","` ersetzt, oder `axes.formatter.use_locale` mit deutscher Locale setzen; Abbildung neu erzeugen und PDF S. 13 prüfen.

### M8. Überschriften werden gespreizt und mitten im Wort getrennt

**Befund:** PDF S. 4 zeigt „3.1. Vollstrom,      Speicher      und      p90-“ mit großen Wortabständen. PDF S. 7 zeigt „4.4. Siedeschutz, Unsicherheit und Hoch-wasser“ und „5. Nachweis, Falsifikation und Mo-dellprüfung“. Die Überschriften sind im Blocksatz gesetzt und werden durch `\sloppy` auseinandergezogen beziehungsweise getrennt. Auf S. 11 erzeugt derselbe Effekt im Anhang B große Lücken um `python model/run_all.py` und `python -m unittest discover -s model`.

**Beleg:** `review/rendered/report_pages/page-04.png`, `page-07.png`, `page-11.png`; `report/preamble.tex:30` (`\sloppy`), `:36–37` (`titlesec`); `report/main.tex:258–262`.

**Korrektur:** `\titleformat{\section}{\raggedright...}` und `\titleformat{\subsection}{\raggedright...}` verwenden, `\hyphenpenalty=10000` für Überschriften setzen und den Code-Absatz in Anhang B mit `\raggedright` oder `flushleft` setzen. `\sloppy` global entfernen oder durch `\emergencystretch` ersetzen.

### M9. Folie 8 zeigt das falsche Diagramm für die 38,57-%-Aussage

**Befund:** Folie 8 trägt den Titel „Die Hülle begrenzt das Versprechen“ und sagt „Begrenzte Stichprobe ohne Überlast“. Das Bild ist aber `fig04_sensitivitaet.png`, die deterministische Sensitivität mit sechs Balken („Abfluss 0,7“, „Abfluss 4,7“, „Sieden nach 8“, „Sieden nach 12“, „Ziel 7“, „Ziel 11“). Die Narration sagt „38,57 Prozent der Ziehungen“; das Bild zeigt keine 10.000 Ziehungen, keine 38,57 % und keine 1053,3-MW-Linie. Text und Bild passen nicht zusammen.

**Beleg:** `review/rendered/presentation_pages/slide-08.png`; `presentation/main.tex:157` (`fig04_sensitivitaet.png`); `presentation/narration.json:47`; `presentation/speaker_notes.md:83`; `presentation/timings.json` (Folie 8).

**Korrektur:** Auf Folie 8 `fig05_unsicherheit.png` verwenden und die 1053,3-MW-Linie ergänzen, oder die Narration auf die deterministische Sensitivität umstellen. Die Monte-Carlo-Aussage braucht ein Monte-Carlo-Bild.

### M10. Die Testkennung ist keine offizielle Team-ID

**Befund:** Der Bericht heißt `TEST-K31pro-max.pdf`, das Deckblatt trägt „Team-ID: TEST-K31pro-max“. Die offiziellen Vorgaben verlangen den Dateinamen der Team-ID und auf dem Deckblatt die Team-ID, nicht eine Testkennung. Das Paket dokumentiert das selbst als menschliche Restaufgabe; für eine reale Einreichung ist es dennoch ein blockierender Formalpunkt.

**Beleg:** `report/main.tex:19`; `README.md:44`; `compliance/checklist.md:10`; offizielle Vorgaben S. 2 (`1234.pdf`).

**Korrektur:** Offizielle Team-ID einsetzen, Datei umbenennen und Deckblatt anpassen. Das ist eine menschliche Aufgabe, keine Modellkorrektur.

### M11. Die Prüfskripte prüfen die beiden gefundenen Fehler nicht

**Befund:** `verify_report.py` prüft nur, ob „Zusammenfassung“ auf Seite 2 steht, nicht ob der Absatz vollständig ist. `verify_presentation.py` prüft die VTT nur auf Existenz, nicht auf Parsebarkeit. Deshalb konnte `make verify` mit dem abgeschnittenen Satz und der ungültigen VTT „bestehen“.

**Beleg:** `scripts/verify_report.py:37,63`; `scripts/verify_presentation.py:25`; `Makefile:15–19`; `revision.json` (`verification_result: passed`).

**Korrektur:** Konkrete Regressionstests ergänzen: (a) der Satz „Kapazitätsreserve ausgelegt“ muss im PDF-Text stehen; (b) die VTT muss mit einem WebVTT-Parser mindestens 60 Cues liefern und Punkt-Zeitstempel haben; (c) die 1053,3-MW-Linie muss in Abbildung 4 vorhanden sein. Danach `make verify` erneut ausführen.

### M12. „Unabhängige Handrechnungen“ sind im Bericht nicht belegt

**Befund:** Der Bericht sagt: „NIST-Werte und unabhängige Handrechnungen verankern die zentrale Leistung.“ Eine Handrechnung existiert in `research_notes/Blautopf Wärmeschutz/physical_system.md:53` (9,646 MW/K, etwa 878 MW), aber der Bericht verweist nicht darauf, und die Rechnung stammt aus demselben Recherchelauf, nicht aus einer unabhängigen externen Prüfung. Die Formulierung ist stärker als die Evidenz.

**Beleg:** `report/main.tex:206`; `research_notes/Blautopf Wärmeschutz/physical_system.md:53`; `model/validation.py` (interne Identitäten); `review/revisions.md:81`.

**Korrektur:** Entweder die Handrechnung als kurze Rechnung in den Anhang aufnehmen und zitieren, oder die Formulierung auf „NIST-Werte und eine dokumentierte Handrechnung“ abschwächen. Keine externe Validierung behaupten.

## 4. Wirkung der früheren Befunde

Die früheren Befunde aus `review/revisions.md` sind überwiegend nachvollziehbar behoben. Die wichtigsten Prüfungen:

| Früherer Befund | Aktueller Befund | Status |
|---|---|---|
| 0,1 % wird als 0 % angezeigt | Tabelle 4 zeigt „0,1 %“ mit 0,9 MW, 3 Mio. €, 0,0056 Mrd. € | behoben (`report/generated/flow_fractions.tex:9`; PDF S. 12) |
| Gleichung 3 mit mehrdeutigem Dezimalkomma | `9{,}1\,t` ist im PDF als `9+9,1 t` gesetzt | behoben (`report/main.tex:89`; PDF S. 3) |
| Gleichungsnummer auf eigener Zeile | Gleichung (9) ist zweizeilig; die Nummer steht an der zweiten Zeile, nicht mehr allein | akzeptabel, keine eigene Zeile mehr (PDF S. 4) |
| Fast leere Anhangsseite 14 | Die alte Seite 14 ist weg, aber PDF S. 8 hat eine leere rechte Spalte | teilweise behoben, neuer Layoutfehler |
| Tabelle 2 vermischt Kühlleistung und Wärmeabgabe | Getrennte Zeilen „Kühlleistung (Wärmeentzug)“ und „Davon Wärmeabgabe an Luft“ | behoben (PDF S. 5) |
| Gequetschte Tabelle 4 / lange NIST-URL | Tabelle 4 ist kompakt; die NIST-URL ist weiterhin sehr lang und bricht nach „https:“ | teilweise behoben |
| Getrennte Komposita | „Sollwertrampe“, „Ventilrampe“, „Dieselvorrat“ sind korrigiert; keine Treffer mehr | behoben |
| Speicherlinie in Folie 3 abgeschnitten | Untergrenze 0,02 MW und 0,03-Tick vorhanden; Linie sichtbar | behoben (`slide-03.png`) |
| Folien 4 und 9 gespreizt/getrennt | Beide Folien sind sauber gesetzt | behoben (`slide-04.png`, `slide-09.png`) |
| COP 5 über Feldbereich | COP 4,0, Bereich 3,0 bis 6,5 | behoben (`data/parameters.yml:52`) |
| Verfügbarkeit senkt Kosten | 95 % Verfügbarkeit erhöht den Barwert auf 3,817 Mrd. € | behoben (`results.json` `availability_scenarios`) |
| Fester Posten ohne 60 % | 95 Mio. € sind als All-in-Posten erklärt; 60 % nur auf variable Ausrüstung | behoben (PDF S. 3) |
| „Unabhängige Validierung“ | „Interne Konsistenz- und Plausibilitätsprüfungen“ ist jetzt korrekt benannt; „unabhängige Handrechnungen“ bleibt eine zu starke Formulierung | teilweise behoben |
| 9 °C nicht gegen Siedeschutz abgewogen | `boil_guard`: 94,97 °C, 48,5 MW, 203,6 Mio. €, 0,289 Mrd. € | behoben (PDF S. 7) |
| Standortfeasibilität offen | Standort-Screening mit 8,19 ha, 182,7 MW, 2.237 m³; kein Standort ausgewählt | teilweise behoben, bewusst offen |
| Same-Model-Review | Als Same-Model-Kontext offengelegt | dokumentiert, nicht „gelöst“ |
| Hashweichung durch Zeitstempel | Alle 136 Hashes stimmen mit dem Arbeitsbaum und `HEAD` überein | behoben |
| Stale Revision / Hypothesenherkunft | Figur 5 ist eingebunden, H1-Skalierung erklärt, Runde-3-Commit dokumentiert | behoben |
| p90-Kapazität statt Mittelwert | 2152,5 MW installiert; 38,57 % bezieht sich aber auf 1053,3 MW, Abbildung 4 auf 877,8 MW | Kapazität behoben, Kennzahl inkonsistent |

Die früheren Befunde sind damit in der Substanz weitgehend adressiert. Die verbleibenden Probleme sind nicht einfach Wiederholungen: Die abgeschnittene Zusammenfassung und die 38,57-%-Inkonsistenz sind mit der p90-Überarbeitung neu entstanden; die VTT ist ein alter, nie geprüfter Fehler; die halbleere Seite 8 und die Überschriftenprobleme sind Layoutfolgen.

## 5. Restrisiken und Dissens

Auch nach einer hohen Einzelbewertung bleiben sichtbar:

- **Standort und Genehmigung:** 8,19 ha Luftsenke, zweimal 182,7 MW Netz, 2.237 m³ Diesel und 1.283 Mio. € in einem Naturdenkmal-/FFH-Umfeld sind nicht standortbezogen nachgewiesen. Das Paket sagt das selbst; die Lösung bleibt ein bedingter Szenarioentwurf.
- **Kosten und COP:** 500 €/kW Kältemaschine, 120 €/kW Trockenkühler, 15 €/kW Wärmetauscher, 95 Mio. € Tiefbau, 60 % Zuschlag und COP 4,0 sind Szenarioannahmen ohne Angebote oder Herstellerkurven. Die absoluten Kosten sind belastbarer als die H1/H2-Relation, aber keine Baukosten.
- **Stoffwerte:** Die Rechnung verwendet konstante NIST-Werte bei etwa 10 °C. Bei 100 °C sinkt die Dichte, sodass die 877,8 MW eher konservativ sind; der Bericht nennt die Näherung, aber die Detailauslegung braucht IAPWS.
- **Validierung:** ODE-Kontrolle und gekoppelte Kostenrechnung sind interne Konsistenzprüfungen, keine externe oder Feldvalidierung. Feldmessungen, Tracer, Pumpen- und Kühlertests fehlen.
- **p90-Begriff:** 4,7 m³/s ist das 90-Prozent-Abflussquantil, keine probabilistische p90-Last. Die installierte Kapazität ist 20 % darüber. Das ist im Bericht definiert, aber der Kurzbegriff „p90-Kapazität“ kann überinterpretiert werden.
- **9-°C-Ziel:** Das Ziel ist strenger als die Frage nach dem Siedepunkt. Der reine Siedeschutz bei 48,5 MW wird gezeigt, aber nicht für den p90-Fall durchgerechnet. Ein Jury-Mitglied kann die 877,8 MW deshalb für überdimensioniert halten.
- **Untertitel und Ton:** Die VTT ist ungültig; die synthetische Stimme habe ich nicht angehört. Die Verständlichkeit und die Satzzeitsynchronität sind ungeprüft.
- **Menschliche Restaufgaben:** Offizielle Team-ID, menschliche Fachprüfung, Medienrechte, Finalisten-E-Mail, eigene Live-Probe und Einreichung fehlen. Das Paket behauptet sie nicht; das ist korrekt, aber es bleibt eine Restaufgabe.
- **KI-Eigenleistung:** Das Paket ist vollständig KI-gestützt und ohne menschliche Prüfung. Die Offenlegung ist vorbildlich, aber die Wettbewerbsanforderung „Eigenleistung“ und die persönliche Auseinandersetzung sind damit nicht belegt.
- **Reproduktion:** `reproduction.md` belegt eine Archivkopie von `babe04c`, nicht des exakten Freeze-Commits `77c1f97`. Der Diff ist nur Dokumentation, die Artefakt-Hashes sind unverändert; ein strenger Nachweis wäre ein Build auf `77c1f97`.
- **D4RT-Vergleich:** Ich habe die Seiten 1, 2 und 6 verglichen; der Bericht ist zweispaltig und Times-basiert, aber weniger dicht und weniger poliert als D4RT. Die D4RT-Regelverstöße (US Letter, 10 pt) werden zu Recht nicht übernommen.
- **Q&A Q11:** Die Antwort führt „getrennte Leitungen“ und einen „Diffusor“ ein, die im Bericht nicht als Design dokumentiert sind. Der Messplan belegt die Sensorik, nicht die Ansaug- und Rücklaufgeometrie. Das sollte ergänzt oder abgeschwächt werden.

**Dissens, den ich ausdrücklich stehen lasse:** Ein anderer Reviewer könnte die visuellen Mängel als optionale Politur und die 38,57-%-Unschärfe als hinnehmbar werten und mehrere 9en vergeben. Ich tue das nicht, weil die Zusammenfassung einen ganzen Satz verliert, die VTT nachweislich 0 Cues parst und die offizielle Zusammenfassungsregel verletzt ist. Ein anderer Reviewer könnte Kriterium 9 auf 8 senken, weil die 38,57-%-Diskussion unscharf ist; ich halte die kritische Diskussion dennoch für 9. Ein anderer Reviewer könnte Kriterium 5 auf 8 senken, weil die Lösung technisch konventionell ist; ich halte die dokumentierte Unabhängigkeit für 9. Ein anderer Reviewer könnte 12b auf 7 senken, weil die VTT und Folie 8 fehlerhaft sind; ich halte die Kernmaterialien für 8, weil MP4, Sprechtext, Zeitprobe, Q&A und Rechte tatsächlich vorliegen.

## 6. Keine 10

Es gibt keine 10. Die beiden 9en sind die Kriterien 5 und 9; sie sind keine 10, weil die Herleitung zwar unabhängig dokumentiert ist, die Lösung aber technisch konventionell bleibt und die kritische Diskussion die 38,57-%-Kennzahl nicht sauber mit Abbildung 4 verbindet. Die Fehlersuche war nicht erfolglos: Sie hat die abgeschnittene Zusammenfassung, die ungültige VTT, die 38,57-%-Inkonsistenz, die halbleere Seite 8, die URL- und Dezimalfehler, die Überschriftenprobleme und die Folien-8-Mischung gefunden. Damit ist eine 10 auf dieser Revision nicht vertretbar.

## 7. Abschließendes Urteil zur Stoppregel

**Die Stoppregel ist auf dieser Revision nicht erfüllt.**

Meine Bewertung lautet: **8, 8, 8, 8, 9, 8, 8, 9, 8, 6, 7, 8**. Zehn der zwölf Kriterien liegen unter 9. Die Stoppregel verlangt, dass alle zwölf Einzelbewertungen bei beiden Reviewern auf demselben Commit mindestens 9 betragen und kein substanzieller Einwand gegen Richtigkeit, Machbarkeit, Wissenschaftlichkeit, Unabhängigkeit, Regelkonformität oder Auslieferbarkeit offen bleibt. Schon meine Bewertung blockiert den Konsens, unabhängig von der Bewertung des zweiten Reviewers.

Die blockierenden Punkte sind: die abgeschnittene Zusammenfassung (M1), der Verstoß gegen die Fachbegriffsregel (M2), die ungültige VTT (M3), die 38,57-%-Inkonsistenz (M4), die halbleere Seite 8 (M5), die URL- und Dezimalfehler (M6, M7), die Überschriftenprobleme (M8), die Folien-8-Mischung (M9) und die Testkennung (M10). Das Paket ist ein starker, ehrlicher Arbeitsstand mit einer überdurchschnittlichen kritischen Diskussion und guten Finalmaterialien. Für eine abgabebereite Einreichung müssen die Zusammenfassung repariert und in Alltagssprache neu geschrieben, die VTT korrigiert und geprüft, die 1053,3-MW-Linie in Text und Abbildung konsistent gemacht, Seite 8 balanciert, die Typografie bereinigt und die offizielle Team-ID eingesetzt werden. Danach sind eine erneute Renderprüfung und ein neuer Freeze nötig.