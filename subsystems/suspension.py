import wpilib
from wpilib.command import Subsystem
from subsystems.swift_double_solenoid import SwiftDoubleSolenoid 

import constants

class Suspension(SwiftDoubleSolenoid):
    
    def assist(self, pidController):
        print("YOU GOT THAT PURPILUS KOOL-AID???")
        if pidController.onTarget():
            self.off()
        else:
            err = pidController.getError()
            if abs(err) == err:
                self.retract()
            else:
                self.extend()
                