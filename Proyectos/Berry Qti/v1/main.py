
from machine import Pin
from berry_qti import BerryQti
from motores import carro

led_izq = Pin(2, Pin.OUT)
led_der = Pin(3, Pin.OUT)

coche = carro(14, 15)
coche.setvelocidad(180,0)

def intermitente(izq = 0, der = 0, time = 0.1):
    led_izq.value(izq)
    led_der.value(der)

posibities_led = {"00":(0,0,0.5), 
              "10":(1,0,0.5),
              "01":(0,1,0.5),
              "11":(1,1,0.5)}

posibities_motores

if __name__ == "__main__":

    berry = BerryQti(pin_izq = 27, pin_der = 28)
    
    #berry.medicion_normal()
    #izq, der, time = posibities[berry.medicion_digital()]
    #intermitente(izq = izq, der = der, time = time)
    
    coche.moveadelante()