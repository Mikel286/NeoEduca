from time import sleep
from melectronic import Joystick

joystick = Joystick()
apretado = False

while apretado == False :
    
    x, y, apretado = joystick.medir()
    print(f"x:{x}	y:{y}	apretado:{"apretado" if apretado else "libre"}")
    sleep(0.05)