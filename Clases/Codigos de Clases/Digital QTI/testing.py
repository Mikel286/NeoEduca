from machine import Pin
from time import sleep
from acciones import Step_n, Step_Counter, Step_Avanzar

xtr_izq = Pin(7, Pin.IN, Pin.PULL_UP)
izq = Pin(8, Pin.IN, Pin.PULL_UP)
cen = Pin(9, Pin.IN, Pin.PULL_UP)
der = Pin(10, Pin.IN, Pin.PULL_UP)
xtr_der = Pin(11, Pin.IN, Pin.PULL_UP)

acciones = {
    "00000":Step_Counter,
    "00001":Step_n,
    "00010":Step_n,
    "00011":Step_n,
    "00100":Step_n,
    "00101":Step_n,
    "00110":Step_n,
    "00111":Step_n,
    "01000":Step_n,
    "01001":Step_n,
    "01010":Step_n,
    "01011":Step_n,
    "01100":Step_n,
    "01101":Step_n,
    "01110":Step_n,
    "01111":Step_n,
    "10000":Step_n,
    "10001":Step_n,
    "10010":Step_n,
    "10011":Step_n,
    "10100":Step_n,
    "10101":Step_n,
    "10110":Step_n,
    "10111":Step_n,
    "11000":Step_n,
    "11001":Step_n,
    "11010":Step_n,
    "11011":Step_n,
    "11100":Step_n,
    "11101":Step_n,
    "11110":Step_n,
    "11111":Step_Avanzar}

time_step = 0.5
bucle = True 
while bucle:
    
    medicion = f"{xtr_izq.value()}{izq.value()}{cen.value()}{der.value()}{xtr_der.value()}"
    bucle = acciones[medicion](medicion = medicion)
    sleep(time_step)
    
    