import rev
import wpilib.interfaces
from wpilib.interfaces._interfaces import SpeedController


class MotorController(SpeedController):

    def __init__(self, motor, maximum_safe_speed: float = 0.01):
        super().__init__()
        self.motor = motor
        self.maximum_safe_speed = maximum_safe_speed

    @staticmethod
    def validate_input(self, power: float) -> float:
        if power > 0.01:
            raise ValueError("WHAT ARE YOU DOING ARE YOU TRYING TO BREAK THE ROBOT")
        else:
            return power

    def stop(self):
        self.motor.stop_motor()

    def get(self) -> float:
        return self.motor.get()

    def set(self, power: float):
        self.motor.set(self.validate_input(power))

    def getInverted(self) -> bool:
        return self.motor.getInverted()

    def setInverted(self, isInverted: bool) -> None:
        self.motor.setInverted(isInverted)

    def setVoltage(self, output) -> None:
        self.motor.setVoltage(output)

    def stopMotor(self) -> None:
        self.motor.stopMotor()


class SparkMaxMotorController(MotorController):
    def __init__(self, motor_number, maximum_safe_speed: float = 0.01):
        motor = rev.CANSparkMax(motor_number)
        super().__init__(motor, maximum_safe_speed)
