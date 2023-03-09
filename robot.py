from ntpath import join
import numpy
import pybullet as p
from motor import MOTOR
import pyrosim.pyrosim as pyroism
from sensor import SENSOR
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
class ROBOT:
        
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyroism.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")
    
    def Prepare_To_Act(self):
        self.motors = dict()
        for jointName in pyroism.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t, robot):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle, robot)
                #print(neuronName + " ," + jointName + ", " + str(desiredAngle))

        # for jointName in self.motors:
        #     self.motors[jointName].Set_Value(t, robot)
            
    def Prepare_To_Sense(self):
        self.sensors = dict()
        for linkName in pyroism.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName, numpy.zeros(c.program_run_time))
    
    def Sense(self, t):
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(t)
            
    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        # print("========")
        # print(xCoordinateOfLinkZero)
        # print("========")
        f = open("fitness.txt","w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()