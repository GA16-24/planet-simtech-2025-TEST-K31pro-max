# Review- und Revisionsübersicht

## Vorgeschriebene Reviewer

- DeepSeek-V4.1-Flash, exakte ID `deepseek-account/deepseek-flash`, `reasoning_effort=max`.
- Kimi K3.1 Pro, exakte ID `kimi-code/k3.1-pro`, `thinking=max`.
- Der implementierende Agent ist ebenfalls Kimi K3.1 Pro mit `thinking=max` und hat keine unabhängige Council-Stimme.
- Council B ist ein unabhängiger Same-Model-Kontext, keine externe oder menschliche Prüfung. Diese Wahl ist durch die Nutzervorgabe festgelegt.

Die Auflösung und Verfügbarkeit sind in `review/model_configuration.md` belegt. Jede Runde erhält beide Reviewer mit demselben vollständigen Paket und einem eingefrorenen Commit. Die Reviews erfolgen getrennt und read-only.

## Runden und Bewertungen

Runde 1 und Runde 2 sind vollständig dokumentiert. Die Stoppregel war jeweils nicht erfüllt. Runde 3 wird erst nach erneuter Prüfung und Einfrierung der überarbeiteten Revision zulässig. Es werden keine Werte vorweggenommen oder übertragen.

| Runde | Revision | DeepSeek, alle Kriterien | Kimi, alle Kriterien | Offene Arbeit |
| --- | --- | --- | --- | --- |
| 1 | `9b3a83bcea1358184b14de6759af117a049114f5` | 7 bis 9, Kriterien 5 und 9 erreichen 9 | 7 bis 9, Kriterien 1, 5, 8, 9 und 10 erreichen 9 | Kostenkopplung, Quellen, Rampenmodell, technische Auslegung und sichtbare Renderfehler |
| 2 | `cc25cc903681ebbc4d6865309236885f729d6d77` | 7 bis 9, Kriterien 5 und 9 erreichen 9 | 7 bis 9, Kriterien 5 und 10 erreichen 9 | Hydrologie, Alternativen, Standort, Notfall, Tarif, COP und Satzfehler |
| 3 | wird nach vollständigen Prüfungen eingefroren | noch keine Bewertung | noch keine Bewertung | Neue Modell- und Dokumentenrevision, danach Einfrierung |

Die vollständigen Matrizen mit Begründungen und Belegen stehen in `rounds/round1/scorecard.md` und `rounds/round2/scorecard.md`. Der erste Kimi-Lauf in Runde 1 wurde wegen blockierender Leseberechtigungen verworfen. Der Neustart arbeitete mit technisch weiteren Berechtigungen, aber einem ausdrücklich read-only Auftrag und ohne Kenntnis des DeepSeek-Reviews. Beide Runde-2-Reviews liefen read-only mit `runtimeMode=full-access`. `review/model_configuration.md` hält die tatsächlichen Einstellungen fest.

Die Kriterien 1 bis 6, 8 bis 11 sowie 12a und 12b werden einzeln dokumentiert. Frühere Bewertungen gelten nie für eine neue Revision.

## Befundzuordnung

Alle Befunde werden in `review/revisions.md` mit genauer Belegstelle, konkreter Korrektur und erneuter Prüfung protokolliert. Die unabhängigen Rohberichte und Scorecards liegen in `review/rounds/<runde>/`. Differenzen zwischen den Reviewern bleiben erhalten.

## Verbleibende Risiken und menschliche Aufgaben

Vor einer realen Abgabe müssen Menschen die Inhalte prüfen, die offizielle Team-ID einsetzen, behördliche und technische Machbarkeit klären, Medienrechte freigeben, die Finalisten-E-Mail lesen und eine eigene Live-Probe durchführen. Kein Council-Ergebnis garantiert Jurybewertungen, Qualifikation oder Wettbewerbserfolg.
