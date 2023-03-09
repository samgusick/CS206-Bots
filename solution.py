import numpy as numpy
import pyrosim.pyrosim as pyrosim
import os
import random


class SOLUTION:


    def __init__(self):



        self.weights = numpy.random.rand(3, 2)


        # print(self.weights)


        self.weights = self.weights * 2 - 1
        
        

        # print(self.weights)

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1
        self.Create_Brain()

    def Evaluate(self, view):
        file = "python3 simulate.py " + view
        os.system(file)
        f = open("fitness.txt","r")
        self.fitness = float(f.read())
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


    def Create_Brain(self):


        pyrosim.Start_NeuralNetwork("brain.nndf")



        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso"),


        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg"),


        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")



        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0 )


        # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0 )


        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -1.0 )


        # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -1.0 )



        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg"),


        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")



        for currentRow in range(3):


            for currentColumn in range(2):
                pyrosim.Send_Synapse(


                    sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])



        pyrosim.End()


