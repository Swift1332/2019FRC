import wpilib
from wpilib.command import Subsystem
from subsystems.swift_double_solenoid import SwiftDoubleSolenoid

import constants

class Suspension(SwiftDoubleSolenoid):
    
    def assist(self, inputValue):
        if inputValue >= abs(0.1):
            if inputValue == abs(inputValue):
                self.extend()
            else:
                self.retract()
        else:
            self.off()
                