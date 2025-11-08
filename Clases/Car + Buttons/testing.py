from motores import carro, servo360
from time import sleep

pin_motorIzq = 14
pin_motorDer = 15
auto = carro(pin_motorIzq, pin_motorDer)

# Codigo de prueba para que veais como funciona las ruedas
auto.moveadelante()
sleep(1)
auto.movedetener()


