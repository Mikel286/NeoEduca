from json import dump
from sensores import Ultrasonico
from time import sleep


def json_ultrasonico() -> None:

    sensor = Ultrasonico()
    mediciones = []
    for i in range(20):
        print("Medicion realizada...")
        mediciones.append({"medicion":sensor.medir(), "tiempo":i})
        sleep(1)
    with open("medicion.json", "w") as file:
        dump(file, mediciones)