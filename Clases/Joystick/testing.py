from machine import Pin, ADC
import time

# Configurar los pines del joystick
x = ADC(26)   # VRx -> GP26 / ADC0
y = ADC(27)   # VRy -> GP27 / ADC1
boton = Pin(2, Pin.IN, Pin.PULL_UP)  # SW -> GP2

# Función para leer valores normalizados (0 a 65535)
def leer_joystick():
    valor_x = x.read_u16()
    valor_y = y.read_u16()
    pulsado = not boton.value()  # activo en bajo
    return valor_x, valor_y, pulsado

while True:
    vx, vy, btn = leer_joystick()

    # Convertir a un rango más legible (−100 a +100)
    eje_x = round(((vx - 32768) / 32768) * 100)
    eje_y = round(((vy - 32768) / 32768) * 100)

    print(f"X: {eje_x:>4}  Y: {eje_y:>4}  Botón: {'PRESIONADO' if btn else 'libre'}")

    time.sleep(0.1)
