from machine import Pin
import sys

led = Pin(2, Pin.OUT)  # Usa el LED incorporado

while True:
    comando = sys.stdin.readline().strip()
    if comando == "1":
        led.value(1)
        print("LED encendido")
    elif comando == "0":
        led.value(0)
        print("LED apagado")
