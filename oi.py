import wpilib

class OI:


    #Controller Classes:
    ##there are multiple types of controllers that PyFRC can interface with. Two that are useful (more importantly, that we have controllers for) are Joystick and XBoxController.
    ##in both cases, there is a class in wpilib that represents the controller.
    # Code for Joystick input:
    # self.joystick = wpilib.Joystick(port_number)
    # 
    # Code for XBox input:
    # self.xbox = wpilib.XboxController(port_number)   



    def __init__(self):
        '''Runs once at the beginning - set up variables'''
        #Create the Controller - see above


        #set value variables; EX: self.inSpeed = 0


    # Pulling User Input:
    ## During the control loop, you can get the values of buttons/axes on the joystick/conroller by calling various methods of the joystick and the xbox controller. Some examples are below:
    # Joystick position: X (left/right), Y (forward/backward), Z (Twist): self.joystick.getX(), .getY(), .getZ()

    # Xbox Controller buttons: self.xbox.getAButton(), .getBButton(), .getXButton()
    # Xbox Controller right stick Y: self.xbox.getY(wpilib.XboxController.Hand.kRightHand)
    # For the left stick, use .kLeftHand instead
    # For all Xbox controller options, see https://first.wpi.edu/FRC/roborio/release/docs/java/edu/wpi/first/wpilibj/XboxController.html 

    # For help on any of this, ask Colin and Harrison

    def execute(self):
        '''Runs every control loop'''

        #set values to operator input; EX: self.inSpeed = self.joystick.getX() or self.a_pressed = self.xbox.getAButton()