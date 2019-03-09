#!/usr/bin/env python3

import wpilib
import constants

from wpilib.command import Scheduler

from typing import Optional

from oi import OI
from subsystems.drivetrain import DriveTrain
from subsystems.arm import Arm
from subsystems.pneumatic import Pneumatic


class MyRobot(wpilib.TimedRobot):
    """Main robot class."""

    def robotInit(self):
        """Robot-wide initialization code should go here."""  
        wpilib.CameraServer.launch()
        self.configuration = constants.COMP_BOT 
        self.arm = Arm(self)   
        self.drivetrain = DriveTrain(self)     
        self.pneumatic = Pneumatic(self)
        self.compressor = wpilib.Compressor()
        self.oi = OI(self)

    def robotPeriodic(self):
        self.putData()


    def autonomousInit(self):
        """Called only at the beginning of autonomous mode."""
        pass

    def autonomousPeriodic(self):
        """Called every 20ms in autonomous mode."""
        pass

    def disabledInit(self):
        """Called only at the beginning of disabled mode."""

    def disabledPeriodic(self):
        """Called every 20ms in disabled mode."""

    def teleopInit(self):
        """Called only at the beginning of teleoperated mode."""
        self.arm.wrist.pid.reset()
        self.arm.wrist.encoder.reset()
        self.arm.wrist.pid.setSetpoint(0)
        self.arm.wrist.pid.setEnabled(True)

        self.arm.elbow.pid.reset()
        self.arm.elbow.encoder.reset()
        self.arm.elbow.pid.setSetpoint(0)
        self.arm.elbow.pid.setEnabled(True)

        self.arm.shoulder.pid.reset()
        self.arm.shoulder.encoder.reset()
        self.arm.shoulder.pid.setSetpoint(0)
        self.arm.shoulder.pid.setEnabled(True)

        #self.compressor.stop()
        self.pneumatic.lift.solenoid.set(self.pneumatic.lift.solenoid.Value.kForward)
        self.pneumatic.hatch.solenoid.set(self.pneumatic.hatch.solenoid.Value.kOff)


    def teleopPeriodic(self):
        """Called every 20ms in teleoperated mode"""
        # Print out the num ber of loop iterations passed every second
        Scheduler.getInstance().run()
        self.drivetrain.drive.arcadeDrive(constants.DRIVE_INPUT_Y_AXIS_MULTIPLIER * (self.oi.joy1.getY() * -1), self.oi.joy1.getRawAxis(4) * constants.DRIVE_INPUT_X_AXIS_MULTIPLIER)
        #self.drivetrain.arcadeDrive(self.oi.joy1.getY(), self.oi.joy1.getRawAxis(4) * -1)
        
        axisValue = self.oi.joy2.getRawAxis(1)
        
        if abs(axisValue) >= .1: 
            pass
        else:
            axisValue = 0
        
        value = self.arm.shoulder.pid.getSetpoint() 
        
        self.arm.shoulder.pid.setSetpoint(
            value + ((axisValue * -1) * constants.SHOULDER_MAX_DEGREES_PER_SECOND)
            )

        self.pneumatic.suspension.assist(axisValue)
        
        value = self.arm.elbow.pid.getSetpoint()
        axisValue = self.oi.joy2.getRawAxis(5)

        if abs(axisValue) >= .1: 
            pass
        else:
            axisValue = 0

        self.arm.elbow.pid.setSetpoint(
            value + ((axisValue * -1) * constants.ELBOW_MAX_DEGREES_PER_SECOND)
            )
        

        value = self.arm.wrist.pid.getSetpoint()
        controlValue = (-1 * self.oi.joy2.getRawAxis(3)) + self.oi.joy2.getRawAxis(2)
        self.arm.wrist.pid.setSetpoint(
            value + (controlValue * constants.WRIST_MAX_DEGREES_PER_SECOND)
            )


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

        wpilib.SmartDashboard.putNumber("Front Left Encoder", self.drivetrain.front_left_encoder.get())
        wpilib.SmartDashboard.putNumber("Front Left Setpoint", self.drivetrain.frontLeftPID.getSetpoint())
        wpilib.SmartDashboard.putNumber("Front Right Encoder", self.drivetrain.front_right_encoder.get())
        wpilib.SmartDashboard.putNumber("Front Right Setpoint", self.drivetrain.frontRightPID.getSetpoint())
        wpilib.SmartDashboard.putNumber("Rear Left Encoder", self.drivetrain.rear_left_encoder.get())
        wpilib.SmartDashboard.putNumber("Rear Left Setpoint", self.drivetrain.rearLeftPID.getSetpoint())
        wpilib.SmartDashboard.putNumber("Rear Right Encoder", self.drivetrain.rear_right_encoder.get())
        wpilib.SmartDashboard.putNumber("Rear Right Setpoint", self.drivetrain.rearRightPID.getSetpoint())



if __name__ == "__main__":
    wpilib.run(MyRobot)
