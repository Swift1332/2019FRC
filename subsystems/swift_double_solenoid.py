import wpilib
from wpilib.command import Subsystem

import constants

class SwiftDoubleSolenoid(Subsystem):

    def __init__(self, robot, retract, extend):
        super().__init__()
        self.robot = robot 

        self.solenoid = wpilib.DoubleSolenoid(
            extend,
            retract
        )

    def extend(self):
        self.solenoid.set(self.solenoid.Value.kForward)
    
    def retract(self):
        self.solenoid.set(self.solenoid.Value.kReverse)

    def off(self):
        self.solenoid.set(self.solenoid.Value.kOff)