import pybullet as p

class WORLD:
    def __init__(self, myID) -> None:
        p.loadSDF("world" + str(myID) + ".sdf")
        self.planeId = p.loadURDF("plane.urdf")