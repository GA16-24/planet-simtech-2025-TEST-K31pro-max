# Verbindliche Modellkonfiguration

Auflösung über `orchestrator_capabilities` am 07.11.2026.

| Rolle | Anbieterinstanz | Exakte Modell-ID | Angezeigter Name | Reasoning-Einstellung | Status |
| --- | --- | --- | --- | --- | --- |
| Implementierung | `kimi` | `kimi-code/k3.1-pro` | K3.1 Pro | `thinking=max` | verfügbar, aktive Sitzung |
| Council A | `deepseekHarness` | `deepseek-account/deepseek-flash` | DeepSeek-V4.1-Flash | `reasoning_effort=max` | verfügbar, child tasks erlaubt |
| Council B | `kimi` | `kimi-code/k3.1-pro` | K3.1 Pro | `thinking=max` | verfügbar, child tasks erlaubt |

Für Kimi-Instanzen in Recherche, Implementierung und Review gilt durchgehend `thinking=max`. Für DeepSeek wird nur die ausdrücklich verlangte Flash-ID verwendet. `deepseek-account/deepseek-v4-pro` ist nicht zulässig und wird nicht aufgerufen.

Die Council-Läufe verwenden T3 `delegate_task` mit getrennten `clientRequestId`-Werten je Runde und Reviewer. In Runde 1 lief DeepSeek read-only mit `interactionMode=plan`. Der erste Kimi-Lauf mit demselben Modus wurde wegen blockierender Leseberechtigungen abgebrochen und nicht gewertet. Der Neustart verwendete `runtimeMode=full-access`, aber einen ausdrücklich read-only Auftrag ohne Dateiänderungen. Beide wertenden Läufe erhielten ausschließlich denselben Commit und keine Bewertung des anderen Reviewers. Ab Runde 2 verwenden beide Reviewer `runtimeMode=full-access` mit ausdrücklich read-only Auftrag, damit sie Prüfprogramme ohne Dateiänderungen ausführen können. Die Rollenbeschränkung bleibt `review`, Schreiben oder Bauen ist untersagt. Die Verfügbarkeit beider IDs wurde erneut über `orchestrator_capabilities` bestätigt. Council B ist wegen der Nutzervorgabe ein unabhängiger Same-Model-Kontext, keine externe oder menschliche Prüfung. Recherche- und Schreibläufe sind keine unabhängigen Council-Stimmen und werden gesondert im Provenienzprotokoll ausgewiesen. Die Punktzahlen einer früheren Runde werden nicht auf neue Revisionen übertragen.
