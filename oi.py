import wpilib

import constants
from wpilib.buttons.joystickbutton import JoystickButton

from commands.extend_shoulder import ExtendShoulder
from commands.retract_shoulder import RetractShoulder
from commands.stop_shoulder import StopShoulder

from commands.extend_elbow import ExtendElbow
from commands.retract_elbow import RetractElbow
from commands.stop_elbow import StopElbow

from commands.extend_wrist import ExtendWrist
from commands.retract_wrist import RetractWrist
from commands.stop_wrist import StopWrist

from commands.pickup_intake import PickupIntake
from commands.eject_intake import EjectIntake
from commands.stop_intake import StopIntake

from commands.extend_lift import ExtendLift 

from commands.arm_go_to_pickup import ArmGoToPickup
from commands.arm_go_to_score import ArmGoToScore
from commands.arm_stop import ArmStop
from commands.arm_go_to_tower import ArmGoToTower

class OI:
    def __init__(self, robot):
        self.joy1 = wpilib.Joystick(constants.DRIVER_STATION_JOYSTICK_0)
        self.joy1_btn_a = JoystickButton(self.joy1, 1)
        self.joy1_btn_b = JoystickButton(self.joy1, 2)
        self.joy1_btn_x = JoystickButton(self.joy1, 3)
        self.joy1_btn_y = JoystickButton(self.joy1, 4)
        self.joy1_btn_lb = JoystickButton(self.joy1, 5)
        self.joy1_btn_rb = JoystickButton(self.joy1, 6)

        self.joy2 = wpilib.Joystick(constants.DRIVER_STATION_JOYSTICK_1)

        self.joy2_btn_a = JoystickButton(self.joy2, 1)
        self.joy2_btn_b = JoystickButton(self.joy2, 2)
        self.joy2_btn_x = JoystickButton(self.joy2, 3)
        self.joy2_btn_y = JoystickButton(self.joy2, 4)
        self.joy2_btn_select = JoystickButton(self.joy2, 7)
        self.joy2_btn_start = JoystickButton(self.joy2, 8)




        #self.joy1_btn_a.whileActive(TestCommand(robot))
        '''
        self.joy1_btn_a.whenPressed(ExtendShoulder(robot))
        self.joy1_btn_a.whenReleased(StopShoulder(robot))
        self.joy1_btn_b.whenPressed(RetractShoulder(robot))
        self.joy1_btn_b.whenReleased(StopShoulder(robot))

        self.joy1_btn_x.whenPressed(ExtendElbow(robot))
        self.joy1_btn_x.whenReleased(StopElbow(robot))
        self.joy1_btn_y.whenPressed(RetractElbow(robot))
        self.joy1_btn_y.whenReleased(StopElbow(robot))

       
        self.joy2_btn_a.whenPressed(ExtendWrist(robot))
        self.joy2_btn_a.whenReleased(StopWrist(robot))
        self.joy2_btn_b.whenPressed(RetractWrist(robot))
        self.joy2_btn_b.whenReleased(StopWrist(robot))
        '''

        self.joy2_btn_x.whenPressed(PickupIntake(robot))
        self.joy2_btn_x.whenReleased(StopIntake(robot))
        self.joy2_btn_y.whenPressed(EjectIntake(robot))
        self.joy2_btn_y.whenReleased(StopIntake(robot))

        self.joy1_btn_x.whenPressed(ExtendLift(robot))        
        
        self.joy2_btn_a.whenPressed(ArmGoToPickup(robot))
        self.joy2_btn_a.whenReleased(ArmStop(robot))
        self.joy2_btn_b.whenPressed(ArmGoToScore(robot))
        self.joy2_btn_b.whenReleased(ArmStop(robot))

        self.joy2_btn_start.whenPressed(ArmGoToTower(robot))
        self.joy2_btn_start.whenReleased(ArmStop(robot))