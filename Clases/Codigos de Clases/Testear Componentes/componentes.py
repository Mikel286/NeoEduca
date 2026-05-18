
from motores import servo360
from sensores import Ldr, Qti, Ultrasonico
from tone import Buzzer
from machine import Pin
from time import sleep

class Componentes:

    def __init__(self, **kwargs):
        
        self.led_1 = Pin(kwargs["led1"], Pin.OUT) if kwargs.get("led1") is not None else None
        self.led_2 = Pin(kwargs["led2"], Pin.OUT) if kwargs.get("led2") is not None else None
        self.led_3 = Pin(kwargs["led3"], Pin.OUT) if kwargs.get("led3") is not None else None

        self.buzzer = Buzzer(kwargs["buzzer"]) if kwargs.get("buzzer") is not None else None

        self.motor_13 = servo360(kwargs["motor13"]) if kwargs.get("motor13") is not None else None
        self.motor_14 = servo360(kwargs["motor14"]) if kwargs.get("motor14") is not None else None
        self.motor_15 = servo360(kwargs["motor15"]) if kwargs.get("motor15") is not None else None

        self.ultrasonido = Ultrasonico() 
        self.ldr = Ldr(kwargs["ldr"]) if kwargs.get("led1") is not None else None

        self.qti_1 = Qti(kwargs["qti1"]) if kwargs.get("qti1") is not None else None
        self.qti_2 = Qti(kwargs["qti2"]) if kwargs.get("qti2") is not None else None
        self.qti_3 = Qti(kwargs["qti3"]) if kwargs.get("qti3") is not None else None
        self.qti_4 = Qti(kwargs["qti4"]) if kwargs.get("qti4") is not None else None

    def testing_leds(self):
        
        componentes = [self.led_1, self.led_2, self.led_3]
        for componente in componentes:
            if componente is not None:
                componente.on()
                sleep(1)
                componente.off()
    
    def testing_buzzer(self):

        if self.buzzer is not None:
            self.buzzer.on()
            sleep(1)
            self.buzzer.off()

    def testing_motores(self):

        componentes = [self.motor_13, self.motor_14, self.motor_15]
        for componente in componentes:
            if componente is not None:
                componente.barrer()

    def detener_motores(self):

        componentes = [self.motor_13, self.motor_14, self.motor_15]
        for componente in componentes:
            if componente is not None:
                componente.detener()


    def testing_sensores(self):

        componentes = [self.ultrasonido, self.ldr, self.qti_1, self.qti_2, self.qti_3, self.qti_4]
        for componente in componentes:
            if componente is not None:
                print(f"La medición de este sensor es: {componente.medir()}")

if __name__ == "__main__":

    pines = {
        "led1":2,
        "led2":3,
        "led3":4,
        "buzzer":5,
        "motor13":13,
        "motor14":14,
        "motor15":15,
        "ldr":7,
        "qti1":6,
        "qti2":8,
        "qti3":10,
        "qti4":12
    }

    robot = Componentes(**pines)

    robot.testing_leds()
    robot.testing_buzzer()
    robot.testing_motores()
    robot.testing_sensores()
    robot.detener_motores()