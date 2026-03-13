
from motores import servo360, carro
from tone import Buzzer
from machine import Pin
from time import sleep

class Berry18(servo360, carro, Buzzer):

    def __init__(self, **kwargs):


        self.led_izq = Pin(kwargs["led_pin1"], Pin.OUT)
        self.led_cen = Pin(kwargs["led_pin2"], Pin.OUT)
        self.led_der = Pin(kwargs["led_pin3"], Pin.OUT)
        
        self.motores = carro(motor_pin1 = kwargs["motor_pin1"], motor_pin2 = kwargs["motor_pin2"])
        self.servo_ultrasonido = servo360(servo_pin = kwargs["servo_pin"])

    def encender_leds(self, izq_state:int, cen_state:int ,der_state:int, time:float):

        self.led_izq.value(izq_state)
        self.led_cen.value(cen_state)
        self.led_der.value(der_state)
        sleep(time)
        self.led_izq.value(0)
        self.led_cen.value(0)
        self.led_der.value(0)
        

if __name__ == "__main__":

    berry18 = Berry18(
                led_pin1 = 2,
                led_pin2 = 3,
                led_pin3 = 4,
                servo_pin = 13, 
                motor_pin1 = 14, 
                motor_pin2 = 15)

    