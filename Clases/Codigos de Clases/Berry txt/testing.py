
from random import randint

path = "output.txt"

def medicion_utrasonido(path):
    
    with open(path, 'w') as file:
        
        mediciones = [(i, randint(5, 45)) for i in range(1, 10)]
        for tiempo, medicion in mediciones:
            file.write("[Medicion] ")
            file.write(f"Tiempo: {tiempo}  Medicion: {medicion}\n\n")
            
            file.write("[Condicion] ")
            if medicion > 0 and medicion < 30:
                file.write(f"Obstaculo encontrado a una distancia de {medicion}\n\n")
            else:
                file.write(f"Obstaculos a una distancia demasiado lejana\n\n")

def medicion_digital_qti(path):
    
    medicion = ""
    
    with open(path, 'w') as file:
        
        mediciones = [(randint(0,1) for _ in range(4)) for _ in range(10)]
        for muestra in mediciones:
            for i in muestra:
                medicion += str(i)
            file.write("[Medicion] ")
            file.write(f"Medicion: {medicion}\n\n")
            medicion = ""
            

medicion_digital_qti(path)
    