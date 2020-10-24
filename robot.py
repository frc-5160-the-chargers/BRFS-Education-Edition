import magicbot
import wpilib
import wpilib.drive
import rev

from components.drivetrain import Drivetrain
from oi import OI


class MyRobot(magicbot.MagicRobot):
    drivetrain: Drivetrain  # Create drivetrain module
    oi: OI  # Create operator interface

    def teleopPeriodic(self):
        """Loops while teleop is enabled"""

        # THIS IS PROBABLY TOO SLOW, FIX DURING TESTING TOMORROW
        self.drivetrain.drive(self.oi.inSpeed / 100, self.oi.inTurn / 100)  # Drive SLOWLY so things don't break


if __name__ == "__main__":
    wpilib.run(MyRobot)  # Run the robot
#I'm not exactly sure what we're supposed to do so here's my "contribution" for now? 
