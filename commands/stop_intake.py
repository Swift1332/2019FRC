from wpilib.command import Command

class StopIntake(Command):
    def __init__(self, robot):        
        super().__init__()

        self.robot = robot
        self.requires(self.robot.arm.intake)

    def initialize(self):
        self.robot.arm.intake.stop()

    def end(self):
        self.robot.arm.intake.stop()

    def interrupted(self):
        self.end()

    def isFinished(self):
        return True