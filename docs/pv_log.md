# Measurement of global irradiance
***Accurate measurement of global irradiance (GI) is a prerequisite for the analysis of PV smoothing:***  

* Accurate short-term forecasting (nowcasting) of PV power is crucial to minimize the accumulation of energy by the PV power smoothing. PV power predictors are based on artificial intelligence (AI) and they can be trained by a sky-imagery and by the measured signal GI(t), in particular its fraction intercepted by a tilted PV panel.
* Using the measured time series GI(t), we can "ex-post" excite the low-pass filter by a "predicted" input signal GI~f~(t+Δt). That is, the measured signal is shifted to the left and its values are artificially biased by the simulated prediction error, simulating its real prediction. Given the predicted signal and a desired ramping limit of the smoothed PV power, the accumulated energy by the filter should be minimized, hence minimized costs of the PV power smoothing.
* However low is the accumulated energy by smoothing, it is not for free. The smoothing pays-off only with a favourable "smooth feed-in tariff" which should be legalized by a technical standard, defining the power ramping limits to be met by those PV plants having a favourable feed-in tariff granted. This keeps the grid control costs within the specified limit, and on the other hand, the PV power infeed does not exceed the allowed ramping up/down limits. Having the filter model optimized for the standard, the accumulation rate and the corresponding smoothing cost can be aggregated by means of the measured GI signal. The ramping limit can be further iterated in order to maximize the difference "reduction in the grid control costs due to smoothing" minus "smoothing costs". This is, how the PV ramping limits and the corresponding "smooth feed-in tariff" can be optimized.

Measurement of solar irradiance for the analysis of PV smoothing must meet the folloowing demands:

- Capture the full spectrum of solar intermittency using sufficient sampling frequency
- Measure the fraction of irradiance which is intercepted by a tilted plane of incidence. 
- Respect the physical properties of planar silicon PV panels (reflexion and spectral response)

![PV console](img/PV_Panels.JPG){ width="300"  align=right }

In general, the momentary solar irradiance has to be measured at any plane of incidence under given atmospheric conditions. Fulfilling all of these demands is not possible only by measuring the global (GHI) and diffused (dHI) horizontal irradiance (both of which are regularly measured by national weather services).

A corresponding measurement system with data logger has been developed and is in operation since 04/2021 at the author's site (48.2°, 17.1°).

![PV_logger](img/PV_Logger.JPG){ width="300"  align=right }

 The system consists of 2 units:

1. external console carrying 4 reference PV panels mounted in different angles, and temperature sensors sticked on the panels,
2. internal measurement unit, serving as a MPPT controller, battery charger, heat sink, A/D converter, and data logger.

## System features

* The reference monocrystaline silicon PV panels (sensors) have been calibrated by means of 
[Ineichen’s clear-sky model](https://pvlib-python.readthedocs.io/en/v0.4.3/generated/pvlib.clearsky.ineichen.html)
, having its 
[Linke-turbidity factor](https://glossary.ametsoc.org/wiki/Linke_turbidity_factor)
 calibrated by the reference GHI, dHI measured at the near meteorological site. The PV panels are re-calibrated once a year.
* Temperature sensors are fixed onto each PV panel. The panels are always operated at the
[maximum output power (MPPT)](https://www.leonics.com/support/article2_14j/articles2_14j_en.php)
. Their operating point is being dynamically adjusted for the temperature drift of their A-V characteristics and for their internal resistance. The measured output power of each panel is divided by its active surface area and by its (known) efficiency at given surface temperature. The measurement is eventually expressed as "photovoltaic global irradiance" in W/m2 analogous to GI measured at given angle of the plane of incidence, but taking into account the reflexion and spectral response of PV panels.
* Data logger samples GI with a dynamic frequency. The sampling period ranges from 0.5 second to 10 minutes, according to the solar intermittency. This captures the whole spectrum of solar intermittency, but eliminates the redundancy in stored data. Several years of such an irregular time series can be stored in a relational database with tablespace <1TB.
* The off-grid measurement system is self-powered 24 hours x 7 days a week. In addition to measurement, the PV sensors supply power to the data logger and charge its backup accumulator. The system requires a minimum maintenance.
![GI](img/GI.2022-01-15.png){ width="300"  align=right }
* Simultaneous measurement of GI in 4 fixed normal angles allows an accurate interpolation of GI at any plane of incidence pointing its normal vector among the 4 fixed normal vectors (intra-normal area).

Daily (12 h) profiles of photovoltaic GI [W/m2] measured at 4 fixed planes. GHI corresponds to the horizontal plane and extrapolated GNI corresponds to a virtual solar-tracked plane of incidence. Its normal vector points to the extra-normal area in winter while the solar elevation is lower than the elevation of the 4 fixed normal vectors. The approximated GNI is therefore less accurate in winter.
![Cels](img/Cels.2022-01-15.png){ width="300"  align=right }

Daily (24 h) temperature profiles at PV surfaces, and the ambient temperature. The PV surface's temperature is affected by the ambient temperature, solar radiation, and by the wind. The ambient temperature is higher than the sky temperature, so the PV panels are always cooled by their own radiation. This effect can be observed in the night when the panels are not exposed to solar radiation.

