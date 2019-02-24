import wpilib
from wpilib.command import Subsystem
from wpilib.drive import DifferentialDrive
from wpilib.drive import RobotDriveBase
import math

import constants

class DriveTrain(Subsystem):
    
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        
        self.maxOutput = 1 
        self.deadband =  .02

        self.front_left_motor = wpilib.Spark(constants.FRONT_LEFT)   
        self.front_left_motor.setInverted(True) 
        self.front_left_encoder = wpilib.Encoder(constants.FRONT_LEFT_ENCODER_A, constants.FRONT_LEFT_ENCODER_B)
        

        self.front_right_motor = wpilib.Spark(constants.FRONT_RIGHT)

        self.rear_left_motor = wpilib.Spark(constants.REAR_LEFT)
        self.rear_left_motor.setInverted(True)   
        self.rear_left_encoder = wpilib.Encoder(constants.REAR_LEFT_ENCODER_A, constants.REAR_LEFT_ENCODER_B)     

        self.rear_right_motor = wpilib.Spark(constants.REAR_RIGHT)
        self.rear_right_encoder = wpilib.Encoder(constants.REAR_RIGHT_ENCODER_A, constants.REAR_RIGHT_ENCODER_B)

        self.left_group = wpilib.SpeedControllerGroup(
            self.front_left_motor,            
            self.rear_left_motor            
            )
       
        
        self.left_group.setInverted(True)
        
        self.right_group = wpilib.SpeedControllerGroup(
            self.front_right_motor,
            self.rear_right_motor
            )
        self.front_right_encoder = wpilib.Encoder(constants.FRONT_RIGHT_ENCODER_A, constants.FRONT_RIGHT_ENCODER_B)
        

        self.drive = DifferentialDrive(
            self.left_group,
            self.right_group,
        )

        self.frontLeftPID = wpilib.PIDController(.01, 0, 0, self.front_left_encoder, self.front_left_motor)
        self.rearLeftPID = wpilib.PIDController(.01, 0, 0, self.rear_left_encoder, self.rear_left_motor)
        self.frontRightPID = wpilib.PIDController(.01, 0, 0, self.front_right_encoder, self.front_right_motor)
        self.rearRightPID = wpilib.PIDController(.01, 0, 0, self.rear_right_encoder, self.rear_right_motor)

    def arcadeDrive(
        self, xSpeed: float, zRotation: float, squareInputs: bool = True) -> None:
        """Arcade drive method for differential drive platform.

        :param xSpeed: The robot's speed along the X axis `[-1.0..1.0]`. Forward is positive
        :param zRotation: The robot's zRotation rate around the Z axis `[-1.0..1.0]`. Clockwise is positive
        :param squareInputs: If set, decreases the sensitivity at low speeds.
        """

        xSpeed = RobotDriveBase.limit(xSpeed)
        xSpeed = RobotDriveBase.applyDeadband(xSpeed, self.deadband)

        zRotation = RobotDriveBase.limit(zRotation)
        zRotation = RobotDriveBase.applyDeadband(zRotation, self.deadband)

        if squareInputs:
            # Square the inputs (while preserving the sign) to increase fine
            # control while permitting full power.
            xSpeed = math.copysign(xSpeed * xSpeed, xSpeed)
            zRotation = math.copysign(zRotation * zRotation, zRotation)

        maxInput = math.copysign(max(abs(xSpeed), abs(zRotation)), xSpeed)

        if xSpeed >= 0.0:
            if zRotation >= 0.0:
                leftMotorSpeed = maxInput
                rightMotorSpeed = xSpeed - zRotation
            else:
                leftMotorSpeed = xSpeed + zRotation
                rightMotorSpeed = maxInput
        else:
            if zRotation >= 0.0:
                leftMotorSpeed = xSpeed + zRotation
                rightMotorSpeed = maxInput
            else:
                leftMotorSpeed = maxInput
                rightMotorSpeed = xSpeed - zRotation

        leftMotorSpeed = RobotDriveBase.limit(leftMotorSpeed) * self.maxOutput
        rightMotorSpeed = RobotDriveBase.limit(rightMotorSpeed) * self.maxOutput

        self.frontLeftPID.setSetpoint(leftMotorSpeed)
        self.rearLeftPID.setSetpoint(leftMotorSpeed)
        self.frontRightPID.setSetpoint(rightMotorSpeed)
        self.rearRightPID.setSetpoint(rightMotorSpeed)
