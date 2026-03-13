from sensores import Ultrasonico
from motores import servo360, carro
from time import sleep

def step_0():
    return False

def step_1():

    rueda_izq = servo360(14)
    rueda_der = servo360(15)

    rueda_izq.barrer()
    rueda_der.barrer()

    return True

def step_2():

    coche = carro(14, 15)

    try:
        angulo_izq = int(input("Indique el angulo del motor izq (0-180): "))
        angulo_der = int(input("Indique el angulo del motor der (0-180): "))
        coche.calibrar(angulo_izq, angulo_der)
    except TypeError as error:
        print(f"Error: {error}")
    return True

def step_3():

    coche = carro(14, 15)

    try:
        angulo_izq = int(input("Indique el angulo del motor izq (0-180): "))
        angulo_der = int(input("Indique el angulo del motor der (0-180): "))
        coche.setvelocidad(angulo_izq, angulo_der)

        coche.moveadelante()
        sleep(1)
        coche.movederecha()
        sleep(1)
        coche.moveizquierda()
        sleep(1)
        coche.moveatras()
        sleep(1)
        coche.movedetener()

    except TypeError as error:
        print(f"Error: {error}")
    return True

def step_4():

    sensor = Ultrasonico()
    
    for _ in range(10):
        print(f"Distancia: {sensor.medir()}")
        sleep(1)
    return True

steps = {"0":step_0, "1":step_1, "2":step_2, "3":step_3, "4":step_4}

if __name__ == "__main__":

    text = """Indique el step que desea realizar
    [0] Detener el programa
    [1] Probar motores
    [2] Calibrar auto
    [3] Movimientos auto
    [4] Sensor Ultrasonico
    
    Coloque el numero del step: """

    bucle = True
    while bucle:

        step = input(text)

        if step in steps.keys():
            bucle = steps[step]()
        else:
            print("Step no se reconoce...")