import wpilib
from wpilib.command import Subsystem

import constants

class Elbow(Subsystem):
    
    def __init__(self, robot, left_pwm, right_pwm, encoder_a, encoder_b):
        super().__init__()
        self.robot = robot

        self.encoder = wpilib.Encoder(
            encoder_a, 
            encoder_b, 
            False, 
            wpilib.Encoder.EncodingType.k4X
            )
        self.encoder.setDistancePerPulse(constants.ENCODER_DISTANCE_PER_PULSE)
        
        self.leftMotor = wpilib.VictorSP(constants.LEFT_ELBOW)
        self.rightMotor = wpilib.VictorSP(constants.RIGHT_ELBOW)
        self.leftMotor.setInverted(True)

        self.motors = wpilib.SpeedControllerGroup(self.leftMotor, self.rightMotor)

        self.pid = wpilib.PIDController(.01, 0, 0, self.encoder, self.motors)
        self.pid.setAbsoluteTolerance(3)
        self.pid.setEnabled(False)

    def extend(self):
        self.motors.set(0.2)

    def retract(self):
        self.motors.set(-0.2)

    def stop(self):
        self.motors.set(0)