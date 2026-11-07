# Review- und Revisionsübersicht

## Vorgeschriebene Reviewer

- DeepSeek-V4.1-Flash, exakte ID `deepseek-account/deepseek-flash`, `reasoning_effort=max`.
- Kimi K3.1 Pro, exakte ID `kimi-code/k3.1-pro`, `thinking=max`.
- Der implementierende Agent ist ebenfalls Kimi K3.1 Pro mit `thinking=max` und hat keine unabhängige Council-Stimme.

Die Auflösung und Verfügbarkeit sind in `review/model_configuration.md` belegt. Jede Runde erhält beide Reviewer mit demselben vollständigen Paket und einem eingefrorenen Commit. Die Reviews erfolgen getrennt und read-only.

## Runden und Bewertungen

Bisher wurde noch keine Council-Runde durchgeführt. Diese Tabelle wird erst nach tatsächlich vorliegenden Reviews ausgefüllt. Es werden keine Werte vorweggenommen.

| Runde | Revision | DeepSeek, alle Kriterien | Kimi, alle Kriterien | Offene Arbeit |
| --- | --- | --- | --- | --- |
| 1 | wird nach vollständigen Prüfungen eingefroren | noch keine Bewertung | noch keine Bewertung | Render- und Integritätsprüfung |

Die Kriterien 1 bis 6, 8 bis 11 sowie 12a und 12b werden einzeln dokumentiert. Frühere Bewertungen gelten nie für eine neue Revision.

## Befundzuordnung

Alle Befunde werden in `review/rounds/<runde>/findings.md` mit Reviewer, Kriterium, genauer Belegstelle, Korrektur oder begründeter Zurückweisung und erneuter Prüfung protokolliert. Differenzen zwischen den Reviewern bleiben erhalten.

## Verbleibende Risiken und menschliche Aufgaben

Vor einer realen Abgabe müssen Menschen die Inhalte prüfen, die offizielle Team-ID einsetzen, behördliche und technische Machbarkeit klären, Medienrechte freigeben, die Finalisten-E-Mail lesen und eine eigene Live-Probe durchführen. Kein Council-Ergebnis garantiert Jurybewertungen, Qualifikation oder Wettbewerbserfolg.
