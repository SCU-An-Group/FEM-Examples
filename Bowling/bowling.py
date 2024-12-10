# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from optimization import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

Mdb()

#MODEL
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Model-1'].sketches['__profile__'].ArcByCenterEnds(center=(0.0, 0.0)
    , direction=COUNTERCLOCKWISE, point1=(0.0, -0.105), point2=(0.0, 0.105))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, -0.105), 
    point2=(0.0, 0.105))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='ball', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['ball'].BaseSolidRevolve(angle=360.0, 
    flipRevolveDirection=OFF, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['ball'].DatumPlaneByPrincipalPlane(offset=0.0, 
    principalPlane=XYPLANE)
mdb.models['Model-1'].parts['ball'].DatumPlaneByPrincipalPlane(offset=0.0, 
    principalPlane=YZPLANE)
mdb.models['Model-1'].parts['ball'].DatumPlaneByPrincipalPlane(offset=0.0, 
    principalPlane=XZPLANE)
mdb.models['Model-1'].parts['ball'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['ball'].cells, datumPlane=mdb.models['Model-1'].parts['ball'].datums[2])
mdb.models['Model-1'].parts['ball'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['ball'].cells, datumPlane=mdb.models['Model-1'].parts['ball'].datums[3])
mdb.models['Model-1'].parts['ball'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['ball'].cells, datumPlane=mdb.models['Model-1'].parts['ball'].datums[4])


#与提供的cae模型中的瓶有少许差别
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    0.0251, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spline(points=((0.0251, 0.0), (
    0.06, 0.0762), (0.038, 0.328531), (0.051, 0.35347)))
mdb.models['Model-1'].sketches['__profile__'].ArcByStartEndTangent(point1=(0.0, 
    0.381), point2=(0.051, 0.35347), vector=(1.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.381), point2=
    (0.0, 0.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='bottle', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['bottle'].BaseSolidRevolve(angle=360.0, 
    flipRevolveDirection=OFF, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']



mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    1.024, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.024, 0.0), point2=
    (1.024, 17.795839))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.024, 17.795839), 
    point2=(1.497067, 17.795839))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.497067, 17.795839)
    , point2=(1.497067, 19.15))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.497067, 19.15), 
    point2=(-0.502673, 19.15))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.502673, 19.15), 
    point2=(-0.502673, 17.795839))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.502673, 
    17.795839), point2=(0.0, 17.795839))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 17.795839), 
    point2=(0.0, 0.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='road', type=
    DISCRETE_RIGID_SURFACE)
mdb.models['Model-1'].parts['road'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['road'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['road'].faces, point1=mdb.models['Model-1'].parts['road'].vertices[0], point2=
    mdb.models['Model-1'].parts['road'].vertices[3])
mdb.models['Model-1'].parts['road'].ReferencePoint(point=
    mdb.models['Model-1'].parts['road'].InterestingPoint(
    mdb.models['Model-1'].parts['road'].edges[0], MIDDLE))

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    0.0, 1.354161))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.99974, 1.354161), 
    point2=(1.9997400000001, 0.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='wall', type=
    DISCRETE_RIGID_SURFACE)
mdb.models['Model-1'].parts['wall'].BaseShellExtrude(depth=0.4, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['wall'].ReferencePoint(point=
    mdb.models['Model-1'].parts['wall'].InterestingPoint(
    mdb.models['Model-1'].parts['wall'].edges[4], MIDDLE))



#Material
mdb.models['Model-1'].Material(name='ball')
mdb.models['Model-1'].materials['ball'].Density(table=((1500.0, ), ))
mdb.models['Model-1'].materials['ball'].Elastic(table=((4000000000.0, 0.3), ))
mdb.models['Model-1'].Material(name='bottle')
mdb.models['Model-1'].materials['bottle'].Density(table=((500.0, ), ))
mdb.models['Model-1'].materials['bottle'].Elastic(table=((9500000000.0, 0.3), 
    ))
mdb.models['Model-1'].HomogeneousSolidSection(material='ball', name='Section-1'
    , thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='bottle', name=
    'Section-2', thickness=None)
mdb.models['Model-1'].parts['ball'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['ball'].cells), sectionName='Section-1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['bottle'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['bottle'].cells), sectionName='Section-2', thicknessAssignment=
    FROM_SECTION)


#ASSEMBLY
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='ball-1', part=
    mdb.models['Model-1'].parts['ball'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='road-1', part=
    mdb.models['Model-1'].parts['road'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='wall-1', part=
    mdb.models['Model-1'].parts['wall'])
mdb.models['Model-1'].rootAssembly.translate(instanceList=('wall-1', ), vector=
    (-0.502673, 17.795839, 0.0))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('ball-1', ), vector=
    (0.0, 0.0, 0.105))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('ball-1', ), vector=
    (0.512, 0.0, 0.0))

mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bottle-1', 
    part=mdb.models['Model-1'].parts['bottle'])
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(10.0, 0.0, 
    0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('bottle-1', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bottle-1', ), 
    vector=(0.512, 18.0, 0.0))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bottle-2', 
    part=mdb.models['Model-1'].parts['bottle'])
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(10.0, 0.0, 
    0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('bottle-2', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bottle-2', ), 
    vector=(0.6644, 18.2638, 0.0))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bottle-3', 
    part=mdb.models['Model-1'].parts['bottle'])
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(10.0, 0.0, 
    0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('bottle-3', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bottle-3', ), 
    vector=(359.6E-03,18.2638,0.0))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bottle-4', 
    part=mdb.models['Model-1'].parts['bottle'])
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(10.0, 0.0, 
    0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('bottle-4', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bottle-4', ), 
    vector=(816.8E-03,18.5276,0.0))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bottle-5', 
    part=mdb.models['Model-1'].parts['bottle'])
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(10.0, 0.0, 
    0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('bottle-5', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bottle-5', ), 
    vector=(512.E-03,18.5276,0.0))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bottle-6', 
    part=mdb.models['Model-1'].parts['bottle'])
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(10.0, 0.0, 
    0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('bottle-6', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bottle-6', ), 
    vector=(207.2E-03,18.5276,0.0))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bottle-7', 
    part=mdb.models['Model-1'].parts['bottle'])
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(10.0, 0.0, 
    0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('bottle-7', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bottle-7', ), 
    vector=(969.2E-03,18.7914,0.0))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bottle-8', 
    part=mdb.models['Model-1'].parts['bottle'])
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(10.0, 0.0, 
    0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('bottle-8', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bottle-8', ), 
    vector=(664.4E-03,18.7914,0.0))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bottle-9', 
    part=mdb.models['Model-1'].parts['bottle'])
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(10.0, 0.0, 
    0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('bottle-9', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bottle-9', ), 
    vector=(359.6E-03,18.7914,0.0))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bottle-10', 
    part=mdb.models['Model-1'].parts['bottle'])
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(10.0, 0.0, 
    0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('bottle-10', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bottle-10', ), 
    vector=(54.8E-03,18.7914,0.0))



#STEP
mdb.models['Model-1'].ExplicitDynamicsStep(improvedDtMethod=ON, name='Step-1', 
    previous='Initial', timePeriod=3.5)
mdb.models['Model-1'].steps['Step-1'].setValues(improvedDtMethod=ON, 
    massScaling=((SEMI_AUTOMATIC, MODEL, THROUGHOUT_STEP, 0.0, 1e-06, 
    BELOW_MIN, 1, 0, 0.0, 0.0, 0, None), ))
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(timeInterval=
    0.035)


#interaction
mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.1, ), ), temperatureDependency=OFF)
mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
    allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
    pressureOverclosure=HARD)
mdb.models['Model-1'].ContactExp(createStepName='Step-1', name='Int-1')
mdb.models['Model-1'].interactions['Int-1'].includedPairs.setValuesInStep(
    stepName='Step-1', useAllstar=ON)
mdb.models['Model-1'].interactions['Int-1'].contactPropertyAssignments.appendInStep(
    assignments=((GLOBAL, SELF, 'IntProp-1'), ), stepName='Step-1')



#LOAD
mdb.models['Model-1'].EncastreBC(createStepName='Step-1', localCsys=None, name=
    'BC-1', region=Region(referencePoints=(
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].referencePoints[2], 
    mdb.models['Model-1'].rootAssembly.instances['road-1'].referencePoints[3], 
    )))
mdb.models['Model-1'].Velocity(axisBegin=(1.0, 0.0, 0.7), 
    axisEnd=(-1.0, 0.0, 0.7), distributionType=MAGNITUDE, field=
    '', name='Predefined Field-1', omega=-20.0, region=Region(
    cells=mdb.models['Model-1'].rootAssembly.instances['ball-1'].cells, 
    faces=mdb.models['Model-1'].rootAssembly.instances['ball-1'].faces, 
    edges=mdb.models['Model-1'].rootAssembly.instances['ball-1'].edges, 
    vertices=mdb.models['Model-1'].rootAssembly.instances['ball-1'].vertices))
mdb.models['Model-1'].Gravity(comp3=-9.8, createStepName='Step-1', 
    distributionType=UNIFORM, field='', name='Load-1')


#MESH
mdb.models['Model-1'].parts['ball'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.015)
mdb.models['Model-1'].parts['ball'].generateMesh()
mdb.models['Model-1'].parts['bottle'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.015)
mdb.models['Model-1'].parts['bottle'].setMeshControls(elemShape=TET, regions=
    mdb.models['Model-1'].parts['bottle'].cells, technique=FREE)
mdb.models['Model-1'].parts['bottle'].setElementType(elemTypes=(ElemType(
    elemCode=UNKNOWN_HEX, elemLibrary=EXPLICIT), ElemType(
    elemCode=UNKNOWN_WEDGE, elemLibrary=EXPLICIT), ElemType(elemCode=C3D10M, 
    elemLibrary=EXPLICIT)), regions=(
    mdb.models['Model-1'].parts['bottle'].cells, ))
mdb.models['Model-1'].parts['bottle'].generateMesh()
mdb.models['Model-1'].parts['road'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.25)
mdb.models['Model-1'].parts['road'].generateMesh()
mdb.models['Model-1'].parts['wall'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.15)
mdb.models['Model-1'].parts['wall'].generateMesh()

mdb.models['Model-1'].rootAssembly.regenerate()

mdb.Job(activateLoadBalancing=False, atTime=None, contactPrint=OFF, 
    description='', echoPrint=OFF, explicitPrecision=DOUBLE_PLUS_PACK, 
    historyPrint=OFF, memory=90, memoryUnits=PERCENTAGE, model='Model-1', 
    modelPrint=OFF, multiprocessingMode=DEFAULT, name='Job-1', 
    nodalOutputPrecision=FULL, numCpus=1, numDomains=1, 
    parallelizationMethodExplicit=DOMAIN, queue=None, resultsFormat=ODB, 
    scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)