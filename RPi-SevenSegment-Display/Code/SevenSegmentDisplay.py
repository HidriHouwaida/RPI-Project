#Importation des bibliothéques nécessaires 
import RPi.GPIO as GPIO
import time

#chaque point dans le segement est consideré comme un led et assigné à un pin 
SEGMENTS = {
    'A': 17, 'B': 27, 'C': 22, 'D': 23, 
    'E': 24, 'G': 14, 'F': 15, 'DP': 25
}
#définition des numéros à afficher en utilisant les noms des led
DIGITS = {
    0: ['A','B','C','D','E','F'],
    1: ['B','C'],
    2: ['A','B','D','E','G'],
    3: ['A','B','C','D','G'],
    4: ['B','C','F','G'],
    5: ['A','C','D','F','G'],
    6: ['A','C','D','E','F','G'],
    7: ['A','B','C'],
    8: ['A','B','C','D','E','F','G'],
    9: ['A','B','C','D','F','G']
}

def afficher_chiffre(chiffre, point=False):
    GPIO.setmode(GPIO.BCM)
    
    
    for pin in SEGMENTS.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)  
    
    
    if chiffre in DIGITS:
        for segment in DIGITS[chiffre]:
            GPIO.output(SEGMENTS[segment], GPIO.LOW)
    
    
    if point:
        GPIO.output(SEGMENTS['DP'], GPIO.LOW)

i=0
if __name__ == "__main__":
    while not False :
        afficher_chiffre(i)  
        time.sleep(5)
        i=i+1

