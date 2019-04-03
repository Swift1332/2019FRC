import wpilib
from wpilib.command import Subsystem
import rev
import constants
from swift_can_encoder import SwiftCanEncoder

class Wrist(Subsystem):
    
    def __init__(self, robot, can_id):
        super().__init__()
        self.robot = robot

        self.wristMotor = rev.CANSparkMax(can_id, rev.MotorType.kBrushless)
        self.encoder = SwiftCanEncoder(self.wristMotor.getEncoder())
        self.encoder.setDistancePerPulse(constants.WRIST_DEGREES_FACTOR)  
        self.encoder.setPosition(constants.WRIST_START_POSITION)   
                
        self.pid = wpilib.PIDController(.07, 0, 0, self.encoder, self.wristMotor)
        self.pid.setAbsoluteTolerance(3)
        self.pid.setEnabled(False)

    def extend(self):
        self.wristMotor.set(0.2)

    def retract(self):
        self.wristMotor.set(-0.2)

    def stop(self):
        self.wristMotor.set(0)



