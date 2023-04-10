from solution import *
import numpy as numpy
from constants import *
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
        

    def Evolve(self):
        
        self.parent.Evaluate("GUI")
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Show_Best(self): 
        self.parent.Evaluate("GUI")

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("GUI")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        print(self.child.fitness)
        print(self.parent.fitness)

    def Select(self):
        if (self.parent.fitness < self.child.fitness):
            self.parent = self.child

    def Print(self):
        #print("parent fitness: " + str(self.parent.fitness) + " child fitness: " + str(self.child.fitness))
        pass



