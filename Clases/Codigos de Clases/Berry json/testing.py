from json import dump
from time import sleep

datos = []

for i in range(10):
    medicion = { "tiempo": i, "distancia": i*2}
    datos.append(medicion)
    sleep(1)
    
with open("data.json", "w") as file:
    dump(datos, file)