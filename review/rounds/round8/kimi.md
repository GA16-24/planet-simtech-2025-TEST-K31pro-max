# Rohbericht zu Commit `c76d40d3dabf894fb2475c714af5eed213f82c90`

## Prüfumfang und Nachweislage

Geprüft wurden die Kontaktübersicht, alle dreizehn PDF-Seiten, die D4RT-Referenzseiten 1, 2 und 6, das Modell, die Ergebnisdateien, die Quellen- und Provenienznachweise sowie die Archivreproduktion. Seitenangaben bezeichnen im Folgenden physische PDF-Seiten. Die gedruckte Seitenzahl beginnt erst auf PDF-Seite 2.

Frühere Rohreviews und Scorecards wurden nicht geöffnet. Es wurden keine früheren Punktzahlen übernommen und kein anderer Reviewer kontaktiert.

Die wichtigsten eigenen Prüfergebnisse:

- Der Arbeitsbaum entspricht dem Zielcommit. Alle 181 versionierten Dateien sind unverändert.
- Alle 37 Paperartefakte aus dem Archivnachweis stimmen mit `review/rounds/round8/revision.json` überein und sind zwischen dem reproduzierten Elterncommit `2385effc...` und dem Zielcommit unverändert.
- 25 unabhängige numerische Nachrechnungen zu Wärme, Reserve, Speicher, Hochwasser, Diesel, Hydraulik, Verdunstung, NPV und Sensitivität waren erfolgreich.
- Alle 43 Manifest-Hashes und zwölf Statistiken aus den vier NPZ-Reihen mit jeweils 10.000 Werten stimmen.
- Die PDF hat 13 A4-Seiten, davon 8 Haupttext- und 4 Literatur-/Anhangsseiten. Der kleinste gemessene Seitenrand beträgt 25,933 mm. Das Autorenmetadatum ist leer. Die Schriften sind eingebettet.
- NIST-Stoffwerte, Fan-Abflussquantile, LGRB-Hochwasserwert, BDEW-Tarife und die aktuellen offiziellen Berichtsregeln wurden direkt an den Primärquellen kontrolliert.

## Einzelbewertungen

| Kriterium | Bewertung | Begründung und genaue Belegorte |
|---|---:|---|
| 1. Qualität der Argumentation | 8 | Die Hauptargumentation folgt schlüssig aus advektiver Wärmebilanz, Vollstrombetrachtung und externer Wärmesenke. PDF-Seite 2, Zusammenfassung; PDF-Seite 3, Gleichungen 1 bis 4; PDF-Seite 4, §3.1 und §3.2. Die Behauptung, H2 sei physikalisch gleichwertig, ist dagegen ohne Nachweis des heißen Wärmeübertrager-Endes unbegründet. PDF-Seite 5, §3.3; `report/main.tex:168`. |
| 2. Vorgehen und Methodik | 8 | Sieben Ansätze, deterministiche und Monte-Carlo-Sensitivitäten, dynamische Ausfallrechnung und Volumensensitivität bilden eine breite Methodik. `docs/hypothesen.md`, H1 bis H7; `model/run_all.py:186-263`; PDF-Seiten 7 bis 9, §4.2 bis §5. Der H2-Test prüft jedoch nur 36 > 32 °C am kalten Ende und weder heiße Temperatur noch Sekundärmassenstrom. `model/test_model.py:73-77`. |
| 3. Qualität der vorgeschlagenen Lösung | 9 | H1 schließt den Wärmeentzug einschließlich Antriebsenergie, enthält modulare Reserve, Notstrom, Ausfallrechnung und ausdrückliche Verwerfungsbedingungen. Die Auslegung wird als bedingter Szenarioentwurf und nicht als Baufreigabe angeboten. PDF-Seiten 4 bis 9, §3.1 bis §6; `output/model/results.json`, `baseline`, `design`, `validation`. Die fehlenden Standort- und Herstellerdaten bleiben korrekt als Grenzen sichtbar. |
| 4. Mathematische und wissenschaftliche Modellierung | 7 | Die zentralen H1-Gleichungen und Energiebilanzen sind rechnerisch konsistent. H2 ist dagegen thermodynamisch unvollständig: Aus Quellstrom 100 → 36 °C und Sekundärkreislauf 100 → 32 °C folgt am heißen Ende des Wärmeübertragers 100 − 100 = 0 K. Ein anderer Verlauf oder ein positiver Mindestabstand wird nicht modelliert. `data/parameters.yml:49-55`; `model/core.py:66-87`; `report/main.tex:168`; `docs/alternativenvergleich.md:38`. |
| 5. Ableitung neuer Ansätze | 9 | Die Hypothesenbildung dokumentiert sieben eigenständig strukturierte Ansätze vor der quantitativen Auswahl, einschließlich der späteren Skalierung von H1 auf den Vollstrom. `docs/hypothesen.md`, besonders H1 bis H7 und „Skalierung nach der Wärmebilanz“. `PROVENANCE.md`, „Unabhängigkeit und Ausgangslage“; `EXCLUSION_LOG.md`. Es gibt keinen Beleg für die Wiederverwendung früherer Lösungen. |
| 6. Wissenschaftliche Qualität | 7 | Zentrale Messwerte und Stoffdaten sind quellenfest, und die Grenzen der internen Validierung werden benannt. Der H2-Pinchfehler und die ungenaue Kostenherkunft verhindern dennoch eine hohe wissenschaftliche Bewertung. PDF-Seite 5, §3.3; `report/main.tex:100,168`; HAW-Quelle [19], Tabelle 5.6; `sources/registry.yml:29`. |
| 8. Klare Erklärung von Annahmen, Methoden, Ergebnissen und Schlussfolgerungen | 8 | Tabelle 1 trennt Messwerte und Annahmen klar; Ergebnisse und Zielgrenzen sind verständlich dokumentiert. PDF-Seite 4, Tabelle 1; PDF-Seite 9, §6. Bei H2 fehlen jedoch vier Wärmeübertrager-Temperaturen und der Sekundärmassenstrom. Außerdem steht das 9-°C-Label in Abbildung 1 räumlich neben der oberen Temperaturkurve statt bei der 9-°C-Linie. PDF-Seite 5, Abbildung 1 und §3.3. |
| 9. Kritische Diskussion der Ergebnisse | 8 | Hochwasser, reiner Siedeschutz, Volumenversagen, Dieselverfügbarkeit, Tarif und Verteilungsgrenzen werden ausdrücklich kritisiert. PDF-Seiten 7 bis 9, §4.2 bis §5; `output/model/results.json`, `volume_sensitivity`, `uncertainty`. Die kritische Prüfung von H2 bleibt aber unvollständig, weil der heiße Pinch nicht als mögliches Falsifikationskriterium untersucht wird. |
| 10. Klare Berichtsstruktur und nachvollziehbare Argumentation | 8 | Der Haupttext folgt einer klaren Folge von Prämissen, Methode, Ergebnissen, Diskussion und Schluss. Die Anhänge sind dagegen schlecht umbrochen: Anhang A beginnt auf PDF-Seite 11 unten in der rechten Spalte, PDF-Seite 12 nutzt fast nur die linke Spalte, und PDF-Seite 13 lässt die gesamte rechte Hälfte leer. `report/main.tex:262-299`; PDF-Seiten 11 bis 13. |
| 11. Format, Zitation, Einreichungsanforderungen und D4RT-Vergleich | 8 | A4, Seitenbudget, Mindestrand, Anonymität, numerische Verweise und KI-Anhang sind erfüllt. Gegen D4RT wirken die Hauptseiten geordnet, aber die Anhangsseiten 12 und 13 sind wesentlich schwächer genutzt als die Referenzseiten 2 und 6. Hinzu kommen die fehlerhafte Platzierung des Ziel-Labels und die ungenaue Herkunft der Kostenparameter. PDF-Seiten 5 und 10 bis 13; `review/rendered/d4rt_page02.png`, `d4rt_page06.png`; `report/main.tex:100`. |
| 12a. Bereitschaft für die schriftliche Runde | 8 | Die Archivkette und die technischen Artefakte sind stark: 37 von 37 Paperartefakte sind hashidentisch. `review/rounds/round8/reproduction.md`; Freeze-Prüfung oben. Vor einer realen Abgabe bleiben jedoch der H2-Fehler, die Darstellungskorrekturen, die offizielle Team-ID und die ausdrücklich noch fehlende menschliche Fach- und KI-Ausgabenprüfung. PDF-Seite 1, Testkennung; PDF-Seite 12, Anhang A; `PROVENANCE.md:42-44`. |

## Materielle Mängel und konkrete Korrekturen

### M1. H2 hat keinen nachgewiesenen positiven Pinch am heißen Ende

**Beleg:** `report/main.tex:168`, `docs/alternativenvergleich.md:38`, `data/parameters.yml:49-55` und `model/test_model.py:73-77`.

Das Paper beschreibt einen Sekundärkreislauf von 100 auf 32 °C und einen Quellstrom von 100 auf 36 °C. Damit beträgt der dokumentierte Abstand am kalten Ende 4 K, am heißen Ende jedoch 0 K. Ein endlicher Wärmeübertrager kann mit dieser Temperaturkonstellation die behauptete Wärmeübertragung nicht nachweisen. Der vorhandene Test erkennt das nicht, weil er nur `36 > 32` prüft.

**Korrektur:**

1. Sekundärmassenstrom und alle vier Wärmeübertrager-Temperaturen explizit modellieren.
2. Heißen und kalten Pinch sowie die Energiebilanz des Sekundärkreislaufs testen.
3. Erst danach H2 als physikalisch gleichwertig bezeichnen. Andernfalls H2 als ungelöste Auslegungsoption kennzeichnen.

Ein konsistenter Ausgangspunkt wäre beispielsweise ein Sekundärstrom von 32 auf 96 °C bei gleichem Wärmekapazitätsstrom wie der Quellstrom. Dann betrügen die Abstände 100 − 96 = 4 K am heißen und 36 − 32 = 4 K am kalten Ende. Die Verdampfungsenthalpie, der Wasserbedarf, die Kosten und alle betroffenen Papierwerte wären mit diesem tatsächlichen Temperaturbereich neu zu rechnen.

### M2. Die Kostenherkunft ist ungenau dokumentiert

**Beleg:** `report/main.tex:100`, `data/parameters.yml:103-123`, HAW-Quelle [19], Tabelle 5.6.

Der Paper ordnet Kältemaschinen, Trockenkühler und Verdunstungsanlagen gemeinsam der Literaturbasis 2012 zu. Die HAW-Tabelle nennt für Kompressionskältemaschinen Werte wie 75 bis 125, 125 bis 350 und 185 bis 236 €/kW. Der Modellwert von 500 €/kW liegt darüber. Er kann eine bewusst konservative Szenarioannahme sein, ist aber kein direkter Tabellenwert. Für Trockenkühlung und Verdunstung dokumentieren die Recherchenotizen gerade keine gefundene Beschaffungsquote.

**Korrektur:** Die tatsächliche HAW-Range nennen und `500 €/kW` ausdrücklich als eigenen konservativen Szenariowert oberhalb dieser Range kennzeichnen. Trockenkühler- und Verdunstungskosten getrennt als eigene Annahmen ausweisen, statt sie derselben Literaturquelle zuzuordnen. Falls stattdessen Quellenwerte verwendet werden, Investition, Ersatz, Wartung, Barwerte, Tabellen und Abbildungen neu berechnen.

Kleiner zugehöriger Registerfehler: `sources/registry.yml:29` nennt weiterhin 3,17007 bar, während URL, Modell und Paper 3,17080686 bar verwenden. Der Registereintrag ist auf den aktuellen Wert zu korrigieren.

### M3. Die Anhangsgestaltung bleibt deutlich unter der D4RT-Referenz

**Beleg:** PDF-Seiten 11 bis 13; `report/main.tex:262-299`; `review/rendered/d4rt_page02.png` und `d4rt_page06.png`.

PDF-Seite 12 enthält nur die Fortsetzung von Anhang A in der linken Spalte. Die rechte Spalte ist leer. PDF-Seite 13 nutzt nur einen Teil der linken Seitenhälfte. D4RT bindet Abbildungen und Tabellen wesentlich dichter und ausgeglichener ein.

**Korrektur:** Anhang A und B gemeinsam neu umbrechen. Entweder bereits vor Anhang A auf einspaltigen Satz wechseln und Anhang B auf derselben beziehungsweise folgenden ausgefüllten Fläche anschließen oder einen ausgeglichenen zweispaltigen Anhang setzen. Danach alle Seiten erneut rendern und Seitenbudget, Quellenumbrüche und Glyphengrößen prüfen. D4RTs US Letter, kleinere Schrift und geringere Ränder dürfen dabei nicht übernommen werden.

### M4. Das 9-°C-Label in Abbildung 1 ist irreführend platziert

**Beleg:** PDF-Seite 5, Abbildung 1; `model/run_all.py:282-286`.

Die gestrichelte 9-°C-Linie liegt unten im Diagramm. Ihre Legende wird durch `loc="upper left"` oben links neben der steigenden Szenariokurve platziert. Dadurch erscheint „Regelziel 9 °C“ im Bereich der 100-°C-Darstellung.

**Korrektur:** Die Achsenlegende entfernen und „Regelziel 9 °C“ direkt neben der unteren gestrichelten Linie oder mit einer eindeutigen Beschriftungslinie zu dieser platzieren. Anschließend die tatsächliche PDF-Seite erneut sichtprüfen.

### M5. Die reale Abgabebereitschaft ist noch nicht hergestellt

**Beleg:** PDF-Seite 1, `TEST-K31pro-max`; PDF-Seite 12, Anhang A; `PROVENANCE.md:42-44`; offizielle Berichtsvorgaben, §9 Regeln 1, 3 und 4.

Die Testkennung ist für das Testpaket nachvollziehbar, aber keine offizielle Team-ID. Die menschliche Fachprüfung wird ausdrücklich als nicht erfolgt genannt. Die offiziellen Regeln verlangen außerdem, dass KI die persönliche Auseinandersetzung unterstützt und nicht ersetzt und dass Ausgaben auf Richtigkeit, mögliche Ähnlichkeiten sowie rechtliche und ethische Vereinbarkeit geprüft werden.

**Korrektur:** Nach M1 bis M4 muss ein berechtigtes Teammitglied den vollständigen Paper fachlich prüfen, die KI-Prüfung einschließlich Ähnlichkeits- und Rechteprüfung dokumentieren, die offizielle Team-ID in Dateiname und Deckblatt einsetzen und die erforderlichen Erklärungen abgeben. Danach sind PDF, Seitenbilder, Modellartefakte und Archivreproduktion erneut zu erstellen und zu prüfen.

## Restrisiken und Dissens

- **Karst und Hydrologie:** Betroffener Stromanteil, Astabflüsse, Bathymetrie, Durchmischung und Wärmebilanz sind nicht feldkalibriert. Ein Vollstromentwurf kann erst nach Messungen bestätigt werden. PDF-Seiten 2, 8 und 9, §2.1, §4.4 und §5.
- **Technik und Standort:** Herstellerkurven, Teillast, Feuchtkugelstatistik, Luftführung, Schall, Netzanschluss, Flächeneigentum und Genehmigungen fehlen. Die Werte 8,41 ha, zweimal 234,3 MW und 2.869 m³ Diesel sind Screening-Größen, keine Standortzusage. PDF-Seite 7, §4.3.
- **Unsicherheit:** Die Dreiecks- und Lognormalverteilungen sind deklarierte Szenarien, keine empirischen Häufigkeitsmodelle. Die Begrenzung auf 4,7 m³/s schließt Extremhochwasser und andere Wärmequellen aus. PDF-Seite 8, §4.4; PDF-Seite 13, Abbildung 3.
- **Hochwasser und dauerhafte Zusage:** Für 32,7 m³/s wären 12,48 GW erforderlich. Dieser Fall ist nicht abgedeckt. Ebenso wenig sind Temperaturen über 100 °C oder eine unbegrenzt wachsende Wärmezufuhr beherrschbar. PDF-Seite 9, §4.4.
- **Dynamik:** Das 20-°C-Kriterium ist eine interne ökologische Alarmschwelle, kein Siedenachweis. Bei 10.000 m³ effektivem Volumen wird sie verfehlt. Der 48-Stunden-Dieselvorrat deckt nur den modellierten Kurzausfall; die 95-%-Kostensensitivität setzt unbegrenzte Diesellieferung voraus. PDF-Seiten 6 bis 8.
- **Reproduktion:** Der Nachweis gilt für dieselbe verknüpfte Referenzumgebung. Er belegt weder eine frische Abhängigkeitsinstallation auf einem fremden Rechner noch eine externe wissenschaftliche Validierung. Ich habe wegen des Build-Verbots keinen neuen Archivbuild ausgeführt, sondern die 37 Artefakte und ihre Commit-Zuordnung hashbasiert geprüft.
- **Reviewunabhängigkeit:** Der zweite Kimi-Kontext ist keine externe oder menschliche Prüfung. Eine mögliche abweichende Bewertung der Testkennung oder der Anhangsgestaltung ändert nichts am fachlichen H2-Einwand.
- **D4RT:** Der Vergleich betrifft nur die visuelle Ordnung. D4RTs Verstöße gegen die PlaNeT-Vorgaben zu Papierformat, Rand und Schriftgröße sind nicht übernahmefähig.

## Bewertungen von 10 und erfolglose Fehlersuche

Es wurde keine 10 vergeben. Deshalb gibt es keine zugehörigen Nachweise einer erfolglosen substanziellen Fehlersuche. Die eigene Fehlersuche hatte vielmehr einen substanziellen Treffer: Der bisherige H2-Test übersieht den null Kelvin großen Temperaturabstand am heißen Ende. Weitere Prüfungen führten zu den Kostenherkunfts- und Darstellungsbefunden M2 bis M4.

## Stoppregelurteil

**Die Stoppregel ist auf dieser Revision nicht erfüllt.**

Die niedrigste Einzelbewertung beträgt 7. Nur die Kriterien 3 und 5 erreichen 9; keine Zeile erreicht 10. Mit dem ungeklärten H2-Wärmeübertrager bleibt ein substanzieller Einwand gegen die wissenschaftliche Qualität und einen Teil der Alternativbewertung bestehen. Hinzu kommen offene Korrekturen an Nachweisen, Layout und realer Abgabebereitschaft. Die technische Existenz und Hash-Integrität aller Paperartefakte ändert daran nichts. Eine weitere Reviewrunde nach M1 bis M5 ist erforderlich.

## Betriebsprotokoll

Es wurden keine Builds oder Modelltests ausgeführt. Bei einer versuchten Raster-ausgabe nach stdout erzeugte `pdftoppm` abweichend vom erwarteten Verhalten kurzzeitig die Datei `-.png`. Sie war hashidentisch mit `review/rendered/report_pages/page-01.png` und wurde unmittelbar als eigenes Prüfartefakt entfernt. Der abschließende Git-Status zeigt wieder nur die beiden bereits vorhandenen unversionierten Dateien `review/rounds/round8/prompt.md` und `review/rounds/round8/revision.json`; alle versionierten Dateien entsprechen dem Zielcommit.
