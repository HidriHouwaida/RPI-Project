# imporatation des bibliothÃ©ques nÃ©cessaires 
from gpiozero import RGBLED 
import time

# Configuration des broches
led = RGBLED(red= 17, green= 18, blue=27, active_high=False)
# Boucle pour l'affichage des différents couleurs 
try:
    while True:
        led.color = (1, 0, 0)
        print("le led est allumÃ© avec le couleur rouge ")
        time.sleep(2)
        led.color = (0, 1, 0)
        print("le led est allumÃ© avec le couleur vert ")
        time.sleep(2)
        led.color = (0, 0, 1)
        print("le led est allumÃ© avec le couleur blue ")
        time.sleep(2)
        led.color = (1, 1, 0)
        print("le led est allumÃ© avec le couleur jaune ")
        time.sleep(2)
        led.color = (0, 1, 1)
        print("le led est allumÃ© avec le couleur cyan ")
        time.sleep(2)
        led.color = (1, 0, 1)
        print("le led est allumÃ© avec le couleur magenta ")
        time.sleep(2)
        led.color = (0, 0, 0)
        print("le led est eteint ")
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()


