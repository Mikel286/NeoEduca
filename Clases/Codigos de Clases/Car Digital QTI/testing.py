from random import randint
from machine import Pin
from time import sleep
from motores import carro

xtr_izq = Pin(7, Pin.IN, Pin.PULL_UP)
izq = Pin(8, Pin.IN, Pin.PULL_UP)
der = Pin(10, Pin.IN, Pin.PULL_UP)
xtr_der = Pin(11, Pin.IN, Pin.PULL_UP)

auto = carro(15, 14)
auto.setvelocidad(95, 85)

led_izq = Pin(2, Pin.OUT)
led_der = Pin(3, Pin.OUT)

cont = 0
time_step = 0.05

auto.movedetener()

def realizar_medicion(file, opcion):
    file.write("[MEDICION] ")
    if opcion == 1:
        medicion = f"{xtr_izq.value()}{izq.value()}{der.value()}{xtr_der.value()}"
        file.write(f"Medicion: {medicion}\n\n")
        return medicion
    elif opcion == 2:
        medicion = f"{randint(0,1)}{randint(0,1)}{randint(0,1)}{randint(0,1)}"
        file.write(f"Medicion: {medicion}\n\n")
        return medicion
    
def output_accion(file, accion):
    file.write("[ACCION] ")
    file.write(f"Accion: {accion}\n\n")
    
    
def avanzar(file):
    output_accion(file, "avanzar")
    led_izq.on()
    led_der.on()
    auto.moveadelante()
    return True

def girar_izq(file):
    output_accion(file, "girar izquierda")
    led_izq.on()
    led_der.off()
    auto.moveizquierda()
    return True

def girar_der(file):
    output_accion(file, "girar derecha")
    led_izq.off()
    led_der.on()
    auto.movederecha()
    return True

def negro(file):
    output_accion(file, "negro")
    global cont
    cont += 1
    file.write("[CONTADOR] ")
    file.write(f"Contador: {cont}\n\n")
    return True 

acciones = {
    "0000":negro,
    "1000":girar_der,
    "0100":avanzar,
    "0010":avanzar,
    "0001":girar_izq,
    "1100":girar_der,
    "1010":avanzar,
    "1001":avanzar,
    "1111":avanzar,
    "0111":girar_izq,
    "1011":girar_izq,
    "1101":girar_der,
    "1110":girar_der,
    "0011":girar_izq,
    "0101":avanzar,
    "0110":avanzar}


if __name__ == "__main__":
    
    path = "output.txt"
    with open(path, 'w') as file:
        
        bucle = True
        bucle_cont = 0
        while bucle:
            
                medicion = realizar_medicion(file, 1)
                
                bucle = acciones[medicion](file)
                sleep(time_step)
                bucle_cont += 1
        
    
