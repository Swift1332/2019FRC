from wpilib.command import Command

class ExtendLift(Command):
    def __init__(self, robot):        
        super().__init__()

        self.robot = robot
        self.lift = self.robot.pneumatic.lift
        self.requires(self.lift)        

    def initialize(self):        
        pass

    def execute(self):
        tsi = self.timeSinceInitialized()
        tsi = tsi * 10
        value = tsi % 1

        if value > .0 and value < 0.1111:
            # extend
            self.lift.solenoid.set(self.lift.solenoid.Value.kReverse)
        else:
            # off
            self.lift.solenoid.set(self.lift.solenoid.Value.kOff)
        

    def end(self):
        self.lift.solenoid.set(self.lift.solenoid.Value.kOff)

    def interrupted(self):        
        self.end()

    def isFinished(self):        
        tsi = self.timeSinceInitialized()
        if tsi > 5:
            return True
        else:
            return False 

