from machine import PWM, Pin
from time import sleep
from sensores import Ultrasonico

class RGB:
    
    def __init__(self, pin_red, pin_green, pin_blue):
        
        self.pin_red = PWM(Pin(pin_red, Pin.OUT))
        self.pin_green = PWM(Pin(pin_green, Pin.OUT))
        self.pin_blue = PWM(Pin(pin_blue, Pin.OUT))
        
        self.pin_red.freq(1000)
        self.pin_green.freq(1000)
        self.pin_blue.freq(1000)
        
    def set_color(self, r_value, g_value, b_value): # Maximo valor: 65535
        self.pin_red.duty_u16(int(r_value))
        self.pin_green.duty_u16(int(g_value))
        self.pin_blue.duty_u16(int(b_value))
        
    def def_ultra(self):
        self.ultrasonido = Ultrasonico()
    
    def ultra_rgb(self):
        
        R0 = 30000
        G0 = 30000
        B0 = 0
        
        distancia_max = 30
        distancia_min = 0
        rango_max = 65535
        rango_min = 0
        delta_max = rango_max - R0
        
        # Calculo de la medicion
        distancia = self.ultrasonido.medir()
        if distancia < distancia_min:
            distancia = distancia_min
        elif distancia > distancia_max:
            distancia = distancia_max
            
        # Calculo de factor de proximidad
        distancia_clamped = max(0.0, min(distancia_max, distancia))
        proximidad = (distancia_max - distancia_clamped) / distancia_max
        
        # Calculo de delta
        delta = proximidad * delta_max  
        
        R = R0 + delta
        G = G0 - delta
        B = B0
        
        if R > rango_max: R = rango_max
        if G < rango_min: G = rango_min
        
        self.set_color(R,G,B)    
        
if __name__ == "__main__":

    pass