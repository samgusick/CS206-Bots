import numpy
import matplotlib.pyplot


# backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
# frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
# matplotlib.pyplot.plot( backLegSensorValues, linewidth=5, label='back leg')
# matplotlib.pyplot.plot(frontLegSensorValues, linewidth=5, label='front leg')

targetAngles = numpy.load("data/targetAngles.npy")
matplotlib.pyplot.plot(targetAngles, linewidth=5)

matplotlib.pyplot.legend()

matplotlib.pyplot.show()