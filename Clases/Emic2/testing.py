from machine import UART, Pin
import time
import sys

# UART1 en GPIO4 (TX) y GPIO5 (RX)
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# Espera a que el módulo arranque
time.sleep(2)

# Limpia cualquier mensaje inicial
while uart.any():
    uart.read()

# Envía texto al Emic 2
def hablar(texto):
    comando = f'S{texto}\n'
    uart.write(comando)
    # El Emic responde con ':' cuando termina de hablar
    while True:
        if uart.any():
            if uart.read(1) == b':':
                from machine import Pin

while True:
    informacion = sys.stdin.readline().strip()
    hablar(informacion)



