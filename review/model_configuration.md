# Verbindliche Modellkonfiguration

Auflösung über `orchestrator_capabilities` am 07.11.2026.

| Rolle | Anbieterinstanz | Exakte Modell-ID | Angezeigter Name | Reasoning-Einstellung | Status |
| --- | --- | --- | --- | --- | --- |
| Implementierung | `kimi` | `kimi-code/k3.1-pro` | K3.1 Pro | `thinking=max` | verfügbar, aktive Sitzung |
| Council A | `deepseekHarness` | `deepseek-account/deepseek-flash` | DeepSeek-V4.1-Flash | `reasoning_effort=max` | verfügbar, child tasks erlaubt |
| Council B | `kimi` | `kimi-code/k3.1-pro` | K3.1 Pro | `thinking=max` | verfügbar, child tasks erlaubt |

Für Kimi-Instanzen in Recherche, Implementierung und Review gilt durchgehend `thinking=max`. Für DeepSeek wird nur die ausdrücklich verlangte Flash-ID verwendet. `deepseek-account/deepseek-v4-pro` ist nicht zulässig und wird nicht aufgerufen.

Die Council-Läufe verwenden T3 `delegate_task`, getrennte `clientRequestId`-Werte je Runde und Reviewer sowie `interactionMode=plan` für read-only Prüfung. Recherche- und Schreibläufe sind keine unabhängigen Council-Stimmen und werden gesondert im Provenienzprotokoll ausgewiesen.
