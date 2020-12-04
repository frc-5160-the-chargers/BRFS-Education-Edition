import magicbot
import wpilib
import wpilib.drive
import rev
import ctre

class Drivetrain:


    #MOTOR CLASSES
    # There are many different classes of motors, because there are many different types of motors in real life, with varying use cases.
    # Programmers of the robot have to work with the hardware provided and use motor classes accordingly.
    #
    # The motors that are currently on the robot's drivetrain are REV Spark Maxes. Their class is the rev.CANSparkMax class, which is used like this:
    # self.motorLeft1 = rev.CANSparkMax(motor_number); self.motorLeft1.set(speed) 
    # NOTE: speed values passed to any motor must be within [-1,1]; For safety, set the motor power between -0.01 and 0.01
    # 
    # There are other types of motors that (if you have time) we may let you use, such as the intake or the color wheel motors. Those motors are talonSRXs, which use the ctre.TalonSRX class:
    # self.otherMotor = ctre.TalonSRX(motor_number); self.otherMotor.set(speed)


    #The motor numbers fot the main drive motors are:
    # Front_left: 1
    # Back_left: 2
    # Front_right: 3
    # Back_right: 4

    #if you want to set other motor powers, ask Colin / Harrison for the motor numbers

    
    def __init__(self):
        #Create motors (Controllers are REV Spark Maxes)
        self.motorL1 = rev.CANSparkMax(1,rev.Motortype.kbrushless)
        self.motorL2 = rev.CANSparkMax(2,rev.Motortype.kbrushless)
        self.motorR1 = rev.CANSparkMax(3,rev.Motortype.kbrushless)
        self.motorR2 = rev.CANSparkMax(4,rev.Motortype.kbrushless)

        #idk what i'm doing, after comparing to main, i j added these oop
        self.leftM = wpilib.SpeedControllerGroup(self.motorL1, self.motorL2)
        self.rightM = wpilib.SpeedControllerGroup(self.motorR1, self.motorR2)

        self.speed = 0
        self.turn = 0

        self.dt = wpilib.drive.DifferentialDrive(
            self.leftM,
            self.rightM


    def drive(self, speed, turn):
        '''Method to call when operator moves the joystick

            Inputs:
            Speed = How fast the robot moves (negative values go backward)
            Turn = How fast it is turning (negative values turn the counterclockwise)
        '''
        self.speed = speed
        self.turn = turn
    
    def execute(self):
        '''Runs every control loop'''
        #set motor powers
        #NOTE: MAXIMUM POWER IS 0.01 FOR SAFETY
        self.dt.arcadeDrive(self.speed, self.turn) #Just tells it to drive lul