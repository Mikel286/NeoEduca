from motores import carro
from machine import Pin
from time import sleep

switch = Pin(0, Pin.IN, Pin.PULL_UP)
auto = carro(14, 15)
auto.setvelocidad(30,120)

while True:
    if switch.value() == 0:
        print("🔘 El switch está PRESIONADO")
        ## ✏️ Colocad aqui el codigo de motores
        auto.moveadelante()
    else:
        print("⚪ El switch está LIBERADO")
        auto.movedetener()
    sleep(0.2)



