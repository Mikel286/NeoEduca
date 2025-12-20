from machine import Pin, ADC
from motores import servo360
from sensores import Ldr
from time import sleep

# Configuracion de los motores
ejeH = servo360(15)
ejeV = servo360(14)

# Configurar los pines del joystick
x = ADC(26)   # VRx -> GP26 / ADC0
y = ADC(27)   # VRy -> GP27 / ADC1
boton = Pin(7, Pin.IN, Pin.PULL_UP)  # SW -> GP2

# Función para leer valores normalizados (0 a 65535)
def leer_joystick():
    valor_x = x.read_u16()
    valor_y = y.read_u16()
    pulsado = not boton.value()  # activo en bajo
    return valor_x, valor_y, pulsado


bucle = True 
while bucle:
    vx, vy, btn = leer_joystick()

    # Convertir a un rango más legible (−100 a +100)
    eje_x = round(((vx - 32768) / 32768) * 100)
    eje_y = round(((vy - 32768) / 32768) * 100) * -1

    print(f"X: {eje_x:>4}  Y: {eje_y:>4}  Botón: {'PRESIONADO' if btn else 'libre'}")

    if btn:
        bucle = False 

    if eje_x >= 99 and eje_y < 99:
        ejeH.girar(0)
    elif eje_x <= -99:
        ejeH.girar(180)
    elif eje_y >= 99:
        ejeV.girar(0)
    elif eje_y <= -99:
        ejeV.girar(180)
    else:
        ejeH.detener()
        ejeV.detener()

    sleep(0.1)

