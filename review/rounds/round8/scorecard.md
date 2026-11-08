# Scorecard Runde 8

Revision: `c76d40d3dabf894fb2475c714af5eed213f82c90`, 181 Dateien. Der reproduzierte Paperkandidat ist `2385effc1d03a39bdf3965222d4121030d7a6569`. Beide Reviewer prüften unabhängig und read-only mit `reasoning_effort=max` beziehungsweise `thinking=max`. Keine früheren Rohberichte oder Scorecards wurden verwendet. Die vollständigen Begründungen stehen in `deepseek.md` und `kimi.md`. Die zugehörigen Taskergebnisse sind in `deepseek_result.json` und `kimi_result.json` archiviert.

Der Prüfumfang ist der Research Paper mit den Kriterien 1, 2, 3, 4, 5, 6, 8, 9, 10, 11 und 12a. Kriterium 12b gehört nicht mehr zum Lieferumfang.

| Kriterium | DeepSeek-V4.1-Flash | Kimi K3.1 Pro |
| --- | ---: | ---: |
| 1 Qualität der Argumentation | 9 | 8 |
| 2 Vorgehen und Methodik | 9 | 8 |
| 3 Qualität der vorgeschlagenen Lösung | 8 | 9 |
| 4 Mathematische und wissenschaftliche Modellierung | 9 | 7 |
| 5 Ableitung neuer Ansätze | 9 | 9 |
| 6 Wissenschaftliche Qualität | 8 | 7 |
| 8 Klare Erklärungen | 8 | 8 |
| 9 Kritische Diskussion | 9 | 8 |
| 10 Struktur und Juryführung | 8 | 8 |
| 11 Format, Zitation und D4RT-Vergleich | 7 | 8 |
| 12a Schriftliche Bereitschaft | 8 | 8 |

## Ergebnis

Die Stoppregel ist nicht erfüllt. Kein Reviewer vergibt eine 10. Die Punktzahlen werden nicht gemittelt und nicht auf eine neue Revision übertragen.

## DeepSeek, materielle Befunde

- Die 9-°C-Legende kollidiert mit der Jahreslinie. Anhang A hat unzureichende Absatztrennung und eine zu kleine Inline-Formel. Anhang B nutzt die Seite nicht aus. Die Referenzlinie für den Barwert ist nicht erklärt und die Nachkommastellen sind uneinheitlich.
- Die H2-Temperaturbeschreibung widerspricht der Energiebilanz. Die Ausfallzeiten, Diesel-Lastbasis und unterschiedlichen Auslegungsabflüsse von Siedeschutz und H1 sind nicht klar genannt. H4 bis H7 sind nicht aufgelöst, 165 km² fehlt ein Quellenverweis.
- Die Zusammenfassung enthält noch Fachbegriffe. Die Kostenaufschlüsselung fehlt. Frühere Layoutnachweise beschreiben den gerenderten Stand falsch.

## Kimi, materielle Befunde

- Der Sekundärkreislauf beginnt bei 100 °C. Damit beträgt der Pinch am heißen Ende 0 K. Der vorhandene Test prüft weder dieses Ende noch den Sekundärmassenstrom und die Energiebilanz.
- Die HAW-Kostenbereiche sind nicht korrekt vom eigenen konservativen Szenariowert 500 €/kW getrennt. Trockenkühlung und Verdunstung brauchen getrennt deklarierte Szenariokosten. Das Quellenregister nennt einen veralteten hydrostatischen Druck.
- Anhang A und B sind schlecht umbrochen. Das 9-°C-Label ist nicht bei seiner Linie platziert. Menschliche Prüfung, offizielle Team-ID und rechtliche Freigabe bleiben offene Abgabevoraussetzungen.

## Nachbearbeitung

Die nächste Revision muss die H2-Temperaturführung und ihre Bilanz testen, die Kostenherkunft trennen, alle Klarheitsbefunde bearbeiten und das gerenderte Paper einschließlich Anhang erneut prüfen. `review/revisions.md` ordnet die Befunde zu. Neue Punktzahlen werden erst nach erneuter Archivreproduktion und unabhängiger Review erhoben.
