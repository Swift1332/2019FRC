import wpilib
from wpilib.command import Subsystem

import constants

class Wrist(Subsystem):
    
    def __init__(self, robot, left_pwm, encoder_a, encoder_b):
        super().__init__()
        self.robot = robot

        self.encoder = wpilib.Encoder(
            encoder_a, 
            encoder_b, 
            False, 
            wpilib.Encoder.EncodingType.k4X
            )
        self.encoder.setDistancePerPulse(360/1024)
                
        self.wristMotor = wpilib.VictorSP(constants.WRIST)

        self.pid = wpilib.PIDController(.01, 0, 0, self.encoder, self.wristMotor)
        self.pid.setAbsoluteTolerance(3)
        self.pid.setEnabled(False)

    def extend(self):
        self.wristMotor.set(0.2)

    def retract(self):
        self.wristMotor.set(-0.2)

    def stop(self):
        self.wristMotor.set(0)



