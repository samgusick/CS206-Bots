import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p

class MOTOR:
    def __init__(self, jointName) -> None:
        self.jointName = jointName
        self.Prepare_To_Act()
        
    def Prepare_To_Act(self):
        
        
        if (self.jointName == "Torso_BackLeg"):
            self.frequency = c.frequency_back_leg
            self.offset = c.phase_offset_back_leg
            self.amplitude = c.amplitude_back_leg
        else:
            self.frequency = c.frequency_front_leg
            self.offset = c.phase_offset_front_leg
            self.amplitude = c.amplitude_front_leg

        val = self.frequency * numpy.linspace(0, 2 * c.pi, c.program_run_time) + self.offset
        self.motorValues = self.amplitude * numpy.sin(val)


    
            
    def Set_Value(self, t, robot):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot.robotId, 
                                    jointName = self.jointName, 
                                    controlMode = p.POSITION_CONTROL, 
                                    targetPosition =  self.motorValues[t], 
                                    maxForce = 100)
        
    def Save_Values(self):
        numpy.save('data\\MotorValues.npy', self.motorValues)