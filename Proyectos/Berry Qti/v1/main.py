
from machine import Pin
from berry_qti import BerryQti

led_izq = Pin(2, Pin.OUT)
led_der = Pin(3, Pin.OUT)

def intermitente(izq = 0, der = 0, time = 0.1):
    led_izq.value(izq)
    led_der.value(der)

posibities = {"00":(0,0,0.5), 
              "10":(1,0,0.5),
              "01":(0,1,0.5),
              "11":(1,1,0.5)}

if __name__ == "__main__":

    berry = BerryQti(pin_izq = 26, pin_der = 27)
    izq, der, time = posibities[berry.medicion_digital()]
    intermitente()