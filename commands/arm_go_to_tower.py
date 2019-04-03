from wpilib.command import Command
import constants 

class ArmGoToTower(Command):
    def __init__(self, robot):        
        super().__init__()

        self.robot = robot
        self.requires(self.robot.arm.elbow)  
        self.requires(self.robot.arm.wrist)
        self.requires(self.robot.arm.shoulder)      

    def initialize(self):
                
        self.robot.arm.elbow.pid.setOutputRange(constants.ELBOW_AUTOMATIC_MINIMUM, constants.ELBOW_AUTOMATIC_MAXIMUM)
        self.robot.arm.wrist.pid.setOutputRange(constants.AUTOMATIC_ARM_MINIMUM, constants.AUTOMATIC_ARM_MAXIMUM)
        self.robot.arm.shoulder.pid.setOutputRange(constants.AUTOMATIC_ARM_MINIMUM, constants.AUTOMATIC_ARM_MAXIMUM)
        
        self.robot.arm.elbow.pid.setSetpoint(constants.ELBOW_TOWER_POSITION)
        self.robot.arm.wrist.pid.setSetpoint(constants.WRIST_TOWER_POSITION)
        self.robot.arm.shoulder.pid.setSetpoint(constants.SHOULDER_TOWER_POSITION)
    
    def execute(self):
        pass

    def end(self):
        pass

    def interrupted(self):        
        self.end()

    def isFinished(self):        
        return False