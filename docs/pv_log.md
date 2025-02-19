# Measurement of global irradiance
***Accurate measurement of the global irradiance (GI) is a prerequisite for the analysis of PV smoothing:***  

* Accurate nowcasting of PV power is crucial when shrinking the accumulation of energy by the PV power smoothing. PV power predictors are based on artificial intelligence (AI) and they can be trained by a sky-imagery and by the measured signal GI(t), in particular its fraction intercepted by a tilted PV panel.
* Having the measured time series GI(t), a low-pass filter can be ex-post excited by a "predicted" input signal GI~f~(t+Δt). That is, the measured signal is shifted to the left on its time axis and its values are optionally distorted by a simulated prediction error. Given such a predicted PV power signal and having the LPF tuned to meet the given ramping limit of PV power, the accumulated energy by filter should be then minimized such that the smoothing costs are minimized.

Following demands should be met by the measurement of solar irradiance for the analysis of PV smoothing:  

- Capture the full spectrum of solar intermittency with a sufficiently high sampling frequency
- Measure the fraction of irradiance which is intercepted by a tilted plane of incidence (PV panel). 
- Respect the physical properties of planar silicon PV panels (reflexion and spectral response)

![PV console](img/PV_Panels.JPG){ width="300"  align=right }

For general purposes, the momentary solar irradiance has to be measured at any plane of incidence under given atmospheric conditions. Fulfilling of all these demands is not possible only by measuring the global (GHI) and diffused (dHI) horizontal irradiance (both of them are measured by the national weather services).

A corresponding measurement system with a data logger has been developed and installed at the author's site (48.2°, 17.1°) and is in operation since 04/2021.

![PV_logger](img/PV_Logger.JPG){ width="300"  align=right }

 The system consists of 2 units:

1. external console carrying 4 reference PV panels mounted at different angles, and with temperature sensors sticked onto PV panels,
2. internal measurement unit serving as a MPPT controller, A/D converter of measured PV power and temperature, data logger, battery charger, heat sink.

## System features

* The reference monocrystaline silicon PV panels (sensors) are calibrated by means of 
[Ineichen/Perez clear-sky model](https://pvlib-python.readthedocs.io/en/v0.4.3/generated/pvlib.clearsky.ineichen.html)
, having its 
[Linke-turbidity factor](https://glossary.ametsoc.org/wiki/Linke_turbidity_factor)
 calibrated by the reference GHI, dHI measured at the near meteorological site. The PV panels are re-calibrated once a year.
* Temperature sensors are fixed onto each PV panel. The panels are always operated at their
[maximum output power (MPPT)](https://www.leonics.com/support/article2_14j/articles2_14j_en.php)
. Their optimum operating point is dynamically adjusted according to the insolation and the temperature drift of their V-I characteristic. The measured output power of each panel is divided by its active surface area and by its (known) efficiency at the measured surface temperature. The result is eventually expressed as a "photovoltaic global irradiance" in W/m^2^ analogous to GI measured at given angle of the plane of incidence, but taking into account the reflexion and spectral response of PV panels.
* The data logger samples GI values with a dynamic frequency. The sampling period varies from 0.5 second to 10 minutes, depending on the momentary solar intermittency. The whole spectrum of solar intermittency is captured and stored without redundancy. Several years of such a irregular time series occupy <1GB of storage.
* The off-grid measurement system is self-powered 24 hours x 7 days a week. In addition to measurement, the PV sensors supply power to the data logger and charge its backup battery. The system requires a minimum maintenance.
![GI](img/GI.2022-01-15.png){ width="300"  align=right }
* Simultaneous measurement of GI in 4 fixed normal angles allows an accurate interpolation of GI at any plane of incidence pointing its normal vector among the fixed normal vectors (intra-normal area).

Daily (12 h) profiles of photovoltaic GI [W/m2] measured at 4 fixed planes. GHI corresponds to the horizontal plane of incidence while the extrapolated GNI corresponds to a virtual solar-tracked normal plane of incidence. Its normal vector points to the extra-normal area in winter when the solar elevation is lower than the elevation of the four fixed normal vectors. The approximated GNI is therefore less accurate in winter.
![Cels](img/Cels.2022-01-15.png){ width="300"  align=right }

Daily (24 h) temperature profiles at PV surfaces, and the ambient temperature. The PV surface's temperature is affected by the ambient temperature, solar radiation, and by wind. Since the ambient temperature is higher than the sky temperature, the PV panels are always cooled by their own radiation. This effect can be observed in the night when the panels are not exposed to the solar radiation.

