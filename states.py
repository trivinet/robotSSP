# states.py

from actions import (
    drive_forward,
    avoid_obstacle,
    avoid_boundary,
    collect_gem,
    check_and_recover_if_bumped
)
from utils import (COLOR_GREEN, COLOR_RED)

class StateMachine:
    def __init__(self, robot):
        self.robot = robot
        self.state = "explore"
        self.has_gem = False

    def update(self):
        print(f"[STATE] Current state: {self.state}")

        if self.state == "explore":
            if self.robot.is_white_boundary():
                self.state = "avoid"
                avoid_boundary(self.robot)

            elif self.robot.is_obstacle_ahead():
                self.state = "avoid"
                avoid_obstacle(self.robot)

            elif self.robot.is_touch_pressed():
                self.state = "avoid"
                check_and_recover_if_bumped(self.robot)

            elif self.robot.color_sensor.color in [COLOR_GREEN, COLOR_RED]:  # e.g. green or red gem
                self.state = "collect"
                collect_gem(self.robot)
                self.has_gem = True

            else:
                drive_forward(self.robot)

        elif self.state == "avoid":
            print("[STATE] Avoid complete. Returning to explore.")
            self.state = "explore"

        elif self.state == "collect":
            print("[STATE] Collected gem. Returning to explore.")
            self.state = "explore"
