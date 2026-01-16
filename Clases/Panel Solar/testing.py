from motor import servo360
from time import sleep
from sensores import Ldr


ejeH = servo360(15)
ejeV = servo360(14)
sensor = Ldr(28)

def step_0():
    return False 

def step_1():
    
    angulo_H = int(input("Indique el angulo Horizontal (0-180): "))
    time_H = float(input("Indique el tiempo de giro Horizontal (0.1-0.05): "))
    
    ejeH.girar(angulo_H)
    sleep(time_H)
    ejeH.detener()
    
    angulo_V = int(input("Indique el angulo Vertical (0-180): "))
    time_V = float(input("Indique el tiempo de giro Vertical (0.1-0.05): "))
    
    ejeV.girar(angulo_V)
    sleep(time_V)
    ejeV.detener()
    
    return True

def step_2():
    
    print(sensor.medir())
    return True 

steps = {'0':step_0, '1':step_1, '2':step_2}

if __name__ == '__main__':
    
    bucle = True
    while bucle:
        
        step = input("Indique el step: ")
        
        if step in steps.keys():
            bucle = steps[step]()