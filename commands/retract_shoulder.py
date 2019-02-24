from wpilib.command import Command

class RetractShoulder(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.arm.shoulder)

    def initialize(self):
        self.robot.arm.shoulder.retract()

    def end(self):
        self.robot.arm.shoulder.stop()                

    def interrupted(self):
        self.end()

    def isFinished(self):
        return False