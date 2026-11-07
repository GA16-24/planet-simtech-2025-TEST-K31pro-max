# Scorecard Runde 2

Revision: `cc25cc903681ebbc4d6865309236885f729d6d77`, 127 Dateien. Beide Reviewer erhielten denselben Prüfauftrag und dieselbe Befundhistorie. Sie bewerteten unabhängig, ohne die jeweils andere Punktzahl oder frühere Scorecards zu lesen. Beide arbeiteten read-only mit `runtimeMode=full-access`. Die vorgeschriebenen Reasoning-Einstellungen waren `reasoning_effort=max` und `thinking=max`.

| Kriterium | DeepSeek-V4.1-Flash | Kimi K3.1 Pro |
| --- | ---: | ---: |
| 1 Qualität der Argumentation | 8 | 8 |
| 2 Vorgehen und Methodik | 8 | 7 |
| 3 Qualität der vorgeschlagenen Lösung | 7 | 7 |
| 4 Mathematische und wissenschaftliche Modellierung | 8 | 8 |
| 5 Ableitung neuer Ansätze | 9 | 9 |
| 6 Wissenschaftliche Qualität | 8 | 8 |
| 8 Klare Erklärungen | 8 | 8 |
| 9 Kritische Diskussion | 9 | 8 |
| 10 Struktur und Juryführung | 8 | 9 |
| 11 Format, Zitation und D4RT-Vergleich | 7 | 8 |
| 12a Schriftliche Bereitschaft | 8 | 8 |
| 12b Finale Bereitschaft | 8 | 8 |

## Ergebnis

Die Stoppregel ist nicht erfüllt. Kein Reviewer vergibt eine 10. Die Rohberichte stehen in `deepseek.md` und `kimi.md`. DeepSeek dokumentiert 19 Befundgruppen, Kimi 8. Ihre unterschiedlichen Schwerpunktsetzungen und Bewertungen bleiben erhalten.

## Gemeinsame materielle Einwände

- Die Referenzanlage hält 9 °C nur für höchstens 2,3 m³/s. Kimi weist in der vorhandenen Monte-Carlo-Stichprobe 3.857 von 10.000 Fällen oberhalb der installierten 1.053,3 MW nach, also 38,57 %.
- H2 ist ohne Feuchtkugelgrenze und ergänzende Kältemaschine nicht unter allen Auslegungsbedingungen gleichwertig.
- Luftsenke, Standort, Netzanschluss und dynamischer Notfallnachweis sind unvollständig.
- Die Tabelle rundet 0,1 % auf 0 %. Weitere Satzfehler betreffen insbesondere Gleichung 10 und eine fast leere Anhangsseite.
- Der Freeze weicht für `output/verification_summary.json` nur im Erstellungszeitpunkt vom Commit ab. Das ist kein inhaltlicher Modellfehler, verletzt aber die geforderte Commit-Treue.

## Zusätzliche Einwände und Dissens

- DeepSeek verlangt eine quantitative Trennung zwischen reinem Siedeschutz und dem ökologischen 9-°C-Ziel, einen vorsichtigeren COP, eine korrekte Behandlung der Verfügbarkeit sowie eine klare Kennzeichnung fest angesetzter Kosten.
- Kimi weist auf den ungeeigneten Stromtarif für 650 GWh pro Jahr und auf Überbehauptungen in Folie 10 und Sprechtext hin.
- DeepSeek beanstandet die Bezeichnung unabhängiger Reviewer bei modellgleichem Council B. Die Vorgabe des Nutzers verlangt gerade dieses Modell. Die nächste Dokumentation bezeichnet ihn deshalb präzise als unabhängigen Same-Model-Kontext, nicht als externe oder menschliche Prüfung.
- Beide Reviewer sehen offizielle Team-ID, menschliche Fachprüfung, Rechtefreigabe, Finalisten-E-Mail und echte Live-Probe als verbleibende menschliche Aufgaben. Das Paket behauptet diese Schritte nicht.

Die Bearbeitung aller Befunde wird in `review/revisions.md` mit konkreten Änderungen oder einer begründeten Zurückweisung dokumentiert. Keine Punktzahl wird auf eine spätere Revision übertragen.
