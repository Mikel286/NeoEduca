from sensores import Qti

class BerryQtiExtend:
    def __init__(self,Pines = [1,2,3,4]):
        self.PinQtis = Pines
    
    def medicionNormal(self):
        
        for N in range(len(self.PinQtis)):
        
            PinActual = Qti(N)
            RetornoQti = PinActual.medir()
            
            print(f"El qti Nº {N} mide {RetornoQti} con un umbral {PinActual.umbral}")
            
            return [RetornoQti , PinActual]
    
    
    
    def MedicionDigital(self):
        
        medicion = ""
        
        for N in len(self.PinQtis) :
            
            PinActual = Qti(N)
            
            if PinActual.medir() > PinActual.umbral:
                medicion += "1"
            else:
                medicion += "0"

        print(medicion)
        return medicion
        
    
            
            