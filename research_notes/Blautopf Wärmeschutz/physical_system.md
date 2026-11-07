# Blautopf physical system and heat-scenario research notes

All web sources and data queries were accessed on 2026-11-07. Page, table, figure and equation locations below refer to the linked document. Values calculated for these notes are labeled as calculations, not measurements. The deep volcanic heating and the ten-year forecast are scenario premises from the assignment. None of the cited sources verifies either premise.

## What defensible baseline geometry, discharge, temperature and seasonal boundary data exist for Blautopf and the Blau, and which values are scenario premises?

### Takeaway

Public sources support a useful hydrologic baseline, but not a survey-grade thermal model. Discharge is unusually well documented. Pool area, current bathymetry, river cross-sections, branch flows and a long water-temperature series still need field data. The volcanic source and ten-year forecast must enter the model as declared forcing assumptions, never as observed Blautopf behavior.

### Cited Findings

- **Catchment and aquifer.** The state geological service gives a catchment area of about 165 km². It describes two connected cave drainage branches, Ur-Blau and Nord-Blau, and a known Blauhöhlensystem length of about 15.5 km as of 2020. The total system length is unknown, so 15.5 km is not a defensible conduit length for a heat-transport model. The same page reports saturated Upper Jurassic carbonate rocks and a complex aquifer base. [LGRB, "Geologisch-Hydrogeologischer Rahmen", "Quellaustritt" and "Markierungsversuche"](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele)

- Fan et al. independently use approximately 165 km², catchment elevations of 609 to 878 m above sea level, and two subcatchments estimated to contribute about half of spring discharge each. They report saturated and unsaturated zone thicknesses of 50 to 120 m and 100 to 150 m. These are regional aquifer dimensions, not the dimensions of the spring pool or a single flow tube. [Fan et al. 2023, "Study site" and Fig. 1, DOI 10.1007/s10040-023-02703-9](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

- **Pool geometry and outlet.** LGRB gives a pool depth of about 20.6 m, a water level of about 512 m above NHN, and an artificial impoundment of 3 to 4 m for energy use. These values cite Villinger's 1987 work and should not be treated as a current bathymetric survey. [LGRB, "Quellaustritt"](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele)

- The city calls the pool a funnel-shaped karst spring with a depth of 22 m. It says the Blau travels 22 km to the Danube at Ulm. The 20.6 m and 22 m depths differ in precision, date and possibly datum. Use a measured water-level-to-bed profile in the model rather than silently choosing one. [Stadt Blaubeuren, "Geopoint Blautopf"](https://www.blaubeuren.de/Geopoint-Blautopf)

- No cited authority supplies the pool surface area, volume, a stage-area-volume curve, the current river width and depth along the Blau, or the wetted perimeter of each conduit. LGRB explicitly states that the full cave system length is unknown. [LGRB, opening description of Blauhöhlensystem](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele)

- **Discharge record.** LGRB reports measurements beginning in October 1924 and gives the following values for 1951 to 2007, based on Selg and Schwarz 2009: lowest discharge NQ 0.251 m³/s, mean discharge MQ 2.330 m³/s and high discharge HQ 32.700 m³/s. [LGRB, "Schüttungsverhalten und Karstwasserkomponenten"](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele)

- Fan et al. analyzed LUBW station ID 76273 from 1 January 1952 through 31 December 2021. A stage-discharge relation was used through 2004. Since 2005, discharge has been calculated as the difference between downstream and upstream river discharge. The authors report consistent results between the methods in their supplement. Data were hourly through 2016 and at 15-minute intervals thereafter, with no daily gaps after error removal. This is the best documented route to an auditable discharge time series found in this research. [Fan et al. 2023, "Karst discharge data", DOI 10.1007/s10040-023-02703-9](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

- For 1952 to 2021, Fan et al. report daily discharge from 0.1 to 32.6 m³/s, mean 2.3 m³/s, and 10th and 90th percentiles of 0.7 and 4.7 m³/s. The 0.1 m³/s daily minimum and LGRB's 0.251 m³/s NQ are not interchangeable statistics or periods. [Fan et al. 2023, "Discharge and climate trends" and Fig. 4h](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

- **Seasonal discharge and weather.** Fan et al. report mean June to August discharge of 1.7 m³/s, compared with the annual mean of 2.3 m³/s. August to October has the lowest monthly mean discharge, averaging 1.2 m³/s. March has the highest discharge, associated with snowmelt. Daily mean catchment air temperature ranged from -23.0 to +26.7 °C in their record. [Fan et al. 2023, "Discharge and climate trends", Fig. 4 and Table 2](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

- Fan Table 2 gives annual total precipitation minimum, mean and maximum of 640, 950 and 1288 mm, annual potential evapotranspiration of 497, 552 and 629 mm, annual mean air temperature of 5.4, 7.0 and 8.9 °C, and annual mean discharge of 1.3, 2.3 and 4.0 m³/s. These are annual statistics across 1952 to 2021, not bounds on individual storms or the next ten years. [Fan et al. 2023, Table 2](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

- Fan Table 1 identifies the DWD stations and variables used for precipitation, air temperature, snow height and snow water equivalent. Station 3402 supplies the continuous catchment air-temperature series. The study used daily data from the DWD Climate Data Center. [Fan et al. 2023, "Climate data" and Table 1](https://publikationen.bibliothek.kit.edu/1000163518/151549041); [DWD Climate Data Center open-data directory](https://opendata.dwd.de/climate_environment/CDC/)

- **Water temperature.** The city gives approximately 9 °C throughout the year. This is a broad public-information value, with no sensor record, uncertainty, seasonal percentiles or storm response supplied. It is suitable only as an initial condition to be checked against LUBW or new logger data. [Stadt Blaubeuren, "Geopoint Blautopf"](https://www.blaubeuren.de/Geopoint-Blautopf)

- **Response times and storage.** LGRB reports an approximately two-day delay between modeled recharge and the first spring-discharge response. It identifies that response as pressure transmission that displaces older groundwater, not arrival of the new water itself. Event water lasts hours to days and accounts for an estimated 5 to 10% of an event's discharge. Separately, short-term components are estimated at 2 to 3% of total discharge. These percentages have different denominators. [LGRB, "Schüttungsverhalten und Karstwasserkomponenten"](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele)

- LGRB gives tritium-based mean water residence times of 12 to 14 years and a tritium-free component of about 20 to 30%. A two-day hydraulic response therefore does not imply a two-day water or heat residence time. [LGRB, "Schüttungsverhalten und Karstwasserkomponenten"](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele)

- Fan et al. estimate a three-day precipitation-to-discharge lag, a 40-day system memory at autocorrelation 0.2, and both fast and slow flow components. The low cross-correlation peak of 0.22 shows strong attenuation of the precipitation signal. [Fan et al. 2023, "Karst system hydrodynamics" and Fig. 3](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

- Across 17 tracer tests with spring breakthrough, LGRB reports mean maximum distance velocities of 67 to 350 m/h, with an average of 131 m/h. In-cave work found mean velocities up to 275 m/h in an open-channel, near-spring epiphreatic section, while phreatic velocities were about one order of magnitude lower. These observations argue against one plug-flow velocity for the whole aquifer. [LGRB, tracer-test table and "Markierungsversuche"](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele); [Lauber et al. 2014, abstract and results, DOI 10.5194/hess-18-435-2014](https://doi.org/10.5194/hess-18-435-2014)

- **Scenario status.** Deep volcanic heating, its location, its time history and a ten-year forecast horizon come from the assignment. The scientific sources above document a karst aquifer with multiple flow paths and storage times. They do not document volcanic activity at Blautopf or provide a ten-year volcanic forecast. This distinction follows from the scope and content of the cited Blautopf studies. [Fan et al. 2023](https://doi.org/10.1007/s10040-023-02703-9); [LGRB Blautopf case description](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele)

### Inferences

- Use at least three coupled model domains: a branching karst conduit network, the spring pool and the 22 km river. A single well-mixed tank cannot represent both the observed fast pressure response and the long water-residence components. [LGRB](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele); [Fan et al. 2023, Fig. 3](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

- For an initial conservative design case, pair low discharge with adverse weather and the scenario's maximum credible heat input. August to October mean flow of 1.2 m³/s and the observed daily 10th percentile of 0.7 m³/s are defensible historical stress cases. The 0.1 m³/s observed daily minimum is an extreme historical case, not a ten-year prediction. [Fan et al. 2023, Fig. 4](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

- A calculation using NIST water properties at about 10 °C gives heat-capacity flow ρQcₚ of 9.646 MW/K at Q = 2.3 m³/s, 5.033 MW/K at 1.2 m³/s and 2.936 MW/K at 0.7 m³/s. Raising the mean flow from 9 to 99.974 °C therefore requires about 878 MW before surface and bed losses. At 1.2 m³/s the same calculation gives about 458 MW. These are steady advective heat-rate calculations, not estimates of the volcanic source. Inputs are ρ = 999.702 kg/m³ and cₚ = 4195.14 J/(kg K). [NIST WebBook isobaric water table at 1.01325 bar](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Type=IsoBar&Digits=6&P=1.01325&TLow=0&THigh=100&TInc=10&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm); [Fan et al. 2023, Fig. 4](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

- The same calculation gives 9.646 MW for each 1 K change at mean flow, or 106.1 MW for warming from 9 to 20 °C. Mean annual discharge volume is 72.58 million m³ using 365.25 days. This scale makes flow measurement and the definition of the heat-source control volume consequential. [NIST WebBook](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Type=IsoBar&Digits=6&P=1.01325&TLow=0&THigh=100&TInc=10&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm); [Fan et al. 2023, Table 2](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

### Gaps

- Where can the raw, quality-controlled LUBW station 76273 discharge files and any matching spring-temperature files be downloaded or formally requested? The paper documents the source and processing, but the public download endpoint was not established here.
- Is there a continuous, multi-season spring-water temperature record with sensor depth, calibration and uncertainty? The city's approximate 9 °C does not answer this.
- What are the current pool bathymetry, surface area, operating water level and outflow rating after the ongoing construction work? What surveyed river cross-sections and roughness values represent the Blau?
- What are the time-varying discharges and temperatures in Ur-Blau, Nord-Blau and any diffuse matrix inflows? A total spring hydrograph cannot uniquely partition heat among branches.
- What local hourly wind, relative humidity, air pressure, shortwave and longwave radiation records represent the pool and shaded river reaches? DWD air temperature and precipitation alone cannot close the water-surface heat balance.
- Which scenario document specifies the heat-source depth, area, power, start time and forecast uncertainty? No physical measurement or probability for the volcanic premise was supplied or found.

## Which heat transfer mechanisms matter for the spring pool, connected karst conduit and river?

### Takeaway

Advection dominates the movement of heat through the connected water system, while conduction and convection exchange heat with rock and air. At the free surface, shortwave and longwave radiation, evaporation and sensible heat can change the available cooling by hundreds of watts per square metre. Boiling is controlled by local absolute pressure, so a surface-only model can miss both deep superheating and flash boiling during depressurization.

### Cited Findings

- **River energy equation.** Ouellet and Caissie give a one-dimensional equation for a vertically well-mixed stream with unsteady storage, downstream advection, longitudinal dispersion, atmospheric heat exchange and streambed conduction. They use c_w = 4187 J/(kg °C) and ρ_w = 1000 kg/m³ as approximations. [Ouellet and Caissie 2023, preprint p. 9, Eq. 1, DOI 10.1080/07011784.2023.2177196](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- Their surface budget contains net shortwave radiation, net longwave radiation, evaporation and sensible heat. Bed exchange includes conduction and, where water crosses the bed, advection. They caution that hydrogeological setting and site-specific coefficients are often neglected. [Ouellet and Caissie 2023, preprint pp. 4-6 and 9-14](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- For net shortwave radiation, the study uses incoming measured radiation minus reflection. It cites reflected fractions of 1 to 6%, with a mean of 3% for its study setting. This is a transferable modeling parameter to measure locally, not a Blautopf measurement. [Ouellet and Caissie 2023, preprint p. 10, Eq. 3](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- For outgoing longwave radiation, the study uses the Stefan-Boltzmann law with σ = 5.67 × 10⁻⁸ W/(m² K⁴) and water emissivity ε_w = 0.97 ± 0.005. Temperature must be in kelvin. [Ouellet and Caissie 2023, preprint pp. 10-11, Eqs. 4-6](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- Evaporative heat flux equals evaporation mass flux times latent heat. The study uses L = 2.45 MJ/kg at river temperatures and a Dalton-type evaporation equation, E = (a + b u₂)(e*s - e_a). The coefficients a and b are site-specific, and the paper explicitly recommends local calibration. [Ouellet and Caissie 2023, preprint pp. 11-12, Eqs. 7-8](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- Sensible heat can be obtained from the Bowen ratio, the ratio of sensible to evaporative heat flux. The paper's formulation depends on air-water temperature difference, vapor-pressure difference and the same wind function used for evaporation. [Ouellet and Caissie 2023, preprint pp. 12-13, Eqs. 9-11](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- Streambed conduction follows Fourier's law and requires thermal conductivity and the vertical temperature gradient at the water-bed interface. The study uses shallow bed-temperature profiles to estimate that gradient. [Ouellet and Caissie 2023, preprint p. 13, Eq. 12](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- The Canadian case study is not Blautopf, but it demonstrates why these terms cannot be dropped without checking. During its ten-day example, mean net shortwave input was +206 W/m². Mean losses were 97 W/m² by evaporation, 51 W/m² by net longwave radiation, 41 W/m² by streambed heat flux and 12 W/m² by sensible heat. Instantaneous evaporative loss approached 300 W/m². These values show possible magnitudes, not Blautopf calibration values. [Ouellet and Caissie 2023, abstract and preprint pp. 20-22](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- **Conduction and convection at conduit and exchanger walls.** Bergman et al. give Fourier's law, q″_x = -k dT/dx, and Newton's law of cooling, q″ = h(T_s - T_∞). They distinguish advection, meaning transport by bulk fluid motion, from convection at a bounding surface, which combines molecular diffusion and bulk motion. [Bergman et al., Fundamentals of Heat and Mass Transfer, Wiley excerpt, Chapter 1, pp. 4-8](https://catalogimages.wiley.com/images/db/pdf/9781119382911.excerpt.pdf)

- Table 1.1 gives broad engineering ranges for the convection coefficient h in W/(m² K): free convection in gases 2 to 25, free convection in liquids 50 to 1000, forced convection in gases 25 to 250, forced convection in liquids 100 to 20,000, and boiling or condensation 2500 to 100,000. These are order-of-magnitude screening ranges. The liquid values apply to fluid-solid exchange, not directly to evaporation from the pool. Boiling coefficients are irrelevant before boiling starts and must not be used to credit cooling in a prevention design. [Bergman et al., Table 1.1, p. 8](https://catalogimages.wiley.com/images/db/pdf/9781119382911.excerpt.pdf)

- **Sensible and latent energy.** For a temperature change without phase change, q = m c ΔT. During vaporization, added heat changes phase while the saturation temperature remains constant. OpenStax uses 40.67 kJ/mol at water's normal boiling point and 44.01 kJ/mol at standard temperature, demonstrating that latent heat is temperature-dependent. [OpenStax Chemistry 2e, Section 10.3, "Enthalpy of Vaporization", "Heating and Cooling Curves" and Example 10.10](https://openstax.org/books/chemistry-2e/pages/10-3-phase-transitions)

- **Boiling and pressure.** Boiling begins when equilibrium vapor pressure equals the pressure of the gaseous surroundings. The normal boiling point is defined at 1 atm, approximately 101.3 kPa. Clausius-Clapeyron gives an approximate two-point relation, but IAPWS saturation equations are preferable for final calculations. [OpenStax Chemistry 2e, Section 10.3, "Boiling Points" and Example 10.7](https://openstax.org/books/chemistry-2e/pages/10-3-phase-transitions); [IAPWS IF97, Region 4 saturation-curve description](https://iapws.org/relguide/IF97-Rev.html)

- IAPWS-IF97 supplies thermodynamically consistent density, heat capacity, enthalpy and vapor-liquid equilibrium equations. Its main range is 273.15 to 1073.15 K at pressures to 100 MPa, which covers the scenario's liquid-water and boiling calculations. [IAPWS, Revised Release on IAPWS-IF97](https://iapws.org/relguide/IF97-Rev.html)

- NIST's IAPWS-based table gives the saturation temperature 99.9743 °C at 1.01325 bar. At that point liquid density is 958.367 kg/m³ and the liquid and vapor enthalpies are 419.058 and 2675.53 kJ/kg, giving latent heat 2256.472 kJ/kg by subtraction. [NIST WebBook isobaric table, rows at 99.9743 °C](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Type=IsoBar&Digits=6&P=1.01325&TLow=0&THigh=100&TInc=10&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm)

- **Heat rejection by a heat pump.** A refrigerator's coefficient of performance is COP_C = Q_c/W. Energy conservation gives Q_h = Q_c + W. A heat pump moves heat from a cold reservoir to a hot reservoir rather than eliminating it. [OpenStax University Physics Volume 2, Section 4.3, Eqs. 4.3-4.4](https://openstax.org/books/university-physics-volume-2/pages/4-3-refrigerators-and-heat-pumps)

- The reversible limits are COP_C,Carnot = T_c/(T_h - T_c) and COP_H,Carnot = T_h/(T_h - T_c), with reservoir temperatures in kelvin. Real equipment performs below these reversible limits. [OpenStax University Physics Volume 2, Section 4.5, Eqs. 4.6-4.7 and Carnot's principle](https://openstax.org/books/university-physics-volume-2/pages/4-5-the-carnot-cycle)

### Inferences

The following equations are modeling adaptations of the cited conservation laws, not calibrated Blautopf models. Define heat flux as positive into water and use SI units throughout.

- **Pool storage and mixing.** A defensible lumped pool balance is

  d(ρ V cₚ T_p)/dt = Σ_i(ρ Q_i cₚ T_i) - ρ Q_out cₚ T_p + Q̇_anom(t) + A_s q″_surf + A_b q″_bed - Q̇_cooling.

  The inputs are branch and diffuse inflows, the scenario heat source, surface and bed exchange, and any engineered heat removal. A constant-volume approximation is acceptable only after the operating level and rating relation are verified. If evaporation is material, the water balance must include it as well as the heat balance. This adapts the river energy budget and sensible-heat relation to the pool. [Ouellet and Caissie 2023, Eqs. 1 and 14](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf); [OpenStax Chemistry 2e, heating curves](https://openstax.org/books/chemistry-2e/pages/10-3-phase-transitions)

- A 20.6 to 22 m deep pool should not automatically be treated as well mixed. Measure vertical temperature and conductivity profiles. If buoyancy creates stratification, replace the single tank with vertical layers and mixing driven by inflow momentum and density differences. The geometry and lack of a cited vertical profile come from the sources above. [Stadt Blaubeuren](https://www.blaubeuren.de/Geopoint-Blautopf); [LGRB](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele)

- **Karst conduit.** For one conduit reach with cross-section A_c, discharge Q, wetted perimeter P_c and rock-wall temperature T_r, an advection-dispersion form is

  ρcₚA_c ∂T/∂t + ρcₚQ ∂T/∂x = ∂/∂x(ρcₚA_cD_L ∂T/∂x) + P_c h_w(T_r - T) + q′_anom(x,t).

  Here q′_anom is scenario heat input per conduit length in W/m. For steady flow without longitudinal dispersion, the left storage term and dispersion term vanish. Junction mixing is flow weighted, T_mix = ΣQ_iT_i/ΣQ_i when density and heat capacity are effectively equal. This adapts the river equation and Newton's law to a pressurized or open-channel conduit. [Ouellet and Caissie 2023, Eq. 1](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf); [Bergman et al., pp. 6-8](https://catalogimages.wiley.com/images/db/pdf/9781119382911.excerpt.pdf)

- A steady wall coefficient h_w is only a closure approximation. A persistent hot-rock anomaly may require transient conduction in the surrounding limestone, coupled to water advection. The two cave branches and order-of-magnitude velocity difference make a network model preferable to an average conduit. [Lauber et al. 2014](https://doi.org/10.5194/hess-18-435-2014); [Bergman et al., Fourier's law, p. 4](https://catalogimages.wiley.com/images/db/pdf/9781119382911.excerpt.pdf)

- **Blau river.** With river cross-section A, width W, mean velocity v and longitudinal dispersion D_L, use

  ∂T/∂t + v∂T/∂x = (1/A)∂/∂x(AD_L∂T/∂x) + W(H_surf + H_cond)/(ρc_wA) + q_L(T_L - T)/A.

  The last term is an added lateral-inflow closure, where q_L is inflow per river length in m²/s and T_L is its temperature. Omit that term if there is no inflow. The first two terms and surface/bed terms follow the published river equation. [Ouellet and Caissie 2023, Eq. 1](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- **Free-surface heat budget.** With reflectance r, incoming shortwave R_SW, incoming longwave R_LW, air temperature T_a, water-surface temperature T_w, air-side coefficient h_a and evaporation rate E in m/s, a consistent sign convention is

  q″_surf = (1-r)R_SW + εR_LW - εσ(T_w + 273.15)⁴ + h_a(T_a - T_w) - ρL_vE.

  E may be estimated with a locally calibrated Dalton function f(u₂)[e_sat(T_w) - e_a]. If the vapor-pressure difference is negative, the same framework represents condensation. Radiation penetration into a clear, deep pool may require a depth-dependent absorption model rather than assigning all shortwave energy to the surface layer. [Ouellet and Caissie 2023, Eqs. 3-11](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- **Pressure-dependent boiling.** For a static pool, approximate p_abs(z) = p_atm + ρgz and calculate T_sat(p_abs) with IAPWS Region 4. In a flowing conduit, use modeled or measured static pressure along the route, not atmospheric pressure plus an assumed depth everywhere. The criterion is T < T_sat(p_abs) at every location and time, with an explicit safety margin. [OpenStax Chemistry 2e, boiling definition](https://openstax.org/books/chemistry-2e/pages/10-3-phase-transitions); [IAPWS IF97](https://iapws.org/relguide/IF97-Rev.html)

- Calculation for the pool-floor example: using ρ = 999.702 kg/m³, g = 9.80665 m/s², z = 22 m and p_atm = 1.01325 bar gives p_abs = 3.17007 bar. NIST gives T_sat = 135.413 °C at that pressure. This is a hydrostatic example at the cave entrance, not a measurement of pressure throughout the cave network. [NIST WebBook isobaric table at 3.17007 bar](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Digits=6&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm&Type=IsoBar&P=3.1700700760259997&TLow=130&THigh=140&TInc=1)

- Hot water rising from depth can cross its saturation curve when pressure falls even if its temperature falls slightly. A prevention model therefore needs both temperature and pressure transients. Visible bubbles alone do not prove steam boiling, because dissolved gases can exsolve. Gas composition or direct steam evidence is needed to distinguish those mechanisms. The pressure-temperature part follows from the saturation relation; the gas warning is a diagnostic limitation of visual observation. [OpenStax Chemistry 2e, vapor pressure and boiling](https://openstax.org/books/chemistry-2e/pages/10-3-phase-transitions)

- **Cooling-duty closure.** At steady pool temperature T_target, the required removal is the scenario heat input plus incoming advective heat above the target, plus surface and bed gains, minus any credited natural losses. For a bypass heat exchanger, independently check Q̇_c = ρQ_bcₚ(T_in - T_out). Do not count both bypass cooling and an identical reduction in downstream advection as two separate benefits. [Ouellet and Caissie 2023, energy-budget Eqs. 1 and 14](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- If all mean discharge reached its normal boiling point and vaporized, latent duty would be about 5.19 GW using Q = 2.3 m³/s, ρ = 999.702 kg/m³ and L_v = 2256.472 kJ/kg. This is a scale calculation for complete vaporization, not the heat input required to initiate boiling and not a predicted steam flow. [NIST WebBook](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Type=IsoBar&Digits=6&P=1.01325&TLow=0&THigh=100&TInc=10&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm); [Fan et al. 2023, Fig. 4](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

- A ten-year prevention claim requires time integration of the full heat and water balances under scenario forcing, not a steady calculation at mean flow. Test low pressure, low discharge, hot and dry weather, storms, snowmelt, equipment downtime and uncertainty in the scenario heat source. [Fan et al. 2023, seasonal and discharge results](https://publikationen.bibliothek.kit.edu/1000163518/151549041); [OpenStax heat-pump energy balance](https://openstax.org/books/university-physics-volume-2/pages/4-3-refrigerators-and-heat-pumps)

### Gaps

- Which parts of the connected cave are pressurized, open-channel or air-filled at each discharge? Their surface heat and mass exchanges differ.
- What are the local limestone and sediment thermal conductivities, heat capacities, wall areas and initial temperature fields? No defensible Blautopf-specific set was found.
- Does the pool stratify under the scenario heat input, and how much shortwave radiation reaches deeper layers?
- What wind function and sensible-heat coefficient reproduce measured evaporation and heat loss at Blautopf? Literature coefficients from a Canadian river are not a substitute.
- Can dissolved-gas and bubble observations distinguish vapor formation from gas exsolution during a pressure drop?
- What is the scenario heat-source function q′_anom(x,t), and what independent uncertainty bounds should the ten-year ensemble span?

## Which source-supported parameter ranges are suitable for properties, heat-transfer coefficients, heat-pump performance and ecological limits?

### Takeaway

Use IAPWS or NIST temperature-dependent properties for final work. Constant values near 1000 kg/m³ and 4.19 kJ/(kg K) are fine for first estimates near the baseline, but not for the full path to boiling. Ecological constraints are much stricter than the boiling threshold, and cooling too quickly can also cause harm.

### Cited Findings

- **Density and heat capacity.** At 1.01325 bar, NIST gives liquid density 999.844 kg/m³ at 0.01 °C, 999.702 at 10.01 °C, 998.205 at 20.01 °C and 958.367 kg/m³ at 99.9743 °C. Over this 0 to 100 °C table, cₚ stays within approximately 4.179 to 4.220 kJ/(kg K), with 4.19514 at 10.01 °C and 4.21564 at 99.9743 °C. [NIST WebBook isobaric water table](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Type=IsoBar&Digits=6&P=1.01325&TLow=0&THigh=100&TInc=10&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm)

- The same table gives liquid thermal conductivity of 0.555675 W/(m K) at 0.01 °C and 0.677201 W/(m K) at 99.9743 °C. This is water's molecular conductivity, not an effective turbulent conductivity for a river or conduit. [NIST WebBook isobaric water table](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Type=IsoBar&Digits=6&P=1.01325&TLow=0&THigh=100&TInc=10&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm)

- **Latent heat.** At the normal boiling point, NIST enthalpies give L_v = 2256.472 kJ/kg. At 9.98163 °C saturation, NIST gives liquid and vapor enthalpies of 41.9442 and 2519.17 kJ/kg, so L_v = 2477.226 kJ/kg. For ordinary river-temperature screening, Ouellet and Caissie use 2.45 MJ/kg. Final calculations should evaluate latent heat at local temperature and pressure. [NIST isobaric table at 1.01325 bar](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Type=IsoBar&Digits=6&P=1.01325&TLow=0&THigh=100&TInc=10&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm); [NIST saturation table at 9.98163 °C](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Digits=6&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm&Type=SatP&PLow=3.16&PHigh=3.16&PInc=1); [Ouellet and Caissie 2023, Eq. 7](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- Across the cited NIST saturation table from approximately 0 to 100 °C, latent heat decreases from about 2.501 to 2.256 MJ/kg. A constant 2.45 MJ/kg is therefore appropriate only for moderate-temperature evaporation estimates, not boiling at depth. [NIST saturation table](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Digits=6&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm&Type=SatP&PLow=3.16&PHigh=3.16&PInc=1)

- **Convection and radiation parameters.** The broad h ranges in Bergman Table 1.1 are 2 to 25 W/(m² K) for free convection in gases, 50 to 1000 for free convection in liquids, 25 to 250 for forced convection in gases, 100 to 20,000 for forced convection in liquids, and 2500 to 100,000 for boiling or condensation. The text stresses that h depends on geometry, fluid motion and fluid properties. [Bergman et al., Table 1.1 and pp. 8-9](https://catalogimages.wiley.com/images/db/pdf/9781119382911.excerpt.pdf)

- For the water-surface radiation model, use σ = 5.67 × 10⁻⁸ W/(m² K⁴) and an initial ε_w = 0.97 ± 0.005, then check sensitivity. The shortwave reflection bracket from the river study is 1 to 6%. Neither emissivity nor reflection was measured at Blautopf in the cited work. [Ouellet and Caissie 2023, pp. 10-11](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- **Heat-pump performance.** The US Department of Energy guide says geothermal systems move between three and five times the energy they consume between a building interior and the ground. The same guide reports 300 to 600% efficiency on the coldest winter nights. These are heating-oriented, system-level statements, not a certified cooling COP for a Blautopf chiller. [US DOE, Guide to Geothermal Heat Pumps, DOE/EE-0385, 2011, pp. 1-2](https://www.energy.gov/sites/prod/files/guide_to_geothermal_heat_pumps.pdf)

- The thermodynamic definitions remain COP_C = Q_c/W, COP_H = Q_h/W and Q_h = Q_c + W. The reversible maxima depend on the actual evaporator and condenser temperatures in kelvin. [OpenStax Sections 4.3 and 4.5](https://openstax.org/books/university-physics-volume-2/pages/4-3-refrigerators-and-heat-pumps); [OpenStax Carnot equations](https://openstax.org/books/university-physics-volume-2/pages/4-5-the-carnot-cycle)

- **Current German ecological values.** OGewV Annex 7, Section 2.1.1, gives "good ecological status or potential" summer maxima for April to November of 20 °C for Sa-ER and Sa-MR, 21.5 °C for Sa-HR, 23 °C for Cyp-R, 25 °C for EP and 28 °C for MP and HP. Corresponding maximum warming across a heat-discharge point is 1.5, 1.5, 1.5, 2, 3, 3 and 3 K. Winter maxima for December to March are 8 °C for Sa-ER and 10 °C for the other listed fish communities, with warming limits of 1, 1.5, 1.5, 2, 3, 3 and 3 K respectively. [OGewV 2016, Anlage 7, Section 2.1.1](https://www.gesetze-im-internet.de/ogewv_2016/anlage_7.html)

- For "very good ecological status or highest potential", OGewV Section 1.1.1 gives summer maxima below 18 °C for the salmonid and cyprinid rhithral communities, below 20 °C for EP and MP, and below 25 °C for HP, with zero permitted heat-discharge increment in summer. Winter values and increments are also tabulated. [OGewV 2016, Anlage 7, Section 1.1.1](https://www.gesetze-im-internet.de/ogewv_2016/anlage_7.html)

- The Blau's exact OGewV water-body type and fish community were not established by the sources reviewed. The ordinance table itself assigns fish communities by water-body type in its upper matrix. Do not select a salmonid limit without confirming that classification. [OGewV 2016, Anlage 7, Section 1.1.1](https://www.gesetze-im-internet.de/ogewv_2016/anlage_7.html)

- **Life-stage and rate-of-change evidence.** The LAWA review identifies brown trout as a sensitive indicator for salmonid and cyprinid rhithral communities. It gives an upper spawning preference of 11 °C and an upper lethal temperature for eggs of 14 °C, while noting that the adult limit is higher. A general summer or winter maximum does not protect every life stage. [van Treeck and Wolter 2020, LAWA project O 10.20, Summary, p. 65](https://www.laenderfinanzierungsprogramm.de/static/LFP/Dateien/LAWA/AO/O_10.20_211119_Endbericht_O10.20_TempEmpf_Fische.pdf)

- The LAWA review states that rapid temperature changes are harmful and should not exceed ±1 K/h, citing Beitinger et al. It recommends considering cold-water additions as well as heating. Its Table 7 proposes symmetric seasonal deviation limits and a shorter summer period. These are expert recommendations for revising management, not values to misquote as the currently binding OGewV table. [LAWA review, pp. 10-11 and pp. 62-68, especially Table 7](https://www.laenderfinanzierungsprogramm.de/static/LFP/Dateien/LAWA/AO/O_10.20_211119_Endbericht_O10.20_TempEmpf_Fische.pdf)

### Inferences

- For first calculations near 9 to 20 °C, ρ = 1000 kg/m³ and cₚ = 4.19 kJ/(kg K) introduce little error compared with the unknown scenario heat input. Use NIST values ρ = 999.702 kg/m³ and cₚ = 4.19514 kJ/(kg K) at about 10 °C for reproducible calculations. Switch to IAPWS functions across the full heating path. [NIST WebBook](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Type=IsoBar&Digits=6&P=1.01325&TLow=0&THigh=100&TInc=10&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm); [IAPWS IF97](https://iapws.org/relguide/IF97-Rev.html)

- For evaporation below boiling, 2.45 MJ/kg is a defensible screening value. At normal boiling use 2.256472 MJ/kg, not 2.45 MJ/kg. At 3.17007 bar and 135.413 °C, NIST liquid and vapor enthalpies give 2157.91 kJ/kg by subtraction, showing why pressure-dependent properties matter for deep boiling. [NIST isobaric table at 3.17007 bar](https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7732185&Digits=6&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm&Type=IsoBar&P=3.1700700760259997&TLow=130&THigh=140&TInc=1)

- Use the Bergman h ranges only to bound sensitivity calculations. A defensible Blautopf model needs h_w calibrated from measured wall-water temperature and heat flux, and a separate air-water model calibrated from local weather and water temperature. Do not use a solid-liquid exchanger h for pool evaporation or a boiling h to prevent boiling. [Bergman et al., Table 1.1](https://catalogimages.wiley.com/images/db/pdf/9781119382911.excerpt.pdf); [Ouellet and Caissie 2023, site-specific wind-function discussion](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- For equipment studies, calculate COP_C across a stated sensitivity set such as 2, 3, 4, 5 and 6, but label those as modeling choices rather than measured product performance. Obtain manufacturer maps at the design water temperatures and include pumps, fans, part load and standby power. The DOE heating range cannot certify these cooling values. [US DOE guide](https://www.energy.gov/sites/prod/files/guide_to_geothermal_heat_pumps.pdf); [OpenStax COP definitions](https://openstax.org/books/university-physics-volume-2/pages/4-3-refrigerators-and-heat-pumps)

- Example reversible bounds, not equipment ratings: at T_c = 283.15 K and T_h = 313.15 K, COP_C,Carnot = 9.44. At T_h = 333.15 K with the same cold reservoir, it is 5.66. A larger heat-rejection temperature sharply increases work demand. These are direct substitutions into the Carnot equation. [OpenStax, Eq. 4.6](https://openstax.org/books/university-physics-volume-2/pages/4-5-the-carnot-cycle)

- Every cooling option needs an external heat-sink balance. If the chiller rejects heat to the same connected water system, Q_h = Q_c + W means the intervention returns both the removed heat and the electrical input as heat. A permanent design must identify where that rejected energy goes and verify that it cannot return through air, groundwater or the river. [OpenStax Section 4.3](https://openstax.org/books/university-physics-volume-2/pages/4-3-refrigerators-and-heat-pumps)

- A two-limit acceptance rule is appropriate. The physical anti-boiling condition is T + uncertainty < T_sat(p_abs) minus a declared safety margin at every point and time. The ecological condition should use the confirmed OGewV classification, natural-reference ΔT, sensitive life stages and a controlled cooling rate. Satisfying only the first rule can still destroy the ecosystem. [OGewV Annex 7](https://www.gesetze-im-internet.de/ogewv_2016/anlage_7.html); [LAWA review, pp. 62-68](https://www.laenderfinanzierungsprogramm.de/static/LFP/Dateien/LAWA/AO/O_10.20_211119_Endbericht_O10.20_TempEmpf_Fische.pdf); [IAPWS IF97](https://iapws.org/relguide/IF97-Rev.html)

### Gaps

- What is the Blau's legally assigned OGewV type and fish community, and which locally protected species and life stages require stricter limits?
- What cooling COP, part-load performance and refrigerant leakage risk apply to equipment large enough for the calculated duties? No site-specific equipment curve was evaluated.
- What measured Blautopf values exist for air-water sensible transfer, evaporation wind function, wall-water transfer and effective thermal dispersion?
- What uncertainty and safety margin should regulators require below local saturation temperature and below ecological thresholds?
- What heat sink can absorb Q_c + W for ten years without warming the same catchment or violating another water body's thermal limits?

## Which observations could identify the location and strength of anomalous heating and falsify a proposed thermal intervention?

### Takeaway

Use synchronized heat, flow and pressure measurements in both cave branches, at several pool depths and along the river. Temperature anomalies alone cannot locate the source or prove success. A defensible intervention must pass an out-of-sample thermal forecast, an independent cooling-energy measurement and an external heat-rejection audit.

### Cited Findings

- **Heat tracing.** Constantz reviews direct stream and streambed temperature measurements, observation wells, remote sensing, heat-pulse timing, analytical solutions and coupled heat-water models. He recommends visualizing temperature patterns before selecting a site-specific analysis. These methods can constrain groundwater exchange, but they still require hydraulic information to turn a thermal anomaly into water and heat flux. [Constantz 2008, USGS abstract and 20-page review, DOI 10.1029/2008WR006996](https://pubs.usgs.gov/publication/70032522)

- **Distributed temperature sensing.** EPA describes fiber-optic DTS deployments in the water column, at the sediment-water interface, in bed sediment and in boreholes. Raman backscatter can provide sub-metre spatial sampling over several kilometres. Precision improves with longer integration time and distance, and the system requires thermal and spatial calibration. [US EPA, Fiber Optic Distributed Temperature Sensing, "Basic Concepts" and "Theory"](https://www.epa.gov/environmental-geophysics/fiber-optic-distributed-temperature-sensing)

- EPA notes that DTS commonly detects gaining groundwater inflows rather than surface-water losses. Thermal infrared can survey large areas quickly but measures surface skin temperature and identifies submerged seeps best in shallow water. It is not a reliable standalone survey of a 20 m deep heated pool. [US EPA, "Applications" and Hare et al. 2015 case summary](https://www.epa.gov/environmental-geophysics/fiber-optic-distributed-temperature-sensing)

- The original DTS hydrology paper reports instruments with temperature resolution of 0.01 °C, spatial resolution of 1 m and sub-minute temporal resolution under suitable configurations. These are instrument capabilities, not guaranteed field accuracy. EPA stresses calibration and the trade-off among spatial, temporal and temperature resolution. [Selker et al. 2006, DOI 10.1029/2006WR005326, abstract reproduced by EPA](https://www.epa.gov/environmental-geophysics/fiber-optic-distributed-temperature-sensing)

- **Blautopf-specific tracer evidence.** Lauber et al. used two tracers injected into the caves and two surface injections, with field fluorimeters in caves and at the spring. Their results demonstrate a dendritic drainage structure and distinct open-channel and phreatic transport. This establishes a direct method for testing which branch carries a thermal anomaly, subject to cave access and permitting. [Lauber et al. 2014, abstract, DOI 10.5194/hess-18-435-2014](https://doi.org/10.5194/hess-18-435-2014)

- LGRB reports that the 2012 injections directly into Ur-Blau and Nord-Blau established their connections to the Blauhöhle and Blautopf. It lists observation locations including Halle des Verlorenen Flusses, Mörikedom and Blautopf. These are scientifically defensible starting points for a monitoring design, not a claim that every heat-bearing pathway is accessible. [LGRB, "Markierungsversuche" and in-cave velocity table](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele)

- **Natural forcing and monitoring frequency.** Fan's LUBW record has 15-minute resolution from 2016 onward, while discharge responds to precipitation within days and storage persists much longer. Monitoring that samples only monthly cannot resolve pressure pulses, storm dilution or flash boiling. [Fan et al. 2023, "Karst discharge data" and "Karst system hydrodynamics"](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

- The river heat-budget study measured water and air temperature, humidity, wind, incoming longwave and shortwave radiation, precipitation and discharge at hourly resolution. These are the minimum weather variables needed to separate atmospheric heat exchange from anomalous subsurface heating in the same modeling framework. [Ouellet and Caissie 2023, "Study sites and data", pp. 7-9](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- LAWA recommends a thermally unaffected reference logger and cumulative assessment of temperature changes along the fish community. It also warns that lower flows reduce allowable thermal inputs. This supports using an upstream or unheated branch as a reference rather than comparing only against a fixed historical mean. [LAWA review, Fig. 24 and pp. 58-62](https://www.laenderfinanzierungsprogramm.de/static/LFP/Dateien/LAWA/AO/O_10.20_211119_Endbericht_O10.20_TempEmpf_Fische.pdf)

### Inferences

- **Minimum observation network.** Install synchronized loggers for temperature, pressure and electrical conductivity in Ur-Blau and Nord-Blau, at the Blautopf cave entrance, at several pool depths, at the outflow and at multiple downstream Blau stations. Measure branch discharge and total discharge at the same timestamps. Record precipitation, air temperature, humidity, wind, atmospheric pressure, shortwave and longwave radiation at the pool. Add river transects for width, depth and velocity. This design combines the measurement requirements of the karst and heat-budget studies. [Lauber et al. 2014](https://doi.org/10.5194/hess-18-435-2014); [Ouellet and Caissie 2023, pp. 7-14](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- Collect at least one full seasonal cycle before final calibration, including low flow, storms and snowmelt. Continue through the full intervention period. Use 15-minute or faster sampling for control and pressure safety, with slower co-located checks for calibration. The historical record and multiple response times support this choice. [Fan et al. 2023](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

- Use DTS along accessible cave streams, the pool water column and the Blau to find persistent spatial anomalies. Use thermal infrared only as a surface reconnaissance tool. Follow each anomaly with flow gauging, conductivity and, where useful, tracer testing. A warm patch without flow data cannot yield watts. [US EPA DTS guidance](https://www.epa.gov/environmental-geophysics/fiber-optic-distributed-temperature-sensing); [Constantz 2008](https://pubs.usgs.gov/publication/70032522)

- For a candidate anomalous inflow a, estimate its advective excess heat as Ḣ_a = ρQ_acₚ(T_a - T_ref), where T_ref is the synchronized temperature of a hydraulically comparable unheated branch or a validated baseline model. Sum candidate terms and subtract modeled natural surface and bed gains. Propagate uncertainty in Q_a, T_a and T_ref. A significant positive residual localized to one branch supports that source; a residual distributed across many inflows supports a diffuse source. This follows directly from sensible advective energy. [OpenStax sensible-heat relation](https://openstax.org/books/chemistry-2e/pages/10-3-phase-transitions); [Ouellet and Caissie 2023, Eq. 1](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- Independently estimate rock-to-water heat using q″ = -k∂T/∂n at instrumented walls or q″ = h_w(T_r - T_w) where the closure is justified. Agreement between branch advection, rock heat flux and downstream heat accumulation is stronger evidence than any single estimate. [Bergman et al., Fourier and Newton equations](https://catalogimages.wiley.com/images/db/pdf/9781119382911.excerpt.pdf); [Constantz 2008](https://pubs.usgs.gov/publication/70032522)

- Use time-lag and attenuation tests. A signal that appears first in one cave branch and later at the spring supports an upstream pathway. A discharge pulse arriving within days without a matching new-water thermal or conductivity signature is consistent with pressure transmission rather than source-water arrival. Long storage means a weak early thermal signal does not falsify a deep source. [LGRB residence-time and pressure-response findings](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele); [Fan et al. 2023, Fig. 3](https://publikationen.bibliothek.kit.edu/1000163518/151549041)

- **Falsification protocol.** Before operation, freeze a model calibrated on one period and publish predicted temperature, pressure and discharge responses at every sensor for a later period. Failure to predict low flow, storm dilution and seasonal changes invalidates that model for intervention design even if its training fit is good. The required variables and unsteady dynamics follow from the cited models. [Ouellet and Caissie 2023, Eqs. 1-14](https://repository.library.noaa.gov/view/noaa/49285/noaa_49285_DS1.pdf)

- If operating conditions and ecological rules permit, use stepped or intermittent cooling tests. Compare the measured downstream response at the predicted travel time with an unheated upstream or branch reference. Independently calculate cooler duty from ρQ_bcₚ(T_in - T_out) and electricity use from W = Q_c/COP_C. Reject the intervention if predicted and measured cooling differ beyond the declared uncertainty or if rejected heat returns to the connected system. [OpenStax heat-pump balance](https://openstax.org/books/university-physics-volume-2/pages/4-3-refrigerators-and-heat-pumps); [LAWA reference-logger approach](https://www.laenderfinanzierungsprogramm.de/static/LFP/Dateien/LAWA/AO/O_10.20_211119_Endbericht_O10.20_TempEmpf_Fische.pdf)

- A permanent anti-boiling claim is falsified by any verified exceedance of the agreed saturation-margin criterion at the minimum local pressure. An ecological claim is separately falsified by exceedance of the applicable temperature, natural-reference ΔT or rate-of-change criterion. A cooler pool surface does not prove protection at depth or downstream. [IAPWS saturation formulation](https://iapws.org/relguide/IF97-Rev.html); [OGewV Annex 7](https://www.gesetze-im-internet.de/ogewv_2016/anlage_7.html)

- Record cooler inlet and outlet temperature, bypass flow, electrical power, heat-sink temperature and flow, equipment availability and all bypasses or failures. Ten-year permanence is a reliability and energy-balance claim as much as a temperature claim. [OpenStax heat-pump balance](https://openstax.org/books/university-physics-volume-2/pages/4-3-refrigerators-and-heat-pumps)

- Distinguish what each null result means. No detected thermal anomaly in one reach falsifies only that monitored source hypothesis within detection limits. Failure of one cooler falsifies that design, not the scenario premise. Conversely, cooling at the spring does not prove that the inferred volcanic source was correctly located or that another pathway cannot emerge. The branching network and storage evidence prevent a stronger claim. [Lauber et al. 2014](https://doi.org/10.5194/hess-18-435-2014); [LGRB](https://lgrbwissen.lgrb-bw.de/hydrogeologie/regionalbeschreibung-mittlere-alb/fallbeispiele)

### Gaps

- Which cave stations can host safe, permitted, long-term pressure, temperature and flow instruments without disturbing the protected system?
- What are the detection limits for branch heat flux after sensor uncertainty, mixing and weather noise are included?
- Can repeated natural tracers or a newly approved tracer test independently confirm the branch carrying the anomaly and its travel time?
- What baseline period is long enough to separate the scenario anomaly from climatic variability and long residence-time behavior?
- What intervention failure rate and backup capacity are acceptable over ten years, and what regulator-approved alarm and shutdown logic applies?
- What independent measurement will verify that rejected heat does not return to the Blau, its aquifer or the local air-water heat balance?
