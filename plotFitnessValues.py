import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import matplotlib.pyplot



fitnessData = numpy.load('fitnessDataB.npy')

avg = numpy.empty((1, c.numberOfGenerations))

for x in range(c.numberOfGenerations):
    print(sum(fitnessData[:, x])/c.populationSize)
    avg[0, x] = sum(fitnessData[:, x])/c.populationSize

matplotlib.pyplot.plot(avg[0,:])
# for x in range(c.populationSize):
#     matplotlib.pyplot.plot(fitnessData[x,:], label=("Solution #" + str(x)))
matplotlib.pyplot.show()
