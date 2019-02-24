from wpilib.command import Command

class StopElbow(Command):
    def __init__(self, robot):        
        super().__init__()

        self.robot = robot
        self.requires(self.robot.arm.elbow)

    def initialize(self):
        self.robot.arm.elbow.stop()

    def end(self):
        self.robot.arm.elbow.stop()

    def interrupted(self):
        self.end()

    def isFinished(self):
        return True