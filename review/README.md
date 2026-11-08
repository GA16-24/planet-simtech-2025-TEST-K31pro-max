# Review- und Revisionsübersicht

## Vorgeschriebene Reviewer

- DeepSeek-V4.1-Flash, exakte ID `deepseek-account/deepseek-flash`, `reasoning_effort=max`.
- Kimi K3.1 Pro, exakte ID `kimi-code/k3.1-pro`, `thinking=max`.
- Der implementierende Agent ist ebenfalls Kimi K3.1 Pro mit `thinking=max` und hat keine unabhängige Council-Stimme.
- Council B ist ein unabhängiger Same-Model-Kontext, keine externe oder menschliche Prüfung. Diese Wahl ist durch die Nutzervorgabe festgelegt.

Die Auflösung und Verfügbarkeit sind in `review/model_configuration.md` belegt. Jede Runde erhält beide Reviewer mit demselben vollständigen Paket und einem eingefrorenen Commit. Die Reviews erfolgen getrennt und read-only.

## Aktueller Prüfumfang

Der Nutzer hat den Lieferumfang nach Runde 5 auf den Research Paper beschränkt. Ab Runde 6 bewerten beide Council-Mitglieder die Kriterien 1 bis 6, 8 bis 11 und 12a anhand derselben eingefrorenen PDF, des Modells und der Nachweise. Kriterium 12b und die Präsentationsartefakte gehören nicht mehr zum Lieferumfang. Nach den fachlichen Runden folgt ein eigener Council-Lauf nur für das Design des Research Paper.

## Runden und Bewertungen

Runde 1 bis Runde 5 sind vollständig dokumentiert. Die Stoppregel war jeweils nicht erfüllt. Es werden keine Werte vorweggenommen oder auf neue Revisionen übertragen.

| Runde | Revision | DeepSeek, alle Kriterien | Kimi, alle Kriterien | Offene Arbeit |
| --- | --- | --- | --- | --- |
| 1 | `9b3a83bcea1358184b14de6759af117a049114f5` | 7 bis 9, Kriterien 5 und 9 erreichen 9 | 7 bis 9, Kriterien 1, 5, 8, 9 und 10 erreichen 9 | Kostenkopplung, Quellen, Rampenmodell, technische Auslegung und sichtbare Renderfehler |
| 2 | `cc25cc903681ebbc4d6865309236885f729d6d77` | 7 bis 9, Kriterien 5 und 9 erreichen 9 | 7 bis 9, Kriterien 5 und 10 erreichen 9 | Hydrologie, Alternativen, Standort, Notfall, Tarif, COP und Satzfehler |
| 3 | `77c1f972df9c67a00354e395ce31f27fd0c1b95c` | 1 bis 4, 6, 8, 10: 8; 5, 9: 9; 11: 6; 12a: 7; 12b: 8 | 1 bis 4, 6, 8 bis 10: 8; 5: 9; 11: 7; 12a: 7; 12b: 8 | Zusammenfassung, WebVTT, Kapazitätslinien, p90-Ausfall, Satz und Nachweisführung |
| 4 | `2fd9f3cd11e2f984f4fb8ce693b855529cabc580` | 1 bis 3, 5, 6, 9, 10: 9; 4, 8, 11, 12a, 12b: 8 | 1 bis 6, 8 bis 10: 9; 11, 12a, 12b: 8 | Ausfallzeit, Strangleistung, Fußzeile, Diagrammschrift, Quellen und Finalmaterialien |
| 5 | `e821bf60ef9fe637a5c5915a50d7748ab829c46c` | 7 bis 9; nur 3, 5 und 9 erreichen 9 | 8 bis 9; nur 3 und 12b bleiben bei 8 | Kostenmodell, Sättigungsdaten, Satz, Literatur und reale Machbarkeitsgrenzen |
| 6 | `473e397c4d45a909cc024e1722d572cdbd73df7d` | 1, 2, 3, 5, 8, 9, 10: 9; 4, 6, 11, 12a: 8 | 1, 3, 5, 9, 10: 9; 2, 4, 6, 8, 11, 12a: 8 | Teilstrom-Notstrom, Betriebsjahre, Monte-Carlo-Dokumentation, Achsenlabel und Schlusssatz |
| 7 | `a405cd19f187e2e6c80b51453617a6b6d883ae2a` | 1 bis 10 und 12a: 9; 11: 8 | 1, 5, 8, 10, 11: 9; 2, 3, 4, 6, 9, 12a: 8 | Elektrische Min-COP-Auslegung, Anhang, Tabellenplatzierung, Typografie und Zitationen |
| 8 | Kandidat `2385effc1d03a39bdf3965222d4121030d7a6569`, Review `c76d40d3dabf894fb2475c714af5eed213f82c90` | 1, 2, 4, 5, 9: 9; 3, 6, 8, 10, 12a: 8; 11: 7 | 3, 5: 9; 1, 2, 8, 9, 10, 11, 12a: 8; 4, 6: 7 | H2-Temperaturführung, Kostenherkunft, Klarheit, Anhang und Diagrammbeschriftung |
| 9 | Kandidat `becd50a0ddd77df4add7d03e8cb69866239f9b12`, Review `8e1b72d5235162172f31b00775cd1bb0c55d24ce` | Alle elf Kriterien: 9 | 1, 4, 5, 6, 8, 9, 10, 11: 9; 2, 3, 12a: 8 | Wärmegetriebene Kühlung fehlt; Bewertung der menschlichen Abgabevoraussetzungen |
| 10 | Kandidat `3f2324cb7b7323f1a04fbbad82a87c6e48dd8f64`, Review `2c8deecf575e3c837a505be00f1e170348d28a27` | 1 bis 10 und 12a: 9; 11: 8 | 1 bis 10: 9; 11, 12a: 8 | HAW-Kostenbezeichnung, Anhangsdichte, Seitenflag und kleinere Nachweise |
| 11 | Kandidat nach Runde 10 in Vorbereitung | ausstehend | ausstehend | Erneute Archivreproduktion und unabhängige Prüfung |

Die vollständigen Matrizen mit Begründungen und Belegen stehen in `rounds/round1/scorecard.md` bis `rounds/round10/scorecard.md`. Der erste Kimi-Lauf in Runde 1 wurde wegen blockierender Leseberechtigungen verworfen. Der Neustart arbeitete mit technisch weiteren Berechtigungen, aber einem ausdrücklich read-only Auftrag und ohne Kenntnis des DeepSeek-Reviews. Die Reviews seit Runde 2 liefen read-only mit `runtimeMode=full-access`. `review/model_configuration.md` hält die tatsächlichen Einstellungen fest.

Frühere Bewertungen gelten nie für eine neue Revision. Auch der Wechsel zum Paperumfang überträgt keine alte Punktzahl.

## Befundzuordnung

Alle Befunde werden in `review/revisions.md` mit genauer Belegstelle, konkreter Korrektur und erneuter Prüfung protokolliert. Die unabhängigen Rohberichte und Scorecards liegen in `review/rounds/<runde>/`. Differenzen zwischen den Reviewern bleiben erhalten.

## Verbleibende Risiken und menschliche Aufgaben

Vor einer realen Abgabe müssen Menschen die wissenschaftlichen Inhalte und Rechte prüfen, die offizielle Team-ID einsetzen sowie behördliche und technische Machbarkeit klären und selbst einreichen. Präsentations- und Finalaufgaben gehören nicht mehr zum Lieferumfang. Kein Council-Ergebnis garantiert Jurybewertungen, Qualifikation oder Wettbewerbserfolg.
