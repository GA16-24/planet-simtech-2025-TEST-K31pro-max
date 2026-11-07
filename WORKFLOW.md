# Arbeits- und Prüfplan

## Ziel und Umfang

Das Paket beantwortet die gestellte Blautopf-Aufgabe auf Deutsch. Vulkanische Aktivität und die Zehnjahresprognose sind Szenarioannahmen. Die Lösung muss unter diesen Annahmen dauerhaft wirken, aber ihre Abhängigkeit von Wärmeeintrag, Hydraulik, Kosten und Modellform offenlegen.

Der Umfang umfasst einen Bericht nach dem Stand 10/2026 der offiziellen Vorgaben, ein reproduzierbares Rechenmodell, Sensitivitäts- und Kostenanalysen, einen Alternativenvergleich, eine fertige Präsentation mit Sprechtext und Video, eine dokumentierte Zeitprobe, adversariale Juryfragen, formale Prüfungen sowie vollständige Herkunfts- und Reviewnachweise.

## Falsifizierbares Abnahmekriterium

Die Arbeit ist intern abnahmebereit, wenn auf einem Commit beide vorgeschriebenen Council-Mitglieder unabhängig jedes Bewertungskriterium und beide Bereitschaftsteile mit mindestens 9/10 bewerten. Alle Befunde müssen durch eine nachvollziehbare Änderung oder eine belegte Zurückweisung geschlossen sein. Die Berechnungen, automatischen Prüfungen und Sichtprüfungen der tatsächlich gerenderten PDF- und Videodateien müssen auf genau diesem Commit bestehen. Ein leerer Platzhalter, ein fehlendes Finalvideo oder eine nicht geprüfte Ausgabe gilt nicht als bestanden.

Council-Konsens ist keine Garantie für eine Jurybewertung oder einen Wettbewerbserfolg. Eine echte menschliche Präsentation wird nicht behauptet, solange keine stattgefunden hat.

## Strenge und Entscheidungen

Die Strenge ist hoch, weil physikalische Dauerhaftigkeit, Umweltwirkungen, Wirtschaftlichkeit und formale Abgabefähigkeit zusammenwirken. Lokale Dateien und private Git-Commits sind reversibel. Eine öffentliche Veröffentlichung oder Wettbewerbseinreichung findet nicht statt.

Die Arbeit gliedert sich in kleine, einzeln prüfbare Einheiten. Zuerst werden Quellen und Annahmen fixiert. Danach folgen mehrere physikalisch verschiedene Hypothesen, ein gemeinsames Berechnungsmodell, der Bericht, die Finalrundenmaterialien und die eingefrorenen Reviews. Jede Einheit endet mit einem nachvollziehbaren Befund. `decisions.tsv` protokolliert Entscheidungen und ihre Belege.

## Prüfkette

1. Ein reproduzierbarer Modelllauf erzeugt alle berichteten Zahlen, Tabellen und wissenschaftlichen Abbildungen aus versionierten Eingaben.
2. Analytische Grenzfälle, Energiebilanzen, Einheiten, Gitter- und Zeitschrittstudien sowie unabhängige Rückrechnungen prüfen das Modell.
3. Ein Dokumentenbuild erzeugt Bericht und Präsentation. PDF-Seiten und Folien werden als PNG gerendert und einzeln sichtbar geprüft.
4. Das Video wird aus den fertigen Folien und der vertonten Sprechfassung erzeugt. Dauer, Ton, Bildfolge und Dateiintegrität werden an der MP4-Datei geprüft.
5. Formale Prüfungen kontrollieren Seitenzahl, Seitenformat, Ränder, Schriftgröße, Querverweise, Literatur, Anonymität, Dateinamen und Videodauer.
6. Erst danach wird ein Commit mit Dateihashes eingefroren und beiden Reviewern übergeben.
7. Jeder Befund erhält eine Korrektur oder eine begründete Zurückweisung. Anschließend werden alle betroffenen Berechnungen und Renderprüfungen wiederholt und eine neue Revision unabhängig reviewt.

## Recherche und Rollen

Drei getrennte Recherchestränge behandeln Regeln und Layout, physikalische Grundlagen sowie Technik, Kosten und Umwelt. Ihre Ergebnisse sind Arbeitsnotizen, keine Council-Stimmen. Ein gesonderter Schreiblauf synthetisiert die Notizen. Der implementierende Agent prüft und korrigiert jede übernommene Aussage anhand der Originalquelle und der Modellausgaben.

Die Council-Mitglieder arbeiten in jeder Runde read-only, getrennt und ohne Zugriff auf die Bewertung des jeweils anderen Mitglieds. Sie erhalten dasselbe vollständige Paket und dieselbe Bewertungsrubrik.
