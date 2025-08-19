from gpiozero import Buzzer, Button   
import time 
 
buzzer = Buzzer(17) 
button = Button(18) 
 
def onButtonPressed(): 
    buzzer.on() 
    print("Button is pressed, buzzer turned on >>>") 
     
def onButtonReleased(): 
    buzzer.off() 
    print("Button is released, buzzer turned on <<<") 
 
def loop(): 
    button.when_pressed = onButtonPressed 
    button.when_released = onButtonReleased 
    while True : 
        time.sleep(2) 
         
def destroy(): 
    buzzer.close() 
    button.close() 
 
try:
  loop() 
except KeyboardInterrupt:
  destroy() 
