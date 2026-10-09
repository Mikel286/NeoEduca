
from machine import Pin, ADC
import time

class Joystick:
    
    def __init__(self, pin_x = 26, pin_y = 27, pin_button = 6):
        
        self.pin_x = ADC(pin_x)
        self.pin_y = ADC(pin_y) 
        self.pin_button = Pin(pin_button, Pin.IN, Pin.PULL_UP)
        
    def leer_promedio(self, adc, n=10):
        """Promedia n lecturas para reducir el ruido del ADC."""
        return sum(adc.read_u16() for _ in range(n)) // n
    
    def normalizar(self, valor, zona_muerta=8):
        """Convierte 0-65535 a -100..+100 e ignora variaciones pequeñas."""
        resultado = round(((valor - 32768) / 32768) * 100)
        return 0 if abs(resultado) < zona_muerta else resultado

    def medir(self):
        eje_x = self.normalizar(self.leer_promedio(self.pin_x))
        eje_y = self.normalizar(self.leer_promedio(self.pin_y)) * -1  # invertido: arriba = positivo
        pulsado = not self.pin_button.value()
        return (eje_x, eje_y, pulsado)
    
class Keyboard():
    
    def __init__(self):
        
        self.rows = [Pin(i, Pin.OUT) for i in [9,8,7,6]]
        self.cols = [Pin(i, Pin.IN, Pin.PULL_UP) for i in [13,12,11,10]]

        self.keys = [
            ["1","2","3","A"],
            ["4","5","6","B"],
            ["7","8","9","C"],
            ["*","0","#","D"]]

    def scan(self):
        for i, row in enumerate(self.rows):
            row.low()
            for j, col in enumerate(self.cols):
                if col.value() == 0:
                    return self.keys[i][j]
            row.high()
        return None
        
class RGB:
    
    def __init__(self, pin_red, pin_green, pin_blue):
        
        self.pin_red = PWM(Pin(pin_red, Pin.OUT))
        self.pin_green = PWM(Pin(pin_green, Pin.OUT))
        self.pin_blue = PWM(Pin(pin_blue, Pin.OUT))
        
        self.pin_red.freq(1000)
        self.pin_green.freq(1000)
        self.pin_blue.freq(1000)
        
    def set_color(self, r_value, g_value, b_value): # Maximo valor: 65535
        self.pin_red.duty_u16(r_value)
        self.pin_green.duty_u16(g_value)
        self.pin_blue.duty_u16(b_value)
