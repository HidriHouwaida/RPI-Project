# 7-Segment Display Controller for Raspberry Pi

This project controls a 7-segment display using a Raspberry Pi and Python. It sequentially displays numbers from 0 to 9 with a 5-second interval between each number.

## Features

- Controls a common cathode 7-segment display
- Displays digits 0-9 sequentially
- Uses GPIO pins on Raspberry Pi
- Simple and easy-to-understand code structure

## Hardware Requirements

- Raspberry Pi (any model with GPIO pins)
- 7-segment display (common cathode)
- Jumper wires
- Breadboard (optional)
- 220Ω resistors (8 pieces, recommended for current limiting)

## Wiring

The 7-segment display segments are connected to the following GPIO pins:

| Segment | GPIO Pin |
|---------|-----------|
| A       | 17        |
| B       | 27        |
| C       | 22        |
| D       | 23        |
| E       | 24        |
| F       | 15        |
| G       | 14        |
| DP      | 25        |
|_____________________|
