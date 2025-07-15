# main.py
from robot import Robot
from time import sleep

robot = Robot()

print("Starting robot...")

try:
    while True:
        """ if robot.is_white_tape_detected():
            print("White boundary detected! Turning.")
            robot.turn_right()
            continue

        if robot.is_obstacle_ahead() or robot.is_touch_pressed():
            print("Obstacle detected! Avoiding.")
            robot.stop()
            robot.beep()
            robot.turn_left()
            continue

        robot.move_forward() """
        sleep(2)
        print("Already started robot...")
        

except KeyboardInterrupt:
    robot.stop()
    print("Stopped by user.")
