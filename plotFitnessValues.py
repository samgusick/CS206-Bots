import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import matplotlib.pyplot


fitnessDataA = numpy.load('fitnessDataA.npy')
fitnessDataB = numpy.load('fitnessDataB.npy')

avg = numpy.empty((2, c.numberOfGenerations))

for x in range(c.numberOfGenerations):
    avg[0, x] = sum(fitnessDataA[:, x])/c.populationSize
    avg[1, x] = sum(fitnessDataB[:, x])/c.populationSize
    
matplotlib.pyplot.plot(avg[0,:], label="Test A Quadruped")
matplotlib.pyplot.plot(avg[1,:], label="Test B Hexapod")
matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Fitness Score Average')
# for x in range(c.populationSize):
#     matplotlib.pyplot.plot(fitnessData[x,:], label=("Solution #" + str(x)))
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
