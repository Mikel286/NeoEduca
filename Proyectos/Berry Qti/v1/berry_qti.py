
from sensores import Qti

class BerryQti:

    def __init__(self, pin_izq, pin_der) -> None:
        self.qti_izq = Qti(pin = pin_izq)
        self.qti_der = Qti(pin = pin_der)
    
    def ajustar_umbral(self, qti, valor) -> None:
        
        colection = {"qti_izq": self.qti_izq.umbral, "qti_der": self.qti_der.umbral}

        try:
            colection[qti] = valor
        except KeyError as error:
            print(f"Key error: {error}")

    def medicion_digital(self) -> int:

        medicion = ""
        
        for sensor in (self.qti_izq, self.qti_der):
            
            if sensor.medir() > sensor.umbral:
                medicion += "1"
            else:
                medicion += "0"

        print(medicion)
        return medicion
