from keyboard import Keyboard
from machine import Pin
import time

def llamar(numero):
    
    if len(numero) == 9:
        return True
    return False 

teclado = Keyboard()
contactos = dict()
numero = ""
while True:
    tecla = teclado.scan()
    if tecla is not None:
        print("Tecla:", tecla)
        if tecla in ("1234567890"):
            numero += tecla
            print(f"Es un numero: {numero}")
        else:
            pass
        time.sleep(0.3)