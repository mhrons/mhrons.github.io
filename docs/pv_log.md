# Photovoltaic intermittency and its measurement
## Impact on the grid
Intermittency of solar irradiance causes that time course of photovoltaic (PV) power generation is unstable over time. As the share of photovoltaic (PV) energy in the grid increases, the intermittency of solar power is posing still higher risk to power quality and grid's stability. To mitigate the temporary unbalance between PV infeed and power consumption, the grid operator sets PV generators off-grid (or at least to a low efficiency status) while the PV intermittency is strong. For example, the losses of intermittent PV energy were 7% in 2011 in the US state Arizona. This rate is determined by the penetration of PV energy in the grid: The higher PV penetration, the higher losses due to its intermittency. Extra grid-control costs are raised by the PV intermittency. This overall impact is expressed e.g. by the last guaranteed feed-in tariff for new PV installations in Germany: In 2020, a new feed-in tariff was only about 1/3 of the purchase tariff. The state guarantee has been canceled as of 2021, and there is no more doubt that only technical innovations can further boost the share of PV energy in the grid: Smoothing of PV power could eliminate the losses of intermitent PV energy and additional grid control costs. The smooth time course of renewable power can easily be compensated by other resources (e.g. gas- and water turbines).  
On the other hand, the loss-free PV smoothing takes up expensive accumulation capacity, otherwise usable as energy storage. **We will analyze and optimize methods for efficient and affordable smoothing of PV power on days with strong solar intermittency.**

## Measurement of global irradiance
***Accurate measurement of global irradiance (GI) is a prerequisite for PV smoothing:***  

* Accurate short-term forecasting (nowcasting) of PV power is crucial to minimize the accumulation of energy in PV power smoothing. PV power predictors have to be continuously trained by the sky-imagery and by the signal GI(t), in particular by its fraction intercepted by a tilted PV panel.
* By means of the measured signal GI(t), we can excite a low-pass filter by "ex-post predicted" input signal GIf(t+Δt), as if its GIf values were biased by a prediction error, simulating the operation of a real predictor. Given the prediction error and the desired quality of smoothed PV power, the accumulated energy by the filter has to be minimized. By optimizing the filter model, we minimize the energy accumulation hence minimize the cost of PV power smoothing.
* However low is the accumulated energy by PV smoothing, it is not for free and pays-off only if a favourable "smooth feed-in tariff" exists. Ramping limits of the smooth PV infeed should be specified by a technical standard (which currently does not exist). Once the the filter model is optimized and the prediction error is known, real accumulation costs can be aggregated, based on the measured GI signal. A trade-off between the smoothing costs and the smoothing quality, defining a corresponding reduction in the grid control costs, can be optimized. This is, how the PV ramping standard and the "smooth feed-in tariff" can be matched together.

Measurement of solar irradiance for the sake of PV smoothing must meet the folloowing demands:

- Capture the full spectrum of solar intermittency with sufficient sampling frequency
- Replicate the physical properties of planar silicon photovoltaic panels
- Measure only that fraction of incident radiation, which is intercepted by a tilted PV panel. 

![PV console](img/PV_Panels.JPG){ width="300"  align=right }

Actually, the momentary solar irradiance has to be measured at any plane of incidence under given atmospheric conditions. Fulfilling all of these demands is not possible only by measuring the global (GHI) and diffused (dHI) horizontal irradiance (both of which are regularly measured by national weather services).

A corresponding measurement system with data logger has been developed and is in operation since 04/2021 at the author's site (48.2°, 17.1°).

![PV_logger](img/PV_Logger.JPG){ width="300"  align=right }

 The system consists of 2 units:

1. external console having 4 reference PV panels fixed in different angles, and temperature sensors sticked to the panels,
2. internal measurement unit, serving as a MPPT controller, battery charger, heat sink, A/D converter, and data logger.

Here are the main system highlights:

* Four monocrystaline PV panels (sensors) are mounted at different angles. The panels are calibrated by means of Ineichen’s clear-sky model, having its Linke-turbidity factor calibrated by the reference GHI, dHI measured at the near meteorological site. The PV panels are re-calibrated once a year.
* Temperature sensors are fixed onto each PV panel. The panels are always operated at maximum output power (MPPT). Their operating point is dynamically adjusted according to the temperature drift of their A-V characteristics and internal resistance. The measured output power of each panel is then divided by its active surface area and by its (known) efficiency at given surface temperature. The measurement is finally expressed as "photovoltaic global irradiance" in W/m2 analogous to GI measured at given angle of the plane of incidence, but taking into account the spectral and optical properties of PV panels.
* Data logger operates with a dynamic sampling frequency. This captures the whole spectrum of solar intermittency, but eliminates redundancy in the stored data. The sampling period ranges from 0.5 second to 10 minutes, according to the solar intermittency. Several years of such a irregular time series can be stored in a relational database with tablespace <1TB.
* The off-grid measurement system is self-powered 24 hours x 7 days a week. Except the measurement, the PV sensors supply power to the data logger and charge its backup accumulator. The system requires a minimum maintenance.
![GI](img/GI.2022-01-15.png){ width="300"  align=right }
* Simultaneous measurement of GI in 4 fixed normal angles allows an accurate interpolation of GI at any plane of incidence pointing its normal vector among the 4 fixed normal vectors (intra-normal area).

Daily profiles (12 h) of photovoltaic GI [W/m2] measured at 4 fixed planes. GHI corresponds to the horizontal plane and extrapolated GNI corresponds to the virtually solar-tracked plane of incidence. Its normal vector points to the extra-normal area in winter while the solar elevation is lower than the elevation of the 4 fixed normal vectors. The approximated GNI is therefore less accurate in winter.
![Cels](img/Cels.2022-01-15.png){ width="300"  align=right }

Daily temperature profiles (24 h) at PV surfaces, and the ambient temperature. The PV surface's temperature is affected by the ambient temperature, solar irradiance (infrared spectrum), and by the wind. The ambient temperature is higher than the sky temperature in the night while the PV panels are cooled by their own radiation.

