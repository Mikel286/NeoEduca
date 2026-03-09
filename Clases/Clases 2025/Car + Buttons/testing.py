from motores import carro
from machine import Pin
from time import sleep

switch_izq = Pin(0, Pin.IN, Pin.PULL_UP)
switch_der = Pin(1, Pin.IN, Pin.PULL_UP)
auto = carro(14, 15)
auto.setvelocidad(30,120)

def adelante(tiempo, angulo_1, angulo_2):
    auto.setvelocidad(angulo_1, angulo_2)
    auto.moveadelante()
    sleep(tiempo)
    auto.movedetener()

def atras(tiempo, angulo_1, angulo_2):
    auto.setvelocidad(angulo_1, angulo_2)
    auto.moveatras()
    sleep(tiempo)
    auto.movedetener()
    
def derecha(tiempo, angulo_1, angulo_2):
    auto.setvelocidad(angulo_1, angulo_2)
    auto.movederecha()
    sleep(tiempo)
    auto.movedetener()

def adelante(tiempo, angulo_1, angulo_2):
    auto.setvelocidad(angulo_1, angulo_2)
    auto.moveizquierda()
    sleep(tiempo)
    auto.movedetener()


while True:
<<<<<<< HEAD
    if switch.value() == 0:
        print("🔘 El switch está PRESIONADO")
        auto.moveadelante()
=======
    if switch_izq.value() == 0 and switch_der.value() == 0:
        print("🔘 El switch_izq y switch_der está PRESIONADO")
    elif switch_izq.value() == 0:
        print("🔘 El switch_izq está PRESIONADO")
    elif switch_der.value() == 0:
        print("🔘 El switch_der está PRESIONADO")
>>>>>>> 8cd6321924c73c52ef02a7d397d0e29e3703a36a
    else:
        print("⚪ Ambos switch está LIBERADO")
        auto.movedetener()
    sleep(0.2)




