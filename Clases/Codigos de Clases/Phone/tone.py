from machine import Pin, PWM
from time import sleep

class Buzzer:
    def __init__(self, pin: int) -> None:
        self.pin = Pin(pin)
        self.buzzer = PWM(self.pin)
    
    def on(self, frecuencia: int=440) -> None:
        self.buzzer.freq(frecuencia)
        self.buzzer.duty_u16(2**15)
        
    def off(self) -> None:
        self.buzzer.duty_u16(0)
        
    def tone(self, frecuencia: int, duracion: float, silencio: float = 0) -> None:
        """
        Reproduce un tono con la frecuencia especificada durante la duración dada,
        seguido de un silencio opcional.
        
        :param frecuencia: Frecuencia del tono en Hz.
        :param duracion: Duración del tono en segundos.
        :param silencio: Duración del silencio entre tonos (por defecto 0).
        """
        self.on(frecuencia)
        sleep(duracion)
        self.off()
        sleep(silencio)
