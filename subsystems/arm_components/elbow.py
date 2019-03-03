import wpilib
from wpilib.command import Subsystem
import rev

from swift_can_encoder import SwiftCanEncoder
import constants

class Elbow(Subsystem):
    
    def __init__(self, robot, left_id, right_id):
        super().__init__()
        self.robot = robot
        
        self.leftMotor = rev.CANSparkMax(left_id, rev.MotorType.kBrushless)
        self.rightMotor = rev.CANSparkMax(right_id, rev.MotorType.kBrushless)
        self.leftMotor.setInverted(True)

        self.encoder = SwiftCanEncoder(self.leftMotor.getEncoder())
        self.encoder.setDistancePerPulse(constants.ENCODER_DISTANCE_PER_PULSE)

        self.motors = wpilib.SpeedControllerGroup(self.leftMotor, self.rightMotor)

        self.pid = wpilib.PIDController(.05, 0, 0, self.encoder, self.motors)
        self.pid.setAbsoluteTolerance(3)
        self.pid.setEnabled(False)

    def extend(self):
        self.motors.set(0.2)

    def retract(self):
        self.motors.set(-0.2)

    def stop(self):
        self.motors.set(0)