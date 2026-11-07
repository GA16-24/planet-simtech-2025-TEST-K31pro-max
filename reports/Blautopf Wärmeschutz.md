# PlaNeT SimTech

> Arbeitsnotiz der Berichtssynthese. Die verbindliche, regelgeprüfte Fassung ist `output/pdf/TEST-K31pro-max.pdf`. Die Quellennummern dieser Arbeitsnotiz entsprechen ihrer eigenen Reihenfolge und sind nicht Teil des finalen Quellenregisters.

**Team-ID:** TEST-K31pro-max
**Datum:** 07.11.2026
**Aufgabe:** "Wie kann dauerhaft verhindert werden, dass das Wasser im Blautopf den Siedepunkt erreicht?"

## Blautopf dauerhaft vor dem Sieden bewahren

**Szenariobericht mit Auslegung, Alternativenprüfung und Unsicherheitsanalyse**

Vulkanische Tiefenerwärmung und die Prognose über zehn Jahre werden als Vorgaben des Szenarios behandelt. Sie sind keine durch diesen Bericht bestätigten Beobachtungen.

\newpage

# Blautopf dauerhaft vor dem Sieden bewahren

## Zusammenfassung

Der Blautopf ließe sich im vorgegebenen Szenario dauerhaft vor dem Sieden schützen, indem der gesamte betroffene Quellstrom in einer geschlossenen Leitung gekühlt wird, bevor er ins Freie gelangt. Das Wasser wird zuerst über große Luftkühler geführt. Danach senken Kältemaschinen seine Temperatur auf etwa 9 °C. Ein Mischbecken sorgt dafür, dass sich das zurückgeführte Wasser am ökologischen Kontrollpunkt höchstens um 1 °C pro Stunde ändert. Die Wärme darf nicht in denselben Wasserkreislauf zurückkehren.

Die Aufgabe ist vor allem eine Frage der Größe. Im zehnten Jahr müsste die Anlage **877,8 Megawatt Wärme abführen**. Diese Zahl folgt daraus, dass jede Sekunde 2,3 Kubikmeter Wasser von 100 auf 9 °C abgekühlt werden. Eine Rechnung, die nur das angenommene Wasservolumen des Beckens erwärmt, ergibt dagegen 0,0303 Megawatt. Sie übergeht den ständigen Zufluss heißen Wassers und taugt deshalb nicht zur Auslegung.

Der gewählte Entwurf besitzt sechs Module. Fünf tragen im Auslegungsjahr die volle Last, das sechste ersetzt ein ausgefallenes Modul. Ein Puffer von 8280 Kubikmetern entspricht einer Stunde des mittleren Quellstroms. Notstrom, Ersatzmodule und unabhängige Temperatur- und Druckmessungen sind nötig, weil ein einfacher Speicher bei einem Ausfall keine ausreichende Sicherheit bietet.

Die geschlossene Bauweise ist teuer, erhält aber den Wasserhaushalt. Die Szenarioschätzung ergibt **719 Millionen Euro Investition** und rund **138 Millionen Euro Betriebskosten im zehnten Jahr**. Die über 25 Jahre auf den Startzeitpunkt umgerechneten Gesamtkosten betragen **2,90 Milliarden Euro**. Verdunstungskühlung wäre billiger, würde aber jährlich 11,30 Millionen Kubikmeter Wasser verbrauchen und zusätzliche Hygienepflichten auslösen. Kaltwasserzumischung bräuchte eine nicht nachgewiesene Wasserquelle mit mehr als dem Zwanzigfachen des natürlichen Quellstroms.

Die Lösung gilt nur innerhalb einer klaren Hülle: höchstens 2,3 Kubikmeter pro Sekunde sind von der Erwärmung betroffen, ihre Temperatur steigt binnen zehn Jahren von 9 auf 100 °C und bleibt danach höchstens dort. Ein vollständig erwärmter Hochwasserstrom würde 12,48 Gigawatt Kühlung verlangen und ist nicht abgedeckt. Vor einem Bau müssen Messungen zeigen, welcher Karstast wie viel Wärme führt. Alle Kosten sind Schätzungen in Euro von 2026, keine Angebote. Eine Genehmigung, menschliche Prüfung oder tatsächliche Einreichung wird nicht behauptet.

## 1 Einleitung: Nicht das Sieden, sondern die Wärme ist das Problem

Wenn Dampf über dem Blautopf stünde, wäre das eigentliche Ziel bereits verfehlt. Sieden ist die späte physikalische Grenze. Für Organismen können weit niedrigere Temperaturen und auch ein zu schnelles Abkühlen schädlich sein [10,11]. Die Antwort muss deshalb mehr leisten als eine Abdeckung, die Dampfblasen verbirgt, oder ein höherer Druck, der das Sieden erst bei höherer Temperatur eintreten lässt. Die zugeführte Wärme muss das verbundene Wassersystem verlassen.

Der Blautopf entwässert einen Karstaquifer von etwa 165 km². Zwei verbundene Höhlenäste, Ur-Blau und Nord-Blau, sind bekannt. Die bekannte Systemlänge von etwa 15,5 km ist keine vollständige Länge des unterirdischen Strömungsnetzes [1]. Tracerversuche zeigen unterschiedliche Strömungsbereiche und Fließgeschwindigkeiten [4]. Eine Anlage, die nur eine bequem zugängliche Stelle kühlt, könnte deshalb den Wärmeträger verfehlen.

Gleichzeitig ist der Quellstrom gut dokumentiert. Für 1952 bis 2021 beträgt der mittlere Abfluss 2,3 m³/s, die Quantile für 10 und 90 Prozent liegen bei 0,7 und 4,7 m³/s [2]. Gerade dieser Durchfluss macht die Aufgabe anspruchsvoll. Er transportiert pro Kelvin Temperaturdifferenz etwa 9,65 Megawatt Energie. Ein kleiner Kältekreislauf an einem Teilstrom kann deshalb nur dann genügen, wenn Messungen beweisen, dass auch nur dieser kleine Teilstrom die Anomalie trägt.

Dieser Bericht vergleicht sieben Ansätze mit denselben physikalischen Regeln. Er wählt die hybride Vollstromkühlung H1, rechnet ihre Wärme- und Kostenbilanz und benennt die Beobachtungen, die Entwurf oder Erfolg widerlegen würden. Die vulkanische Ursache und die Zehnjahresprognose bleiben dabei Szenariovorgaben. Die zitierten Fachquellen belegen weder vulkanische Aktivität am Blautopf noch eine solche Prognose.

## 2 Datengrundlage, Annahmen und Rechenmethode

### 2.1 Messdaten und Szenarioannahmen bleiben getrennt

Die belastbarste Ausgangsgröße ist der Abfluss. Fan, Goeppert und Goldscheider werteten die LUBW-Station 76273 über 1952 bis 2021 aus. Sie berichten neben dem Mittelwert tägliche Werte von 0,1 bis 32,6 m³/s [2]. Das Landesamt für Geologie, Rohstoffe und Bergbau nennt für einen anderen Zeitraum und eine andere Statistik einen Hochwasserwert von 32,7 m³/s [1]. Diese Zahlen sind nicht austauschbar. Der Bericht verwendet 2,3 m³/s als Referenzstrom und 32,7 m³/s ausschließlich als separaten Hochwasser-Stresstest.

| Größe | Verwendeter Wert | Status und Herkunft |
| --- | ---: | --- |
| Mittlerer Quellabfluss | 2,3 m³/s | Ausgewertete Messreihe 1952 bis 2021 [2] |
| Historische Abflussquantile | 0,7 und 4,7 m³/s | 10- und 90-Prozent-Quantil derselben Reihe [2] |
| Beckentiefe | etwa 20,6 bis 22 m | Unterschiedliche Angaben, keine neue Vermessung [1,3] |
| Ausgangstemperatur | etwa 9 °C | Öffentliche Angabe ohne Sensorserie, Szenarioanker [3] |
| Tiefenerwärmung | linear 9 auf 100 °C in zehn Jahren | Reine Szenarioprämisse |
| Temperatur nach Jahr zehn | höchstens 100 °C | Konservative Begrenzung des Entwurfs |
| Betroffener Volumenstrom | höchstens 2,3 m³/s | Entwurfsannahme, kein gemessenes Maximum |
| Angenommenes Beckenvolumen | 25.000 m³ | Rechenannahme, keine Bathymetrie |
| Sommerliche Auslegungsluft | 35 °C | Technische Annahme |
| Rückführziel und Änderungsrate | 9 °C und höchstens 1 K/h | Eigenes ökologisches Regelziel auf Basis von [3,10] |

Die 9 °C der Stadt eignen sich als Ausgangswert, aber nicht als Ersatz für eine mehrjährige Temperaturmessung [3]. Ebenso fehlen aktuelle Beckenvermessung, vertikale Temperaturprofile, Astabflüsse und eine lokale Wärmebilanz der Wasseroberfläche. Diese Lücken werden nicht durch scheinbar genaue Nachkommastellen verdeckt.

### 2.2 Die Wärmebilanz bestimmt die Anlagengröße

Für Wasser ohne Phasenwechsel gilt die sensible Wärmeleistung

\[
\dot Q=\rho\,\dot V\,c_p\,(T_{ein}-T_{ziel}).
\]

Dabei sind \(\rho\) die Dichte, \(\dot V\) der betroffene Volumenstrom und \(c_p\) die spezifische Wärmekapazität. Die Gleichung folgt aus der Energieerhaltung und ist Bestandteil allgemeiner Wasser- und Wärmebilanzen [5,19]. Die Rechnung verwendet \(\rho=999,702\ \mathrm{kg/m^3}\) und \(c_p=4195,14\ \mathrm{J/(kg\,K)}\), Werte aus der NIST-Tabelle bei etwa 10 °C und 1,01325 bar [6]. Über den gesamten Temperaturpfad konstante Stoffwerte sind eine Näherung. Für eine spätere Detailauslegung sind temperatur- und druckabhängige IAPWS-Werte erforderlich [7].

Mit dem Mittelstrom ergibt sich der Wärmekapazitätsstrom

\[
C=\rho\,\dot V\,c_p=9,6459467\ \mathrm{MW/K}.
\]

Das Szenario bildet die Tiefentemperatur als

\[
T_q(t)=\min(9+9,1t,100)\quad [T_q\ \text{in °C},\ t\ \text{in Jahren}]
\]

ab. Die jährlich benötigte Kühlung ist \(C\,[T_q(t)-9]\) für positive Differenzen. Oberflächen- und Sohlverluste werden nicht als Gegenleistung angerechnet, weil Flächen, Windfunktion und lokale Austauschkoeffizienten unbekannt sind. Die allgemeine Flussenergiebilanz enthält Strahlung, Verdunstung, fühlbare Wärme und Sohlaustausch [5]. Diese Terme können die Rechnung später verbessern, werden hier aber nicht mit erfundenen Standortwerten gefüllt.

Zusätzlich muss an jedem Ort und zu jeder Zeit die Siedebedingung

\[
T+u_T<T_{sat}(p_{abs})-\Delta T_S
\]

gelten. Dabei ist \(u_T\) die Mess- und Modellunsicherheit, \(\Delta T_S\) eine noch mit der Behörde festzulegende Sicherheitsmarge. Der Siedepunkt hängt vom absoluten Druck ab [7,19]. Eine Oberflächenmessung allein beweist daher nicht, dass Tiefe, Steigleitung und Rückführung sicher bleiben.

### 2.3 Alternativen und Kosten folgen festen Regeln

Jeder Ansatz muss die gesamte Wärmebilanz schließen, bei 35 °C Außenluft auf 9 °C kühlen können und die Wärme außerhalb des verbundenen Grund- und Oberflächenwassers abgeben. Eine Umleitung, die das Becken selbst weiter erwärmt, oder eine bloße Erhöhung des Siedepunkts scheidet vor dem Kostenvergleich aus. Erst danach entscheiden Wasserbedarf, Umweltfolgen, Betriebssicherheit und Kosten.

Alle Geldbeträge sind **Szenarioschätzungen in Euro von 2026**. Der Barwert über 25 Jahre lautet

\[
K_0=\sum_{y=0}^{25}\frac{I_y+B_y+M_y+E_y}{(1+0,03)^y}.
\]

Hier sind \(I_y\) Investitionen, \(B_y\) Strom, Wasser und Hygiene abzüglich Wärmeerlösen, \(M_y\) Wartung und \(E_y\) Ersatzinvestitionen. Die Wartung beträgt jährlich 3 % der installierten Investition. In Jahr 15 werden 25 % der variablen Endausrüstung ersetzt. Der Strompreis beträgt 179 €/MWh, passend zum ausgewiesenen Preis von 17,9 ct/kWh für kleine und mittlere Industrie [15]. Für Wasser werden 0,50 €/m³ und für die Hygiene von H2 0,5 Mio. € pro Jahr angesetzt. Wärmeerlöse bleiben im Referenzfall null.

Der Stückpreis von 15 €/kW für Wärmetauscher orientiert sich am oberen Listenpreis eines einzelnen Plattenapparats, nicht an einer Anlage am Blautopf [16]. Kältemaschinen mit 500 €/kW, Trockenkühler mit 120 €/kW, Tiefbau, Steuerung, Notstrom und Zuschläge sind ausdrücklich Modellannahmen. Auf die variable Ausrüstung werden 20 % Leistungsreserve und anschließend 60 % Zuschlag für Engineering und Unvorhergesehenes gerechnet. Es gibt weder standortbezogene Geräteangebote noch Ausschreibungsergebnisse.

## 3 Ergebnis: H1 kühlt den vollen Strom in zwei Stufen

### 3.1 Warum 877,8 MW und nicht 0,0303 MW gebraucht werden

Im zehnten Jahr beträgt die Temperaturdifferenz 91 K. Die erforderliche Wärmeabfuhr ist daher

\[
\dot Q_{10}=999,702\cdot2,3\cdot4195,14\cdot91
=877,781\ \mathrm{MW}.
\]

Diese Zahl enthält noch keine Verdampfung des gesamten Wassers. Sie beschreibt allein die Abkühlung von 100 auf 9 °C. Die volle Anlage muss diese Leistung dauerhaft abführen, solange der heiße Zufluss fortdauert.

Die kleine Speichergrenze entsteht aus einer ganz anderen Frage. Welche durchschnittliche Leistung würde ein abgeschlossenes, angenommenes Beckenvolumen von 25.000 m³ innerhalb von zehn Jahren von 9 auf 100 °C erwärmen? Mit einem Modelljahr von 8760 Stunden gilt

\[
\dot Q_V=\frac{\rho Vc_p(100-9)}{10\cdot365\cdot86400}
=0,0302546\ \mathrm{MW}.
\]

Der Vollstromfall ist rund 29.000-mal größer. Die Speichergrenze ignoriert, dass bei 2,3 m³/s das angenommene Beckenvolumen rechnerisch alle 3,02 Stunden ersetzt wird. Sie beantwortet eine Speicherfrage ohne Zu- und Abfluss. Als alleinige Auslegungsgrundlage würde sie die dauerhafte Wärmezufuhr um mehr als vier Größenordnungen unterschätzen. Umgekehrt ist der Vollstromwert keine Messung der vulkanischen Leistung. Er ist die notwendige Kühlleistung unter der ausdrücklichen Annahme, dass der gesamte Mittelstrom mit 100 °C ankommt.

### 3.2 Trockenkühlung und Kältemaschinen teilen die Last

Bei 35 °C Außenluft und einer angenommenen Annäherung von 5 K kann die direkte Trockenkühlung das heiße Wasser im Auslegungsjahr auf 40 °C bringen. Sie übernimmt

\[
\dot Q_{trocken}=C(100-40)=578,757\ \mathrm{MW}.
\]

Erst die zweite Stufe kühlt von 40 auf 9 °C:

\[
\dot Q_{K}=C(40-9)=299,024\ \mathrm{MW}.
\]

Damit ist H1 keine kleine Wärmepumpe mit einem symbolischen Teilstrom. Die Anlage erfasst den vollen mittleren Quellstrom und kombiniert **578,8 MW direkte Kühlung mit 299,0 MW Kältemaschinenkühlung**. In kühleren Jahren übernehmen die Kältemaschinen einen größeren Anteil, weil die Trockenkühler unterhalb ihrer Annäherungstemperatur nicht weiter kühlen können.

Für die Kältemaschinen gilt \(COP_C=\dot Q_K/W_K\) und \(\dot Q_{Kond}=\dot Q_K+W_K\) [8]. Beim angenommenen \(COP_C=5\) beträgt ihre elektrische Leistung 59,805 MW. Die Kondensatoren müssen deshalb

\[
\dot Q_{Kond}=299,024+59,805=358,829\ \mathrm{MW}
\]

abgeben. Diese Wärme ist größer als die von den Kältemaschinen entzogene Wärme, weil die elektrische Antriebsenergie ebenfalls als Wärme anfällt. Wer nur die 299 MW nennt, unterschlägt einen wesentlichen Teil der Wärmesenke.

Mit 1,5 % Ventilatorhilfsleistung auf Trocken- und Kondensatorkühlung sowie 0,338 MW Pumpenleistung ergibt sich

\[
P_{el}=59,805+0,015(578,757+358,829)+0,338
=74,207\ \mathrm{MW}.
\]

Die vollständige externe Wärmesenke beträgt folglich

\[
\dot Q_{Senke}=578,757+358,829+14,064+0,338
=\dot Q_{10}+P_{el}=951,988\ \mathrm{MW}.
\]

Die Anlage muss also **952,0 MW an Luft oder an nachgewiesene externe Wärmeabnehmer** abgeben. Eine Rückführung in Blau, Blautopf oder denselben Aquifer würde die Bilanz aufheben und zusätzlich die Antriebsenergie eintragen [8]. Flächenbedarf, Luftführung, Rückverwirbelung, Geräusche und lokale Erwärmung sind noch nicht standortbezogen untersucht. Die geschlossene Bilanz beweist die Energieerhaltung, nicht die bauliche Machbarkeit an diesem Ort.

### 3.3 Sechs Module, Puffer und Notstrom sichern den Betrieb

Der Endausbau besitzt sechs thermisch gleiche Module. Fünf Module mit je **175,556 MW** decken die 877,781 MW Last. Das sechste Modul bildet die N+1-Reserve. Installiert sind damit 1053,337 MW, also 20 % mehr als benötigt. Bei einem Modulausfall bleiben fünf betriebsbereite Module für die volle Auslegungslast. Jedes lasttragende Modul führt etwa 0,46 m³/s. Bei einer angenommenen Rohrgeschwindigkeit von 1,2 m/s folgt

\[
d=\sqrt{\frac{4\cdot0,46}{\pi\cdot1,2}}=0,699\ \mathrm{m}.
\]

Dies ist ein hydraulischer Richtwert, noch keine Rohrklasse oder Druckauslegung. Die Entnahme erfolgt geschlossen und druckgehalten, bevor heißes Wasser bei fallendem Druck seinen lokalen Siedepunkt erreichen kann. Als hydrostatisches Beispiel ergeben 22 m Wassertiefe 3,17007 bar absoluten Druck und einen Sättigungspunkt von 135,413 °C [6,7]. Dieses Beispiel ersetzt kein Druckprofil im Höhlennetz.

Der Ausbau folgt der gemessenen Temperatur und dem erfassten Durchfluss. Jahr 0 umfasst Messinfrastruktur, Tiefbau und Steuerung mit 95 Mio. €. Im Modell steigt die benötigte Kühlung von 87,8 MW in Jahr 1 über 438,9 MW in Jahr 5 auf 877,8 MW in Jahr 10. Die Kostenrechnung enthält in jeder Stufe 20 % Reserve. In jeder Ausbaustufe wird die Last auf fünf aktive Stränge und einen reservierten Strang verteilt. Frühe Module sind kleiner und werden erweitert oder ersetzt. Jede Stufe muss vor dem prognostizierten Lastjahr getestet sein. Der Stufenplan spart gegenüber dem sofortigen Endausbau 112,4 Mio. € Barwert, darf aber keine Sicherheitsstufe verzögern.

Ein externer Misch- und Pufferspeicher von

\[
V_P=2,3\cdot3600=8280\ \mathrm{m^3}
\]

fasst eine Stunde des Referenzstroms. Dort wird die Rückführung so geregelt, dass die Temperaturänderung am ökologischen Kontrollpunkt höchstens 1 K/h beträgt. Dieser Wert folgt einer LAWA-Empfehlung für schnelle Temperaturänderungen und wird hier als eigenes Regelziel verwendet, nicht als automatisch geltende Blau-Grenze [10]. Die konkrete OGewV-Typzuordnung der Blau und die behördlich anzulegenden Temperaturgrenzen sind nicht bestätigt [11]. Der Puffer glättet die Rückkehr. Er kühlt nicht dauerhaft und ersetzt weder Reservemodul noch Notstrom.

Für einen Stromausfall ist eine Ersatzstromversorgung für die volle erforderliche Antriebsleistung von 74,2 MW vorzusehen. Der Kostenschätzposten enthält dafür 60 Mio. €. Aggregatzahl, Brennstoffvorrat, Überbrückungsdauer und Netzschutz sind noch nicht ausgelegt. Die Dringlichkeit zeigt ein vereinfachter Ausfalltest: Bei 100 °C heißem Zufluss, 25.000 m³ ideal gemischtem Becken und vollständigem Kühlungsausfall gilt \(T(t)=100+(9-100)e^{-t/\tau}\) mit \(\tau=3,019\) h. Bereits nach 0,389 h oder 23,3 Minuten erreicht das Modell 20 °C. Das ist kein prognostizierter realer Temperaturverlauf, aber ein Argument für automatische Fehlererkennung, redundante Messketten und sofort verfügbare Reserveleistung.

| Ausfall oder Störung | Technische Antwort | Verbleibende Grenze |
| --- | --- | --- |
| Ausfall eines Kühlmoduls | Isolierung, fünf Module übernehmen die Last | N+1 deckt nur einen Einzelausfall |
| Netz- oder Antriebsausfall | Unterbrechungsfreie Steuerung, Ersatzstrom für 74,2 MW | Dauer und gemeinsame Fehlerursachen ungeprüft |
| Ablagerung im Wärmetauscher | Druckdifferenz und Temperaturannäherung überwachen, reinigen | Wasserchemie und Foulingrate fehlen |
| Rückströmung der Abwärme | Luftführung, getrennte Senke, Temperatur- und Feuchtemessung | Kein standortbezogener Strömungsnachweis |
| Hochwasser, Treibgut, Sediment | Anlagen außerhalb des Beckens, erhöhte Elektrik, Absperrung | Keine Hochwasserlinie oder Baugrundprüfung |
| Kälteschock der Rückführung | 8280 m³ Puffer, Regelung auf höchstens 1 K/h | Mischung und Ökotyp müssen gemessen werden |
| Kältemittel- oder Sensorfehler | Lecksuche, Reservekreis, redundante Messkette | Ausfallwahrscheinlichkeiten nicht bekannt |

## 4 Alternativen: Der niedrigste Preis erhält nicht den Quellzustand

### 4.1 H1, H2 und H3 im gleichen Kostenmodell

Die folgende Tabelle verwendet identische Last, Laufzeit und Diskontierung. Die Investition enthält die jeweils modellierte Reserve. Die Betriebskosten beziehen sich auf Jahr 10 und enthalten keine neue Investition oder Ersatzinvestition. Alle Angaben sind Szenarioschätzungen in Euro von 2026.

| Größe im Auslegungsjahr | H1 Hybrid, Vollstrom | H2 Verdunstung | H3 Kaltwasserzumischung |
| --- | ---: | ---: | ---: |
| Erforderliche Wärmeabfuhr | 877,8 MW | 877,8 MW | 877,8 MW |
| Investition | 719,4 Mio. € | 283,9 Mio. € | 119,6 Mio. € |
| Elektrische Leistung | 74,2 MW | 13,5 MW | 12,8 MW |
| Strom pro Jahr | 650,1 GWh | 118,3 GWh | 112,4 GWh |
| Zusatzwasser pro Jahr | 0 m³ im Modell | 11,30 Mio. m³ | 1,650 Mrd. m³ |
| Betriebskosten in Jahr 10 | 137,9 Mio. € | 35,8 Mio. € | 848,8 Mio. € |
| Barwert über 25 Jahre | 2,897 Mrd. € | 0,780 Mrd. € | 11,478 Mrd. € |

Bei H1 setzen sich die jährlichen Betriebskosten aus 116,36 Mio. € Strom und 21,58 Mio. € Wartung zusammen. Der Investitionswert umfasst 15,8 Mio. € Wärmetauscher, 179,4 Mio. € Kältemaschinen, 135,0 Mio. € Trockenkühler und 60,0 Mio. € Notstrom. Hinzu kommen 95,0 Mio. € für Tiefbau und Steuerung sowie der 60-prozentige Zuschlag auf die variable Ausrüstung. Der gestaffelte Barwert liegt bei 2,8969 Mrd. € gegenüber 3,0093 Mrd. € bei sofortigem Endausbau.

H2 nutzt Verdunstungswärme. Mit einem Screeningwert von 2,45 MJ/kg folgt aus der vollen Last ein Wasserdampfstrom von 358,278 kg/s [5]. Der jährliche Ersatzwasserbedarf beträgt 11,302 Mio. m³. Bezogen auf das Quellsystem wären das 15,6 % des mittleren Abflusses. Herkunft und ökologische Verträglichkeit dieses Wassers sind nicht nachgewiesen. Auch das 9-°C-Ziel ist bei warmer, feuchter Luft ohne gemessene Feuchtkugeltemperatur nicht garantiert. Offene Verdunstungssysteme unterliegen Anforderungen zu Bau, Betrieb, Kontrolle, Laboruntersuchung, Protokoll und Prüfung nach der 42. BImSchV [12]. Aerosole, Schaum und Sichtwirkung kommen als Prüffragen hinzu. H2 ist im Modell am billigsten, aber kein gleichwertiger Ersatz für den wasser- und hygieneärmaren H1.

H3 mischt 5 °C kaltes Wasser zu. Aus der Energiebilanz folgt

\[
\dot V_k=\frac{877,781\cdot10^6}{999,702\cdot4195,14\cdot(9-5)}
=52,325\ \mathrm{m^3/s}.
\]

Das ist das 22,75-fache des natürlichen Mittelstroms als **zusätzlicher** Kaltwasserstrom. Die Mischung würde den Abfluss auf 54,625 m³/s erhöhen. Eine ganzjährig verfügbare, kalte und ökologisch verträgliche Quelle dieser Größe ist nicht belegt. Allein der angesetzte Wasserpreis erzeugt 825,06 Mio. € der jährlichen Betriebskosten. H3 scheidet deshalb trotz einfacher Technik aus.

H1 kostet bewusst mehr als H2. Der Aufpreis kauft einen geschlossenen Prozess ohne modellierten jährlichen Wasserverbrauch, ohne offenes Verdunstungssystem und mit trockener Wärmeabgabe. Die 42. BImSchV schließt bestimmte geschlossene Trockenkühler von ihrem Anwendungsbereich aus [12]. Das beseitigt nicht jede rechtliche Prüfung. Wasserentnahme, Rückleitung und Eingriffe können Erlaubnis oder Bewilligung nach dem WHG erfordern [13]. Schutzgebiet, Naturdenkmal, Biotop und das ab dem Blautopf beginnende FFH-Gebiet verlangen eine standortbezogene Prüfung [14]. Dieser Bericht stellt keine Genehmigung in Aussicht.

### 4.2 H4 bis H7 scheitern an Nachweis oder Wärmebilanz

| Ansatz | Entscheidender Befund | Bewertung |
| --- | --- | --- |
| H4 Wärmeentnahme oder Abschirmung im Karst | Die Wärme müsste in zwei verzweigten, nur teilweise bekannten Strömungssystemen vollständig erfasst werden [1,4]. | Forschungsoption, derzeit keine belastbare Dauerlösung |
| H5 Heißes Tiefenwasser am Becken vorbeiführen | Der Bypass kann die Blau entlasten, lässt das verbleibende Becken aber ohne geschlossene Wärmebilanz. | Alleine abgelehnt, nur mit vollständiger Kühlung kombinierbar |
| H6 Druck oder Abdeckung erhöht den Siedepunkt | Höherer Druck verschiebt \(T_{sat}(p)\), entzieht aber keine Wärme und erhöht die thermische Belastung [7,19]. | Aus Prinzip abgelehnt |
| H7 Passive Wärmerohre und Strahlung | Bei 10 W/(m² K) und 20 K Differenz wären 4,39 km² aktive Fläche nötig. Bei 35 °C Luft ist 9 °C passiv nicht erreichbar [9]. | Allenfalls Unterstützung in kalten Perioden |

H4 bliebe interessant, falls Tracer und Temperaturmessungen einen begrenzten heißen Ast nachweisen. Dann könnte eine kleinere Anlage näher an der Ursache arbeiten. Bohr- oder Verpressungsmaßnahmen im Karst bergen jedoch das Risiko neuer Strömungswege und Stoffeinträge. H5 kann als geschlossener Zulauf zu H1 dienen, nicht als alleinige Lösung. H6 behandelt das sichtbare Kriterium und verschlechtert die Energiebilanz. H7 kann Hilfsenergie sparen, besitzt aber bei sommerlicher Auslegungsluft keine ausreichende treibende Temperaturdifferenz.

## 5 Sensitivität, Unsicherheit und kritische Einordnung

### 5.1 Durchfluss und Teilstrom dominieren die Auslegung

Die deterministische Rechnung verändert jeweils eine Eingabe. Alle Kosten bleiben Szenarioschätzungen in Euro von 2026.

| Veränderung | Kühlleistung in Jahr 10 | Barwert über 25 Jahre |
| --- | ---: | ---: |
| Referenz | 877,8 MW | 2,897 Mrd. € |
| Abfluss 0,7 m³/s | 267,2 MW | 1,091 Mrd. € |
| Abfluss 4,7 m³/s | 1793,7 MW | 5,606 Mrd. € |
| Sieden nach 8 statt 10 Jahren | 877,8 MW | 2,961 Mrd. € |
| Sieden nach 12 statt 10 Jahren | 877,8 MW | 2,836 Mrd. € |
| Rückführziel 7 °C | 897,1 MW | 3,058 Mrd. € |
| Rückführziel 11 °C | 858,5 MW | 2,743 Mrd. € |

Ein früherer oder späterer Prognosezeitpunkt verändert die Endlast nicht, solange 100 °C als Obergrenze bleibt. Er verändert jedoch Bauzeit und Kostenpfad. Der Durchfluss wirkt unmittelbar auf die Leistung. Schon das historische 90-Prozent-Quantil würde bei vollständiger Erwärmung mehr als doppelt so viel Kühlung verlangen wie installiert. Deshalb ist die Obergrenze von 2,3 m³/s betroffenem Strom eine zu prüfende Annahme, kein konservativer hydrologischer Maximalwert.

Besonders wichtig ist der Anteil des Stroms, der die Anomalie tatsächlich trägt:

| Betroffener Anteil des Mittelstroms | Kühlleistung | Elektrische Leistung | Investition | Barwert |
| --- | ---: | ---: | ---: | ---: |
| 100 % | 877,8 MW | 74,2 MW | 719 Mio. € | 2,897 Mrd. € |
| 10 % | 87,8 MW | 7,4 MW | 85 Mio. € | 0,310 Mrd. € |
| 1 % | 8,8 MW | 0,74 MW | 12 Mio. € | 0,036 Mrd. € |
| 0,1 % | 0,88 MW | 0,074 MW | 2 Mio. € | 0,0049 Mrd. € |

Diese Tabelle erklärt sowohl die Versuchung als auch den Fehler einer kleinen Wärmepumpe. Ein kleiner Teilstrom wäre viel billiger, aber nur dann richtig, wenn die übrigen 99 oder 99,9 % nachweislich keine relevante Wärme in Becken oder Blau eintragen. Ohne diese Messung bleibt H1 die sichere Vollstromannahme. Die Kosten der kleinen Fälle skalieren Tiefbau und Leitungen mit Potenzgesetzen, Antrieb und Wärmeübertragung direkt mit dem Strom. Sie sind keine Zusicherung realer Baukosten.

### 5.2 Die stochastische Rechnung zeigt Streuung, nicht Sicherheit

Eine Monte-Carlo-Rechnung mit 10.000 Ziehungen variiert den Abfluss dreiecksverteilt zwischen 0,7 und 4,7 m³/s mit dem Modalwert 2,3 m³/s. Für die Kühlleistung ergeben sich ein 5-Prozent-Quantil von 479,7 MW, ein Median von 953,2 MW und ein 95-Prozent-Quantil von 1528,4 MW. Die Verteilung ist eine Rechenannahme über historische Quantile, keine Prognoseverteilung des vulkanischen Szenarios.

Für die Kosten werden zusätzlich der COP zwischen 3,0 und 6,5 sowie ein lognormaler Investitionsfaktor mit Sigma 0,30 variiert. Der Barwert liegt im 5- bis 95-Prozent-Bereich zwischen 2,363 und 3,814 Mrd. €, der Median beträgt 2,948 Mrd. €. Diese Kostenquantile koppeln den zufälligen Abfluss nicht erneut an die jährlichen Lastreihen. Auch Wetter, betroffener Stromanteil, Temperaturpfad, Wärmesenkenrückströmung und Verfügbarkeit fehlen in der gemeinsamen Verteilung. Die Quantile sind deshalb keine vollständige Risikoaussage und keine 95-prozentige Garantie.

Weitere Unsicherheiten bleiben modellstrukturell. Die Rechnung nutzt konstante Stoffwerte für Wasser, vernachlässigt natürliche Wärmeverluste und Gewinne, setzt einen idealen Temperaturverlauf und kennt keine Schichtung. Der COP von 5 ist eine Annahme, keine Herstellerkurve. Die jährliche Stromrechnung entspricht 8760 Betriebsstunden bei voller jeweiliger Last und enthält damit keine zusätzlichen Abschaltungen. Wartung und Reserve mindern dieses Idealbild, ersetzen aber keine Verfügbarkeitssimulation. Auch Spülwasser, Erstbefüllung, Kältemittelverluste, Netzanschluss und Abbau der Anlage sind nicht vollständig bepreist.

### 5.3 Die Auslegungshülle ist Teil des Ergebnisses

Dauerhaft bedeutet hier unbegrenzter Betrieb mit Wartung innerhalb folgender Grenzen: Die Tiefentemperatur steigt linear von 9 auf 100 °C in zehn Jahren und bleibt danach höchstens 100 °C. Höchstens 2,3 m³/s sind betroffen. Die Anlage kann bei 35 °C Luft ihre volle Wärme an eine externe Senke abgeben. Der heiße Zufluss wird vor dem offenen Becken erfasst. Die ökologische Rückführung erreicht 9 °C und höchstens 1 K/h Änderung.

Außerhalb dieser Hülle gibt es keine Scheinzusage. Wenn die Temperatur nach Jahr zehn weiter steigt, wenn mehr als 2,3 m³/s erwärmt werden oder wenn Wärme zusätzlich im Becken eingetragen wird, muss die Anlage wachsen. Eine endliche Anlage kann keine unbegrenzt wachsende vulkanische Leistung beherrschen.

Der Hochwasser-Stresstest macht diese Grenze besonders deutlich. Würden unrealistisch konservative 32,7 m³/s vollständig von 100 auf 9 °C gekühlt, ergäben sich

\[
\dot Q_{HW}=877,781\frac{32,7}{2,3}=12.479,8\ \mathrm{MW}=12,48\ \mathrm{GW}.
\]

Diese Hülle deckt H1 nicht ab. Hochwasser könnte die Wärme auch verdünnen oder andere Karstäste aktivieren. Genau deshalb muss die Zuordnung von Anomalie, Ast und Abflussregime vor dem Bau gemessen werden. Der Stresstest darf weder verschwiegen noch als realistische Lastprognose missverstanden werden.

## 6 Nachweis, Falsifikation und Verbesserung mit mehr Zeit

### 6.1 Messungen müssen die richtige Größe widerlegen können

Vor der Endauslegung sind synchronisierte Temperatur-, Druck-, Leitfähigkeits- und Durchflussmessungen in Ur-Blau, Nord-Blau, am Höhleneingang, in mehreren Beckentiefen, am Ausfluss und entlang der Blau erforderlich. Wetterstation und Referenzlogger trennen atmosphärische von unterirdischer Erwärmung. Tracerversuche können die beteiligten Äste und Laufzeiten prüfen [4]. Faseroptische Temperaturmessung kann räumliche Anomalien eingrenzen, braucht aber Kalibrierung und hydraulische Daten [18]. Mindestens ein vollständiger Jahresgang mit Niedrigwasser, Sturm und Schneeschmelze sollte die Kalibrierung tragen. Für Regelung und Drucksicherheit sind Messintervalle von höchstens 15 Minuten sinnvoll, sicherheitsrelevante Vorgänge brauchen schnellere Messung.

Der Erfolg wird an mehreren unabhängigen Bilanzen geprüft. Der Wärmetauscher muss aus eigener Durchfluss- und Temperaturmessung die berechnete Kühlleistung nachweisen. Stromzähler müssen die angesetzte Antriebsleistung bestätigen. Luft- oder Wärmenetzmessungen müssen die externe Senke schließen. Temperatur und Druck an allen kritischen Punkten müssen die Siedemarge einhalten. Am ökologischen Kontrollpunkt gelten zusätzlich Zieltemperatur, natürliche Referenzdifferenz und 1 K/h. Eine kühle Oberfläche allein beweist nichts über Tiefe oder Fluss.

Die Auslegung ist zu verwerfen oder zu vergrößern, wenn Messungen mehr als 2,3 m³/s betroffenen Strom, Temperaturen über 100 °C nach Jahr zehn oder eine wesentliche Hochwasserbeteiligung zeigen. Sie darf verkleinert werden, wenn reproduzierbare Messungen einen eng begrenzten heißen Ast belegen. Der Erfolg ist falsifiziert, wenn die vereinbarte Siedemarge verletzt wird, das 9-°C-Ziel dauerhaft verfehlt wird, die Rückführänderung 1 K/h überschreitet oder abgegebene Wärme nachweislich in denselben Wasserkreislauf zurückkehrt. Ein Modell, das einen späteren Messzeitraum nicht vorhersagt, ist für die Auslegung ebenfalls verworfen.

### 6.2 Mit mehr Zeit würde zuerst die Unsicherheit kleiner

Der nächste Arbeitsschritt wäre kein größeres Rechenmodell, sondern ein Messprogramm. Eine aktuelle Bathymetrie, zwei unabhängige Temperaturketten, Astabflüsse, Druckprofile und Wasserchemie würden die wichtigsten Annahmen prüfen. Ein Pilotmodul mit Tracer- und Lastwechselversuchen könnte Wärmeübertragung, Durchmischung, Fouling und reale COP-Werte messen. Danach wären IAPWS-Stoffwerte, ein geschichtetes Beckenmodell und gekoppelte Karst-, Fluss- und Wetterbilanzen sinnvoll [5,7].

Für die Wärmesenke wären Standortvarianten, Luftströmung, Lärm, Schattenwurf und Netzanschluss zu untersuchen. Die Technischen Werke Blaubeuren betreiben ein Wärmenetz in der Altstadt, dessen Umbau und Erweiterung geplant sind [17]. Eine Wärmenutzung könnte Kosten und direkte Luftabgabe senken. Ohne Jahreslastgang, Rücklauftemperatur und Anschlusskapazität wird dafür kein Erlös angerechnet. Ebenso fehlen Herstellerkennfelder, belastbare Baukosten, Notstromdauer, Zuverlässigkeitsdaten, ökologische Typzuordnung und behördliche Bewertung. Erst diese Arbeiten könnten aus dem rechnerisch geschlossenen Entwurf ein prüfbares Projekt machen.

## 7 Schlussfolgerung

Die gestellte Frage hat eine eindeutige physikalische Antwort: Das Wasser muss vor dem Druckabfall und vor dem Eintritt ins offene Becken vollständig gekühlt werden, und die entzogene Wärme muss dauerhaft außerhalb des verbundenen Wassersystems bleiben. Unter den geprüften Ansätzen erfüllt H1 diese Bedingung ohne zusätzlichen jährlichen Wasserbedarf im Modell. Die Vollstromauslegung benötigt 877,8 MW Kühlung, 74,2 MW elektrische Leistung und eine 952,0-MW-Senke. Sechs Module, davon eines in Reserve, ein einstündiger Puffer und Ersatzstrom machen daraus einen betreibbaren Szenarioentwurf.

Die höheren Kosten von H1 sind damit keine technische Unachtsamkeit, sondern der Preis für geschlossene Wasserführung und trockene Wärmeabgabe. Entscheidend bleibt jedoch die Beweislage. Solange der betroffene Stromanteil, die lokale Wärmesenke und die Hochwasserantwort nicht gemessen sind, ist die Anlagengröße eine begründete Annahme, keine Baufreigabe. Mit mehr Zeit sollten Messungen zuerst klären, ob H1 verkleinert werden darf oder vergrößert werden muss. Genau diese Offenheit macht den Entwurf überprüfbar.

\newpage

## Literaturverzeichnis

[1] Landesamt für Geologie, Rohstoffe und Bergbau Baden-Württemberg: Regionalbeschreibung Mittlere Alb, Fallbeispiele zum Blautopf. https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele. Abruf: 07.11.2026.

[2] Fan, X.; Goeppert, N.; Goldscheider, N. (2023): Quantifying the historic and future response of karst spring discharge to climate variability and change at a snow-influenced temperate catchment in central Europe. Hydrogeology Journal 31, 2213-2229. https://doi.org/10.1007/s10040-023-02703-9. Abruf: 07.11.2026.

[3] Stadt Blaubeuren: Geopoint Blautopf. https://www.blaubeuren.de/Geopoint-Blautopf. Abruf: 07.11.2026.

[4] Lauber, U.; Ufrecht, W.; Goldscheider, N. (2014): Spatially resolved information on karst conduit flow from in-cave dye tracing. Hydrology and Earth System Sciences 18, 435-445. https://doi.org/10.5194/hess-18-435-2014. Abruf: 07.11.2026.

[5] Ouellet, V.; Caissie, D. (2023): Towards a better understanding of the evaporative cooling of rivers: case study for the Little Southwest Miramichi River (New Brunswick, Canada). Canadian Water Resources Journal 48, 189-205. https://doi.org/10.1080/07011784.2023.2177196. Offen zugängliches Preprint: https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf. Abruf: 07.11.2026.

[6] National Institute of Standards and Technology: NIST Chemistry WebBook, thermophysikalische Eigenschaften von Wasser, isobare Tabelle bei 1,01325 bar. https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Type=IsoBar&Digits=6&P=1.01325&TLow=0&THigh=100&TInc=10&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm. Isobare Tabelle für das Druckbeispiel bei 3,17007 bar: https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Digits=6&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm&Type=IsoBar&P=3.1700700760259997&TLow=130&THigh=140&TInc=1. Abruf: 07.11.2026.

[7] International Association for the Properties of Water and Steam: Revised Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, IF97-Rev. https://iapws.org/relguide/IF97-Rev.html. Abruf: 07.11.2026.

[8] OpenStax: University Physics Volume 2, Abschnitt 4.3, Refrigerators and Heat Pumps. https://openstax.org/books/university-physics-volume-2/pages/4-3-refrigerators-and-heat-pumps. Abruf: 07.11.2026.

[9] Bergman, T. L.; Lavine, A. S.; Incropera, F. P.; DeWitt, D. P.: Fundamentals of Heat and Mass Transfer, Kapitel 1, Wiley-Auszug. https://catalogimages.wiley.com/images/db/pdf/9781119382911.excerpt.pdf. Abruf: 07.11.2026.

[10] van Treeck, R.; Wolter, C. (2020): Temperaturempfindlichkeiten der Fischgemeinschaften in deutschen Fließgewässern, Überprüfung der Orientierungswerte für die Temperatur. LAWA-Projekt O 10.20. https://www.laenderfinanzierungsprogramm.de/static/LFP/Dateien/LAWA/AO/O_10.20_211119_Endbericht_O10.20_TempEmpf_Fische.pdf. Abruf: 07.11.2026.

[11] Bundesrepublik Deutschland: Oberflächengewässerverordnung 2016, Anlage 7, Anforderungen an die Wassertemperatur. https://www.gesetze-im-internet.de/ogewv_2016/anlage_7.html. Abruf: 07.11.2026.

[12] Bundesrepublik Deutschland: Zweiundvierzigste Verordnung zur Durchführung des Bundes-Immissionsschutzgesetzes, 42. BImSchV. https://www.gesetze-im-internet.de/bimschv_42/BJNR237900017.html. Abruf: 07.11.2026.

[13] Bundesrepublik Deutschland: Wasserhaushaltsgesetz, insbesondere §§ 8, 9, 12 und 27. https://www.gesetze-im-internet.de/whg_2009/. Abruf: 07.11.2026.

[14] Stadt Blaubeuren: Blautopf-Sanierung, Grundlagen Naturschutz. https://www.blautopf-sanierung.de/willkommen/Grundlagen/Naturschutz. Abruf: 07.11.2026.

[15] Bundesverband der Energie- und Wasserwirtschaft: BDEW-Strompreisanalyse, Preisangaben 2026. https://www.bdew.de/service/daten-und-grafiken/bdew-strompreisanalyse/. Abruf: 07.11.2026.

[16] tga-shop: Buderus SL333 Plattenwärmetauscher DN100 PN16, 601 bis 700 kW, Produktpreis und Listenpreis. https://tga-shop.de/Buderus-SL333-Plattenwaermetauscher-DN100-PN16-601-700-kW-70-Platten-7738300409/70001-7738300409. Abruf: 07.11.2026.

[17] Stadt Blaubeuren: Kommunale Wärmeplanung. https://www.blaubeuren.de/de/Aktuelles/Kommunale-Waermeplanung. Abruf: 07.11.2026.

[18] United States Environmental Protection Agency: Fiber Optic Distributed Temperature Sensing. https://www.epa.gov/environmental-geophysics/fiber-optic-distributed-temperature-sensing. Abruf: 07.11.2026.

[19] OpenStax: Chemistry 2e, Abschnitt 10.3, Phase Transitions. https://openstax.org/books/chemistry-2e/pages/10-3-phase-transitions. Abruf: 07.11.2026.

[20] PlaNeT SimTech: Vorgaben für den Bericht, Stand 10/2026. https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Vorgaben-Bericht.pdf. Abruf: 07.11.2026.

[21] PlaNeT SimTech: Teilnahmebedingungen, Stand 10/2026. https://www.planet-simtech.de/wp-content/uploads/2023/05/PlaNeT_Teilnahmebedingungen.pdf. Abruf: 07.11.2026.

## Anhang A: KI-Verwendung, Unabhängigkeit und Prüfstatus

Für den zugrunde liegenden Arbeitsstand wurden Kimi K3.1 Pro bei `thinking=max` für Rechercheunterstützung, Implementierung, Programmierung, Textentwürfe, Abbildungserzeugung und redaktionelle Änderungen verwendet. DeepSeek-V4.1-Flash und ein separates Exemplar von Kimi K3.1 Pro bei maximaler Reasoning-Stufe wirkten als KI-Reviewer. Der vorliegende Bericht wurde mit Kimi K3.1 Pro aus den Recherchenotizen, den versionierten Modellparametern und den berechneten Ergebnissen synthetisiert. Diese Verwendung geht über sprachliche Schliffhilfe hinaus und wird deshalb für den gesamten Bericht erklärt [20].

Fachliche Aussagen stützen sich auf die nummerierten Quellen oder auf im Haupttext nachvollziehbare Rechnungen. KI-Aussagen allein wurden nicht als wissenschaftliche Belege verwendet. Die Modellprüfung schließt die Energiebilanz, Stufenaufteilung, Wärmesenke, Verdunstungs- und Mischungsbilanz sowie den Test der Becken-Zeitfunktion ein. Diese Prüfungen sind Rechenkontrollen, keine Feldvalidierung.

Es fand keine menschliche fachliche Prüfung dieses Arbeitsstands statt. Die KI-Reviewer sind keine menschlichen Gutachter. Vor einer tatsächlichen Einreichung müssen berechtigte Teammitglieder sämtliche Inhalte prüfen, ihre offizielle Team-ID einsetzen, die erforderlichen Erklärungen abgeben und selbst einreichen [20,21]. Dieser Entwurf wurde nicht eingereicht. Standortbezogene Angebote, eine rechtliche Genehmigung, eine durchgeführte Lieferung und weltweite Neuheit werden nicht behauptet.

Es wurden keine früheren PlaNeT-SimTech-Einreichungen, Gewinnerberichte, Lösungszusammenfassungen, Reviews, Präsentationen, Videos, einschlägigen Diskussionen oder bestehenden aufgabenbezogenen Lösungsrepositories geöffnet oder verwendet. Der Ansatz wurde aus dem Aufgabentext, allgemeinen Fachquellen und eigenen Berechnungen entwickelt.
