import rev


class MotorController:

    def __init__(self, motor, maximum_safe_speed: float = 0.01):
        self.motor = motor
        self.maximum_safe_speed = maximum_safe_speed

    def set(self, power: float):
        if power > 0.01:
            raise ValueError("WHAT ARE YOU DOING ARE YOU TRYING TO BREAK THE ROBOT")
        else:
            self.motor.set(power)

    def stop(self):
        self.motor.stop_motor()


class SparkMaxMotorController(MotorController):
    def __init__(self, motor_number, maximum_safe_speed: float = 0.01):
        motor = rev.CANSparkMax(motor_number)
        super().__init__(motor, maximum_safe_speed)
