# Blautopf, dauerhafte Verhinderung des Siedens

Unabhängig erstellter deutscher Forschungsbericht für die vom Nutzer übergebene Blautopf-Aufgabe. Vulkanische Aktivität und die Zehnjahresprognose sind Szenarioprämissen, keine durch dieses Repository bestätigten Messbefunde.

Der aktuelle Lieferumfang ist auf Nutzerkorrektur nur der Research Paper. Das PDF, seine LaTeX-Quelle und das reproduzierbare Rechenmodell bilden das Produkt. Die bereits vorhandenen Präsentations- und Finaldateien bleiben als historische Arbeitsstände erhalten, gehören aber nicht mehr zum Lieferumfang und werden nicht weiterentwickelt.

Das private GitHub-Repository wurde neu angelegt. Ein Push erfolgte nicht, da keine externe Bereitstellung der Arbeitsdateien freigegeben wurde. Eine Wettbewerbsabgabe oder öffentliche Veröffentlichung hat nicht stattgefunden.

## Zentrale Antwort

Die Lösung ist eine zweistufige, modular aufgebaute Vollstromkühlung. Direkte Trockenkühlung nutzt die hohe Temperaturdifferenz zuerst. Kältemaschinen bringen das Wasser danach auf 9 °C. Die Wärme einschließlich Kondensator- und Hilfsenergie wird an Luft abgegeben, nicht an Blau oder Grundwasser. Im p90-Fall tragen elf Stränge die Last, ein zwölfter ist Reserve. Im Mittelbetrieb modulieren fünf.

Im erwarteten Vollstromszenario sind im zehnten Jahr 877,8 MW Kühlleistung erforderlich. Für das historische 90-Prozent-Abflussquantil von 4,7 m³/s werden 1.793,7 MW benötigt und mit 20 % Reserve 2.152,5 MW installiert. Die isolierte Speicherrechnung liefert dagegen nur 0,0303 MW als untere energetische Grenze, nicht als Kühlbedarf des durchströmten Systems. Vor der endgültigen Dimensionierung müssen Durchfluss, betroffener Karstast, Netzanschluss und Standort geprüft werden.

## Produkt und Nachweise

- `output/pdf/TEST-K31pro-max.pdf` ist der fertige anonyme Research Paper.
- `report/main.tex` und `report/preamble.tex` enthalten den editierbaren Berichtssatz.
- `data/parameters.yml` enthält die Eingaben, Einheitenbezüge und Szenarioentscheidungen.
- `data/nist_saturation_32_100.tsv` enthält die NIST-Sättigungsdaten für die Verdampfungsenthalpie.
- `model/` enthält Thermodynamik, Kosten, Unsicherheit und Validierung.
- `output/model/results.json` enthält die berichteten Modellgrößen und Jahresreihen.
- `review/rendered/report_pages/` enthält die tatsächlich geprüften Seitenbilder.
- `compliance/` enthält Regeln, Layoutvergleich und Checkliste.
- `review/` enthält Modellkonfiguration, eingefrorene Revisionen, Scorecards und Befundzuordnungen.
- `PROVENANCE.md`, `EXCLUSION_LOG.md` und `decisions.tsv` dokumentieren Herkunft, Ausschlüsse und Entscheidungen.

## Voraussetzungen

Das Rechenmodell verwendet Python 3.14 und die Pakete aus `requirements.lock.txt`. Der Bericht benötigt Tectonic mit LaTeX-Paketen. Die PDF-Prüfung benötigt Poppler. Die Referenzumgebung verwendet Python 3.14.6, Tectonic 0.17.0 und Poppler 26.10.0. Die Schriften kommen aus den LaTeX-Paketen, nicht aus betriebssystemspezifischen Fontdateien.

## Reproduktion

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.lock.txt
make model
make test
make report
make review-package
```

`make model` erzeugt alle wissenschaftlichen Zahlen, Tabellen und Abbildungen. `make report` erzeugt den Research Paper und prüft das PDF. `make review-package` kopiert die geprüften Seitenbilder und erzeugt die Kontaktübersicht. Die älteren Befehle `make presentation` und `make verify` beziehen sich auf den historischen Gesamtbestand und sind für das aktuelle Produkt nicht erforderlich.

Der Dateiname verwendet die Testkennung `TEST-K31pro-max`, weil keine offizielle Team-ID vorliegt. Vor einer realen Abgabe muss ein berechtigtes Team diese Kennung in Deckblatt und Dateiname durch seine eigene ID ersetzen.

## Review und Provenienz

Jede Council-Runde erhält denselben eingefrorenen Commit und dasselbe Paperpaket. DeepSeek-V4.1-Flash und Kimi K3.1 Pro prüfen unabhängig mit maximaler Reasoning-Stufe. Frühere Bewertungen werden nicht auf neue Revisionen übertragen. Die genauen Modellkennungen stehen in `review/model_configuration.md`.

Die fachliche Prüfung umfasst die Kriterien 1 bis 6, 8 bis 11 und 12a. Kriterium 12b entfällt mit dem zurückgezogenen Finalprodukt. Nach den fachlichen Runden prüft ein eigener Council-Lauf ausschließlich das Design des Research Paper, wieder mit beiden vorgeschriebenen Modellen bei maximaler Reasoning-Stufe.

Die Übersicht der Runden, Einzelbewertungen, Befundkorrekturen und verbleibenden Risiken steht in `review/README.md`. Das Provenienzprotokoll unterscheidet Quellen, KI-Recherche, KI-Schreibunterstützung, Berechnungen und menschliche Restaufgaben. Das Ausschlussprotokoll erfasst auch unbeabsichtigte Kontakte mit nicht erlaubtem Material.

## Grenzen und menschliche Restaufgaben

Kein endliches System verhindert Sieden bei unbegrenzt wachsender Wärmezufuhr. Die Auslegung gilt nur innerhalb ihrer dokumentierten Hülle. Der Hochwasserfall mit vollständig erwärmtem Abfluss von 32,7 m³/s ist nicht abgedeckt. Das LGRB nennt diesen HQ-Wert für 1951 bis 2007 ohne ein bestimmtes Wiederkehrintervall.

Vor einer echten Abgabe müssen Menschen die wissenschaftlichen Annahmen, behördlichen Vorgaben, Rechte und offizielle Team-ID prüfen und selbst einreichen. Council-Konsens bedeutet nur interne Review-Bereitschaft und garantiert weder Jurybewertungen noch Qualifikation oder Wettbewerbserfolg.
