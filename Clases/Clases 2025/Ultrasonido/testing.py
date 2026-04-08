from sensores import Ultrasonico
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
sensor = Ultrasonico()

for _ in range(10):
    
    distancia = sensor.medir()
    
    if distancia < 400:
        led.value(1)
    else:
        led.value(0)
    sleep(1)
        
    
    
    
    