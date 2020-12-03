import magicbot
import wpilib
import wpilib.drive
import rev

class Drivetrain:
    def __init__(self):
        #Create motors (Controllers are REV Spark Maxes)
        self.motorLeft1 = rev.CANSparkMax(1, rev.MotorType.kBrushless)
        self.motorLeft2 = rev.CANSparkMax(2, rev.MotorType.kBrushless)
        self.motorRight1 = rev.CANSparkMax(3, rev.MotorType.kBrushless)
        self.motorRight2 = rev.CANSparkMax(4, rev.MotorType.kBrushless)

        #Create speed controller groups so motors on the same side of the drivetrain behave the same
        self.leftMotors = wpilib.SpeedControllerGroup(self.motorLeft1, self.motorLeft2)
        self.rightMotors = wpilib.SpeedControllerGroup(self.motorRight1, self.motorRight2)

        self.speed = 0 #How fast to move forward (or backward if negative)
        self.turn = 0 #How much to turn

        #Create drivetrain
        self.dt = wpilib.drive.DifferentialDrive(
            self.leftMotors,
            self.rightMotors
        )

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
        self.dt.arcadeDrive(self.speed, self.turn) #Just tells it to drive lul
