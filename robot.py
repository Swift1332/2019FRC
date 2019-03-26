#!/usr/bin/env python3

import wpilib
import constants

from wpilib.command import Scheduler

from typing import Optional

from oi import OI
from subsystems.drivetrain import DriveTrain
from subsystems.arm import Arm
from subsystems.pneumatic import Pneumatic
from subsystems.camera_servo import CameraServo

from swift_camera_server import SwiftCameraServer

import logging
logger = logging.getLogger("swift.robot")

class MyRobot(wpilib.TimedRobot):
    """Main robot class."""

    def robotInit(self):
        self.activated = False
        """Robot-wide initialization code should go here."""
        #SwiftCameraServer().launch('camera1.py:main')
        #SwiftCameraServer().launch('camera2.py:main')
        wpilib.CameraServer.launch()
        self.configuration = constants.COMP_BOT 
        self.arm = Arm(self)   
        self.drivetrain = DriveTrain(self)     
        self.pneumatic = Pneumatic(self)
        self.compressor = wpilib.Compressor()
        self.camera_servo_1 = CameraServo(self, constants.CAMERA_1_PWM, constants.CAMERA_1_DEFAULT)
        self.camera_servo_2 = CameraServo(self, constants.CAMERA_2_PWM, constants.CAMERA_2_DEFAULT)
        self.oi = OI(self)

    def robotPeriodic(self):
        if constants.SEND_DATA:
            self.putData()


    def autonomousInit(self):
        """Called only at the beginning of autonomous mode."""
        if not self.activated:
            self.activeInit()

    def autonomousPeriodic(self):        
        self.activePeriodic()

    def disabledInit(self):
        self.activated = False

    def disabledPeriodic(self):
        """Called every 20ms in disabled mode."""

    def teleopInit(self):
        if not self.activated:
            self.activeInit()

    def activeInit(self):
        self.activated = True
        self.arm.wrist.pid.reset()
        self.arm.wrist.encoder.setPosition(constants.WRIST_START_POSITION)
        self.arm.wrist.pid.setSetpoint(constants.WRIST_START_POSITION)
        self.arm.wrist.pid.setEnabled(True)

        self.arm.elbow.pid.reset()
        self.arm.elbow.encoder.setPosition(constants.ELBOW_START_POSITION)
        self.arm.elbow.pid.setSetpoint(constants.ELBOW_START_POSITION)
        self.arm.elbow.pid.setEnabled(True)

        self.arm.shoulder.pid.reset()
        self.arm.shoulder.encoder.setPosition(constants.SHOULDER_START_POSITION)
        self.arm.shoulder.pid.setSetpoint(constants.SHOULDER_START_POSITION)
        self.arm.shoulder.pid.setEnabled(True)

        if constants.DRIVETRAIN_USE_PID:
            self.drivetrain.resetPID()
            self.drivetrain.enablePID()

        #self.compressor.stop()
        self.pneumatic.lift.solenoid.set(self.pneumatic.lift.solenoid.Value.kForward)
        self.pneumatic.hatch.solenoid.set(self.pneumatic.hatch.solenoid.Value.kOff)

    def teleopPeriodic(self):
        self.activePeriodic()

    def activePeriodic(self):
        """Called every 20ms in teleoperated mode"""
        # Print out the num ber of loop iterations passed every second
        Scheduler.getInstance().run()

        # begin drive 
        y_axis_drive_input = self.oi.joy1.getY()
        x_axis_drive_input = self.oi.joy1.getRawAxis(4)

        if constants.DRIVETRAIN_USE_PID:
            self.drivetrain.drive.setSafetyEnabled(False)
            self.drivetrain.arcadeDrive(y_axis_drive_input, x_axis_drive_input * -1 * constants.DRIVE_INPUT_X_AXIS_MULTIPLIER)
        else:
            self.drivetrain.drive.arcadeDrive(constants.DRIVE_INPUT_Y_AXIS_MULTIPLIER * (y_axis_drive_input * -1), x_axis_drive_input * constants.DRIVE_INPUT_X_AXIS_MULTIPLIER)
        
        # end drive 

        
        shoulderAngle = self.arm.shoulder.pid.getSetpoint() 
        
        elbowAngle = self.arm.elbow.pid.getSetpoint()


        # begin shoulder 
        axisValue = self.oi.joy2.getRawAxis(1)
        print("Shoulder axis value:" + str(axisValue))
        if abs(axisValue) >= .05: 
            pass
        else:
            axisValue = 0


        #if (elbowAngle > constants.MOVE_SHOULDER_ELBOW_MAX or elbowAngle < constants.MOVE_SHOULDER_ELBOW_MIN) or shoulderAngle > constants.MOVE_ELBOW_SHOULDER_MIN:           
        newSetpoint = shoulderAngle + ((axisValue * -1) * constants.SHOULDER_MAX_DEGREES_PER_SECOND)
        override = self.oi.joy2.getRawButton(5) or self.oi.joy2.getRawButton(6)
        fixingSetpoint = (shoulderAngle >= constants.SHOULDER_SETPOINT_MAX and newSetpoint < shoulderAngle) or (shoulderAngle <= constants.SHOULDER_SETPOINT_MIN and newSetpoint > shoulderAngle)

        if fixingSetpoint or override or (newSetpoint >= constants.SHOULDER_SETPOINT_MIN and newSetpoint <= constants.SHOULDER_SETPOINT_MAX):

            self.arm.shoulder.pid.setSetpoint(
                newSetpoint
                )

            self.pneumatic.suspension.assist(axisValue)
        #else:
        #    pass 

        # end shoulder

        # begin elbow

        axisValue = self.oi.joy2.getRawAxis(5)
        print("Elbow axis value:" + str(axisValue))
        if abs(axisValue) >= .05: 
            pass
        else:
            axisValue = 0

        #if shoulderAngle < constants.MOVE_ELBOW_SHOULDER_MIN and (elbowAngle < constants.MOVE_SHOULDER_ELBOW_MAX and elbowAngle > constants.MOVE_SHOULDER_ELBOW_MIN):
        #    pass
        #else:
        self.arm.elbow.pid.setSetpoint(
            elbowAngle + ((axisValue * -1) * constants.ELBOW_MAX_DEGREES_PER_SECOND)
            )
        # end elbow

        # begin wrist 

        value = self.arm.wrist.pid.getSetpoint()
        controlValue = (-1 * self.oi.joy2.getRawAxis(3)) + self.oi.joy2.getRawAxis(2)
        self.arm.wrist.pid.setSetpoint(
            value + (controlValue * constants.WRIST_MAX_DEGREES_PER_SECOND)
            )
        # end wrist

        if self.oi.joy1_btn_b.get():
            self.pneumatic.lift.extend()
            #self.pneumatic.suspension.extend()
        elif self.oi.joy1_btn_a.get(): 
            self.pneumatic.lift.retract()
            #self.pneumatic.suspension.retract()
        elif self.oi.joy2_btn_b.get():
            self.pneumatic.hatch.extend()
        elif self.oi.joy2_btn_a.get():
            self.pneumatic.hatch.retract() 

    def putData(self):
        wpilib.SmartDashboard.putNumber("Arm Length", self.arm.getArmLength())
        wpilib.SmartDashboard.putNumber("Shoulder Encoder", self.arm.shoulder.encoder.get())
        wpilib.SmartDashboard.putNumber("Shoulder Encoder Direction", self.arm.shoulder.encoder.getDirection())
        wpilib.SmartDashboard.putNumber("Shoulder Encoder Rate", self.arm.shoulder.encoder.getRate())
        wpilib.SmartDashboard.putBoolean("Shoulder PID on Target", self.arm.shoulder.pid.onTarget())
        wpilib.SmartDashboard.putNumber("Shoulder PID Error", self.arm.shoulder.pid.getError())
        wpilib.SmartDashboard.putNumber("Shoulder PID Set Point", self.arm.shoulder.pid.getSetpoint())
        wpilib.SmartDashboard.putNumber("Shoulder PWM", self.arm.shoulder.motors.get())
        wpilib.SmartDashboard.putNumber("Shoulder Encoder Angle", self.arm.shoulder.encoder.getDistance())
        
        wpilib.SmartDashboard.putNumber("Elbow Encoder", self.arm.elbow.encoder.get())
        wpilib.SmartDashboard.putNumber("Elbow Encoder Direction", self.arm.elbow.encoder.getDirection())
        wpilib.SmartDashboard.putNumber("Elbow Encoder Rate", self.arm.elbow.encoder.getRate())
        wpilib.SmartDashboard.putBoolean("Elbow PID on Target", self.arm.elbow.pid.onTarget())
        wpilib.SmartDashboard.putNumber("Elbow PID Error", self.arm.elbow.pid.getError())
        wpilib.SmartDashboard.putNumber("Elbow PID Set Point", self.arm.elbow.pid.getSetpoint())
        wpilib.SmartDashboard.putNumber("Elbow PWM", self.arm.elbow.motors.get())
        wpilib.SmartDashboard.putNumber("Elbow Encoder Angle", self.arm.elbow.encoder.getDistance())

        wpilib.SmartDashboard.putNumber("Wrist Encoder", self.arm.wrist.encoder.get())
        wpilib.SmartDashboard.putNumber("Wrist Encoder Direction", self.arm.wrist.encoder.getDirection())
        wpilib.SmartDashboard.putNumber("Wrist Encoder Rate", self.arm.wrist.encoder.getRate())
        wpilib.SmartDashboard.putBoolean("Wrist PID on Target", self.arm.wrist.pid.onTarget())
        wpilib.SmartDashboard.putNumber("Wrist PID Error", self.arm.wrist.pid.getError())
        wpilib.SmartDashboard.putNumber("Wrist PID Set Point", self.arm.wrist.pid.getSetpoint())
        wpilib.SmartDashboard.putNumber("Wrist PWM", self.arm.wrist.wristMotor.get())
        wpilib.SmartDashboard.putNumber("wrist Encoder Angle", self.arm.wrist.encoder.getDistance())
        
        wpilib.SmartDashboard.putNumber("Left Shoulder Temp:", (self.arm.shoulder.leftMotor.getMotorTemperature() * 9/5) + 32)
        wpilib.SmartDashboard.putNumber("Right Shoulder Temp:", (self.arm.shoulder.rightMotor.getMotorTemperature() * 9/5) + 32)

        wpilib.SmartDashboard.putNumber("Left Elbow Temp:", (self.arm.elbow.leftMotor.getMotorTemperature() * 9/5) + 32)
        wpilib.SmartDashboard.putNumber("Right Elbow Temp:", (self.arm.elbow.rightMotor.getMotorTemperature() * 9/5) + 32)

        wpilib.SmartDashboard.putNumber("Wrist Temp:", (self.arm.wrist.wristMotor.getMotorTemperature() * 9/5) + 32)

        #wpilib.SmartDashboard.putNumber("Front Left Encoder", self.drivetrain.front_left_encoder.get())
        #wpilib.SmartDashboard.putNumber("Front Left Setpoint", self.drivetrain.frontLeftPID.getSetpoint())
        #wpilib.SmartDashboard.putNumber("Front Right Encoder", self.drivetrain.front_right_encoder.get())
        #wpilib.SmartDashboard.putNumber("Front Right Setpoint", self.drivetrain.frontRightPID.getSetpoint())
        #wpilib.SmartDashboard.putNumber("Rear Left Encoder", self.drivetrain.rear_left_encoder.get())
        #wpilib.SmartDashboard.putNumber("Rear Left Setpoint", self.drivetrain.rearLeftPID.getSetpoint())
        #wpilib.SmartDashboard.putNumber("Rear Right Encoder", self.drivetrain.rear_right_encoder.get())
        #wpilib.SmartDashboard.putNumber("Rear Right Setpoint", self.drivetrain.rearRightPID.getSetpoint())



if __name__ == "__main__":
    wpilib.run(MyRobot)
