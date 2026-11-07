# Blautopf, dauerhafte Verhinderung des Siedens

Unabhängig erstelltes Wettbewerbspaket für die vom Nutzer übergebene Blautopf-Aufgabe. Vulkanische Aktivität und die Zehnjahresprognose sind Szenarioprämissen, keine durch dieses Repository bestätigten Messbefunde.

Das private Repository enthält einen deutschen Bericht, das vollständige Rechenmodell, Sensitivitäts- und Wirtschaftlichkeitsanalysen, eine animierte Finalpräsentation mit Video, Sprechtext, Zeitprobe, adversariale Juryfragen sowie Herkunfts-, Prüf- und Reviewnachweise. Eine Einreichung oder öffentliche Veröffentlichung hat nicht stattgefunden.

## Zentrale Antwort

Die Lösung ist eine zweistufige, modular aufgebaute Vollstromkühlung. Direkte Trockenkühlung nutzt die hohe Temperaturdifferenz zuerst. Kältemaschinen bringen das Wasser danach auf 9 °C. Sechs Module stellen im Auslegungsjahr fünf betriebsnotwendige Module und eine Reserve. Die Wärme einschließlich Kondensator- und Hilfsenergie wird an Luft abgegeben, nicht an Blau oder Grundwasser.

Im konservativen Fall eines vollständig betroffenen mittleren Quellstroms sind im zehnten Jahr 877,8 MW Kühlleistung erforderlich. Die isolierte Speicherrechnung liefert dagegen nur 0,0303 MW. Der Unterschied ist der wichtigste wissenschaftliche Befund. Vor der endgültigen Dimensionierung müssen Durchfluss und betroffener Karstast gemessen werden.

## Dateien

- `output/pdf/TEST-K31pro-max.pdf` ist der fertige anonyme Bericht.
- `report/main.tex` und `report/preamble.tex` enthalten den editierbaren Berichtssatz.
- `data/parameters.yml` enthält sämtliche Eingaben, Einheitenbezüge und Szenarioentscheidungen.
- `model/` enthält Thermodynamik, Kosten, Unsicherheit und Validierung.
- `output/model/results.json` enthält jede berichtete Modellgröße und die Jahresreihen.
- `output/presentation/` enthält PDF-Folien und das Finalvideo.
- `presentation/` enthält Folienquelle, Sprechtext, Zeitprobe, Juryfragen und Rechtenachweis.
- `compliance/` enthält Regeln, Layoutvergleich und die erfüllte Checkliste.
- `review/` enthält Modellkonfiguration, eingefrorene Revisionen, Scorecards und Befundzuordnungen.
- `PROVENANCE.md`, `EXCLUSION_LOG.md` und `decisions.tsv` dokumentieren Herkunft, Ausschlüsse und Entscheidungen.

## Voraussetzungen

Für das Rechenmodell werden Python 3.14 und die Pakete aus `requirements.lock.txt` verwendet. Bericht und Folien benötigen Tectonic mit LaTeX-Paketen. PDF-Prüfungen benötigen Poppler. Das Video benötigt FFmpeg mit H.264 und AAC. Die optionale Neueinstellung der deutschen Stimme verwendet eSpeak NG 1.52.0. Die bereits erzeugten Audiodateien ermöglichen die Videoreproduktion ohne diesen Schritt.

## Reproduktion

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.lock.txt
make model
make test
make report
make presentation
make verify
```

`make model` erzeugt alle wissenschaftlichen Zahlen, Tabellen und Abbildungen. `make report` erzeugt den Bericht und prüft das PDF. `make presentation` erzeugt Folien, Video, Untertitel und Zeitnachweise. `make verify` prüft Modell, Dokumente, Video und formale Anforderungen erneut.

Der Dateiname verwendet die Testkennung `TEST-K31pro-max`, weil keine offizielle Team-ID vorliegt. Vor einer realen Abgabe muss ein berechtigtes Team diese Kennung in Deckblatt und Dateiname durch seine eigene ID ersetzen.

## Review und Provenienz

Jede Council-Runde erhält denselben eingefrorenen Commit und dasselbe vollständige Paket. DeepSeek-V4.1-Flash und Kimi K3.1 Pro prüfen unabhängig mit maximaler Reasoning-Stufe. Frühere Bewertungen werden nicht auf neue Revisionen übertragen. Die genauen Modellkennungen stehen in `review/model_configuration.md`.

Die Übersicht der Runden, Einzelbewertungen, Befundkorrekturen und verbleibenden Risiken wird in `review/README.md` geführt. Das Provenienzprotokoll unterscheidet Quellen, KI-Recherche, KI-Schreibunterstützung, Berechnungen und menschliche Restaufgaben. Das Ausschlussprotokoll erfasst auch unbeabsichtigte Kontakte mit nicht erlaubtem Material.

## Grenzen und menschliche Restaufgaben

Kein endliches System verhindert Sieden bei unbegrenzt wachsender Wärmezufuhr. Die Auslegung gilt nur innerhalb ihrer dokumentierten Hülle. Der Hochwasserfall mit vollständig erwärmtem Abfluss von 32,7 m³/s ist nicht abgedeckt und wird als kritischer Stresstest ausgewiesen.

Vor einer echten Abgabe müssen Menschen die wissenschaftlichen Annahmen, behördlichen Vorgaben, Medienrechte und Finalisten-E-Mail prüfen. Eine menschliche Präsentation und eine echte Live-Zeitprobe sind nicht durch die synthetische Vertonung ersetzt. Council-Konsens bedeutet nur interne Review-Bereitschaft und garantiert weder Jurybewertungen noch Qualifikation oder Wettbewerbserfolg.
