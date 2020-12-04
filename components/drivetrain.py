import magicbot
import wpilib
import wpilib.drive
import rev
import ctre

from utils.motor_controller import MotorController


class Drivetrain:

    front_left: MotorController
    front_right: MotorController
    back_left: MotorController
    back_right: MotorController

    TURN_MULTIPLIER: float = 1.0

    # MOTOR CLASSES There are many different classes of motors, because there are many different types of motors in
    # real life, with varying use cases. Programmers of the robot have to work with the hardware provided and use
    # motor classes accordingly.
    #
    # The motors that are currently on the robot's drivetrain are REV Spark Maxes. Their class is the rev.CANSparkMax
    # class, which is used like this: self.motorLeft1 = rev.CANSparkMax(motor_number); self.motorLeft1.set(speed)
    # NOTE: speed values passed to any motor must be within [-1,1]; For safety, set the motor power between -0.01 and
    # 0.01
    # 
    # There are other types of motors that (if you have time) we may let you use, such as the intake or the color
    # wheel motors.
    # Those motors are talonSRXs, which use the ctre.TalonSRX class:
    # self.otherMotor = ctre.TalonSRX(motor_number); self.otherMotor.set(speed)

    # The motor numbers fot the main drive motors are:
    # Front_left: 1
    # Back_left: 2
    # Front_right: 3
    # Back_right: 4

    # if you want to set other motor powers, ask Colin / Harrison for the motor numbers

    def __init__(self):
        pass
        # Create motors (Controllers are REV Spark Maxes)

    def drive(self, speed, turn):
        """
        Method to call when operator moves the joystick
            Inputs:
            Speed = How fast the robot moves (negative values go backward)
            Turn = How fast it is turning (negative values turn the counterclockwise)
        """
        self.speed = speed
        self.turn = turn

    def execute(self):
        """Runs every control loop"""
        # set motor powers
        # NOTE: MAXIMUM POWER IS 0.01 FOR SAFETY

        front_left = self.speed + (self.TURN_MULTIPLIER * self.turn)
        back_left = self.speed + (self.TURN_MULTIPLIER * self.turn)
        front_right = self.speed - (self.TURN_MULTIPLIER * self.turn)
        back_right = self.speed - (self.TURN_MULTIPLIER * self.turn)

        max_power = max(front_left, back_left, front_right, back_right)

        self.back_left.set(max_power * back_left)
        self.front_left.set(max_power * front_left)
        self.front_right.set(max_power * front_right)
        self.back_right.set(max_power * back_right)




