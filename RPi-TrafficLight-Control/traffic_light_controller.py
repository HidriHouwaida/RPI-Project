import RPi.GPIO as GPIO
import time

# Définition des broches GPIO (modifiable selon votre câblage)
ledRougePin = 11
ledVertPin = 13
ledJaunePin = 15

def setup():
    GPIO.setmode(GPIO.BOARD)  # Utilise la numérotation physique des broches
    GPIO.setup(ledRougePin, GPIO.OUT)
    GPIO.setup(ledVertPin, GPIO.OUT)
    GPIO.setup(ledJaunePin, GPIO.OUT)
    # Éteint toutes les LEDs au démarrage
    GPIO.output(ledRougePin, GPIO.LOW)
    GPIO.output(ledVertPin, GPIO.LOW)
    GPIO.output(ledJaunePin, GPIO.LOW)
    
    print(f"Configuration OK - Rouge: pin{ledRougePin}, Vert: pin{ledVertPin}, Jaune: pin{ledJaunePin}")

def loop():
    while True:
        # Phase ROUGE (arrêt)
        GPIO.output(ledRougePin, GPIO.HIGH)
        print("🔴 Feu ROUGE allumé (Arrêt)")
        time.sleep(5)  # 5 secondes
        
        # Phase VERT (passage)
        GPIO.output(ledRougePin, GPIO.LOW)
        GPIO.output(ledVertPin, GPIO.HIGH)
        print("🟢 Feu VERT allumé (Passage)")
        time.sleep(5)  # 5 secondes
        
        # Phase JAUNE (attention)
        GPIO.output(ledVertPin, GPIO.LOW)
        GPIO.output(ledJaunePin, GPIO.HIGH)
        print("🟡 Feu JAUNE allumé (Attention)")
        time.sleep(2)  # 2 secondes
        
        # Éteindre le jaune avant de revenir au rouge
        GPIO.output(ledJaunePin, GPIO.LOW)

def destroy():
    GPIO.cleanup()  # Nettoyage des broches GPIO
    print("Programme arrêté. GPIO nettoyées.")

if __name__ == '__main__':
    print("Démarrage du simulateur de feux de circulation...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Ctrl+C pour arrêter
        destroy()
