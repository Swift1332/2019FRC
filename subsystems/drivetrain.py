import wpilib
from wpilib.command import Subsystem
from wpilib.drive import DifferentialDrive
from wpilib.drive import RobotDriveBase
import rev

import math

from swift_can_encoder import SwiftCanEncoder
import constants

class DriveTrain(Subsystem):
    
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        
        self.maxOutput = 1 
        self.deadband =  .02

        self.front_left_motor_a = wpilib.Spark(constants.PWM_FRONT_LEFT_A)   
        self.front_left_motor_a.setInverted(True) 
        self.front_left_motor_b = rev.CANSparkMax(constants.CAN_FRONT_LEFT_B, rev.MotorType.kBrushless)
        self.front_left_motor_b.setInverted(True)

        self.front_left_encoder = SwiftCanEncoder(self.front_left_motor_b.getEncoder())
        self.front_left_encoder.setPIDSourceType(SwiftCanEncoder.PIDSourceType.kRate)
        self.front_left_encoder.setDistancePerPulse(constants.DRIVE_TRAIN_FPS_FACTOR)

        self.front_right_motor_a = wpilib.Spark(constants.PWM_FRONT_RIGHT_A)
        self.front_right_motor_b = rev.CANSparkMax(constants.CAN_FRONT_RIGHT_B, rev.MotorType.kBrushless)

        self.front_right_encoder = SwiftCanEncoder(self.front_right_motor_b.getEncoder())
        self.front_right_encoder.setPIDSourceType(SwiftCanEncoder.PIDSourceType.kRate)
        self.front_right_encoder.setDistancePerPulse(constants.DRIVE_TRAIN_FPS_FACTOR)

        self.rear_left_motor_a = rev.CANSparkMax(constants.CAN_REAR_LEFT_A, rev.MotorType.kBrushless)
        self.rear_left_motor_a.setInverted(True)
        self.rear_left_motor_b = rev.CANSparkMax(constants.CAN_REAR_LEFT_B, rev.MotorType.kBrushless)
        self.rear_left_motor_b.setInverted(True)
        
        self.rear_left_encoder = SwiftCanEncoder(self.rear_left_motor_b.getEncoder())
        self.rear_left_encoder.setPIDSourceType(SwiftCanEncoder.PIDSourceType.kRate)
        self.rear_left_encoder.setDistancePerPulse(constants.DRIVE_TRAIN_FPS_FACTOR)

        self.rear_right_motor_a = rev.CANSparkMax(constants.CAN_REAR_RIGHT_A, rev.MotorType.kBrushless)
        self.rear_right_motor_b = rev.CANSparkMax(constants.CAN_REAR_RIGHT_B, rev.MotorType.kBrushless)

        self.rear_right_encoder = SwiftCanEncoder(self.rear_right_motor_b.getEncoder())
        self.rear_right_encoder.setPIDSourceType(SwiftCanEncoder.PIDSourceType.kRate)
        self.rear_right_encoder.setDistancePerPulse(constants.DRIVE_TRAIN_FPS_FACTOR)

        self.front_left_group = wpilib.SpeedControllerGroup(
            self.front_left_motor_a,
            self.front_left_motor_b
        )
        
        self.front_right_group = wpilib.SpeedControllerGroup(
            self.front_right_motor_a,
            self.front_right_motor_b
        )

        self.rear_left_group = wpilib.SpeedControllerGroup(
            self.rear_left_motor_a,
            self.rear_left_motor_b
        )
        
        self.rear_right_group = wpilib.SpeedControllerGroup(
            self.rear_right_motor_a,
            self.rear_right_motor_b
        )

        self.left_group = wpilib.SpeedControllerGroup(
            self.front_left_group,
            self.rear_left_group
        )       
        
        self.left_group.setInverted(True)
        
        self.right_group = wpilib.SpeedControllerGroup(
            self.front_right_group,
            self.rear_right_group   
        )        

        self.drive = DifferentialDrive(
            self.left_group,
            self.right_group,
        )

        self.frontLeftPID = wpilib.PIDController(.01, 0, 0, self.front_left_encoder, self.front_left_group)
        self.frontLeftPID.setEnabled(False)
        self.rearLeftPID = wpilib.PIDController(.01, 0, 0, self.rear_left_encoder, self.rear_left_group)
        self.rearLeftPID.setEnabled(False)
        self.frontRightPID = wpilib.PIDController(.01, 0, 0, self.front_right_encoder, self.front_right_group)
        self.frontRightPID.setEnabled(False)
        self.rearRightPID = wpilib.PIDController(.01, 0, 0, self.rear_right_encoder, self.rear_right_group)
        self.rearRightPID.setEnabled(False)

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

        leftMotorSpeed = RobotDriveBase.limit(leftMotorSpeed) * self.maxOutput * constants.DRIVETRAIN_PID_MAX
        rightMotorSpeed = RobotDriveBase.limit(rightMotorSpeed) * self.maxOutput * constants.DRIVETRAIN_PID_MAX

        self.frontLeftPID.setSetpoint(leftMotorSpeed)
        self.rearLeftPID.setSetpoint(leftMotorSpeed)
        self.frontRightPID.setSetpoint(rightMotorSpeed)
        self.rearRightPID.setSetpoint(rightMotorSpeed)
