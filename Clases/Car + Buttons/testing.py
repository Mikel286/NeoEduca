from motores import servo360
from machine import Pin
import time

switch = Pin(0, Pin.IN, Pin.PULL_UP)
motor = servo360(15)
motor.barre()

while True:
    if switch.value() == 0:
        print("🔘 El switch está PRESIONADO")
        ## ✏️ Colocad aqui el codigo de motores
        
    else:
        print("⚪ El switch está LIBERADO")
    time.sleep(0.2)



