from wpilib.command import Command

class RetractWrist(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.arm.wrist)

    def initialize(self):
        self.robot.arm.wrist.retract()

    def end(self):
        self.robot.arm.wrist.stop()                

    def interrupted(self):
        self.end()

    def isFinished(self):
        return False