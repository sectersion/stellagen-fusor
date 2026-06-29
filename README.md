# stellagen-fusor

A DIY inertial electrostatic confinement (IEC) fusor designed for deuterium-deuterium fusion and neutron production. Named after Philo T. Farnsworth, the inventor of the fusor.

---

## main chamber

Spherical stainless steel vacuum chamber, split at the equator into two hemispheres joined by an ISO-F flange. Each hemisphere has a **5-inch diameter mouth**.

### hemisphere 1 (cathode side)
- **HV feedthrough** — negative, connects to inner grid (cathode)
- **Deuterium feed** — metered gas inlet with needle valve
- **Vacuum pump port** — KF-25 or KF-40 fitting to roughing/turbo pump
- **Vacuum gauge port** — external Pirani or thermocouple gauge (sensor tip exposed to chamber interior, electronics external)

### hemisphere 2 (anode side)
- **Viewport** — borosilicate glass viewport for plasma observation
- **External thermocouple** — monitors chamber wall temperature during runs
- **2x copper water block** — direct-mount liquid cooling on exterior wall

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

- **2x custom copper water blocks** direct-mounted to chamber exterior
- Circulated via standard PC liquid cooling loop
- **4-fan radiator** mounted externally on enclosure
- Coolant: distilled water + corrosion inhibitor

Cooling is required at power inputs above ~500W to prevent chamber wall thermal stress and o-ring degradation at the ISO-F joint.

---

## ports summary

| Port | Hemisphere | Type | Purpose |
|---|---|---|---|
| HV feedthrough | H1 | Ceramic/PTFE | Cathode grid connection |
| Gas inlet | H1 | KF-16 + needle valve | Deuterium feed |
| Pump port | H1 | KF-25 or KF-40 | Vacuum system |
| Gauge port | H1 | KF-16 | Pirani gauge |
| Viewport | H2 | Borosilicate | Plasma observation |
| Thermocouple | H2 | External surface mount | Wall temp monitoring |

---

## safety

- All HV connections fused and interlocked
- Enclosure grounded
- Neutron and X-ray shielding required during deuterium runs
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
