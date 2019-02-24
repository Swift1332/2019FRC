import math

import wpilib
from wpilib.command import Subsystem

import constants
from .arm_components.shoulder import Shoulder
from .arm_components.elbow import Elbow
from .arm_components.wrist import Wrist
from .intake import Intake

class Arm(Subsystem):
    
    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.shoulder = Shoulder(
            robot,
            constants.LEFT_SHOULDER, 
            constants.RIGHT_SHOULDER, 
            constants.SHOULDER_ENCODER_A, 
            constants.SHOULDER_ENCODER_B
            )

        self.elbow = Elbow(
            robot,
            constants.LEFT_ELBOW, 
            constants.RIGHT_ELBOW, 
            constants.ELBOW_ENCODER_A, 
            constants.ELBOW_ENCODER_B
            )

        self.wrist = Wrist(
            robot,
            constants.WRIST, 
            constants.WRIST_ENCODER_A, 
            constants.WRIST_ENCODER_B
            )

        self.intake = Intake(
            robot,
            constants.INTAKE, 
            )
            
    def getArmLength(self):
        encA = math.radians(self.shoulder.encoder.getDistance())
        encB = math.radians(self.elbow.encoder.getDistance())
        encC = math.radians(self.wrist.encoder.getDistance())

        lenA = math.cos(encA) * constants.SHOULDER_ELBOW_LENGTH
        lenB = math.cos(encB) * constants.ELBOW_WRIST_LENGTH
        lenC = math.cos(encC) * constants.WRIST_INTAKE_LENGTH

        return lenA + lenB + lenC  