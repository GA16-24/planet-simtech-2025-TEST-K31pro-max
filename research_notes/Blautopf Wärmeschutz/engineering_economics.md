# Engineering, economic, environmental and regulatory evidence for permanent cooling options at the Blautopf

Prepared 2026-11-07. All URLs were opened on 2026-11-07 unless stated otherwise. Volcanic activity and the ten-year forecast are treated as scenario premises, not as research questions. No prior PlaNeT SimTech submission, report, review, presentation, video or discussion was consulted, and the project exclusion log still records no exposure.

Evidence grades used below:

- A: statute, ordinance or official regulation text.
- B: government agency, utility association or peer-reviewed field measurement.
- C: manufacturer or vendor price, technical data sheet, or a literature compilation of such data.
- D: commercial advice site or my own engineering estimate.

## 1. Technologies that can remove, divert, dilute, export or avoid heat in a karst spring and connected river

### Takeaway
Seven technology families are technically available, and they differ far more in legal headroom and operating cost than in thermodynamics. The decisive physical fact is that the Blautopf moves about 2,300 kg of water per second at roughly 9 °C, so its thermal capacitance is close to 9.6 MW per kelvin. A 1 MW heat load shifts the spring temperature by about 0.1 K at mean flow. Dilution is therefore physically trivial and legally hard, while refrigeration is legally simple and energetically expensive.

### Cited Findings

**Site baseline.** The Blautopf is a 22 m deep funnel-shaped karst spring fed by a 160 km² catchment. Mean discharge is about 2,300 L/s, values above 30,000 L/s occur after heavy rain, and the water temperature is about 9 °C all year. [Stadt Blaubeuren, Geopoint Blautopf](https://www.blaubeuren.de/Geopoint-Blautopf) (grade B, municipal source, not a gauging station record).

**Thermal capacitance, own calculation.** Specific heat capacity of water at 10 °C is 4.191 kJ/(kg·K) [Engineering Toolbox, specific heat capacity of water](https://www.engineeringtoolbox.com/specific-heat-capacity-water-d_660.html) (grade C, standard engineering data). With 2,300 kg/s this gives 2,300 × 4.191 = 9,639 kW/K, or about 9.6 MW/K. The annual discharge follows as 2.3 m³/s × 31.54 × 10⁶ s ≈ 72.5 million m³/yr. Both are my calculations from the cited inputs.

**Mixing temperature versus heat load, own calculation from the two inputs above.**

| Heat load | ΔT at 2,300 L/s mean flow | ΔT at 500 L/s, hypothetical low flow |
| --- | --- | --- |
| 0.5 MW | 0.05 K | 0.24 K |
| 1 MW | 0.10 K | 0.48 K |
| 5 MW | 0.52 K | 2.4 K |
| 10 MW | 1.04 K | 4.8 K |
| 50 MW | 5.2 K | 24 K |
| 100 MW | 10.4 K | 48 K |

The 500 L/s column is a sensitivity case, not a measured low flow. No flow-duration curve was retrieved.

**Direct heat exchange and free cooling.** A gasketed plate heat exchanger rated 601 to 700 kW is listed at 6,418.18 EUR net, reduced from a list price of 8,952.68 EUR [tga-shop, Buderus SL333 plate heat exchanger](https://tga-shop.de/Buderus-SL333-Plattenwaermetauscher-DN100-PN16-601-700-kW-70-Platten-7738300409/70001-7738300409) (grade C, single vendor, 2026 price). That is about 9 to 11 EUR/kW net for the exchanger alone, or 13 to 15 EUR/kW at list price. With a 9 °C source, chilled water at roughly 11 to 13 °C is reachable by exchange alone for much of the year. The pumping penalty is small: 1 MW at a 2 K rise needs about 119 L/s, and at 1.5 bar loop pressure and 70% pump efficiency that is about 26 kW, or 2.6% of delivered cooling. This is my calculation, grade D.

**Heat pumps.** The Swiss Federal Office of Energy field programme monitored 24 large heat pump systems. Groundwater-source units ranged from JAZ 2.33 to 4.76 at the heat pump and 2.07 to 3.82 for the whole plant, against an overall mean of 3.51 and 2.89 [BFE, 16. Tagung des Forschungsprogramms Wärmepumpen, 2010, Hubacher, PDF](https://pubdb.bfe.admin.ch/de/publication/download/4978) (grade B, field measurement, 2010). The same study found a mean seasonal performance factor of 3.87 for single-building systems against 2.52 for multi-building systems with a local heat network, a gap of 1.35 [same source] (grade B). That gap matters if recovered heat is exported into a district network rather than used on site.

**Evaporative cooling and cooling towers.** The 42. BImSchV defines a Verdunstungskühlanlage as an installation that rejects heat to ambient air by evaporating water, and a Kühlturm as the natural-draft variant with more than 200 MW per air outlet [42. BImSchV § 2 Nr. 5 and Nr. 11](https://www.gesetze-im-internet.de/bimschv_42/BJNR237900017.html) (grade A). Water consumption follows from the latent heat: 2,429.8 kJ/kg at 30 °C [Engineering Toolbox, water properties at gas-liquid equilibrium](https://www.engineeringtoolbox.com/water-properties-d_1573.html) (grade C), so 1 kWh of rejected heat evaporates 3,600 / 2,429.8 = 1.48 kg. At 3 to 5 cycles of concentration the make-up water is 1.85 to 2.22 L/kWh. That is my calculation.

**Dry coolers and closed circuits.** The same ordinance explicitly excludes evaporative coolers where condensate formation by falling below dew point is possible, especially units with chillers, and heat exchangers that keep the process fluid in a closed loop and reject heat only through air-side heat transfer [42. BImSchV § 1 Abs. 2 Nr. 1 and Nr. 2](https://www.gesetze-im-internet.de/bimschv_42/BJNR237900017.html) (grade A). A closed dry cooler therefore avoids the entire Legionella regime described in section 3. This is the single most consequential design choice in the technology comparison.

**Bypass, diversion and dilution.** Taking water from or diverting it within a surface water body is a Benutzung under § 9 Abs. 1 Nr. 1 WHG, and introducing substances or discharging into a water body is a Benutzung under § 9 Abs. 1 Nr. 4 WHG [WHG § 9](https://www.gesetze-im-internet.de/whg_2009/__9.html) (grade A). Measures capable of causing lasting or not merely insignificant adverse change to water quality are also a Benutzung under § 9 Abs. 2 Nr. 2 [same source] (grade A). Any of these needs an Erlaubnis or Bewilligung under § 8 Abs. 1 WHG [WHG § 8](https://www.gesetze-im-internet.de/whg_2009/__8.html) (grade A). A bypass channel or a dilution intake is therefore a permitted use, not an exempt one.

**Groundwater and deep borehole heat exchange.** Extracting or lifting groundwater is a Benutzung under § 9 Abs. 1 Nr. 5 WHG [WHG § 9](https://www.gesetze-im-internet.de/whg_2009/__9.html) (grade A). The Baden-Württemberg geothermal guide requires assessment against VDI 4640 Blatt 1 and 2 and warns that high-permeability aquifers and high groundwater velocities make drilling and grouting risky, with loss of drilling fluid and cement intrusion as the specific hazards [Leitfaden zur Nutzung von Erdwärme mit Erdwärmesonden, Baden-Württemberg, PDF](https://www.waermepumpe.de/fileadmin/user_upload/waermepumpe/02_Waermepumpe/Leitfaden_Nutzung_von_Erdwaerme_Baden-Wuerttemberg.pdf) (grade B, but the document dates from 2015 and cites the pre-2010 WHG paragraph numbering, so its legal citations must be re-checked against current law). A deep coaxial borehole heat exchanger is the same legal category with a larger drilling risk.

**Source-zone intervention.** The spring and the cave system sit inside a Landschaftsschutzgebiet, a Naturdenkmal and a mapped protected biotope, and the FFH area "Blau und Kleine Lauter" begins at the spring and runs to Ulm [Stadt Blaubeuren, Naturschutz](https://www.blautopf-sanierung.de/willkommen/Grundlagen/Naturschutz) (grade B, municipal source). Interventions in the cave or the spring throat would need an FFH-Verträglichkeitsabschätzung, as the municipality's own construction project required [same source] (grade A).

**Hybrid control.** No source is needed for the proposition that the options can be staged, and I label it as inference: free cooling first, heat pump or chiller second, evaporative or dry rejection only for peak load, dilution only as a bounded residual.

### Inferences
- Sort the options by physical effect, not by novelty. Dilution has the largest capacity per euro of equipment and the least legal headroom at the spring. Free cooling has the best energy ratio. Evaporative rejection has the lowest equipment cost per kW and the highest regulatory and water burden. Heat pumps create a revenue side only if a heat customer exists.
- Whether dilution is viable depends entirely on the scenario's heat load. Up to about 1 MW it disappears into the spring's thermal capacitance. At 100 MW it would raise the mean spring temperature by more than 10 K and fail any plausible ecological criterion. The comparison must therefore state the load first.
- Because the source is a stable 9 °C cold reservoir, the default cooling design should be exchange, not refrigeration. A chiller should be the peak and backup machine, not the base machine.
- The discharge range from 2,300 L/s to above 30,000 L/s is a factor greater than 13. Any in-stream structure must survive both the low-flow summer condition and the flood condition, which pushes design toward off-channel units with short, valved connections.
- The 42. BImSchV exclusion for closed dry coolers means the hygienically safest option is also the one with the least recurring compliance cost, at the price of a higher electricity demand and a larger air-side footprint.

### Gaps
- No flow-duration curve for the Blautopf was retrieved, so MQ, MNQ and MHQ are unknown and the low-flow column above is hypothetical.
- No measured longitudinal temperature profile of the Blau and no mixing-zone study were found.
- No karst tracer data on travel times from the cave system to the spring were retrieved.
- No cost or performance data for a deep coaxial borehole heat exchanger at this site were found.
- The 2015 Baden-Württemberg guide is the best procedural source found, but it predates the current WG version and needs verification against the current statute.

## 2. Which investment and operating cost ranges can be justified?

### Takeaway
Only four cost anchors survived scrutiny: a 2026 vendor price for a 600 to 700 kW plate heat exchanger, 2026 drilling rates of 60 to 120 EUR/m, 2012 literature ranges of 75 to 350 EUR/kW for compression chillers, and the 2026 BDEW electricity tariffs. Everything else in this section is either an explicit estimate or a gap. I found no public tender award values and no cooling tower or deep-well quotations within this research window.

### Cited Findings

| Item | Range | Price year | Evidence type | Source |
| --- | --- | --- | --- | --- |
| Plate heat exchanger, 601 to 700 kW | 6,418 EUR net, 8,953 EUR list, so 9 to 15 EUR/kW | 2026 | Single vendor price, grade C | [tga-shop](https://tga-shop.de/Buderus-SL333-Plattenwaermetauscher-DN100-PN16-601-700-kW-70-Platten-7738300409/70001-7738300409) |
| Borehole heat exchanger drilling | 60 to 120 EUR/m | 2026 | Commercial estimate, grade D | [clever-bauen.de](https://www.clever-bauen.de/ratgeber/erdwaermepumpe-kosten/) |
| Borehole length, single-family house | 150 to 250 m | 2026 | Commercial estimate, grade D | [clever-bauen.de](https://www.clever-bauen.de/ratgeber/erdwaermepumpe-kosten/) |
| Complete brine-to-water heat pump, house scale | 25,000 to 45,000 EUR | 2026 | Commercial estimate, grade D | [clever-bauen.de](https://www.clever-bauen.de/ratgeber/erdwaermepumpe-kosten/) |
| Compression chiller | 75 to 125 EUR/kW cold typical, up to 350 EUR/kW in one source | 2012 | Literature compilation, grade C | [HAW Hamburg thesis, Table 5.6](https://reposit.haw-hamburg.de/bitstream/20.500.12738/5979/1/Bachelorthesis_Bez_Armin_20120618.pdf) |
| Absorption chiller | 250 to 1,800 EUR/kW cold | 2012 | Literature compilation, grade C | [same source](https://reposit.haw-hamburg.de/bitstream/20.500.12738/5979/1/Bachelorthesis_Bez_Armin_20120618.pdf) |
| Electricity, small and medium industry | 17.9 ct/kWh | 2026 | Utility association, grade B | [BDEW Strompreisanalyse](https://www.bdew.de/service/daten-und-grafiken/bdew-strompreisanalyse/) |
| Electricity, medium industry 20 to 70 GWh/a | 14.6 ct/kWh | H1 2026 | Utility association, grade B | [BDEW](https://www.bdew.de/service/daten-und-grafiken/bdew-strompreisanalyse/) |
| Electricity, large industry 70 to 150 GWh/a | 13.8 ct/kWh | H1 2026 | Utility association, grade B | [BDEW](https://www.bdew.de/service/daten-und-grafiken/bdew-strompreisanalyse/) |
| Electricity, households | 37.3 ct/kWh | 2026 | Utility association, grade B | [BDEW](https://www.bdew.de/service/daten-und-grafiken/bdew-strompreisanalyse/) |

The BDEW figures come with a useful decomposition for 2026 households: procurement and sales 15.4 ct/kWh, grid fees 9.2 ct/kWh, taxes and levies 12.6 ct/kWh [BDEW](https://www.bdew.de/service/daten-und-grafiken/bdew-strompreisanalyse/) (grade B). That decomposition is the right basis for sensitivity analysis, because a large industrial consumer pays a very different grid and levy share than a municipal building.

The 2012 chiller figures are equipment costs only and are not escalated. A 2026 comparison has to apply its own escalation index, and this note does not attempt one.

The 42. BImSchV creates recurring costs that are easy to miss in a CAPEX comparison. Operators of evaporative cooling installations must run internal checks at least every two weeks and laboratory tests for general colony count at least every three months, plus Legionella tests at least every three months, and monthly for cooling towers. They must keep a logbook for five years, register the installation within one month of first filling, and have it inspected by an expert or accredited inspection body every five years [42. BImSchV §§ 4, 7, 12, 13, 14](https://www.gesetze-im-internet.de/bimschv_42/BJNR237900017.html) (grade A). No unit prices for these services were found.

### Inferences
Worked example, my calculation, all labelled grade D: a 1 MW cooling load running 4,000 full-load hours per year delivers 4,000 MWh of cooling.

| Configuration | Electricity | Annual energy cost at 17.9 ct/kWh | Notes |
| --- | --- | --- | --- |
| Free cooling via plate heat exchanger, 2% pumping | 80 MWh | 14,300 EUR | Excludes water abstraction and permit costs |
| Chiller at COP 4.5 | 889 MWh | 159,000 EUR | Excludes recooling and maintenance |
| Chiller plus open cooling tower, 24 to 26% total | 960 to 1,040 MWh | 172,000 to 186,000 EUR | Adds 7,400 to 8,900 m³/yr make-up water at 1.85 to 2.22 L/kWh |
| Heat pump delivering 1 GWh heat at JAZ 3.5 | 286 MWh | 51,000 EUR | Heat cost about 51 EUR/MWh before capital recovery |

The spread between free cooling and a chiller is roughly a factor of eleven in electricity cost. That ratio dominates the operating economics of the whole comparison.

Capital recovery should follow the VDI 2067 annuity method, which the cited thesis uses for cooling systems [HAW Hamburg thesis](https://reposit.haw-hamburg.de/bitstream/20.500.12738/5979/1/Bachelorthesis_Bez_Armin_20120618.pdf) (grade C). The comparison in the main report should quote annualised cost, not CAPEX, or the low-CAPEX evaporative option will look better than it is.

### Gaps
- No public tender, award notice or bid opening result for a comparable cooling plant was retrieved.
- No cooling tower purchase price or installation price was found, so the table has no evaporative CAPEX row.
- No deep borehole heat exchanger cost was found.
- No civil works, building, or grid connection costs were found.
- The Baden-Württemberg Wasserentnahmeentgelt rate was not verified. The state portal page is JavaScript-only and returned no text.
- Water and wastewater prices for Blaubeuren were not retrieved, so the make-up water volumes above are unpriced.
- No maintenance contract prices for heat pumps, chillers or cooling towers were found.

## 3. Failure modes, maintenance, ecology, water law and nature conservation in Blaubeuren and Baden-Württemberg

### Takeaway
The binding constraints on this site are legal and ecological, not thermal. The spring sits inside a stack of protected designations, the Blau is a habitat for Groppe and Bachneunauge, and any discharge or diversion needs a water law permit that can be refused outright if harmful changes are expected. Open evaporative systems add a full hygienic compliance regime on top, while closed dry coolers avoid it.

### Cited Findings

**Permit architecture.** A water body use requires an Erlaubnis or Bewilligung unless a statute says otherwise [WHG § 8 Abs. 1](https://www.gesetze-im-internet.de/whg_2009/__8.html) (grade A). The permit must be refused if harmful water changes are expected that cannot be avoided or compensated by conditions, or if other statutory requirements conflict [WHG § 12 Abs. 1](https://www.gesetze-im-internet.de/whg_2009/__12.html) (grade A). Surface waters must be managed so that their ecological and chemical status does not deteriorate and so that good status is achieved [WHG § 27 Abs. 1](https://www.gesetze-im-internet.de/whg_2009/__27.html) (grade A). This is the legal core of the whole comparison. A thermal discharge is not judged on its own. It is judged against the status of the receiving water body.

**Temperature in the surface water ordinance.** Water temperature is one of the general physico-chemical quality components used to classify ecological status in flowing waters [OGewV Anlage 3](https://www.gesetze-im-internet.de/ogewv_2016/anlage_3.html) (grade A). That annex lists the parameter but sets no numeric limit, so the operative threshold for the Blau has to come from the permitting authority's site-specific assessment.

**Hygiene regime for evaporative systems.** Legionella threshold values are 100, 1,000 and 10,000 CFU per 100 mL for evaporative coolers and 500, 5,000 and 50,000 CFU per 100 mL for cooling towers [42. BImSchV Anlage 1](https://www.gesetze-im-internet.de/bimschv_42/BJNR237900017.html) (grade A). The operator must design against droplet carry-over with separators, avoid dead zones, allow full draining, and dose biocides [42. BImSchV § 3 Abs. 2](https://www.gesetze-im-internet.de/bimschv_42/BJNR237900017.html) (grade A). A risk assessment with a hygiene-qualified person is required before commissioning, and again after any change [42. BImSchV § 3 Abs. 4 and Abs. 6](https://www.gesetze-im-internet.de/bimschv_42/BJNR237900017.html) (grade A). None of this applies to the closed dry cooler excluded under § 1 Abs. 2 [same source] (grade A).

**Protected designations.** The area around the spring and the Blau lies in the Landschaftsschutzgebiet "Blaubeuren" and contains the Naturdenkmal "Blautopf" and the protected biotope "Waldbestand am Blautopf". The FFH area "Blau und Kleine Lauter" starts here and extends to Ulm. Protected species named by the municipality include bats, Groppe, Bachneunauge, Wasseramsel and Gebirgsstelze. The municipality's own construction project required a species protection report, an FFH compatibility assessment and ecological construction supervision, and it pauses work during bird breeding and fish spawning [Stadt Blaubeuren, Naturschutz](https://www.blautopf-sanierung.de/willkommen/Grundlagen/Naturschutz) (grade B, municipal source). This is direct evidence of the permitting standard that any in-stream cooling structure would face.

**Baden-Württemberg procedure for subsurface works.** The state guide describes a notification route under § 108 Abs. 4 WG: the lower water authority confirms receipt, and if it does not open a formal permit procedure within one month, the notifier may assume no permit obligation, with the simplified permit deemed granted under § 108 Abs. 4 Satz 2 WG. The guide also states that only water may be used as the heat carrier fluid in borehole heat exchangers [Leitfaden Erdwärme Baden-Württemberg, PDF](https://www.waermepumpe.de/fileadmin/user_upload/waermepumpe/02_Waermepumpe/Leitfaden_Nutzung_von_Erdwaerme_Baden-Wuerttemberg.pdf) (grade B, 2015 text, legal citations outdated). The procedural logic is useful as an analogy for borehole and deep-well options, but the paragraph numbering must be checked against the current WG before anyone relies on it.

**Karst-specific drilling hazard.** The same guide warns that in highly permeable aquifers and at high groundwater velocities, drilling fluid and cement can migrate through the borehole or the formation, which is the classic karst drilling failure [same source](https://www.waermepumpe.de/fileadmin/user_upload/waermepumpe/02_Waermepumpe/Leitfaden_Nutzung_von_Erdwaerme_Baden-Wuerttemberg.pdf) (grade B). The Blautopf catchment is Jurassic karst with a proven cave system, so this hazard is not theoretical here.

### Inferences

| Failure mode | Mechanism | Consequence | Mitigation | Grade |
| --- | --- | --- | --- | --- |
| Scaling and fouling of the exchanger | Carbonate-rich karst water, temperature rise on the hot side | Falling approach temperature, rising pumping energy, cleaning downtime | Removable plate packs, online backflush, water analysis before design | D |
| Thermal short circuit | Extraction and reinjection too close in a high-velocity aquifer | Source temperature drift, falling COP and capacity | Tracer test, minimum separation, monitoring wells | D |
| Karst drilling loss | Drilling fluid or cement escapes into cavities | Aquifer contamination, abandoned borehole, cost overrun | Pre-drilling geophysics, staged drilling, lost-circulation plan | B for hazard, D for local likelihood |
| Legionella and aerosol drift | Open evaporative circuit near a tourist site | Health risk, shutdown, public opposition | Closed dry cooler, or full 42. BImSchV regime with separators and monitoring | A |
| Visible plume and noise | Evaporative rejection in a narrow valley | Visual impact at a landmark, noise complaints | Dry cooler, hybrid mode, acoustic design | D |
| Flood damage | Discharge range from 2,300 to above 30,000 L/s | Structural damage, debris blockage, sediment | Off-channel siting, valved connections, elevated electricals | D |
| Low-flow dilution collapse | Small receiving flow exactly when heat load peaks in summer | Temperature criterion breached | Load-dependent control, storage, backup rejection | D |
| Refrigerant leakage | Chiller or heat pump circuit | Direct greenhouse gas emissions, loss of capacity | Leak detection, maintenance contract, low-GWP refrigerant | D |

Maintenance workload splits cleanly by option. A closed plate exchanger and dry cooler need periodic cleaning, filter changes and pump service. A heat pump adds compressor and refrigerant service. An open evaporative system adds biweekly internal checks, quarterly or monthly laboratory tests, biocide management, a five-year expert inspection and a permanent logbook, all mandated by the 42. BImSchV [42. BImSchV](https://www.gesetze-im-internet.de/bimschv_42/BJNR237900017.html) (grade A).

The ecology argument cuts both ways. A closed loop with no water abstraction and no discharge has almost no ecological footprint in the river, but it consumes electricity and rejects heat to air. A dilution or bypass scheme uses the river's own capacity but puts new structures and a thermal plume into a protected reach. On the evidence found, the closed loop is the lower-risk permitting path and the dilution scheme is the higher-risk one, which is the opposite of their thermodynamic ranking.

### Gaps
- No site-specific numeric temperature criterion for the Blau was found. The permitting authority's assessment basis is unknown.
- No drinking water protection zone or public water supply designation for the spring was verified.
- No data on water hardness, calcite saturation index or scaling propensity at the Blautopf were found, so the scaling risk is an inference from the Jurassic karst setting.
- No flood hazard map or high-water line for the spring area was retrieved.
- No noise or visual impact study for a cooling installation at this location exists in the sources reviewed.
- The § 108 WG procedure was taken from a 2015 guide and was not confirmed against the current statute text.

## 4. What heat recovery options and control or monitoring architectures could improve economics and reliability?

### Takeaway
There is a real heat customer next door. Blaubeuren's old town already has a district heating network operated by Technische Werke Blaubeuren, it is being transformed and expanded, and sewage heat pumps are under study as a source. Recovered cooling heat could feed that network through a heat pump, but the network penalty on seasonal performance is measurable and must be designed in, not assumed away.

### Cited Findings

**Local heat network.** The municipal heat planning page states that Technische Werke Blaubeuren operate a heating network in the old town which is to be transformed and expanded, that several DN800 sewers run through the area and their thermal potential is being examined, and that the southern old town and Gerhausen are still mainly supplied by gas and oil [Stadt Blaubeuren, Kommunale Wärmeplanung](https://www.blaubeuren.de/de/Aktuelles/Kommunale-Waermeplanung) (grade B, municipal source; no load figures given).

**Network penalty.** Multi-building heat pump systems with a local network reached a mean seasonal performance factor of 2.52 against 3.87 for single-building systems, a difference of 1.35 [BFE 2010, Hubacher, PDF](https://pubdb.bfe.admin.ch/de/publication/download/4978) (grade B). The study attributes the gap to network losses, additional pumping, summer cooling-down losses when domestic hot water is central, and poor part-load behaviour of multistage machines [same source] (grade B).

**Economic method.** The cited thesis computes annual capital costs with the VDI 2067 annuity method and applies it to chiller and absorption chiller comparisons [HAW Hamburg thesis](https://reposit.haw-hamburg.de/bitstream/20.500.12738/5979/1/Bachelorthesis_Bez_Armin_20120618.pdf) (grade C). The Baden-Württemberg guide references VDI 4640 Blatt 1 and 2 for the subsurface design [Leitfaden Erdwärme](https://www.waermepumpe.de/fileadmin/user_upload/waermepumpe/02_Waermepumpe/Leitfaden_Nutzung_von_Erdwaerme_Baden-Wuerttemberg.pdf) (grade B).

**Electricity price spread.** The difference between the small and medium industry tariff of 17.9 ct/kWh and the large industry tariff of 13.8 ct/kWh is 4.1 ct/kWh, or about 23% of the small-industry tariff [BDEW](https://www.bdew.de/service/daten-und-grafiken/bdew-strompreisanalyse/) (grade B).

### Inferences
- Match the heat recovery temperature to the network, not the other way round. A cooling duty delivered at 30 to 40 °C needs a heat pump to reach 70 to 90 °C flow temperatures; the lower the lift, the higher the COP. Recovering heat at the coldest possible temperature and upgrading it in one stage is usually better than recovering at a high temperature and blending.
- Use a buffer tank between the cooling process and the heat offtake. Cooling loads and heat demand rarely coincide, and a storage volume turns an intermittent surplus into dispatchable heat. The tank also lets the heat pump run at full load instead of cycling.
- Sell cold as well as heat. The same cold spring water that cools in summer can pre-cool in winter, and the heat pump's evaporator can be reversed to provide cooling while charging the network. A single machine with reversible operation improves utilisation and therefore the annuity.
- Instrument the plant for JAZ, not just for energy. The key figures are thermal kWh, electrical kWh, flow, both temperatures, and pressure drop across each exchanger. Without these, the seasonal performance factor cannot be verified and an underperforming installation will run unnoticed for years.
- Control architecture should have three layers. A safety layer enforces temperature and pressure limits and trips the plant. A compliance layer logs the upstream and downstream temperatures at the agreed monitoring points, the abstraction and discharge flows, and the Legionella sampling schedule. An optimisation layer runs free-cooling priority, floating setpoints, staging and forecast-based pre-cooling.
- The compliance layer is what makes the difference between a permit that survives review and one that does not. Regulators respond to a continuous, timestamped record of the actual thermal plume far better than to a design calculation.

A monitoring set that covers the plausible failure modes:

| Measurement | Location | Purpose |
| --- | --- | --- |
| Temperature, 4-wire PT100 | Upstream, mixing point, 200 m downstream | Verify plume and compliance |
| Flow, electromagnetic | Abstraction, discharge, each loop | Mass balance and dilution ratio |
| Differential pressure | Each heat exchanger | Fouling trend |
| Turbidity and conductivity | Upstream and downstream | Sediment disturbance and mixing |
| Thermal energy meter | Cooling and heating sides | JAZ and cost allocation |
| Electricity meter, sub-metered | Chiller, pumps, fans, controls | Specific consumption per kWh cold |
| Legionella sampling | Evaporative circuit, if any | 42. BImSchV compliance |
| Refrigerant leak detection | Machine room | F-gas compliance and capacity loss |
| Vibration and bearing temperature | Pumps, compressors, fans | Early fault detection |

### Gaps
- No network temperatures, load duration curve or connection capacity for the Technische Werke Blaubeuren network were published in the sources reviewed.
- No annual heat demand in GWh for Blaubeuren was found, so the recoverable heat cannot be sized against demand.
- No data on summer cooling demand in Blaubeuren, for example from hotels, the monastery, or public buildings, were found.
- No cost data for network connection, heat exchanger stations or buffer storage were found.
- The sewage heat potential study is described as pending, so its results cannot be used.
- No monitoring standard or reporting template from the competent water authority was retrieved.
