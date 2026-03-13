from turtle import Turtle, bye
from serial import Serial
import time

puerto = 'COM3'   # cambia si es necesario
baudrate = 115200

tortuga = Turtle()
tortuga.speed(5)
tortuga.color(0,0,0)
tortuga.pensize(3)

ser = Serial(puerto, baudrate, timeout=1)
time.sleep(2)  # Esperar a que se establezca la conexión

print("Conectado al Pico. Escribe '1' para encender o '0' para apagar el LED. Ctrl+C para salir.")

while True:
    respuesta = ser.readline().decode().strip()
    if respuesta:
        print("Pico:", respuesta)
    if respuesta == "BIDA":
        break
    elif respuesta == "BIA":
        tortuga.right(10)
    elif respuesta == "BDA":
        tortuga.forward(10)
bye()
