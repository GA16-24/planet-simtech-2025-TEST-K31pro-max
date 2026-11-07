# Layoutvergleich mit D4RT

Die vom Nutzer genannte [D4RT-Arbeit](https://storage.googleapis.com/d4rt_assets/D4RT_paper.pdf) ist ausschließlich ein visueller Qualitätsmaßstab. Ihre wissenschaftlichen Inhalte werden nicht verwendet.

## Übernommene Gestaltungsprinzipien

- Zweispaltiger Textsatz mit kompakten, ausrichteten Abbildungen.
- Times-kompatible Serifenschrift mit passendem Mathematiksatz.
- Hierarchie durch Schriftgewicht und wenige Größenstufen statt dekorativer Farbflächen.
- Erklärende Bildunterschriften unter den Abbildungen.
- Tabellen mit horizontalen Linien, ohne vertikale Kästen, mit einheitlichen Dezimalstellen und sparsamer blauer Hervorhebung.
- Numerische Quellenverweise direkt im Text.
- Zurückhaltendes Blau nur für funktionale Akzente und Datenreihen.

## Bewusst nicht übernommene Werte

D4RT verwendet US Letter, etwa 20,7 mm Seitenrand, 10 pt Fließtext und kleinere Tabellen- und Literaturtexte. Diese Werte verletzen die aktuellen PlaNeT-Vorgaben. Der Bericht verwendet A4, 25 mm Rand und 12 pt auch für Tabellen, Bildunterschriften, Fußnoten und Literatur. Die Spalten sind 76 mm breit und durch 8 mm getrennt. Der Zeilenabstand beträgt 14,4 pt.

Der Qualitätsvergleich betrifft visuelle Ordnung, Konsistenz, Abbildungsintegration und Typografie. Er rechtfertigt keine Abweichung von Seitenformat, Schriftgröße, Anonymität oder Seitenbudget. Die konkrete Umsetzung steht in `report/preamble.tex` und wird an der gerenderten PDF-Datei geprüft.

## Prüfbare Referenzbilder

- Originalquelle: `sources/D4RT_paper.pdf`
- `review/rendered/d4rt_page01.png`
- `review/rendered/d4rt_page02.png`
- `review/rendered/d4rt_page06.png`

Die Bilder werden direkt neben den gerenderten Berichtsseiten geprüft. D4RT nutzt die Seitenfläche insbesondere bei großen Abbildungen und breiten Tabellen dichter. Der Bericht übernimmt diese Integrationsweise, ohne seine Schriftgrade oder Seitenränder zu verkleinern. Überschriften bleiben vor den zugehörigen Inhalten, Legenden stehen außerhalb der Datenflächen, und Gleichungsnummern stehen neben den Gleichungen. Der Vergleich bewertet keine fachlichen Aussagen der D4RT-Arbeit.
