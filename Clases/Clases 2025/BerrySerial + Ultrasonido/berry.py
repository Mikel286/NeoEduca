
from sensores import Ultrasonico
from time import sleep

sensor = Ultrasonico()

while True:
    
    dist = sensor.medir()
    print(f"La distancia es: {dist}")
    sleep(0.5)