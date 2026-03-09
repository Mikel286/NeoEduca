from machine import PWM, Pin
from time import sleep

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
        
    def ultra_rgb(self, distancia, r_value, g_value, b_value):
        self.set_color(r_value + distancia, g_value + distancia, b_value + distancia)
        
        
if __name__ == "__main__":

    pass