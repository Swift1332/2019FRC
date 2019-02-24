from wpilib.command import Command

class TestCommand(Command):
    def __init__(self, robot):
        print("Test constructing")
        super().__init__()
        self.robot = robot        
        print("Test constructed")


    def initialize(self):
        """The initialize method is called the first time this Command is run
        after being started.
        """
        print("test initialize")

    def execute(self):
        """The execute method is called repeatedly until this Command either
        finishes or is canceled.
        """
        print("test execute")

    def isFinished(self):
        print("test is finished")

        return False

    def end(self):
        """Called when the command ended peacefully.  This is where you may
        want to wrap up loose ends, like shutting off a motor that was being
        used in the command.
        """
        print("test end")

    def interrupted(self):
        """Called when the command ends because somebody called cancel() or
        another command shared the same requirements as this one, and booted
        it out.

        This is where you may want to wrap up loose ends, like shutting off a
        motor that was being used in the command.

        Generally, it is useful to simply call the end() method within this
        method, as done here.
        """
        print("test interrupted")
        self.end()
