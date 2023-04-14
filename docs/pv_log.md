# Photovoltaic intermittency and its measurement
## Impact on the grid
Intermittency of solar irradiance causes that time course of photovoltaic (PV) power generation is unstable over time. As the share of PV energy in the grid increases, the intermittency of solar power is posing still higher risk to power quality and grid's stability. To mitigate the temporary unbalance between PV infeed and power consumption, a grid operator sets PV generators off-grid (or at least to a low efficiency status) while the solar intermittency is strong. For example, the losses of intermittent PV energy were 7% in 2011 in the US state Arizona. This loss-rate is determined by the unforecasted solar intermittency and by the penetration of PV energy in the grid: The higher PV penetration, the higher relative(!) losses due to the intermittency. Extra grid-control costs are raised by the PV intermittency. This overall impact is expressed e.g. by the last guaranteed feed-in tariff for new PV installations in Germany: In 2020, a new feed-in tariff was only about 1/3 of the purchase tariff. The state guarantee has been canceled as of 2021, and there is no more doubt that only technical innovations can further boost the share of PV energy in the grid: Smoothing of PV power could eliminate the losses of intermitent PV energy and additional grid control costs. A smooth time course of renewable power can easily be complemented by other resources (e.g. gas- and water turbines), which is impossible with the rapidly-intermittent renewable power.  
On the other hand, the loss-free PV smoothing takes up expensive accumulation capacity, otherwise usable as energy storage. **We will analyze and optimize the application of a low-pass filter for smoothing PV power on days with solar intermittency.**

## Measurement of global irradiance
***Accurate measurement of global irradiance (GI) is a prerequisite for PV smoothing:***  

* Accurate short-term forecasting (nowcasting) of PV power is crucial to minimize the accumulation of energy in PV power smoothing. PV power predictors are based on artificial intelligence (AI) and they can be trained by a sky-imagery and by the measured signal GI(t), in particular by its fraction intercepted by a tilted PV panel.
* By means of the measured signal GI(t), we can excite a low-pass filter by "ex-post predicted" input signal GIf(t+Δt), as if its GIf values were the meassured values biased by a simulated prediction error. Given the predicted signal and the desired quality of smoothed PV power, the accumulated energy by the filter should be minimized. By optimizing the filter model, the energy accumulation hence the cost of PV power smoothing can be minimized.
* However low is the accumulated energy by PV smoothing, it is not for free and pays-off only if a favourable tariff is paid for the smooth PV infeed. Maximum limits of PV power ramping should be specified by a technical standard. Once the filter model is optimized to meet the ramping limits and the prediction error is known, real accumulation costs can be aggregated, based on the measured GI signal. There is clearly a trade-off between the cost of smoothing and its quality that allows a corresponding reduction in the grid control costs. Using the measured signal GI(t), it is possible to optimally match the PV ramping standard with the "smooth PV feed-in tariff".

Measurement of solar irradiance for the sake of PV smoothing must meet the folloowing demands:

- Capture the full spectrum of solar intermittency with sufficient sampling frequency
- Replicate the physical properties of planar silicon photovoltaic panels
- Measure only that fraction of incident radiation, which is intercepted by a tilted PV panel. 

![PV console](img/PV_Panels.JPG){ width="300"  align=right }

Actually, the momentary solar irradiance has to be measured at any plane of incidence under given atmospheric conditions. Fulfilling all of these demands is not possible only by measuring the global (GHI) and diffused (dHI) horizontal irradiance (both of which are regularly measured by national weather services).

A corresponding measurement system with data logger has been developed and is in operation since 04/2021 at the author's site (48.2°, 17.1°).

![PV_logger](img/PV_Logger.JPG){ width="300"  align=right }

 The system consists of 2 units:

1. external console carrying 4 reference PV panels fixed in different angles, and temperature sensors sticked to the panels,
2. internal measurement unit, serving as a MPPT controller, battery charger, heat sink, A/D converter, and data logger.

Here are the main system highlights:

* Four monocrystaline PV panels (sensors) are mounted at different angles. The panels are calibrated by means of 
[Ineichen’s clear-sky model](https://pvlib-python.readthedocs.io/en/v0.4.3/generated/pvlib.clearsky.ineichen.html)
, having the 
[Linke-turbidity factor](https://glossary.ametsoc.org/wiki/Linke_turbidity_factor)
 calibrated by the reference GHI, dHI measured at the near meteorological site. The PV panels are re-calibrated once a year.
* Temperature sensors are fixed onto each PV panel. The panels are always operated at 
[maximum output power (MPPT)](https://www.leonics.com/support/article2_14j/articles2_14j_en.php)
. Their operating point is dynamically adjusted to follow to the temperature drift of their A-V characteristics and internal resistance. The measured output power of each panel is further divided by its active surface area and by its (known) efficiency at given surface temperature. The measurement is finally expressed as "photovoltaic global irradiance" in W/m2 analogous to GI measured at given angle of the plane of incidence, but taking into account the spectral and optical properties of PV panels.
* Data logger operates with a dynamic sampling frequency. This captures the whole spectrum of solar intermittency, but eliminates redundancy in the stored data. The sampling period ranges from 0.5 second to 10 minutes, according to the solar intermittency. Several years of such a irregular time series can be stored in a relational database with tablespace <1TB.
* The off-grid measurement system is self-powered 24 hours x 7 days a week. Except the measurement, the PV sensors supply power to the data logger and charge its backup accumulator. The system requires a minimum maintenance.
![GI](img/GI.2022-01-15.png){ width="300"  align=right }
* Simultaneous measurement of GI in 4 fixed normal angles allows an accurate interpolation of GI at any plane of incidence pointing its normal vector among the 4 fixed normal vectors (intra-normal area).

Daily profiles (12 h) of photovoltaic GI [W/m2] measured at 4 fixed planes. GHI corresponds to the horizontal plane and extrapolated GNI corresponds to the virtually solar-tracked plane of incidence. Its normal vector points to the extra-normal area in winter while the solar elevation is lower than the elevation of the 4 fixed normal vectors. The approximated GNI is therefore less accurate in winter.
![Cels](img/Cels.2022-01-15.png){ width="300"  align=right }

Daily temperature profiles (24 h) at PV surfaces, and the ambient temperature. The PV surface's temperature is affected by the ambient temperature, solar irradiance, and by the wind. The ambient temperature is higher than the sky temperature, so the PV pnales are always cooled by their own radiation. This effect can be observed in the night when the panels are not exposed to solar radiation.

