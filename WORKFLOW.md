# Arbeits- und Prüfplan

## Ziel und Umfang

Das Paket beantwortet die gestellte Blautopf-Aufgabe auf Deutsch. Vulkanische Aktivität und die Zehnjahresprognose sind Szenarioannahmen. Die Lösung muss unter diesen Annahmen dauerhaft wirken, aber ihre Abhängigkeit von Wärmeeintrag, Hydraulik, Kosten und Modellform offenlegen.

Nach der Nutzerkorrektur umfasst das Produkt nur den Research Paper nach dem Stand 10/2026 der offiziellen Vorgaben, sein reproduzierbares Rechenmodell, Sensitivitäts- und Kostenanalysen, einen Alternativenvergleich, formale Prüfungen sowie vollständige Herkunfts- und Reviewnachweise. Die älteren Präsentations- und Finaldateien bleiben historische Arbeitsstände und werden nicht weiterentwickelt.

## Falsifizierbares Abnahmekriterium

Die fachliche Arbeit ist intern abnahmebereit, wenn auf einem Commit beide vorgeschriebenen Council-Mitglieder unabhängig jedes verbleibende Bewertungskriterium mit mindestens 9/10 bewerten. Das sind die Kriterien 1 bis 6, 8 bis 11 und 12a. Alle Befunde müssen durch eine nachvollziehbare Änderung oder eine belegte Zurückweisung geschlossen sein. Die Berechnungen, automatischen Prüfungen und Sichtprüfungen der tatsächlich gerenderten PDF müssen auf genau diesem Commit bestehen.

Nach den fachlichen Runden prüft ein eigener Council-Lauf ausschließlich das Design desselben Research Paper. Auch dieser Lauf muss auf einem eingefrorenen Commit ohne bekannte sachliche oder visuelle Mängel mindestens 9/10 von beiden Reviewern erreichen. Kriterium 12b und die Präsentation gehören nicht mehr zum Lieferumfang.

Council-Konsens ist keine Garantie für eine Jurybewertung oder einen Wettbewerbserfolg. Fehlende Standort-, Netz-, Hersteller- und Karstdaten werden nicht als erledigte externe Nachweise ausgegeben.

## Strenge und Entscheidungen

Die Strenge ist hoch, weil physikalische Dauerhaftigkeit, Umweltwirkungen, Wirtschaftlichkeit und formale Abgabefähigkeit zusammenwirken. Lokale Dateien und private Git-Commits sind reversibel. Eine öffentliche Veröffentlichung oder Wettbewerbseinreichung findet nicht statt.

Die Arbeit gliedert sich in kleine, einzeln prüfbare Einheiten. Zuerst werden Quellen und Annahmen fixiert. Danach folgen mehrere physikalisch verschiedene Hypothesen, ein gemeinsames Berechnungsmodell, der Research Paper und die eingefrorenen Reviews. Jede Einheit endet mit einem nachvollziehbaren Befund. `decisions.tsv` protokolliert Entscheidungen und ihre Belege.

## Prüfkette

1. Ein reproduzierbarer Modelllauf erzeugt alle berichteten Zahlen, Tabellen und wissenschaftlichen Abbildungen aus versionierten Eingaben.
2. Analytische Grenzfälle, Energiebilanzen, Einheiten, Gitter- und Zeitschrittstudien sowie unabhängige Rückrechnungen prüfen das Modell.
3. Der Dokumentenbuild erzeugt den Research Paper. Alle PDF-Seiten werden als PNG gerendert und einzeln sichtbar geprüft.
4. Formale Prüfungen kontrollieren Seitenzahl, Seitenformat, Ränder, Schriftgröße, Querverweise, Literatur, Anonymität und Dateinamen.
5. Eine frische Archivkopie muss Modell, PDF und Seitenbilder reproduzieren.
6. Erst danach wird ein Commit mit Dateihashes eingefroren und beiden Reviewern übergeben.
7. Jeder Befund erhält eine Korrektur oder eine begründete Zurückweisung. Anschließend werden alle betroffenen Berechnungen und Renderprüfungen wiederholt und eine neue Revision unabhängig reviewt.

## Recherche und Rollen

Drei getrennte Recherchestränge behandeln Regeln und Layout, physikalische Grundlagen sowie Technik, Kosten und Umwelt. Ihre Ergebnisse sind Arbeitsnotizen, keine Council-Stimmen. Ein gesonderter Schreiblauf synthetisiert die Notizen. Der implementierende Agent prüft und korrigiert jede übernommene Aussage anhand der Originalquelle und der Modellausgaben.

Die Council-Mitglieder arbeiten in jeder Runde read-only, getrennt und ohne Zugriff auf die Bewertung des jeweils anderen Mitglieds. Sie erhalten dasselbe vollständige Paket und dieselbe Bewertungsrubrik.
