# Measurement of global irradiance
***Accurate measurement of global irradiance (GI) is a prerequisite for the analysis of PV smoothing:***  

* Accurate short-term forecasting (nowcasting) of PV power is crucial when minimizing the accumulated energy by the PV power smoothing. PV power predictors are based on artificial intelligence (AI) and they can be trained by a sky-imagery and by the measured signal GI(t), in particular its fraction intercepted by a tilted PV panel.
* Having the measured time series GI(t), a low-pass filter can be ex-post excited by a "predicted" input signal GI~f~(t+Δt). That is, the measured signal is shifted to the left on its time axis and its values are biased with a simulated prediction error. Given the simulated-predicted PV power signal and having LPF tuned to meet the given ramping limit of PV power, the accumulated energy by filter should be then minimized by technical means to minimize the smoothing cost.
* However low is the accumulated energy, the smoothing is not for free and it pays-off only with a favourable "smooth feed-in tariff" granted to those prosumers who meet the requested PV ramping limits. The goal is to keep the sum "grid control costs" plus "PV power losses due to curtailment" plus "PV smoothing costs" at minimum. Given the PV ramping limit and having the measured signal GI(t) over a time span of 1+ year and its prediction error, the accumulation rate hence the smoothing cost can be aggregated. The minimum criterion can be eventually iterated unless the PV ramping limit is optimized.

Folloowing demands should be met by the measurement of solar irradiance for the analysis of PV smoothing:  

- Capture the full spectrum of solar intermittency by a sufficiently high sampling frequency
- Measure the fraction of irradiance which is intercepted by a tilted plane of incidence (PV panel). 
- Respect the physical properties of planar silicon PV panels (reflexion and spectral response)

![PV console](img/PV_Panels.JPG){ width="300"  align=right }

For general purposes, the momentary solar irradiance has to be measured at any plane of incidence under given atmospheric conditions. Fulfilling all of these demands is not possible only by measuring the global (GHI) and diffused (dHI) horizontal irradiance (both of which are regularly measured by the national weather services).

A corresponding measurement system with data logger has been developed by the author and is in operation since 04/2021 at (48.2°, 17.1°).

![PV_logger](img/PV_Logger.JPG){ width="300"  align=right }

 The system consists of 2 units:

1. external console carrying 4 reference PV panels mounted at different angles, and temperature sensors of PV panels,
2. internal measurement unit, serving as MPPT controller, battery charger, heat sink, A/D converter, and data logger.

## System features

* The reference monocrystaline silicon PV panels (sensors) have been calibrated by means of 
[Ineichen’s clear-sky model](https://pvlib-python.readthedocs.io/en/v0.4.3/generated/pvlib.clearsky.ineichen.html)
, having its 
[Linke-turbidity factor](https://glossary.ametsoc.org/wiki/Linke_turbidity_factor)
 calibrated by the reference GHI, dHI measured at the near meteorological site. The PV panels are re-calibrated once a year.
* Temperature sensors are fixed onto each PV panel. The panels are always operated at the
[maximum output power (MPPT)](https://www.leonics.com/support/article2_14j/articles2_14j_en.php)
. Their operating point is being dynamically adjusted for the temperature drift of their A-V characteristics and internal resistance. The measured output power of each panel is divided by its active surface area and by its (known) efficiency at the measured surface temperature. The measurement is eventually expressed as "photovoltaic global irradiance" in W/m^2^ analogous to GI measured at given angle of the plane of incidence, but taking into account the reflexion and spectral response of PV panels.
* The data logger samples GI values with a dynamic frequency. The sampling period varies from 0.5 second to 10 minutes, depending on the momentary solar intermittency. This captures the whole spectrum of solar intermittency, but eliminates the redundancy in stored data. Several years of such an irregular time series can be stored in a relational database with tablespace <1TB.
* The off-grid measurement system is self-powered 24 hours x 7 days a week. In addition to measurement, the PV sensors supply power to the data logger and charge its backup accumulator. The system requires a minimum maintenance.
![GI](img/GI.2022-01-15.png){ width="300"  align=right }
* Simultaneous measurement of GI in 4 fixed normal angles allows an accurate interpolation of GI at any plane of incidence pointing its normal vector among the fixed normal vectors (intra-normal area).

Daily (12 h) profiles of photovoltaic GI [W/m2] measured at 4 fixed planes. GHI corresponds to the horizontal plane while extrapolated GNI corresponds to a virtual solar-tracked plane of incidence. Its normal vector points to the extra-normal area in winter when the solar elevation is lower than the elevation of the four fixed normal vectors. The approximated GNI is therefore less accurate in winter.
![Cels](img/Cels.2022-01-15.png){ width="300"  align=right }

Daily (24 h) temperature profiles at PV surfaces, and the ambient temperature. The PV surface's temperature is affected by the ambient temperature, solar radiation, and by wind. Since ambient temperature is higher than sky temperature, the PV panels are always cooled by their own radiation. This effect can be observed in the night when the panels are not exposed to the solar radiation.

