# Provenienzprotokoll

## Unabhängigkeit und Ausgangslage

Das Repository begann am 07.11.2026 als leeres lokales Git-Repository. Das gleichnamige private GitHub-Repository wurde neu angelegt. Es wurden keine früheren Lösungen, Berichte, Präsentationen, Reviews oder Diskussionen zu PlaNeT SimTech geöffnet oder verwendet. Der Lösungsansatz wird aus dem Aufgabentext, allgemeinen wissenschaftlichen Quellen und eigenen Berechnungen abgeleitet. Eine weltweite Neuheit wird nicht behauptet.

## KI-Beteiligung

Kimi K3.1 Pro bei `thinking=max` übernimmt Regel- und Physikrecherche, Implementierung, Programmierung, Textentwürfe, Abbildungen und Redaktion. DeepSeek-V4.1-Flash bei `reasoning_effort=max` unterstützt die Technik- und Wirtschaftsrecherche. DeepSeek und ein separates Kimi-K3.1-Pro-Exemplar bei maximaler Reasoning-Stufe prüfen getrennt. Der zweite Kimi-Lauf ist ein unabhängiger Same-Model-Kontext, keine externe oder menschliche Prüfung. Weitere KI-Läufe zur Recherche oder Textsynthese werden hier mit Zweck und Modell ergänzt. Menschliche Teamarbeit oder menschliche Prüfung wird nicht behauptet.

Die Verantwortung für die Verwendung der Ausgaben bleibt bei der einreichenden menschlichen Person. Alle übernommenen Zahlen benötigen eine externe Primärquelle oder eine reproduzierbare Rechnung. KI-Aussagen allein gelten nicht als wissenschaftliche Belege.

Konkrete KI-Läufe:

| Zweck | Modell und Einstellung | Produkt | Prüfung |
| --- | --- | --- | --- |
| Regeln und Layout | Kimi K3.1 Pro, `thinking=max` | `research_notes/Blautopf Wärmeschutz/rules_and_format.md` | Abgleich mit offiziellen PDFs und D4RT-Seitenbild |
| Physik und Messdaten | Kimi K3.1 Pro, `thinking=max` | `research_notes/Blautopf Wärmeschutz/physical_system.md` | Quellen- und Einheitenabgleich durch den implementierenden Agenten |
| Technik und Wirtschaftlichkeit | DeepSeek-V4.1-Flash, `reasoning_effort=max` | `research_notes/Blautopf Wärmeschutz/engineering_economics.md` | Quellenabgleich, keine Council-Stimme |
| Hypothesen und Rechenmodell | Kimi K3.1 Pro, `thinking=max` | `docs/hypothesen.md`, `model/`, `output/model/` | Einheiten-, Energie-, Grenzfall- und Renderprüfungen |
| Berichtssynthese | Kimi K3.1 Pro, `thinking=max` | `reports/Blautopf Wärmeschutz.md` | Redaktion und Zahlenabgleich durch den implementierenden Agenten |
| Präsentation und Vertonung | Kimi K3.1 Pro, `thinking=max`, und eSpeak NG 1.52.0 | `presentation/`, PDF-Folien, Sprechtext und MP4 | Sichtprüfung, `ffprobe`, vollständige Decodierung und Laufzeitmessung |
| Council | DeepSeek-V4.1-Flash, `reasoning_effort=max`, und separates Kimi K3.1 Pro, `thinking=max` | Reviews nach Runden in `review/rounds/` | Getrennte read-only Bewertungen derselben eingefrorenen Revision. Council B ist ein unabhängiger Same-Model-Kontext, keine externe Prüfung |
| Übernahme und Paper-Revision | Kimi K3.1 Pro, `thinking=max` | Kostenkorrekturen, NIST-Sättigungsdaten, Bericht und Reviewpaket | 24 Modelltests, `make report`, Sichtprüfung aller 15 Seiten. Der verzögerte Schreibprozess des Ausgangslaufs wurde vor der Übernahme beendet |

## Quellen- und Entscheidungsregister

| Datum | Quelle oder Vorgang | Verwendung | Nachweis |
| --- | --- | --- | --- |
| 07.11.2026 | Vom Nutzer übergebener Aufgabentext | Szenarioprämissen und Lieferumfang | Gesprächsvorgabe, kein externer Faktenbeleg |
| 07.11.2026 | PlaNeT SimTech, Vorgaben für den Bericht, Stand 10/2026, https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Vorgaben-Bericht.pdf | Format, Aufbau, KI-Dokumentation, Zitierweise | `compliance/regeln.md` |
| 07.11.2026 | PlaNeT SimTech, Teilnahmebedingungen, Stand 10/2026, https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Teilnahmebedingungen.pdf | Anonymität, Teamregeln, schriftliche Runde und Finale | `compliance/regeln.md` |
| 07.11.2026 | PlaNeT SimTech, Startseite, https://www.planet-simtech.de/ | Ablauf und öffentlich genanntes Fünf-Minuten-Limit für das Finalvideo | `compliance/regeln.md` |
| 07.11.2026 | Zhang et al., D4RT, https://storage.googleapis.com/d4rt_assets/D4RT_paper.pdf | Ausschließlich visueller Vergleich für Satz, Abbildungen, Tabellen und Referenzstil gemäß Nutzerwunsch | `compliance/layout_referenz.md` |

Weitere wissenschaftliche Quellen werden mit Autor oder Institution, Titel, Jahr, URL oder DOI, Abrufdatum, verwendeter Größe und Fundstelle in den Recherchenotizen und im Literaturverzeichnis registriert.

## Berechnungen

Alle im Bericht und in der Präsentation verwendeten Modellwerte stammen aus `model/run_all.py` und den versionierten Eingaben unter `data/`. Der Lauf schreibt maschinenlesbare Ergebnisse und einen Manifest mit Dateihashes. Handgeschriebene Näherungswerte werden als solche gekennzeichnet und durch dieselben Gleichungen im Code geprüft.

## Menschliche Restaufgaben

Vor einer realen Einreichung müssen berechtigte Teammitglieder die wissenschaftlichen Inhalte prüfen, die Testkennung durch ihre offizielle Team-ID ersetzen, ihre Einverständniserklärungen abgeben, die Rechte am Paper bestätigen und selbst einreichen. Diese Schritte fanden im vorliegenden Lauf nicht statt. Die historischen Präsentationsdateien gehören nicht mehr zum Lieferumfang und werden nicht weiterentwickelt.
