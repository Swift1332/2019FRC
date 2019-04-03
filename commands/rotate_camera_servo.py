from wpilib.command import Command

class RotateCameraServo(Command):
    def __init__(self, robot, camera_servo):
        super().__init__()
        self.robot = robot
        self.requires(camera_servo)
        self.camera_servo = camera_servo
        
    def initialize(self):
        self.camera_servo.rotateClockwise()

    def end(self):
        pass             

    def interrupted(self):
        self.end()

    def isFinished(self):
        return False