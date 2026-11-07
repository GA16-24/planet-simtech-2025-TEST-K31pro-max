# Medien- und Rechtenachweis

## Eigenständig erzeugte Inhalte

| Asset | Herkunft und Werkzeug | Rechte- und Quellenstatus |
| --- | --- | --- |
| Bericht und Folientext | Eigene Synthese aus Aufgabenprämissen, registrierten Fachquellen und Modellrechnungen mit Kimi K3.1 Pro | Keine früheren Wettbewerbsbeiträge oder deren Texte verwendet |
| Datenabbildungen | `model/run_all.py`, Python, NumPy und Matplotlib | Eigene Darstellung aus versionierten Eingaben, keine externen Bilddateien |
| Anlagenschema | LaTeX/TikZ in `presentation/main.tex` | Eigene technische Zeichnung |
| Schrift und Satz | Tectonic, TeX Gyre Termes, NewTX, Helvetica und Arial | Verwendung der LaTeX-Pakete und Systemschriftarten ohne eingebettete externe Markenlogos |
| Sprechtext | `presentation/narration.json` | Eigener Text aus dem Bericht |
| Vertonung | eSpeak NG 1.52.0, deutsche Stimme, anschließend FFmpeg-Loudnessnormalisierung | Synthetische Ausgabe aus eigenem Text, keine Sprach- oder Musikaufnahme Dritter |
| Musik und Soundeffekte | Nicht verwendet | Keine Musik- oder Tonrechte Dritter erforderlich |
| Fotos, Stockbilder und Logos | Nicht verwendet | Keine Bildrechte Dritter erforderlich |

## eSpeak NG

Das unveränderte Kommandozeilenprogramm eSpeak NG steht unter GPL version 3 oder später. Die offizielle Projektseite beschreibt die formantenbasierte Sprachsynthese und die Lizenz: https://github.com/espeak-ng/espeak-ng. Abruf: 07.11.2026.

Das Repository ruft das installierte Programm auf und enthält keine Kopie des Programmcodes. Die Audiodateien werden aus dem eigenen Sprechtext erzeugt. Die genaue Version und der Tempofaktor stehen in `presentation/speaker_notes.md` und `presentation/timings.json`. Die vollständige Sprachfassung ist synthetisch und wird nicht als menschliche Darbietung ausgegeben.

## Wissenschaftliche Quellen und Layoutreferenz

Fakten werden durch die nummerierten Quellen in `sources/registry.yml` und im Literaturverzeichnis belegt. D4RT wurde ausschließlich als visuelle Layoutreferenz gelesen. Seine PDF oder Abbildungen sind nicht Bestandteil von Bericht, Folien oder Video.

## Verbleibende menschliche Freigabe

Vor einer öffentlichen Aufführung müssen die einreichenden Teammitglieder die Nutzungsbedingungen aller eingesetzten Werkzeuge erneut prüfen und die Verwendung der synthetischen Stimme ausdrücklich freigeben. Eine juristische Prüfung wurde nicht durchgeführt. Diese Restaufgabe wird nicht als bereits erfolgte Rechteklärung ausgegeben.
