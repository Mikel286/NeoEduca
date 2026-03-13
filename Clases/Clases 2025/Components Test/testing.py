from machine import Pin
from time import sleep
from motores import servo360
from tone import Buzzer
from sensores import Ultrasonico, Qti, Ldr

text = """Se lista los step disponibles:

    [0] Termimar programa
    [1] Testear Leds
    [2] Testear Servomotores
    [3] Testear Botones
    [4] Testear Buzzer
    [5] Testear Ultrasonido
    
Indique el numero del step que va a ejecutar: """

def step_end():
    return False

def step_leds():
    
    led_izq = Pin(2, Pin.OUT)
    led_cen = Pin(3, Pin.OUT)
    led_der = Pin(4, Pin.OUT)
    
    led_izq.value(1)
    led_cen.value(1)
    led_der.value(1)
    
    sleep(1)
    
    led_izq.value(0)
    led_cen.value(0)
    led_der.value(0)
    
    return True

def step_servomotores():
    
    motor_izq = servo360(14)
    motor_der = servo360(15)
    
    motor_izq.barrer()
    motor_der.barrer()
    
    return True

def step_switch():
    
    switch_izq = Pin(0, Pin.IN, Pin.PULL_UP)
    switch_der = Pin(1, Pin.IN, Pin.PULL_UP)
    
    for _ in range(50):
        print(f"Switch Izquierdo: {switch_izq.value()}", f"Switch derecho: {switch_der.value()}")
        sleep(0.2)
    return True

def step_buzzer():
    
    buzzer = Buzzer(5)
    
    frec_notas = [261, 293, 329, 349, 392]
    
    for frecuencia in frec_notas:
        buzzer.tone(frecuencia, 1, 0.5)
        
    return True 

def step_utltrasonido():
    
    ultrasonido = Ultrasonico()
    
    for _ in range(10):
        print(f"Distancia: {ultrasonido.medir()}")
        sleep(1)
    return True

def step_qti():
    
    pass
    
steps = {"0":step_end, "1":step_leds, "2":step_servomotores, "3": step_switch, "4": step_buzzer, "5": step_utltrasonido}

if __name__ == "__main__":
    
    bucle = True
    while bucle:
        
        step = input(text)
        
        if step in steps.keys():
            bucle = steps[step]()