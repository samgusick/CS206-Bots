import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
class SENSOR:
    def __init__(self, linkName, values) -> None:
        self.values = values
        self.linkName = linkName
    
    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if (t == c.program_run_time - 1):
            #print(self.values)
            pass
    
    def Save_Values(self):
        numpy.save('data\\SensorValues.npy', self.values)

