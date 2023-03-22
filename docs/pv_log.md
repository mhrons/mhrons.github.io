# Photovoltaic intermittency and its smoothing
## Impact of PV intermittency on grid
Intermittency of solar irradiance causes the time course of photovoltaic (PV) power generation to be unstable over time. To mitigate the temporary unbalance between PV infeed and power consumption, the grid operator sets PV generators off-grid (or at least to a low efficiency status) while the PV intermittency is high. The PV resources are not fully utilized, and they raise extra strain on the grid regulation. This impact is expressed e.g. by the last guaranteed feed-in tariff for new PV installations in Germany: In 2020, a new feed-in tariff was only about 1/3 of the purchase tariff. The state guarantee has been canceled as of 2021, and there is no more doubt that only technical innovations can further boost the share of PV energy in the grid: Efficient smoothing can improve the stability of PV power on days with high solar intermittency.  
## Measurement of PV Power
***Accurate photovoltaic measurement is a prerequisite for PV smoothing:***  
As the share of photovoltaic (PV) energy in the grid increases, the intermittency of solar power is posing still higher risk to power quality and grid's stability. Therefore, it is necessary to smooth the time course of PV power, especially from the large-scale PV plants. The smoothing should eliminate, or at least adequately reduce additional grid control costs induced by the intermittency of PV generators. The lossless PV smoothing takes up expensive accumulation capacity that could otherwise be used as the energy storage. Measurement of the global solar irradiance (GI) is an essential prerequisite for the development of effective PV smoothing technology:  

* Accurate short-term forecasting (nowcasting) of PV power is crucial to minimize the accumulation of energy by the smoothing. PV power predictors have to be continuously trained by the sky-imagery and by the signal GI(t), in particular by its fraction intercepted by a tilted PV panel.
* By means of the measured signal GI(t), we can "ex-post" excite a low-pass filter by a "predicted" input signal GIf(t+Δt), as if its GIf values were biased by a prediction error simulated to reproduce the operation of a real predictor. Given the prediction error and the desired quality of "smoothed" PV power, the accumulated energy by the filter has to be minimized. Thus, we have optimized the low-pass filter model (patent pending), minimizing the accumulation and costs of PV smoothing.
* However low is the accumulated energy, the PV smoothing is not for free. It can pay off only if a favourable "smooth feed-in tariff" exists. Ramping limits of the smooth PV infeed should be specified by a technical standard (which currently does not exist). Once the prediction error is known and the filter model is optimized, the real smoothing costs can be calculated by means of the measured GI signal. Hence a trade-off between the smoothing costs and the smoothing quality, defining the corresponding reduction in grid control costs, can be optimized. This is, how the relevant technical standard and the corresponding feed-in tariff can be matched together.

Measurement of solar irradiance for the sake of PV smoothing must meet the folloowing demands:

1. Capture the full spectrum of solar intermittency with sufficient sampling frequency
2. Replicate the physical properties of planar silicon photovoltaic panels
3. Measure only that fraction of incident radiation, which is intercepted by a tilted PV panel. 

![PV console](img/PV_Panels.JPG){ width="300"  align=right }

Actually, the momentary solar irradiance has to be measured for any plane of incidence under given atmospheric conditions. Fulfilling all of these demands is not possible only by measuring the global (GHI) and diffused (dHI) horizontal irradiance (both of which are regularly measured by national weather services).

A corresponding measurement system and data logger have been developed and is in operation since 04/2021 at the author's site (48.2°, 17.1°).

![PV_logger](img/PV_Logger.JPG){ width="300"  align=right }

 The system consists of 2 units:

1. external console having 4 reference PV panels fixed in diferent angles and temperature sensors sticked to the panels,
2. internal measurement unit, serving as a MPPT controller, battery charger, heat sink, A/D converter, and data logger.

Here are the main system highlights:

* Four monocrystaline PV panels (sensors) are mounted at different angles. The panels have been calibrated by means of Ineichen’s clear-sky model, having its Linke-turbidity factor calibrated by the reference GHI, dHI measured at the near meteorological site. The PV panels are re-calibrated once a year.
* Temperature sensors are fixed on each PV panel. The panels are always operated at maximum output power (MPPT). Their operating point is dynamically adjusted according to the temperature drift of their A-V characteristic and their internal resistance. The measured output power of each panel is then divided by its active surface area and by its known efficiency at given surface temperature. The measurement is finally expressed as the irradiance in W/m2 analogous to the measured GI at a given angle of the plane of incidence, but after taking into account the spectral and optical properties of photovoltaic panels.
* Data logger works with a dynamic sampling frequency. This captures the whole spectrum of solar intermittency, but eliminates redundancy in the stored data. The sampling period ranges from 0.5 second to 10 minutes, according to the solar intermittency. Several years of such a irregular time series can be stored in a relational database with tablespace <1TB.
* The off-grid measurement system is self-powered 24 hours x 7 days a week. Except the measurement, the PV sensors supply power to the data logger and charge its backup accumulator. The system requires a minimum maintenance.
![GI](img/GI.2022-01-15.png){ width="300"  align=right }
* Simultaneous measurement of the PV power in 4 fixed angles allows an accurate power interpolation of any virtual PV panel having its normal vector among the 4 fixed normal vectors (intra-normal area).

Daily profiles (12 h) of photovoltaic GI [W/m2] measured by 4 fixed PV planes, where GHI corresponds to the horizontal PV panel and extrapolated GNI corresponds to the virtual solar-tracked panel. Its normal vector points to the extra-normal area in winter while the solar elevation is lower than the elevation of the 4 fixed PV normal vectors. The approximated GNI is therefore less accurate in winter.
![Cels](img/Cels.2022-01-15.png){ width="300"  align=right }

Daily temperature profiles (24 h) at PV surfaces, and the ambient temperature. The PV surface temperature is affected by the ambient temperature, by the infrared solar irradiance, and by the wind. The ambient temperature is higher than the sky temperature in the night, when the PV panels are cooled by their own radiation.
  
.  
.  
.  

## Smoothing of PV Power
Energy balancing between the grid and the battery can eliminate the PV intermittency almost loss-free. If the smooth PV power is generated by a low-pass filter (LPF) excited by the output of PV panels, such a power filter induces high accumulation costs due to a time lag in its response (group delay). The time lag could be eliminated, if LPF was excited by the future PV power signal. Unfortunately, the short-time PV prediction (nowcasting) is not exact and its error dramatically increases the accumulated energy by the predictive low-pass filter (PLPF). Recently, various smart filtering techniques (e.g. moving average, moving median, Kalman filter etc.) have been developed to avoid the LPF time lag and the nowcasting error. Nevertheless, the accumulation costs induced by these non-standard filters still exceed the production cost of e.g. nuclear electricity.  
### Ideal low-pass smoothing of PV power
We simulated the operation of ideal predictive PV smoothing (IPLPF) by means of LPF excited by the exact future signal p(t+Δt) where p(t) is the real PV power (measured) and Δt is its time advance eliminating the filter’s time lag. In theory, this "ex post" smoothing simulation minimizes the accumulated energy by filter. This analysis aims to establish theoretical limits of the technical potential and affordability of PV smoothing. The numeric experiment is based on the measured solar irradiance over a period of 1 year, assuming the contemporary prices of Lithium-Ion accumulators and EDLC supercapacitors.  
The measured GI time series eventually allows to calculate the specific accumulator’s capacity [Wh/m2], its specific power [W/m2], and specific energy throughput [Wh/m2/year] requested by the IPLPF smoothing. Based on the accumulators’ specifications and prices as of 2021, the corresponding accumulation costs have been calculated. The simulation has proven that IPLPF pays-off well with the 2021 German electricity purchase and PV feed-in tariffs. The ideal smoothing costs are substantially lower than the difference between purchase tariff and PV feed-in tariff (assuming that smooth PV infeed partially compensates for the distribution costs). The simulation suggests an affordable smoothing model for a hybrid small-scale PV plant, and foresees a future smoothing technology for large-scale PV plants.  
#### Smoothing by IPLPF vs LPF
***Global irradiance GI measured (legend meas), filtered GI and specific accumulated energy GX  
by LPF (legend lp) and by IPLPF (legend aavg0):***  
![PV Logger](img/GI_PV2.3but7.5.2022-04-04.png){: style="width: 49%; align='left';"}
![PV Logger](img/GX_PV2.3but7.5.2022-04-04.png){: style="width: 49%; align='right';"}

The graph on the left shows the measured and low-passed (legend “lp”) GI signals on a day with strong solar exposure and intermittency. The graph on the right shows the specific accumulated energy GX [Wh/m2] by IPLPF vs. LPF on the same day. The time course of GX is proportional to the state of charge SOC [Wh]. The exact-predicted input signal shifts the IPLPF output to the left (legend “aavg0”), minimizing the difference delta(SOC) = max(SOC) – min(SOC) hence minimizing the necessary accumulation capacity. The accumulated energy throughput (other than delta SOC) is also minimized by IPLPF.

#### Costs of IPLPF smoothing
 Smoothing costs result from the energy accumulation. The accumulation costs are given by its rate and technology (e.g. Lithium battery, supercapacitor etc.). In theory, the rate of accumulation is given by the intermittency of solar irradiance vs. desired time course of output PV power. The accumulation rate can be expressed by the following parameters:

1. maximum power [W] from/to an accumulator, balancing the oscillating PV power
2. mandated accumulator’s capacity, i.e. maximum delta SOC [Wh] reserved for smoothing
3. total accumulated energy throughput [Wh] by smoothing

In practice, parameters 2. and 3. are larger the more imperfectly the balancing power between the grid and the battery is controlled. In the illustrated example, IPLPF uses 24% delta SOC relative to LPF, and IPLPF accumulates about 50% of the energy throughput if compared to LPF. Both the accumulated SOC and energy throughput reach their theoretical minimum by means of IPLPF smoothing.  
The higher LPF order or its lower cut-off frequency, the smoother output, but "earlier" input signal needed to eliminate the filter's time lag. (In case of PLPF smoothing: The greater Δt, the greater prediction error and the greater rate of accumulation.)  
The IPLPF simulation has proven that hybrid PV systems (small-scale, on-grid PV plant having its own battery energy storage system BESS with capacity = 2 hours x Ppvmax) need <10% of their battery capacity to be reserved for smoothing (7% as shown by Illustration 2), while their rest BESS capacity is left for the energy storage. The hybrid PV plants feed their “overflow” power into the grid, as long as the household’s consumption is satisfied and the battery has been charged. With such a storage capacity and battery power, the IPLPF costs are reasonably lower than the expected added value to the smooth PV power infeed.

IPLPF costs, based on GI measured @(48.2°N, 17.1°E) from 04/2021 to 03/2022. PV panel with azimuth=180°, elevation=47° calibrated at its maximum power point (MPPT). The applied LPF is same as on the graphs GI(t) and GX(t): 

### Predictive low-pass smoothing of PV power
***Compare the real smoothing with IPLPF***

<!---
When \(a \ne 0\), there are two solutions to \(ax^2 + bx + c = 0\) and they are
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$

`code example`
-->

