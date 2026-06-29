# Safety Documentation

> This document is required reading before any operation of the Stellagen fusor system.
> Last updated: 2026-06-28

---

## Hazard Overview

A fusor presents multiple simultaneous hazards that are each individually dangerous. All must be understood and mitigated before any powered operation.

| Hazard | Present During | Severity |
|---|---|---|
| High voltage (30–50kV) | All powered operation | ☠️ Lethal |
| X-ray emission | HV + vacuum (even without deuterium) | ⚠️ Serious |
| Neutron radiation | Deuterium runs only | ☠️ Lethal (cumulative) |
| Vacuum implosion | Any vacuum operation | ⚠️ Serious |
| Deuterium (flammable gas) | Deuterium runs only | ⚠️ Serious |
| RF interference | HV operation | ℹ️ Minor |

---

## High Voltage Safety

The fusor operates at 30–50kV DC. This is lethal at even very low currents.

### Rules — no exceptions
- **Never operate alone.** Always have another person present or on call
- **Never touch any part of the HV circuit while powered**
- **Always discharge** the HV supply through bleeder resistors before any physical contact with the system — capacitors in the supply can hold lethal charge for hours after power-off
- **One hand rule** — when working near HV, keep one hand behind your back or in your pocket. Prevents current path across the heart
- All HV connections must be **fused and interlocked** — opening any panel cuts power automatically
- HV wiring must be rated ≥50kV silicone insulation
- No floating grounds — entire chassis bonded to earth ground

### Discharge procedure
1. Power off supply
2. Wait 30 seconds minimum
3. Connect bleeder resistor from HV output to ground
4. Verify zero volts with HV probe before touching anything

---

## X-Ray Hazard

**X-rays are produced any time high voltage is applied in a vacuum — even without deuterium.** This is one of the most underestimated hazards in fusor building.

- X-rays are produced at the grid and chamber walls during all HV + vacuum operation
- Intensity increases with voltage and current
- The wooden/metal enclosure provides partial shielding — never operate with enclosure open
- Personnel should **not stand directly in line** with any viewport or port during operation
- At minimum, maintain **2 meter distance** during powered runs
- Recommended: wear a dosimeter badge during all runs and log cumulative exposure

### Shielding
- Lead sheet (1–2mm) around the chamber significantly reduces X-ray exposure
- Viewport should be leaded glass or kept perpendicular to operator position

---

## Neutron Radiation (Deuterium Runs Only)

Neutrons are produced only when running deuterium. This is the most serious radiation hazard.

- Neutrons are **not stopped by lead** — they require hydrogen-rich material (water, polyethylene)
- Surround the chamber with **4–6 inches of polyethylene sheet** or water containers during deuterium runs
- **Never run deuterium without a neutron detector present** — you need to know your dose rate
- Log all run times, voltages, currents, and estimated neutron flux
- Cumulative neutron exposure is a serious long-term health risk — keep runs short and infrequent until flux is characterized
- Required for fusor.net Neutron Club entry: verified neutron detection data

### Neutron detection methods (fusor.net accepted)
- BTI bubble dosimeter (recommended for first fusion verification)
- He-3 proportional counter
- Analog neutron meter with visible readout
- Silver activation with GM counter

---

## Vacuum Safety

- The chamber operates at pressures far below atmospheric — it contains significant stored mechanical energy
- **Never strike, drop, or apply mechanical stress** to the chamber under vacuum
- Inspect all o-rings and seals before each pump-down
- Viewports are a weak point — use borosilicate rated for vacuum service
- If any fitting makes an unusual sound during pump-down, **vent immediately**
- Vent slowly — sudden venting can crack viewports or damage the pump

---

## Deuterium Handling

- Deuterium is **flammable** — treat like hydrogen gas
- No open flames or ignition sources in the operating area
- Store cylinder secured upright, away from heat
- Use only regulators and valves rated for hydrogen/deuterium service
- Vent any leaks to outside atmosphere immediately
- Detector: a combustible gas detector near the cylinder is recommended

---

## Emergency Procedures

### HV contact
1. Do not touch the person — disconnect power at the wall first
2. Call 911
3. Begin CPR if trained and person is unresponsive

### Vacuum implosion
1. Stand clear of the chamber during all vacuum operation
2. If implosion occurs, do not approach until fully vented and HV confirmed zero
3. Treat glass/metal fragments as a laceration hazard

### Gas leak (deuterium)
1. Cut power immediately
2. Evacuate the room
3. Ventilate before re-entry
4. Do not re-enter with any ignition source

---

## Pre-Run Checklist

### Every run
- [ ] Another person present or on call
- [ ] HV interlock tested
- [ ] All fittings checked for tightness
- [ ] Bleeder resistor connected and verified
- [ ] Enclosure closed and latched
- [ ] Dosimeter worn
- [ ] 2 meter standoff distance maintained during operation
- [ ] Run logged (date, duration, voltage, current, pressure)

### Deuterium runs only
- [ ] Neutron detector present and functional
- [ ] Polyethylene shielding in place
- [ ] Gas cylinder secured
- [ ] Combustible gas detector active
- [ ] Extra person present (not just on call)

---

## References

- fusor.net safety guidelines: https://fusor.net/board/viewforum.php?f=13
- Richard Hull safety posts: fusor.net FAQ section
- NRC regulations for neutron-producing devices: https://www.nrc.gov
- NCRP Report 157 — radiation exposure limits for the public
