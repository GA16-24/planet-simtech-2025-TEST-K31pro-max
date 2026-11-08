# Design-Review Runde 20 — Research Paper `TEST-K31pro-max`

## 0. Prüfungsgrundlage, Commit und Unabhängigkeit

**Repository:** `/Users/macbook_air_m1/.t3/scratch/2026-11-07-create-a-new-separate-github-162aa05c/planet-simtech-2025-TEST-K31pro-max`  
**Gefrorener Commit:** `01a7304980f0a3044f385e40463cf118f4a80dcb`  
**HEAD-Prüfung:** `git rev-parse HEAD` ergibt genau diesen Commit. `git status --porcelain` zeigt nur die beiden untracked Review-Artefakte `review/rounds/round20-design/prompt.md` und `revision.json`; keine versionierte Datei ist verändert.

**Hash-Prüfung mit `shasum -a 256`:** Alle für diese Runde freigegebenen Dateien stimmen mit `revision.json` überein. Stichproben:

| Datei | SHA-256 | Status |
|---|---|---|
| `output/pdf/TEST-K31pro-max.pdf` | `7d495aa752c00ce9ca430e1dd775fb933fe498db4a31f883594f62bea6268f25` | stimmt |
| `review/rendered/report_pages/page-13.png` | `98ea099858afb4e29d6f196174e9605613a922e16b42b72f84e16ecddd56881f` | stimmt |
| `review/rendered/report_pages/page-15.png` | `adb028c7b4662cd3741b95cb1b1398ed71d40496ad0f90bbf7ce0b8ae802f8d7` | stimmt |
| `review/rendered/d4rt_page06.png` | `8c1a39b9c810ed0a669221bcb79c83a7ebcb485ddc61352c9528098afd05896b` | stimmt |
| `report/main.tex` | `18ba3a1f6fa439ef0a9b744e53cb84733716cdaf2241dac5ae6ab8cbd8375fd3` | stimmt |
| `report/preamble.tex` | `b124c4182641acd166906da95554e5b723041029456f488bc96ec7393987fa` | stimmt |
| `compliance/regeln.md` | `20dbb5e026bf98db54ba5c29ced7a4e2e4489415efcabe4fd84fb27234cfeb76` | stimmt |
| `compliance/checklist.md` | `57476a27c323a6eb63bfa0a3da3aefcbbb7203daee0006063ddd82c958e80efd` | stimmt |
| `review/rounds/round20-design/reproduction.md` | `cd9f68e02dacd1b4d37cc2b358205e054b4d09f46dc76705de22f7acc9e5f48e` | stimmt |

Alle übrigen fünfzehn Seitenbilder, `report_contact.png` sowie `d4rt_page01.png` und `d4rt_page02.png` wurden ebenfalls geprüft; auch ihre Hashes stimmen.

**PDF-Geometrie:** `pdfinfo` meldet 15 Seiten, A4 (595,28 × 841,89 pt). `pdffonts` zeigt ausschließlich eingebettete Schriften. Die Tintenkanten liegen bei links 73,14 pt (25,8 mm), rechts 71,61 pt (25,26 mm), oben 74,57 pt (26,3 mm), unten 73,94 pt (26,1 mm). Die 25-mm-Regel ist damit auf jeder Seite erfüllt; die nominale 26-mm-Geometrie wird durch Glyphenüberstand rechts auf 25,26 mm reduziert.

**Sichtprüfung:** Ich habe die Kontaktübersicht, alle fünfzehn Einzelseiten `page-01.png` bis `page-15.png` sowie `d4rt_page01.png`, `d4rt_page02.png` und `d4rt_page06.png` geöffnet. PDF-Text und -Geometrie wurden zusätzlich für die Seiten 5, 6, 13, 14 und 15 ausgewertet.

**Unabhängigkeit:** Keine Builds ausgeführt, keine Dateien verändert, keine Kommunikation mit dem anderen Reviewer. Keine früheren Punktzahlen, Scorecards oder Rohberichte gelesen; die Dateinamen früherer Runden erscheinen lediglich in `revision.json`, ihre Inhalte blieben ungeöffnet. Die wissenschaftliche Modellprüfung ist nicht Gegenstand dieser Runde.

---

## 1. Bewertung D1–D6

| Kategorie | Punkte | Kurzbegründung | Beleg |
|---|---:|---|---|
| **D1 Typografie** | **9** | Sehr konsistente Hierarchie (22/16/14/12 pt), sauberer Mathematik- und Quellensatz, überwiegend korrekte Trennungen. Restpunkte: der 20+-zeilige URL-Block in [4], gemischte Zahlengenauigkeit, `Kuehl` statt `Kühl` in Gleichung (10). | PDF 1–11; Gleichungen (1)–(10); Literatur PDF 11–13 |
| **D2 Seiten- und Spaltennutzung** | **7** | Letzte Literaturseite ist zu ca. 57 % leer; links endet der Inhalt bei ca. 43 %, rechts bei ca. 27 % der Seitenhöhe. Zusätzlich sind [6] und [20] über Seitengrenzen getrennt. Sonst guter Satzspiegel und saubere Spalten. | PDF 13; PDF 11/12; PDF 12/13 |
| **D3 Lesbarkeit und visuelle Führung** | **8** | Tabelle 2 steht vor ihrer einzigen Textreferenz; die in der Revisionsantwort genannte Referenz auf PDF 5 existiert nicht. Die Zusammenfassung ist nur eine Spalte breit, nicht über die volle Satzbreite. Sonst klare Überschriften, gute Verweise auf Anhang B. | PDF 6 (Tabelle 2); PDF 2 (Zusammenfassung); PDF 9/10 |
| **D4 Abbildungen, Tabellen, visuelle Erklärung** | **7** | Tabelle 3 bricht Falllabels wie „Abfluss“/„0,7 m³/s“ in separate Zeilen; Abbildung 3 drängt „MW“ auf 1,3 pt an „1.053,3“ und lässt die untere H1-Linie ohne Führung; Abbildung 2 legt die Legende in den Zeilenkasten von „Betriebsjahr“. Sonst gute Captions, Achsen und Einheiten. | PDF 15 (Tabelle 3); PDF 14 (Abbildung 3); PDF 7 (Abbildung 2) |
| **D5 Formale Compliance** | **10** | A4, mindestens 25,26 mm Rand, 12 pt, 14,4 pt Zeilenabstand, anonymes Deckblatt, Pflichtaufbau, Seitenzählung, numerische Zitate, vollständige NIST-URLs und KI-Offenlegung sind erfüllt. Kein formaler Verstoß gefunden. | `pdfinfo`, `pdffonts`, PDF 1–15; `compliance/regeln.md`, `checklist.md` |
| **D6 Direkter D4RT-Vergleich** | **8** | D4RT-Seiten 1, 2 und 6 zeigen eine stärkere visuelle Hierarchie: full-width Abstract, full-width Figuren mit Subpanel-Labels, gruppierte Tabellenköpfe. Der Bericht ist nahe daran, bleibt aber bei Abbildung 3, Tabelle 3 und Abbildung 2 hinter diesem Feinschliff zurück. | D4RT Seiten 1, 2, 6 vs. PDF 5, 7, 14, 15 |

Die Noten sind ganzzahlig. Maßstab: 9 = gestalterisch und formal bereit ohne bekannten wesentlichen Mangel; 10 = zusätzlich dokumentierte, erfolglose substanzielle Fehlersuche.

---

## 2. Materielle Mängel

### M1 (D2): Letzte Literaturseite ist fast leer

**Befund/Beleg:** Auf PDF 13 (gedruckte Seite 12) endet der Inhalt links bei ca. 43 %, rechts bei ca. 27 % der Seitenhöhe; die unteren ca. 57 % der Seite bleiben leer. Links stehen [21]–[23], rechts nur [24] und [25]. Der erzwungene Spaltenumbruch nach [23] steht in `report/main.tex` Zeile 271; das anschließende `\clearpage` vor Anhang A steht in Zeile 277.

**Warum materiell:** Eine fast leere Literaturseite ist ein sichtbarer Satzspiegel- und Seitenbudgetfehler. Die Revisionsantwort beschreibt zwar korrekt „21–23 links, 24–25 rechts“, behebt aber die Unwucht nicht. [22] steht immerhin vollständig zusammen.

**Korrektur:** `\newpage` in Zeile 271 entfernen und vor `\clearpage` in Zeile 277 `\balance` setzen. Alternativ den Umbruch nach [22] legen und `\balance` verwenden. Wenn Anhang A im freien Raum beginnen darf, `\clearpage` in Zeile 277 entfernen und Anhang A nach der Literatur fließen lassen; die genaue Spaltenzuordnung am gerenderten PDF prüfen. 12 pt, 26 mm Rand und die vorhandenen Zeilenabstände bleiben unverändert; keine Schriftverkleinerung, keine Randverringerung.

### M2 (D2): Zwei LiteraturEinträge sind über Seitengrenzen getrennt

**Befund/Beleg:** Eintrag [6] endet auf PDF 11 rechts mit „Canadian Water Resources“ und setzt auf PDF 12 links mit „Journal 48, 189–205 …“ fort. Eintrag [20] endet auf PDF 12 rechts mit „Aktuelles/“ und setzt auf PDF 13 links mit „Kommunale-Waermeplanung. Abruf: 07.11.2026.“ fort. [22] ist ganz.

**Warum materiell:** Der Leser sieht am Seitenanfang ein nummernloses Fragment; die Zuordnung zum vorherigen Eintrag ist nur über den Seitenwechsel möglich. Das ist ein sichtbarer Eintragstrennungsfehler, auch wenn [22] jetzt zusammensteht.

**Korrektur:** In `report/main.tex` Zeile 241 `\interlinepenalty=10000` statt `100` setzen und vor [6] und [20] `\needspace{6\baselineskip}` einfügen (Paket `needspace`), oder nach jedem `\bibitem` ein `\nopagebreak` ergänzen. 12 pt und 26 mm bleiben; prüfen, ob die Seitenzahl steigt, und die Maßnahme mit M1 abstimmen.

### M3 (D3): Tabelle 2 steht vor ihrer ersten Textreferenz

**Befund/Beleg:** Tabelle 2 steht oben auf PDF 6 (gedruckte Seite 5). Die einzige Textreferenz „Tabelle 2 und Abbildung 2 zeigen diesen Unterschied.“ steht in der linken Spalte **unter** der Tabelle. Auf PDF 5 gibt es keine Referenz. Die Tabelle steht damit vor ihrer ersten Referenz, nicht danach.

**Warum materiell:** Der Leser begegnet der Tabelle, bevor der Text sie ankündigt. Die Caption mildert das, schließt die Reihenfolge aber nicht. Die Revisionsantwort behauptet eine Referenz auf PDF 5, die im gerenderten PDF nicht existiert.

**Korrektur:** In Abschnitt 3.3 auf PDF 5 einen Vorausverweis einfügen, z. B. „Tabelle 2 fasst die drei Varianten zusammen.“, oder den Satz aus `main.tex` Zeile 161 an das Ende des einführenden Absatzes auf PDF 5 verschieben. Der `table*`-Block bleibt oben auf PDF 6; erste Spalte 54 mm, 12 pt, booktabs, innerhalb 26 mm; keine Verkleinerung. Danach den Absatzfluss auf PDF 5/6 prüfen.

### M4 (D4): Tabelle 3 bricht Falllabels und trennt Zahl und Einheit

**Befund/Beleg:** Auf PDF 15, linke Spalte, stehen „Abfluss“ und „0,7 m³/s“ sowie „Sieden,“ und „8 Jahre“ in getrennten Zeilen. Die Zahlenzellen stehen nur auf der ersten Zeile; die zweite Zeile hat leere Zahlenzellen. Der Leser kann „0,7 m³/s“ als separaten Fall ohne Werte lesen.

**Warum materiell:** Die Tabelle ist als Sensitivitätsübersicht nur lesbar, wenn Fall und Wert eindeutig zusammenbleiben. Die aktuelle Form trennt genau diese Einheit.

**Korrektur:** In der erzeugten Tabelle (`generated/sensitivity.tex`, eingebunden über `main.tex` Zeile 314) Gruppenzeilen „Abfluss“ und „Sieden“ (fett, ohne Zahlen) einfügen und darunter die Wertzeilen „0,7 m³/s“, „4,7 m³/s“, „8 Jahre“, „12 Jahre“ setzen. Alternativ die erste Spalte verbreitern und die Zahlenzellen mit `\makecell` vertikal zentrieren. Gesamtbreite ≤ 76 mm, 12 pt, kein Überlauf; die Caption bleibt. Auf PDF 15 ist unter Tabelle 3 Platz für die zusätzlichen Zeilen; Tabelle 4 und 5 dürfen nicht verdrängt werden.

### M5 (D4): Abbildung 3 drängt Achsentitel und Referenzlabels zusammen; die H1-Linie ist ohne Führung

**Befund/Beleg:** Auf PDF 14 endet „MW“ bei 296,1 pt, „1.053,3“ beginnt bei 297,4 pt; das sind nur ca. 1,3 pt (ca. 0,46 mm) Tintenabstand. Die drei Referenzlabels stehen direkt unter der Achse; die untere gestrichelte Linie bei 4,14 Mrd. € ist von „H1 4,14“ ca. 22 mm entfernt, ohne Führungslinie. Die Caption erklärt die gestrichelte Linie nicht. Alle drei Führungslinien sind gleich gestrichelt; die Zuordnung erfolgt nur über Farbe und Reihenfolge.

**Warum materiell:** Die Kapazitätslegende überdeckt keine Daten, aber sie berührt den Achsentitel fast und die H1-Annotation ist nicht eindeutig zuzuordnen. Bei Schwarz-Weiß-Druck oder Farbfehlsichtigkeit ist die Linienzuordnung unsicher.

**Korrektur:** Die Figur mit mindestens 4 pt Abstand zwischen Achsentitel und Labelzeile neu erzeugen (Labelzeile 4–6 pt tiefer oder „MW“ höher). Führungslinien von den Labels zu den drei Linien ziehen oder eine echte Legende mit unterschiedlichen Strichmustern verwenden. Die Caption um „Gestrichelt: H1-Barwert 4,14 Mrd. €.“ ergänzen. Effektive Schriftgröße ≥ 12 pt (aktuell ca. 13,3 pt); keine Datenüberdeckung.

### M6 (D4): Abbildung 2 legt die Legende in den Zeilenkasten der Achsenbeschriftung

**Befund/Beleg:** Auf PDF 7 endet „Betriebsjahr“ bei ca. 605,1 pt (ohne Unterlänge) bzw. 609,1 pt (mit Unterlänge); „H1“ beginnt bei 606,35 pt. Der Tintenabstand beträgt nur ca. 0,65–1,3 pt. Die Legende H1/H2 sitzt damit im Zeilenkasten der x-Achsenbeschriftung. Die Legende wirkt an „Betriebsjahr“ gedrückt; die Trennung von Achsentitel und Legende ist nicht sauber. Das ist kein Datenfehler, aber ein sichtbarer Lesbarkeitsmangel.

**Korrektur:** Den unteren Rand der Figur um 6–8 pt vergrößern und die Legende unter die Achsenbeschriftung setzen; alternativ die Legende in die Achse (z. B. oben links) legen, ohne Daten zu überdecken. 12 pt beibehalten; Caption darunter prüfen.

### M7 (D6): Visueller Feinschliff bleibt hinter D4RT zurück

**Befund/Beleg:** D4RT-Seite 1 zeigt eine full-width Abstract, Seite 2 eine full-width Figure 2 mit Subpanel-Labels und erklärender Caption, Seite 6 eine full-width Figure 5 und eine breite Tabelle 4 mit gruppierten Köpfen. Der Bericht hat dieselbe zweispaltige Ordnung, Times-Hierarchie, numerische Verweise und erklärende Captions, bleibt aber bei Abbildung 3, Tabelle 3 und Abbildung 2 unter diesem Niveau. Die D6-Note 8 ist die Summe dieser Punkte, keine neue Einzelursache.

**Korrektur:** M4–M6 beheben; in Abbildung 1 (PDF 5) die Panels mit (a)/(b) kennzeichnen und die Legende nur unter das rechte Panel setzen. Danach die drei D4RT-Seiten erneut vergleichen. A4, 12 pt und 26 mm bleiben; D4RTs US Letter, kleinere Schrift und engere Ränder werden nicht übernommen. Wenn die Figuren sauber sind, ist D6 9.

---

## 3. Optionale Verbesserungen

1. **Zusammenfassung über die volle Satzbreite (PDF 2):** Derzeit steht sie vollständig in der linken Spalte und ist damit „einsäulig“, nicht über die volle Satzbreite. Das ist zulässig und lesbar; eine full-width Zusammenfassung würde die Hierarchie stärken, muss aber im 15-Seiten-Budget bleiben.
2. **Installationsschema (PDF 14/15):** Es fehlt weiterhin, ist aber nicht erforderlich und senkt die Bewertung nicht. Falls es die visuelle Führung im Sinne des D4RT-Vergleichs verbessern soll, bietet der freie untere Bereich von PDF-Seite 15 Platz. Es müsste aus Abschnitt 2 oder Abschnitt 4.3 referenziert werden, mindestens 12 pt Beschriftung erhalten und ohne zusätzliche Seite auskommen.
3. **Tabelle 1, erste Spalte (PDF 3):** „Trocken- und feuchte Annäherung“ bricht mit einzelnem „Annäherung“ in die zweite Zeile. Kürzen auf „Trocken-/Feuchtannäherung“ oder die erste Spalte leicht verbreitern; 12 pt.
4. **Tabelle 5, erste Spalte (PDF 15):** Mehrere Labels sind zweizeilig, die Zahlenzellen stehen auf der ersten Zeile. Lesbar, aber mit `\makecell` oder einer breiteren ersten Spalte ruhiger.
5. **Abbildung 1 (PDF 5):** Die Legende steht unter beiden Panels und nennt Strömungsanteile, während die linke blaue Kurve die Temperatur ist. Panelkennzeichnungen (a)/(b) und eine Legende nur unter dem rechten Panel würden die Zuordnung schärfen.
6. **Abbildung 2 (PDF 7):** Der Knick bei Betriebsjahr 15 (Ersatzinvestition) ist in der Caption nicht erklärt; ein kurzer Satz würde die Kurve besser lesbar machen.
7. **Symlog-Achse (PDF 5):** Die Caption nennt „Symlog-Skala und linearem Bereich bis 1 MW“; optional ergänzen, dass oberhalb von 1 MW logarithmisch aufgetragen wird.
8. **Zahlengenauigkeit (PDF 2, 5, 6):** „1.595 Mio. €“ im Text vs. „1.595,1“ in Tabelle 2; „4,136 Mrd. €“ vs. „4,38 Mrd. €“ im selben Absatz. Eine einheitliche Rundungsregel oder ein Hinweis „gerundet“ wäre konsistenter.
9. **`Kuehl` vs. `Kühl` (PDF 8, Gleichung 10):** Der Index `Q_{\mathrm{Kuehl,MW}}` verwendet ASCII, während der Text „Kühlung“ schreibt. Einheitlich `Kühl` oder eine bewusste ASCII-Variable kennzeichnen.
10. **KI-Offenlegung (PDF 14):** Anhang A nennt Systeme, Rollen und „gesamten Bericht“; eine kleine Tabelle „System | Abschnitte | Art | Umfang“ würde die geforderte Dokumentation noch expliziter machen. Die bestehende Angabe ist ausreichend.
11. **„Die Vergleichsseiten 1, 2 und 6 liegen bei“ (PDF 14):** Die D4RT-Seiten sind Prüfmaterial, nicht Teil der PDF. Auf „liegen im Prüfpaket bei“ umformulieren oder den Satz streichen.
12. **Seite 15 (PDF 15):** Der Inhalt endet bei ca. 62 % der Seitenhöhe; die unteren ca. 38 % sind leer. Für eine letzte Anhangseite hinnehmbar; eine 14-Seiten-Variante wäre nur mit gestrafftem Anhang B sinnvoll, ist aber nicht erforderlich.

---

## 4. 10er-Prüfung

**D5 (10):** Ich habe die harten Formalien einzeln geprüft: A4 (595,28 × 841,89 pt), Ränder (min. 25,26 mm rechts, 25,8 mm links, 26,3 mm oben, 26,1 mm unten), 12 pt (Text-Bounding-Box 11,96 pt; Tabellen 12 pt; Figurentexte ca. 12,7–13,3 pt), Zeilenabstand 14,4 pt, Anonymität (kein Autor in den Metadaten, kein Name/Schule im Text), Deckblatt (PlaNeT SimTech, TEST-K31pro-max, 07.11.2026, Aufgabenstellung), Pflichtaufbau, Seitenbudget (15 PDF-Seiten; 10 Haupttextseiten; 5 Literatur-/Anhangseiten), Seitenzählung (1–14, Titel unnummeriert), numerische Zitate [1]–[25] mit Abrufdatum, vollständige NIST-URLs in [4] und KI-Offenlegung in Anhang A. Die 26-mm-Angabe in Anhang A ist nominal; die gemessene Tintenkante rechts liegt bei 25,26 mm und damit über der 25-mm-Regel. Die Test-ID und die fehlende menschliche Prüfung/Einreichung sind laut Brief menschliche Restaufgaben und keine Papermängel. Kein formaler Verstoß gefunden; daher 10.

**D1 (9, 10er-Versuch):** Auch D1 wurde auf 10 geprüft. Die Hierarchie, der Mathematik- und Quellensatz und die Trennungen sind sehr konsistent; die 10er-Prüfung förderte aber drei sichtbare Restpunkte zutage: der 20+-zeilige URL-Block in [4] (PDF 11), die gemischte Zahlengenauigkeit und `Kuehl` statt `Kühl` (PDF 8). Diese Punkte sind optional, nicht materiell; sie verhindern aber, dass D1 als völlig abgeschlossen im Sinne einer 10 gilt. Daher 9.

Keine weitere Kategorie erhält 10.

---

## 5. Stoppregel-Urteil

**Die Design-Stoppregel ist aus meiner unabhängigen Sicht nicht erfüllt.**

- **D1 9, D5 10:** Der Textsatz und die formalen Compliance-Anforderungen sind bereit.
- **D2 7, D3 8, D4 7, D6 8:** Diese Kategorien liegen unter 9.
- **Offene materielle Einwände:** M1 und M2 (letzte Literaturseite, Eintragstrennungen), M3 (Tabelle 2 vor ihrer Referenz), M4–M6 (Tabelle 3, Abbildung 3, Abbildung 2) und M7 (D4RT-Feinschliff) sind nicht geschlossen.

Die Korrekturen sind layouttechnisch und benötigen keine Inhaltskürzung, keine Schriftverkleinerung und keine Randverringerung. Sie passen in das bestehende 15-Seiten-Budget; die wissenschaftliche Modellprüfung ist nicht Gegenstand dieser Runde. Eine weitere Designrunde ist erforderlich. Die zweite Reviewer-Stimme ist unabhängig und nicht in diese Bewertung eingeflossen.
