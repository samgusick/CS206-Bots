import time
import numpy as numpy
import pyrosim.pyrosim as pyrosim
import os
import random


class SOLUTION:


    def __init__(self, myID):
        self.myID = myID
        self.weights = numpy.random.rand(3, 2)
        self.weights = self.weights * 2 - 1
    
    def Set_ID(self, myID):
        self.myID = myID

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1
    
    def Start_Simulation(self, view):
        self.Create_Brain(self.myID)
        # self.Create_World()
        # self.Create_Body()
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
    
    def Evaluate(self, view):
        self.Create_Brain(self.myID)
        self.Create_World()
        self.Create_Body()
        file = "START /B python3 simulate.py " + view + " " + str(self.myID)
        os.system(file)
        

        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)


        f = open("fitness" + str(self.myID) + ".txt","r")
        
        self.fitness = float(f.read())
        print(self.fitness)
        f.close()

    def Create_World(self):


        pyrosim.Start_SDF("world.sdf")


        # pyrosim.Send_Cube(name="Box", pos=[1, 1, .5], size=[1, 1, 1])


        pyrosim.End()


    def Create_Body(self):


        pyrosim.Start_URDF("body.urdf")


        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])



        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso",


                        child="BackLeg", type="revolute", position=[1, 0, 1])



        pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[1, 1, 1])



        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",


                        child="FrontLeg", type="revolute", position=[2, 0, 1])



        pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[1, 1, 1])



        pyrosim.End()


    def Create_Brain(self, myID):


        pyrosim.Start_NeuralNetwork("brain" + str(myID) + ".nndf")
        print("brain" + str(myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso"),
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg"),
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg"),
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        for currentRow in range(3):


            for currentColumn in range(2):
                pyrosim.Send_Synapse(
                    sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])



        pyrosim.End()


