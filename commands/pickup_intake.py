from wpilib.command import Command

class PickupIntake(Command):
    def __init__(self, robot):        
        super().__init__()

        self.robot = robot
        self.requires(self.robot.arm.intake)        

    def initialize(self):        
        self.robot.arm.intake.pickup()

    def end(self):
        self.robot.arm.intake.stop()

    def interrupted(self):        
        self.end()

    def isFinished(self):        
        return False