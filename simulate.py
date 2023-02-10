import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random as random

pi = math.pi
amplitudeBackLeg = pi/4
frequencyBackLeg = 5
phaseOffsetBackLeg = 0
amplitudeFrontLeg = pi/4
frequencyFrontLeg = 5
phaseOffsetFrontLeg = 1

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.setGravity(0,0,-9.8)
#p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

programRunTime = 1000

backLegSensorValues = numpy.zeros(programRunTime)
frontLegSensorValues = numpy.zeros(programRunTime)

val = frequencyBackLeg * numpy.linspace(0, 2 * pi, programRunTime) + phaseOffsetBackLeg
targetAnglesBackLeg = amplitudeBackLeg * numpy.sin(val)

val2 = frequencyFrontLeg * numpy.linspace(0, 2 * pi, programRunTime) + phaseOffsetFrontLeg
targetAnglesFrontLeg = amplitudeFrontLeg * numpy.sin(val2)
#numpy.save('data\\targetAngles.npy', targetAngles)




i = 0


for x in range(programRunTime):
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    

    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = "Torso_BackLeg", 
                                controlMode = p.POSITION_CONTROL, 
                                targetPosition =  targetAnglesBackLeg[i], 
                                maxForce = 100)
    
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = "Torso_FrontLeg", 
                                controlMode = p.POSITION_CONTROL, 
                                targetPosition =  targetAnglesFrontLeg[i], 
                                maxForce = 100)
    i += 1
    time.sleep(1/240)

#print(backLegSensorValues)
numpy.save('data\\backLegSensorValues.npy', backLegSensorValues)
numpy.save('data\\frontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()
