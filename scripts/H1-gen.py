import adsk.core, adsk.fusion, adsk.cam, traceback, math

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        rootComp = design.rootComponent
        userParams = design.userParameters

        # ---- pull values from the imported user parameters ----
        # (these must already exist in your parameter table)
        def p(name):
            param = userParams.itemByName(name)
            if param is None:
                raise Exception(f"Missing parameter: {name}")
            return param.value  # returns value in cm (internal Fusion units)

        chamber_ID = p('chamber_ID')
        wall_thk = p('wall_thk')
        chamber_OD = p('chamber_OD')
        mouth_dia = p('mouth_dia')
        flange_face_thk = p('flange_face_thk')
        flange_OD = p('flange_OD')
        bolt_circle_dia = p('bolt_circle_dia')
        bolt_hole_dia = p('bolt_hole_dia')
        hv_boss_dia = p('hv_boss_dia')
        kf40_boss_dia = p('kf40_boss_dia')
        kf16_boss_dia = p('kf16_boss_dia')
        port_stub_len = p('port_stub_len')
        # NOTE: 'deg' unit parameters come back from p() already in radians
        # (Fusion's internal angle unit), so use them directly - no conversion needed.
        atmo_lat = p('atmo_lat')
        atmo_az = p('atmo_az')
        maint_lat = p('maint_lat')
        maint_az = p('maint_az')

        # Pump port placement (not in CSV - hardcoded here since it's a fixed design choice)
        pump_lat = math.radians(75)
        pump_az = math.radians(90)

        sphere_R_outer = chamber_OD / 2.0
        sphere_R_inner = chamber_ID / 2.0

        # ---- new component ----
        occs = rootComp.occurrences
        newOcc = occs.addNewComponent(adsk.core.Matrix3D.create())
        h1 = newOcc.component
        h1.name = 'H1_power_vacuum_hemisphere'

        sketches = h1.sketches
        xzPlane = h1.xZConstructionPlane
        xyPlane = h1.xYConstructionPlane

        # =========================================================
        # 1. SHELL: revolve a half-annulus profile around the Z axis
        #    to create the hollow hemisphere dome (Z >= 0, pole at +Z)
        # =========================================================
        shellSketch = sketches.add(xzPlane)
        lines = shellSketch.sketchCurves.sketchLines
        arcs = shellSketch.sketchCurves.sketchArcs
        origin = adsk.core.Point3D.create(0, 0, 0)

        # outer arc from equator (x=R_outer,z=0) to pole (x=0,z=R_outer)
        outerArc = arcs.addByCenterStartSweep(
            origin,
            adsk.core.Point3D.create(sphere_R_outer, 0, 0),
            math.pi / 2
        )
        # inner arc from equator (x=R_inner,z=0) to pole (x=0,z=R_inner)
        innerArc = arcs.addByCenterStartSweep(
            origin,
            adsk.core.Point3D.create(sphere_R_inner, 0, 0),
            math.pi / 2
        )
        # close the profile: equator edge and pole edge
        lines.addByTwoPoints(adsk.core.Point3D.create(sphere_R_inner, 0, 0),
                              adsk.core.Point3D.create(sphere_R_outer, 0, 0))
        lines.addByTwoPoints(adsk.core.Point3D.create(0, 0, sphere_R_inner),
                              adsk.core.Point3D.create(0, 0, sphere_R_outer))

        prof = shellSketch.profiles.item(0)
        revolves = h1.features.revolveFeatures
        zAxis = h1.zConstructionAxis
        revInput = revolves.createInput(prof, zAxis, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        revInput.setAngleExtent(False, adsk.core.ValueInput.createByReal(2 * math.pi))
        revFeature = revolves.add(revInput)
        shellBody = revFeature.bodies.item(0)
        shellBody.name = 'H1_shell'

        # =========================================================
        # 2. EQUATOR FLANGE: ring at Z=0, OD = flange_OD,
        #    ID = mouth_dia, thickness = flange_face_thk, extruded down (-Z)
        # =========================================================
        flangeSketch = sketches.add(xyPlane)
        circles = flangeSketch.sketchCurves.sketchCircles
        circles.addByCenterRadius(origin, flange_OD / 2.0)
        circles.addByCenterRadius(origin, mouth_dia / 2.0)
        flangeProf = None
        for pr in flangeSketch.profiles:
            # the ring profile is the one with 2 loops
            if pr.profileLoops.count == 2:
                flangeProf = pr
                break

        extrudes = h1.features.extrudeFeatures
        flangeInput = extrudes.createInput(flangeProf, adsk.fusion.FeatureOperations.JoinFeatureOperation)
        flangeInput.setOneSideExtent(
            adsk.fusion.DistanceExtentDefinition.create(adsk.core.ValueInput.createByReal(-flange_face_thk)),
            adsk.fusion.ExtentDirections.NegativeExtentDirection
        )
        # join into the shell body
        flangeInput.participantBodies = [shellBody]
        extrudes.add(flangeInput)

        # ---- 8-bolt hole pattern on the flange ----
        boltSketch = sketches.add(xyPlane)
        boltCircles = boltSketch.sketchCurves.sketchCircles
        boltHoleCenter = adsk.core.Point3D.create(bolt_circle_dia / 2.0, 0, 0)
        firstHole = boltCircles.addByCenterRadius(boltHoleCenter, bolt_hole_dia / 2.0)

        boltExtrudes = h1.features.extrudeFeatures
        boltProf = boltSketch.profiles.item(0)
        boltInput = boltExtrudes.createInput(boltProf, adsk.fusion.FeatureOperations.CutFeatureOperation)
        boltInput.setOneSideExtent(
            adsk.fusion.DistanceExtentDefinition.create(adsk.core.ValueInput.createByReal(-flange_face_thk)),
            adsk.fusion.ExtentDirections.NegativeExtentDirection
        )
        boltInput.participantBodies = [shellBody]
        boltFeature = boltExtrudes.add(boltInput)

        # circular pattern x8 around Z axis
        circularPatterns = h1.features.circularPatternFeatures
        entities = adsk.core.ObjectCollection.create()
        entities.add(boltFeature)
        patInput = circularPatterns.createInput(entities, zAxis)
        patInput.quantity = adsk.core.ValueInput.createByReal(8)
        patInput.totalAngle = adsk.core.ValueInput.createByReal(2 * math.pi)
        patInput.isSymmetric = False
        circularPatterns.add(patInput)

        # =========================================================
        # 3. PORT BOSS HELPER FUNCTION
        #    Builds a cylindrical weld-stub boss + through-bore at
        #    a given latitude (from pole, radians) and azimuth
        #    (around Z axis, radians).
        # =========================================================
        def build_port(name, lat, az, boss_dia):
            # direction vector from sphere center to the port location
            dx = math.sin(lat) * math.cos(az)
            dy = math.sin(lat) * math.sin(az)
            dz = math.cos(lat)
            dirVec = adsk.core.Vector3D.create(dx, dy, dz)
            dirVec.normalize()

            surfacePt = adsk.core.Point3D.create(dx * sphere_R_outer, dy * sphere_R_outer, dz * sphere_R_outer)
            outerPt = adsk.core.Point3D.create(dx * (sphere_R_outer + port_stub_len),
                                                dy * (sphere_R_outer + port_stub_len),
                                                dz * (sphere_R_outer + port_stub_len))

            # 3D sketch line from origin through the surface point, extended outward,
            # used purely as a construction axis for the port direction
            sk3d = sketches.add(xyPlane)  # plane choice irrelevant; we use 3D sketch points
            sk3d.isComputeDeferred = True
            pts = sk3d.sketchPoints
            p0 = pts.add(origin)
            p1 = pts.add(outerPt)
            axisLine = sk3d.sketchCurves.sketchLines.addByTwoPoints(p0, p1)
            sk3d.isComputeDeferred = False

            # construction plane perpendicular to that line, at the outer end point
            planes = h1.constructionPlanes
            planeInput = planes.createInput()
            planeInput.setByNormalToCurveAtPoint(axisLine, axisLine.endSketchPoint)
            portPlane = planes.add(planeInput)
            portPlane.name = f'{name}_plane'

            # sketch the boss circle + bore circle on that plane
            portSketch = sketches.add(portPlane)
            portCircles = portSketch.sketchCurves.sketchCircles
            planeOrigin = adsk.core.Point3D.create(0, 0, 0)
            portCircles.addByCenterRadius(planeOrigin, boss_dia / 2.0)

            portProf = portSketch.profiles.item(0)
            portExtrudes = h1.features.extrudeFeatures
            portInput = portExtrudes.createInput(portProf, adsk.fusion.FeatureOperations.JoinFeatureOperation)
            portInput.setSymmetricExtent(adsk.core.ValueInput.createByReal(port_stub_len), False)
            portInput.participantBodies = [shellBody]
            portExtrudes.add(portInput)

            return portPlane, surfacePt

        # =========================================================
        # 4. BUILD THE FOUR H1 PORTS
        # =========================================================
        build_port('HV_feedthrough', 0.0, 0.0, hv_boss_dia)
        build_port('Pump_port', pump_lat, pump_az, kf40_boss_dia)
        build_port('Atmo_vent', atmo_lat, atmo_az, kf16_boss_dia)
        build_port('Maintenance', maint_lat, maint_az, kf40_boss_dia)

        ui.messageBox('H1 hemisphere built successfully.')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
