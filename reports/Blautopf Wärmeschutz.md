# Arbeitsnotiz zur Berichtssynthese

Diese Datei ist keine zweite Berichtsfassung und nicht zur Abgabe bestimmt. Sie ersetzt den verworfenen Zwischenentwurf, dessen Kosten und Rampenmechanik vor dem Council-Review Runde 1 standen. Die ältere Fassung bleibt nur in der Git-Historie erhalten.

Die einzige maßgebliche Berichtsausgabe ist `output/pdf/TEST-K31pro-max.pdf`. Ihre Quelle ist `report/main.tex`. Jede dargestellte Zahl stammt aus `output/model/results.json` und wird durch `make report` neu erzeugt.

Der unabhängig entwickelte Ansatz ist eine zweistufige Vollstromkühlung mit Trockenkühlern und Kältemaschinen. Im Erwartungsszenario beträgt die erforderliche Kühlleistung 877,8 MW, die Investition mit p90-Reserve 1.283,1 Mio. € und der Barwert über 25 Jahre 3,666 Mrd. €. Diese Eurobeträge sind Szenarioschätzungen, keine Angebote. Der Entwurf gilt nur für höchstens 4,7 m³/s betroffenen Strom und höchstens 100 °C am tiefen Zufluss. Der p90-Spitzenfall verlangt 1.793,7 MW Kühlung und 182,7 MW Antriebsleistung; installiert sind 2.152,5 MW Kühlkapazität.

Die geplante Inbetriebnahme regelt den Kälteauslass mit höchstens 1 K/h. Ein Puffer allein und ein linear geöffnetes Zulaufventil belegen diese Grenze nicht. Der 91-Stunden-Test ist ein Sollwert-Stresstest von 100 auf 9 °C, kein Notfall- oder Wiederanlaufnachweis.

Die Hypothesen stehen in `docs/hypothesen.md`, der Vergleich in `docs/alternativenvergleich.md`. Recherchenotizen liegen unter `research_notes/`. Reviewbefunde und ihre Bearbeitung stehen in `review/revisions.md`. Quellen, Berechnungen und KI-Nutzung dokumentieren `sources/registry.yml`, `PROVENANCE.md` und `decisions.tsv`.
