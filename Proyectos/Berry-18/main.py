from motores import carro
from machine import Pin
from time import sleep

class Berry_18(carro):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.led_izq = Pin(2, Pin.OUT)
        self.led_der = Pin(3, Pin.OUT) 

    def encender_luces(self, tiempo):
        self.led_izq.value(1)
        self.led_der.value(1)
        sleep(tiempo)
        self.led_izq.value(0)
        self.led_der.value(0)


coche = Berry_18(motor_pin1 = 14, motor_pin2 = 15)
coche.calibrar(180,0)
coche.encender_luces(1)
