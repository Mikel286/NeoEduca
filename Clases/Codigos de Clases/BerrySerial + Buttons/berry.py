from machine import Pin
import sys
from time import sleep

switch_izq = Pin(0, Pin.IN, Pin.PULL_UP)
switch_der = Pin(1, Pin.IN, Pin.PULL_UP)

while True:
    if switch_izq.value() == 0 and switch_der.value() == 0:
        print("BIDA") # Botones - Izquierdo - Derecho - Apretados
    elif switch_izq.value() == 0:
        print("BIA") # Botones - Izquierdo - Apretados
    elif switch_der.value() == 0:
        print("BDA") # Botones - Derecho - Apretados
    else:
        print("BNA") # Botones - Derecho - Apretados
    sleep(0.2)