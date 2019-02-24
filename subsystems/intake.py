import wpilib
from wpilib.command import Subsystem

import constants

class Intake(Subsystem):
    
    def __init__(self, robot, pwm):
        super().__init__()
        self.robot = robot

        self.intakeMotor = wpilib.VictorSP(pwm)

    def pickup(self):
        self.intakeMotor.set(1)

    def eject(self):
        self.intakeMotor.set(-1)

    def stop(self):
        self.intakeMotor.set(0)
