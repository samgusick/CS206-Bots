import time
import numpy as numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import constants as c

class SOLUTION:


    def __init__(self, myID):
        self.myID = myID
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
    
    def Set_ID(self, myID):
        self.myID = myID

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons-1)
        randomColumn = random.randint(0, c.numMotorNeurons-1)
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1
    
    def Start_Simulation(self, view):
        self.Create_Brain(self.myID)
        self.Create_World(self.myID)
        self.Create_Body(self.myID)
        file = "START /B python3 simulate.py " + view + " " + str(self.myID)
        os.system(file)
        
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
            
        f = open("fitness" + str(self.myID) + ".txt","r")
        self.fitness = float(f.read())
        #print(self.fitness)
        f.close()
        os.system("del fitness" + str(self.myID) + ".txt")
        os.system("del world" + str(self.myID) + ".sdf")
        os.system("del body" + str(self.myID) + ".urdf")
    
    def Evaluate(self, view):
        file = "START /B python3 simulate.py " + view + " " + str(self.myID)
        os.system(file)
        

        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)


        f = open("fitness" + str(self.myID) + ".txt","r")
        
        self.fitness = float(f.read())
        print(self.fitness)
        f.close()


    def Create_World(self, myID):


        pyrosim.Start_SDF("world" + str(myID) + ".sdf")


        #pyrosim.Send_Cube(name="Box", pos=[1, 1, .5], size=[1, 1, 1])


        pyrosim.End()
        
    
    def Create_Body(self, myID):


        pyrosim.Start_URDF("body" + str(myID) + ".urdf")


        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
        
        pyrosim.Send_Joint(name="Torso_BackRightLeg", parent="Torso", child="BackRightLeg", type="revolute", position=[-.5, -.5, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackRightLeg", pos=[-.5, 0, 0], size=[1, .2, .2])
        
        pyrosim.Send_Joint(name="BackRightLeg_BackRightLowerLeg", parent="BackRightLeg", child="BackRightLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackRightLowerLeg", pos=[0,0,-.5], size=[.2, .2, 1])
        

        pyrosim.Send_Joint(name="Torso_BackLeftLeg", parent="Torso", child="BackLeftLeg", type="revolute", position=[-.5, 0.5, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackLeftLeg", pos=[-.5,0,0], size=[1, .2, .2])
        
        pyrosim.Send_Joint(name="BackLeftLeg_BackLeftLowerLeg", parent="BackLeftLeg", child="BackLeftLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackLeftLowerLeg", pos=[0,0,-.5], size=[.2, .2, 1])
        
        pyrosim.Send_Joint(name="Torso_MiddleRightLeg", parent="Torso", child="MiddleRightLeg", type="revolute", position=[0, -.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="MiddleRightLeg", pos=[0, -.5, 0], size=[.2, 1, .2])
        
        pyrosim.Send_Joint(name="MiddleRightLeg_MiddleRightLowerLeg", parent="MiddleRightLeg", child="MiddleRightLowerLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="MiddleRightLowerLeg", pos=[0,0,-.5], size=[.2, .2, 1])
        

        pyrosim.Send_Joint(name="Torso_MiddleLeftLeg", parent="Torso", child="MiddleLeftLeg", type="revolute", position=[0, .5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="MiddleLeftLeg", pos=[0,.5,0], size=[.2, 1, .2])
        
        pyrosim.Send_Joint(name="MiddleLeftLeg_MiddleLeftLowerLeg", parent="MiddleLeftLeg", child="MiddleLeftLowerLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="MiddleLeftLowerLeg", pos=[0,0,-.5], size=[.2, .2, 1])

        pyrosim.Send_Joint(name="Torso_FrontRightLeg", parent="Torso", child="FrontRightLeg", type="revolute", position=[.5, -.5, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontRightLeg", pos=[.5, 0, 0], size=[1, .2, .2])
        
        pyrosim.Send_Joint(name="FrontRightLeg_FrontRightLowerLeg", parent="FrontRightLeg", child="FrontRightLowerLeg", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontRightLowerLeg", pos=[0,0,-.5], size=[.2, .2, 1])
        

        pyrosim.Send_Joint(name="Torso_FrontLeftLeg", parent="Torso", child="FrontLeftLeg", type="revolute", position=[.5, 0.5, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeftLeg", pos=[.5, 0,0], size=[1, .2, .2])
        
        pyrosim.Send_Joint(name="FrontLeftLeg_FrontLeftLowerLeg", parent="FrontLeftLeg", child="FrontLeftLowerLeg", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeftLowerLeg", pos=[0,0,-.5], size=[.2, .2, 1])

        pyrosim.End()


    def Create_Brain(self, myID):


        pyrosim.Start_NeuralNetwork("brain" + str(myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackRightLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="MiddleRightLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="MiddleLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontRightLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="FrontLeftLeg")


        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_BackRightLeg"),
        pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_BackLeftLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_MiddleRightLeg"),
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_MiddleLeftLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_FrontRightLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_FrontLeftLeg")
        
        for currentRow in range(c.numSensorNeurons):


            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])
                
        pyrosim.End()

