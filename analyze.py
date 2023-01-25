import numpy
import matplotlib.pyplot


backLegSensorValues = numpy.load("data/data.npy")
matplotlib.pyplot.plot( backLegSensorValues, linewidth=5, label='back leg')

matplotlib.pyplot.legend()

matplotlib.pyplot.show()