
def json_ultrasonico() -> None:
    
    from json import dump
    from sensores import Ultrasonico
    from time import sleep

    sensor = Ultrasonico()
    mediciones = []
    for i in range(20):
        print("Medicion realizada...")
        mediciones.append({"medicion":sensor.medir(), "tiempo":i})
        sleep(1)
    with open("medicion.json", "w") as file:
        dump(file, mediciones)
        
def json_clock_ultrasonico() -> None:
    
    from json import dump
    from sensores import Ultrasonico
    
if __name__ == "__main__":
    pass