# robot.py
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_B, OUTPUT_C, OUTPUT_A, MoveTank
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor, TouchSensor, GyroSensor
from ev3dev2.sound import Sound
from time import sleep
from utils import (PORT_TOUCH_LEFT,  PORT_TOUCH_RIGHT, DEFAULT_SPEED, DEFAULT_SPEED_ARM, WHITE_THRESHOLD, OBSTACLE_DISTANCE_CM, DEGREES_180, DEGREES_360, DEGREES_90)

class Robot:
    def __init__(self):
        # Drive motors
        self.tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

        # Gem collection motor (OUTPUT_A assumed)
        self.collector = MediumMotor(OUTPUT_A)

        # Sensors
        self.color_sensor = ColorSensor()
        self.ultrasonic = UltrasonicSensor()
        self.touch_left = TouchSensor(PORT_TOUCH_LEFT)
        self.touch_right = TouchSensor(PORT_TOUCH_RIGHT)
        self.gyro = GyroSensor()

        # Speaker
        self.sound = Sound()

        # Gyro setup
        self.gyro.reset()

    # Movement
    def move_forward(self, speed=DEFAULT_SPEED):
        self.tank_drive.on(speed, speed)

    def move_backward(self, speed=DEFAULT_SPEED):
        self.tank_drive.on(-speed, -speed)

    def stop(self):
        self.tank_drive.off()

    def turn_left(self, speed=DEFAULT_SPEED, degrees=TURN_DEGREES):
        self.tank_drive.on_for_degrees(-speed, speed, degrees)

    def turn_right(self, speed=DEFAULT_SPEED, degrees=TURN_DEGREES):
        self.tank_drive.on_for_degrees(speed, -speed, degrees)

    # Sensors
    def is_white_boundary(self):
        return self.color_sensor.reflected_light_intensity > WHITE_THRESHOLD

    def is_obstacle_ahead(self, threshold_cm=OBSTACLE_DISTANCE_CM):
        return self.ultrasonic.distance_centimeters < threshold_cm

    def is_touch_pressed(self):
        return self.touch_left.is_pressed or self.touch_right.is_pressed

    def get_angle(self):
        return self.gyro.angle

    def reset_gyro(self):
        self.gyro.reset()

    # Collector
    def collect_gem(self):
        self.collector.on_for_degrees(speed=DEFAULT_SPEED_ARM, degrees=DEFAULT_SPEED)  # extend arm
        sleep(0.5)
        self.collector.on_for_degrees(speed=-DEFAULT_SPEED_ARM, degrees=TURN_DEGREES)  # retract

    # Sound
    def beep(self):
        self.sound.beep()

    def say(self, text="Gem collected"):
        self.sound.speak(text)
