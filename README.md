# stellagen-fusor

A DIY inertial electrostatic confinement (IEC) fusor designed for deuterium-deuterium fusion and neutron production. Named after Philo T. Farnsworth, the inventor of the fusor.

---
Thank you to Fusion 360 and IdeaBuilder for your wonderful software!


## main chamber

Spherical stainless steel vacuum chamber, split at the equator into two hemispheres joined by an ISO-F flange. Each hemisphere has a **5-inch diameter mouth**. The 2 hemispheres will be connected by 8 bolts.

The ports have been symmetrically distributed to maximize TIG welding clearance and simplify physical component layout.

### hemisphere 1 (power & vacuum side)
- **HV feedthrough** — negative, connects to inner grid (cathode); centered on top axis.
- **Vacuum pump port** — KF-25 or KF-40 fitting pointing downward to the roughing/turbo pump manifold.
- **atmo port** — KF-16 flange, blanked off during normal operation (usable for vacuum system venting).
- - **Maitnance port** — KF-40 flange, used for samples or maitnance of reactor cage

### hemisphere 2 (diagnostics, gas, & view side)
- **Viewport** — Borosilicate glass viewport for plasma observation (with external lead-glass X-ray shielding).
- **Deuterium feed** — Metered gas inlet with needle valve to bleed process gas away from the main vacuum throat.
- **Vacuum gauge port** — KF-16 flange hosting a Pirani or thermocouple gauge for clean chamber pressure monitoring.
- **External thermocouple** — Monitors chamber wall temperature during runs.
- **2x copper water block** — Custom concave-machined liquid cooling blocks direct-mounted to the exterior wall.

> Note: The chamber wall itself serves as the anode and is grounded. No dedicated positive feedthrough is required.

---

## high voltage system

- Target voltage: **30–50kV DC negative** at the central grid
- Supply: flyback transformer driven by ZVS driver, or neon sign transformer
- Central grid: spherical cage wound from **316 stainless steel wire**

---

## vacuum system

| Stage | Component | Target Pressure |
|---|---|---|
| Rough vacuum | Two-stage rotary vane pump | ~10⁻² torr |
| High vacuum | Turbomolecular pump (optional) | ~10⁻⁴ torr |
| Measurement | Pirani gauge | continuous monitoring |

---

## cooling system

Active liquid cooling for sustained run capability, mounted on hemisphere 2.

- **2x custom copper water blocks** with a 2.5-inch concave radius direct-mounted to chamber exterior
- Circulated via standard PC liquid cooling loop (Reservoir → Pump → Heat Exchanger → Radiator → Reservoir)
- **4-fan radiator** mounted externally on enclosure
- Coolant: distilled water + corrosion inhibitor

Cooling is required at power inputs above ~500W to prevent chamber wall thermal stress and o-ring degradation at the ISO-F joint.

---

## ports summary

| Port | Hemisphere | Type | Purpose |
|---|---|---|---|
| **HV feedthrough** | H1 | Ceramic/PTFE | Cathode grid connection |
| **Pump port** | H1 | KF-25 or KF-40 | Vacuum system throat |
| **Aux/Spare port** | H1 | KF-16 | System venting / expansion |
| **Viewport** | H2 | Borosilicate/Lead-Glass | Plasma observation |
| **Gas inlet** | H2 | KF-16 + needle valve | Deuterium feed |
| **Gauge port** | H2 | KF-16 | Pirani gauge chamber pressure |
| **Thermocouple** | H2 | External surface mount | Wall temp monitoring |

---

## safety

- All HV connections fused and interlocked
- Enclosure grounded
- Neutron and X-ray shielding required during deuterium runs (Lead-glass viewport shroud mandatory)
- Bleeder resistors on HV supply for safe discharge
- Never operate above 10⁻² torr with HV applied

---

## status

- [ ] Chamber design complete
- [ ] Vacuum system sourced
- [ ] HV supply built and tested
- [ ] First plasma (air) — Plasma Club entry
- [ ] Deuterium sourced
- [ ] First fusion — Neutron Club entry
