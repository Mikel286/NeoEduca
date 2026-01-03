from machine import Pin
from motores import servo360, carro
from time import sleep

led_izq = Pin(2, Pin.OUT)
led_der = Pin(3, Pin.OUT)

motor_izq = servo360(14)
motor_der = servo360(15)

coche = carro(14,15)

def step_0():
    return False

def step_1():
    
    global led_izq
    global led_der
    
    led_izq.value(1)
    led_der.value(1)
    sleep(1)
    led_izq.value(0)
    led_der.value(0)
    
    return True 
    
def step_2():
    
    global motor_izq
    global motor_der
    
    motor_izq.barrer()
    motor_der.barrer()
    
    return True

def step_3():
    
    global coche
    
    angulo_1 = int(input("Indique el angulo de giro izquierdo (0-180): "))
    angulo_2 = int(input("Indique el angulo de giro derecho (0-180): "))
    
    coche.calibrar(angulo_1, angulo_2)
    
    return True 
    
def step_4():
    
    global coche
    
    angulo_1 = int(input("Indique el angulo de giro izquierdo (0-180): "))
    angulo_2 = int(input("Indique el angulo de giro derecho (0-180): "))
    
    coche.setvelocidad(angulo_1, angulo_2)
    
    coche.moveadelante()
    sleep(1)
    coche.moveizquierda()
    sleep(1)
    coche.movederecha()
    sleep(1)
    coche.moveatras()
    sleep(1)
    coche.movedetener()
    
    return True 
    
steps = {'0':step_0, '1':step_1, '2':step_2, '3':step_3, '4': step_4}

if __name__  == '__main__':
    
    bucle = True
    
    while bucle:
        step = input("Indique el step que desea ejecutar: ")
        
        if step in steps.keys():
            bucle = steps[step]()
        