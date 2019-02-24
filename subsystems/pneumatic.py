import wpilib
from wpilib.command import Subsystem

import constants

from .pneumatic_components.hatch import Hatch
from .pneumatic_components.lift import Lift 
from .suspension import Suspension

class Pneumatic(Subsystem):

    def __init__(self, robot):
        super().__init__()
        self.robot = robot 

        self.lift = Lift(
            robot,
            constants.LIFT_RETRACT,
            constants.LIFT_EXTEND

        )

        self.hatch = Hatch(
            robot,
            constants.HATCH_RETRACT,
            constants.HATCH_EXTEND
        )

        self.suspension = Suspension(
            robot,
            constants.SUSPENSION_RETRACT,
            constants.SUSPENSION_EXTEND
        )