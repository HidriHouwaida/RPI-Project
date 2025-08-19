# RGB LED Control with Raspberry Pi
A simple Python project to control an RGB LED using a Raspberry Pi. This project cycles through different colors with a common anode RGB LED.
## 🔧 Hardware Requirements
- Raspberry Pi 4

- Common anode RGB LED

- 3 resistors 220Ω 

- Breadboard

- Jumper wires
- 
## 🔌 Wiring Diagram

| RGB LED | Raspberry Pi GPIO | Physical Pin |
|---------|-------------------|------------- |
| Red     | GPIO 17           | Pin 11       |
| Green   | GPIO 18           | Pin 12       |
| Blue    | GPIO 27           | Pin 13       |
| Anode   | 3V                | Pin 6        |
----------------------------------------------

The LED will cycle through the following colors:

- 🔴 Red (2 seconds)

- 🟢 Green (2 seconds)

- 🔵 Blue (2 seconds)

- 🟡 Yellow (2 seconds)

- 🌀 Cyan (2 seconds)

- 🟣 Magenta (2 seconds)

- ⚫ Off (2 seconds)
