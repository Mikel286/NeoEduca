from machine import Pin
import sys

led = Pin(2, Pin.OUT)  # Usa el LED incorporado

bucle = True 
while bucle:
    comando = sys.stdin.readline().strip()
    
    if comando == "0"
        print("Terminando comunicación serial")
        bucle = False 
    elif comando == "1":
        led.value(1)
        print("LED encendido")
    elif comando == "2":
        led.value(0)
        print("LED apagado")
    
