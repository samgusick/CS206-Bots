import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = .5


pyrosim.Start_SDF("box.sdf")

for gridx in range(5):
    for gridy in range(5):
        for a in range(10):
            scale = pow(.9, a)
            pyrosim.Send_Cube(name="Box", pos=[gridx,gridy,z+a] , size=[scale * length, scale * width, scale * height])

# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])

pyrosim.End()
