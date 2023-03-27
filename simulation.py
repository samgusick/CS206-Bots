import time
from robot import ROBOT
from world import WORLD
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if (directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravity)
        self.solutionID = solutionID
        self.world = WORLD(solutionID)
        self.robot = ROBOT(solutionID)

    
    def __del__(self):
        p.disconnect()
        
    def Run(self):
        for x in range(c.program_run_time):
            p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(x, self.robot)
            if (self.directOrGUI == "GUI"):
                time.sleep(c.sleep_time)

    
    def Get_Fitness(self):
        self.robot.Get_Fitness(self.solutionID)