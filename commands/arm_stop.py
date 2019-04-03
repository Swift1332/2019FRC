from wpilib.command import Command
import constants 

class ArmStop(Command):
    def __init__(self, robot):        
        super().__init__()

        self.robot = robot
        self.requires(self.robot.arm.elbow)  
        self.requires(self.robot.arm.wrist)
        self.requires(self.robot.arm.shoulder)      

    def initialize(self):        

        wrist = self.robot.arm.wrist.encoder.get()
        elbow = self.robot.arm.elbow.encoder.get()
        shoulder = self.robot.arm.shoulder.encoder.get()
        
        self.robot.arm.elbow.pid.setSetpoint(elbow)
        self.robot.arm.wrist.pid.setSetpoint(wrist)
        self.robot.arm.shoulder.pid.setSetpoint(shoulder)

        defaultMax = 1.0
        defaultMin = -1.0
        self.robot.arm.elbow.pid.setOutputRange(defaultMin, defaultMax)
        self.robot.arm.wrist.pid.setOutputRange(defaultMin, defaultMax)
        self.robot.arm.shoulder.pid.setOutputRange(defaultMin, defaultMax)
      

    def end(self):
        pass

    def interrupted(self):        
        self.end()

    def isFinished(self):        
        return False