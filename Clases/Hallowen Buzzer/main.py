from machine import Pin, PWM
from time import sleep

from tone import Buzzer
from sensores import Ultrasonico

led = Pin(2,Pin.OUT)
led2 = Pin(3,Pin.OUT)
led3 = Pin(4, Pin.OUT)
buzzer = Buzzer(5)
ultrasonido = Ultrasonico()

def musicalNote(frecuencia:int, tiempo:int)-> None:
    buzzer.on(frecuencia)
    sleep(tiempo)
    buzzer.off()
    
def phase_0()-> bool:
    return False 

def phase_1()-> bool:
    led.value(1)
    sleep(2)
    led.value(0)
    return True 
    
def phase_2()-> bool:
    musicalNote(440, 1)
    musicalNote(131, 1)
    return True 
    
def phase_3()-> bool:
    for _ in range(10):
        print(ultrasonido.medir())
        sleep(0.2)
    return True

def phase_4()-> bool:
    for _ in range(100):
        distance = ultrasonido.medir()
        print(f"The distance is {distance}")
        if distance <= 10:
            led.value(1)
        else:
            led.value(0)
        sleep(0.5)
    return True

def phase_5()-> bool:
    
    notas = {"do":261, "do#": 277, "re": 293, "re#": 311, "mi":329, "fa": 349, "fa#": 369, "sol": 392, "sol#": 415, "la": 440, "la#": 466, "si": 493, "si#": 523}
    cancion = [
    "sol", "sol", "sol", "sol#", "fa", "fa", "fa",
    "fa", "fa", "fa", "fa", "sol", "sol", "sol",
    "sol", "sol", "sol", "sol#", "la#", "sol#",
    "sol", "fa", "fa", "re", "fa", "sol", "sol#",
    "sol", "re#", "re", "sol",
    "la#", "la#", "la#", "la", "sol", "la#",
    "la#", "la#", "sol",
    "la#", "fa", "fa", "re#", "do#", "do", "sol",
    "sol#",
    "si", "si", "si", "si", "si", "la#", "sol#", "si",
    "sol", "sol", "fa#", "mi", "do#",
    "sol#", "sol#", "sol#", "re", "fa#",
    "sol", "re", "fa#", "sol", "fa#",
    "re#", "re#", "re#", "re", "do", "re#",
    "re#", "re#", "re", "do",
    "si", "la#", "sol#", "si", "la#", "sol#",
    "sol#", "sol", "fa", "sol#", "sol", "fa"]
    
    for nota in cancion:
        musicalNote(notas[nota], 0.2)
    led.value(0)
    led2.value(0)
    led3.value(0)
    return True

def phase_6()-> bool:
    
    for _ in range(30):
        if ultrasonido.medir() < 10:
            led.value(1)
            led2.value(1)
            led3.value(1)
            return phase_5()
        sleep(0.5)
    return True 
    
functions = {"0":phase_0, "1":phase_1, "2":phase_2, "3":phase_3, "4":phase_4, "5":phase_5, "6": phase_6}
        
if __name__ == "__main__":
    
    bucle = True 
    while bucle:
        action = input("Plese, indicate the action that I need do [0-6]:")
        bucle = functions[action]()
