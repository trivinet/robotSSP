# actions.py

from time import sleep
from utils import (PORT_TOUCH_LEFT,  PORT_TOUCH_RIGHT, DEFAULT_SPEED, DEFAULT_SPEED_ARM, WHITE_THRESHOLD, OBSTACLE_DISTANCE_CM, DEGREES_180, DEGREES_360, DEGREES_90)

def drive_forward(robot, speed=DEFAULT_SPEED):
    robot.move_forward(speed)

def drive_backward(robot, speed=DEFAULT_SPEED, duration=1):
    robot.move_backward(speed)
    sleep(duration)
    robot.stop()

def avoid_obstacle(robot):
    print("[ACTION] Avoiding obstacle")
    robot.stop()
    robot.beep()
    drive_backward(robot, speed=DEFAULT_SPEED, duration=1)
    robot.turn_right(speed=DEFAULT_SPEED, degrees=DEGREES_180)
    robot.stop()

def avoid_boundary(robot):
    print("[ACTION] Avoiding white boundary")
    robot.stop()
    robot.beep()
    drive_backward(robot, speed=DEFAULT_SPEED, duration=1)
    robot.turn_left(speed=DEFAULT_SPEED, degrees=DEGREES_180)
    robot.stop()

def collect_gem(robot):
    print("[ACTION] Collecting gem")
    robot.stop()
    robot.collect_gem()
    robot.say("Gem collected")
    sleep(0.5)
    robot.stop()

def spin_search(robot, degrees=DEGREES_360):
    print("[ACTION] Spinning to search")
    robot.turn_right(speed=DEFAULT_SPEED, degrees=degrees)

def check_and_recover_if_bumped(robot):
    if robot.is_touch_pressed():
        print("[ACTION] Bump detected, recovering")
        robot.stop()
        robot.beep()
        drive_backward(robot, speed=DEFAULT_SPEED, duration=1)
        robot.turn_left(speed=DEFAULT_SPEED, degrees=DEGREES_90)
