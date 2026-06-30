# Fusor Chamber Design - CAD Project

## Overview
This repository contains the CAD design files for a high-vacuum fusor chamber. The project focuses on a modular dome-based design featuring standardized ISO-KF flange interfaces for vacuum-tight connectivity and diagnostic port alignment.

## Project Structure
- `H1_Dome.f3d`: Primary CAD assembly for the top dome component.
- `Flange_KF40.f3d`: Standardized KF-40 vacuum flange geometry.
- `Flange_KF16.f3d`: Standardized KF-16 vacuum flange geometry.
- `Construction_Reference/`: Auxiliary construction planes and axes used for port alignment.

## Technical Specifications

### Flange Standards
- **KF-40 (NW-40):** Used for primary vacuum and feedthrough ports.
  - Outer Diameter: 55 mm
  - Bore: 40 mm
  - Seal Interface: 15° tapered lip for standard clamps.
- **KF-16 (NW-16):** Used for auxiliary diagnostic/gas ports.
  - Outer Diameter: 30 mm
  - Bore: 17.2 mm

### Design Features
- **Radial Symmetry:** 8-hole circular pattern on the base flange for standard vacuum hardware.
- **Radial Alignment:** Construction planes generated at 120° intervals to ensure port alignment through the spherical surface of the dome.
- **3D Sketch Integration:** Uses 3D sketch paths to define normal vectors for tangentially aligned flange ports.

## Usage Notes for Development
- **Timeline Management:** The design is parametric. If modifications are required, navigate the Timeline at the bottom of the workspace. Ensure all sketches are "Finished" to interact with the timeline marker.
- **Adding Ports:** To add new ports, create a "Tangent Plane" at the desired surface point, then use "Plane Through Point and Axis" to orient the plane normal to the dome's center.
- **Parametric Updates:** Standard dimensions for KF flanges are stored as user parameters; modify the `Parameters` table to adjust bore sizes globally.

## Future Development
- Integrate inner grid structure.
- Add assembly constraints for vacuum gaskets and centering rings.
- Conduct stress analysis on the dome-to-flange junctions.
