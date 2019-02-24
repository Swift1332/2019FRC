from wpilib.command import Command

class ExtendShoulder(Command):
    def __init__(self, robot):
        print("Extend constructing")
        super().__init__()

        self.robot = robot
        self.requires(self.robot.arm.shoulder)
        print("Extend constructed")

    def initialize(self):
        print("Extend initialized")
        self.robot.arm.shoulder.extend()

    def end(self):
        print("Extend ended")
        self.robot.arm.shoulder.stop()

    def interrupted(self):
        print("Extend interrupted")
        self.end()

    def isFinished(self):
        print("Extend finished?")
        return False