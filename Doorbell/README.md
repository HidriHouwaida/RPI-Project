# Doorbell Project with Raspberry Pi
A simple doorbell system using a Raspberry Pi, an active buzzer, and a push button with pull-down resistors.
# 📋 Prerequisites
## Hardware Required
 - Raspberry Pi 4
 - Active buzzer
 - Push button
 - 2x 10kΩ resistors 
 - Jumper wires
# 🔍 Difference Between Passive and Active Buzzers
## Passive Buzzer
  - No internal oscillator - requires external frequency signal
  - Can produce different tones by varying frequency
  - More control over sound (melodies, patterns)
  - Lower power consumption when not active
  - Requires PWM signal from microcontroller
  - Typically cheaper

## Active Buzzer
 - Built-in oscillator - produces fixed tone when powered
 - Simple operation - just apply voltage to sound
 - Limited to one fixed frequency
 - Higher power consumption (always draws current when on)
 - Easier to use (no frequency control needed)
 - Typically more expensive
