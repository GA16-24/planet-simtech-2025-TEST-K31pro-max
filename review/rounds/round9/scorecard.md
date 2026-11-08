# Scorecard Runde 9

Revision: `8e1b72d5235162172f31b00775cd1bb0c55d24ce`, 189 Dateien. Der reproduzierte Paperkandidat ist `becd50a0ddd77df4add7d03e8cb69866239f9b12`. Beide Reviewer prüften read-only mit `reasoning_effort=max` beziehungsweise `thinking=max`. Keine früheren Rohberichte oder Scorecards wurden als Bewertungsgrundlage vorgegeben. Die vollständigen Begründungen stehen in `deepseek.md` und `kimi.md`. Die Taskergebnisse sind in `deepseek_result.json` und `kimi_result.json` archiviert.

Der Prüfumfang ist der Research Paper mit den Kriterien 1, 2, 3, 4, 5, 6, 8, 9, 10, 11 und 12a. Kriterium 12b gehört nicht mehr zum Lieferumfang.

| Kriterium | DeepSeek-V4.1-Flash | Kimi K3.1 Pro |
| --- | ---: | ---: |
| 1 Qualität der Argumentation | 9 | 9 |
| 2 Vorgehen und Methodik | 9 | 8 |
| 3 Qualität der vorgeschlagenen Lösung | 9 | 8 |
| 4 Mathematische und wissenschaftliche Modellierung | 9 | 9 |
| 5 Ableitung neuer Ansätze | 9 | 9 |
| 6 Wissenschaftliche Qualität | 9 | 9 |
| 8 Klare Erklärungen | 9 | 9 |
| 9 Kritische Diskussion | 9 | 9 |
| 10 Struktur und Juryführung | 9 | 9 |
| 11 Format, Zitation und D4RT-Vergleich | 9 | 9 |
| 12a Schriftliche Bereitschaft | 9 | 8 |

## Ergebnis

Die Stoppregel ist nicht erfüllt. Kein Reviewer vergibt eine 10. Die Punktzahlen werden nicht gemittelt und nicht auf eine neue Revision übertragen.

DeepSeek öffnete nach eigenem Betriebsprotokoll versehentlich `review/README.md` mit der Übersicht früherer Punktzahlen. Der Bericht legt diese Exposition offen und erklärt, die Werte nicht verwendet zu haben. Alle Befunde wurden am eingefrorenen Commit geprüft. Der nächste Prüfauftrag schließt diese Datei ausdrücklich aus.

## DeepSeek, Ergebnis und optionale Hinweise

- Alle elf Kriterien erreichen 9, kein materieller Mangel bleibt aus dieser Sicht offen.
- Optionale Verbesserungen betreffen die NIST-URL, die Seitenzählung, die Ventilator- und Pumpenbasis, die Caption von Tabelle 2, die H2-Wasserbilanz ohne Abschlämmung, den Stufenplan, die H1-Weiterentwicklung und die Caption von Abbildung 1.
- Menschliche Prüfung, Team-ID und Einreichung bleiben ausdrücklich außerhalb des technisch geprüften Testpakets.

## Kimi, materielle Befunde

- Der Alternativenvergleich enthält keine wärmegetriebene Absorptions- oder Adsorptionskühlung. Ihre Wärme- und Exergiebilanz, Hilfsenergie, Kosten und Auslegungslast müssen geprüft werden, bevor H1 als Auswahl begründet werden kann. Kriterien 2 und 3 bleiben deshalb bei 8.
- Für eine tatsächliche Wettbewerbseinreichung fehlen offizielle Team-ID, menschliche Freigabe und Rechteprüfung. Kimi bewertet Kriterium 12a deshalb mit 8. Diese externen Schritte werden nicht durch KI ersetzt oder als erledigt ausgegeben.

## Nachbearbeitung

Die nächste Revision muss eine physikalisch geschlossene wärmegetriebene Vergleichsvariante nachrechnen und die übrigen Klarheitsbefunde prüfen. Die Bewertung von Kriterium 12a muss die technische Bereitschaft des Testpakets von einer echten Abgabe unterscheiden, ohne menschliche Aufgaben zu verschweigen. `review/revisions.md` ordnet die Umsetzung zu. Neue Punktzahlen werden erst nach erneuter Archivreproduktion und unabhängiger Review erhoben.
