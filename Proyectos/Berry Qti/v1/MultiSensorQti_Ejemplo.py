from Berry_qtiMultiSensor import BerryQtiExtend
from machine import Pin

PinLed_1, PinLed_2, PinLed_3 = 1, 2, 3

Led1, Led2, Led_3 = Pin(PinLed_1, Pin.OUT), Pin(PinLed_2, Pin.OUT), Pin(PinLed_3, Pin.OUT)

PinSensores = [26,27,28]

sensores = BerryQtiExtend(PinSensores)

OutPut = {
    "000" = (1,0,0),
    "100" = (1,0,0),
    "010" = (1,0,0),
    "001" = (1,0,0),
    "110" = (1,0,0),
    "011" = (1,0,0),
    "111" = (1,0,0)
    }


while True:
    Resultado = sensores.MedicionDigital()
    
    
    
    