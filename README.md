# EV3 Autonomous Robot – Gem Collector

This project controls a LEGO Mindstorms EV3 robot capable of:

- 🚧 Avoiding obstacles using ultrasonic and touch sensors
- 📦 Collecting gems using a third servo motor
- ⛔ Staying inside boundaries (white tape)
- 🤖 Operating in different behavior states (explore, avoid, collect)

---

## 🧩 Hardware Components

- EV3 programmable brick
- 3 servo motors (2 for drive, 1 for gem collection)
- Ultrasonic sensor (obstacle detection)
- 2 touch sensors (wall contact)
- Light sensor (white tape detection)
- Gyro sensor (orientation tracking)

---

## 📁 Project Structure

ev3_project/
├── main.py # Main control loop
├── robot.py # Hardware abstraction (sensors/motors)
├── states.py # State machine (explore, avoid, collect)
├── actions.py # Movement and interaction functions
├── utils.py # Constants and helpers
└── README.md # This file

---

## 🧠 Behavior Overview

The robot runs in 3 states:
- **Explore**: move around, detect gems
- **Avoid**: react to obstacles or tape
- **Collect**: use third motor to collect gem

Transitions are based on sensor input.

---

## 🛠️ Getting Started

1. Flash `ev3dev` to your EV3 brick  
2. Install Python3 and `ev3dev2` on the brick  
3. Copy code via SSH or SCP  
4. Run `main.py` on the robot  
5. Watch it drive, explore, and collect!

---

## 📜 License

MIT License (or your choice)

---

## ✨ To Do

- [ ] Fine-tune sensor thresholds
- [ ] Calibrate movement distances
- [ ] Add logging or visual mapping