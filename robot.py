from ntpath import join
import numpy
import pybullet as p
from motor import MOTOR
import pyrosim.pyrosim as pyroism
from sensor import SENSOR
import constants as c

class ROBOT:
        
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyroism.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        self.motors = dict()
        for jointName in pyroism.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t, robot):
        for jointName in self.motors:
            self.motors[jointName].Set_Value(t, robot)
            
    def Prepare_To_Sense(self):
        self.sensors = dict()
        for linkName in pyroism.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName, numpy.zeros(c.program_run_time))
    
    def Sense(self, t):
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(t)
            
    
        