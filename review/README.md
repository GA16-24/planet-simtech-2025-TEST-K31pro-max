# Review- und Revisionsübersicht

## Vorgeschriebene Reviewer

- DeepSeek-V4.1-Flash, exakte ID `deepseek-account/deepseek-flash`, `reasoning_effort=max`.
- Kimi K3.1 Pro, exakte ID `kimi-code/k3.1-pro`, `thinking=max`.
- Der implementierende Agent ist ebenfalls Kimi K3.1 Pro mit `thinking=max` und hat keine unabhängige Council-Stimme.
- Council B ist ein unabhängiger Same-Model-Kontext, keine externe oder menschliche Prüfung. Diese Wahl ist durch die Nutzervorgabe festgelegt.

Die Auflösung und Verfügbarkeit sind in `review/model_configuration.md` belegt. Jede Runde erhält beide Reviewer mit demselben vollständigen Paket und einem eingefrorenen Commit. Die Reviews erfolgen getrennt und read-only.

## Runden und Bewertungen

Runde 1 bis Runde 3 sind vollständig dokumentiert. Die Stoppregel war jeweils nicht erfüllt. Runde 4 wird erst nach erneuter Prüfung und Einfrierung der überarbeiteten Revision zulässig. Es werden keine Werte vorweggenommen oder übertragen.

| Runde | Revision | DeepSeek, alle Kriterien | Kimi, alle Kriterien | Offene Arbeit |
| --- | --- | --- | --- | --- |
| 1 | `9b3a83bcea1358184b14de6759af117a049114f5` | 7 bis 9, Kriterien 5 und 9 erreichen 9 | 7 bis 9, Kriterien 1, 5, 8, 9 und 10 erreichen 9 | Kostenkopplung, Quellen, Rampenmodell, technische Auslegung und sichtbare Renderfehler |
| 2 | `cc25cc903681ebbc4d6865309236885f729d6d77` | 7 bis 9, Kriterien 5 und 9 erreichen 9 | 7 bis 9, Kriterien 5 und 10 erreichen 9 | Hydrologie, Alternativen, Standort, Notfall, Tarif, COP und Satzfehler |
| 3 | `77c1f972df9c67a00354e395ce31f27fd0c1b95c` | 1 bis 4, 6, 8, 10: 8; 5, 9: 9; 11: 6; 12a: 7; 12b: 8 | 1 bis 4, 6, 8 bis 10: 8; 5: 9; 11: 7; 12a: 7; 12b: 8 | Zusammenfassung, WebVTT, Kapazitätslinien, p90-Ausfall, Satz und Nachweisführung |
| 4 | Endcommit in `rounds/round4/revision.json` nach dem Einfrieren | ausstehend | ausstehend | Neue Prüfung der korrigierten Revision, keine Übernahme früherer Werte |

Die vollständigen Matrizen mit Begründungen und Belegen stehen in `rounds/round1/scorecard.md`, `rounds/round2/scorecard.md` und `rounds/round3/scorecard.md`. Der erste Kimi-Lauf in Runde 1 wurde wegen blockierender Leseberechtigungen verworfen. Der Neustart arbeitete mit technisch weiteren Berechtigungen, aber einem ausdrücklich read-only Auftrag und ohne Kenntnis des DeepSeek-Reviews. Die Reviews in Runde 2 und Runde 3 liefen read-only mit `runtimeMode=full-access`. `review/model_configuration.md` hält die tatsächlichen Einstellungen fest.

Die Kriterien 1 bis 6, 8 bis 11 sowie 12a und 12b werden einzeln dokumentiert. Frühere Bewertungen gelten nie für eine neue Revision.

## Befundzuordnung

Alle Befunde werden in `review/revisions.md` mit genauer Belegstelle, konkreter Korrektur und erneuter Prüfung protokolliert. Die unabhängigen Rohberichte und Scorecards liegen in `review/rounds/<runde>/`. Differenzen zwischen den Reviewern bleiben erhalten.

## Verbleibende Risiken und menschliche Aufgaben

Vor einer realen Abgabe müssen Menschen die Inhalte prüfen, die offizielle Team-ID einsetzen, behördliche und technische Machbarkeit klären, Medienrechte freigeben, die Finalisten-E-Mail lesen und eine eigene Live-Probe durchführen. Kein Council-Ergebnis garantiert Jurybewertungen, Qualifikation oder Wettbewerbserfolg.
