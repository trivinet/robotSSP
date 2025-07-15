# robot.py
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor, TouchSensor
from ev3dev2.sound import Sound
from time import sleep

class Robot:
    def __init__(self):
        self.tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
        self.color_sensor = ColorSensor()
        self.ultrasonic_sensor = UltrasonicSensor()
        self.touch_left = TouchSensor('in1')  # depends on your port
        self.touch_right = TouchSensor('in2')
        self.sound = Sound()

    def move_forward(self, speed=30):
        self.tank_drive.on(speed, speed)

    def stop(self):
        self.tank_drive.off()

    def turn_left(self):
        self.tank_drive.on_for_degrees(-30, 30, 180)

    def turn_right(self):
        self.tank_drive.on_for_degrees(30, -30, 180)

    def is_white_tape_detected(self):
        # White usually has high reflected light
        return self.color_sensor.reflected_light_intensity > 70

    def is_obstacle_ahead(self):
        return self.ultrasonic_sensor.distance_centimeters < 20

    def is_touch_pressed(self):
        return self.touch_left.is_pressed or self.touch_right.is_pressed

    def beep(self):
        self.sound.beep()