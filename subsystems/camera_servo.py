import wpilib
from wpilib.command import Subsystem
import constants

class CameraServo(Subsystem):
    def __init__(self, robot, pwm_channel, default):
        super().__init__()
        self.servo = wpilib.Servo(pwm_channel)
        self.servo.set(default)

    def rotateClockwise(self):
        self.servo.set(self.servo.get() + constants.SERVO_INCREMENT)

    def rotateCounterClockwise(self):
        self.servo.set(self.servo.get() - constants.SERVO_INCREMENT)
