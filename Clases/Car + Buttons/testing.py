
from machine import Pin
import time

# Configura el pin donde está conectado el switch (por ejemplo, el pin 14)
# Pin.IN -> lo configura como entrada
# Pin.PULL_UP -> activa la resistencia interna de pull-up (opcional, depende del circuito)
switch = Pin(0, Pin.IN, Pin.PULL_UP)

while True:
    if switch.value() == 0:
        print("🔘 El switch está PRESIONADO")
    else:
        print("⚪ El switch está LIBERADO")
    time.sleep(0.2)



