#*******************************************************************************
#cantilever beam bending under the action of a uniform pressure loads
#created:23-1-2019
#Place: HAW Hamburg , Hamburg
#Author: Mohan Pannirselvam (B.Eng)

#*******************************************************************************
#1.Initialization

from abaqus import *
from abaqusConstants import *
import regionToolset

session.viewports['Viewport: 1 '].setValues(displayedObject = None)

#-------------------------------------------------------------------------------
#2.create the model
mbd.models.changeKey(fromName='model-1', toName='cantilever Beam')
beamModel = mbd.models['cantilever beam']
#-------------------------------------------------------------------------------
#3.Create the part
import sketch
import part

#a) Sketch the beam cross section using rectangle regionTool
beamProfileSketch = beamModel.ConstrainedSketch(name='Beam CS Profil,
                                                sheetSize=5')
beamProfileSketch.rectangle(point1=(0.1,0.1), point2=(0.3,-0.1))

#b9Create a 3D deformable part named "Beam" by extrudding the Sketch
beamPart=beamModel.Part(name='Beam',dimensionality=THREE_D,
                        type=DEFORMABLE_BODY)
                        beamPart.baseSolidExtrude(sketch=beamProfilSketch,
                        depth=5)
#-------------------------------------------------------------------------------
#4.Define the materials

#-------------------------------------------------------------------------------
#5.Create solid sections and make section assignments

#-------------------------------------------------------------------------------
#6-Create an assembly

#-------------------------------------------------------------------------------
#7.create steps

#-------------------------------------------------------------------------------
#8.Create and define field output requests

#-------------------------------------------------------------------------------
#9.create and define history output requests

#-------------------------------------------------------------------------------
#10.Apply loads

#-------------------------------------------------------------------------------
#11.Apply boundry conditions

#-------------------------------------------------------------------------------
#12.meshing

#-------------------------------------------------------------------------------
#13.Create and run the job

#-------------------------------------------------------------------------------
#14.Post processing

#-------------------------------------------------------------------------------
