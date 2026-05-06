# Proyecto QTI alto rendimiento

## 👋🏻 Presentación

Hola almuno del taller, esta guía esta diseñada para mejorar tus capacidades como competidor de la categoría sumo en alto rendimiento.

Con esta guía, fortaleceras tu código y el diseño de tu robot para el desafio de sumo de la liga de robotica.

## 💻 Reforzando Utrasonico

En el desafio de sumo, la programación de los sensores ultrasonido es clave. Por eso, en esta sección reforzaremos el conocimiento sobre ultrasonico.

### Que es el Ultrasonico

El sensor HC-SR04 es un módulo ultrasónico de medición de distancia, popular y económico, que funciona enviando pulsos de sonido $40\text{kHz}$ y midiendo el tiempo de rebote (ecolocalización). Ofrece un rango de detección de $2\text{cm}$ a $450\text{cm}$ con una precisión de $0.3\text{cm}$.

Respecto a la coexión, esta por standar sera:

- GND

- VCC

- Trigg (PIN 18)

- Echo (PIN 19)

### Libreria `sensores.py`

Para usar el sensor ultrasonico, debemos usar la libreria `sensores.py` donde existe la clase `Ultrasonico` que nos ayudar a programar el sensor. El archvio `sensores.py` tiene el siguiente código en su interior:

```python
from machine import Pin, time_pulse_us
from time import sleep_ms, sleep_us, ticks_diff, ticks_us
class Ldr:
    def __init__(self, pin):
        self.pin = pin
        
    
    def RCtime(self):    
        sensor = Pin(self.pin, Pin.OUT)
        sensor.on() 
        sleep_ms(1)
        
        sensor = Pin(self.pin, Pin.IN) 
        sensor.off()
        start_time = ticks_us()
        while sensor.value():
            pass
        end_time = ticks_us()

        return ticks_diff(end_time, start_time)
    

    def medir(self):
        return self.RCtime()

class Qti:
    def __init__(self, pin):
        self.pin = pin
        
    
    def RCtime(self):    
        sensor = Pin(self.pin, Pin.OUT)
        sensor.on() 
        sleep_ms(1)
        
        sensor = Pin(self.pin, Pin.IN) 
        sensor.off()
        start_time = ticks_us()
        while sensor.value():
            pass
        end_time = ticks_us()

        return ticks_diff(end_time, start_time)
    

    def medir(self):
        return self.RCtime()

class Ultrasonico:   
    def __init__(self):
        self.trig_pin = Pin(18, Pin.OUT) 
        self.echo_pin = Pin(19, Pin.IN)
        self.SOUND_SPEED=340
        
    def medir(self):
        self.trig_pin.value(0)
        sleep_us(5)
        self.trig_pin.value(1)
        sleep_us(10)
        self.trig_pin.value(0)
        ultrason_duration = time_pulse_us(self.echo_pin, 1, 30000)
        distance_cm = self.SOUND_SPEED * ultrason_duration / 20000
        return distance_cm
```

### Probando el sensor ultrasonico 

Para probar el correcto funcionamiento de un Ultrasonico, utilice los siguientes códigos:

-  Codigo para medir con el sensor

```python
from sensores import Ultrasonico
from time import sleep

sensor = Ultrasonico()

print(sensor.medir())
```

-  Código para evaluar la distancia

```python
from sensores import Ultrasonico
from time import sleep

sensor = Ultrasonico()

limite = 30
bucle = True

while bucle:

    medicion = sensor.medir()

    if medicion <= limite:
        print("Obstaculo encontrado...")
    else:
        print("No hay nada...")
```

## 💻 Reforzando motores DC

### Que es un motor DC
Un motor de corriente continua (CC o DC) transforma energía eléctrica en mecánica, creando movimiento rotatorio a través de campos magnéticos y fuerza de Lorentz. Consta principalmente de un estator (imanes) y un rotor (bobinas). Se utiliza en robótica, juguetes y maquinaria, destacando por su control preciso de velocidad y par.

### Que es un puente H

Un puente H es un circuito electrónico de cuatro interruptores (transistores/MOSFETs) que permite controlar el sentido de giro (horario/antihorario) y la velocidad de motores de corriente continua (DC) sin cambiar la alimentación. Su forma en "H" habilita la inversión de polaridad en el motor, siendo fundamental en robótica y actuadores.

## Resolviendo Desafio de sumo

### Modificando libreria sensores

Para el desafio de sumo, necesitaremos mas de un sensor ultrasonico. Por tanto, la libreria de sensores en su forma standar no nos va a servir por que forzamos a que todo objeto  de la clase `Ultrasonico` tenga como pines el GP18 y GP19. Lo anterior, se debe a la siguiente parte del código en `sensores.py`:

```python
class Ultrasonico:   
    def __init__(self):
        self.trig_pin = Pin(18, Pin.OUT) 
        self.echo_pin = Pin(19, Pin.IN)
        self.SOUND_SPEED=340
```

Para solucionar esto, tenemos que cambiar esta parte a lo siguiente:

```python
class Ultrasonico:   
    def __init__(self, pin_trig, pin_eco): # Cambio aquí
        self.trig_pin = Pin(pin_trig, Pin.OUT) # Cambio aquí
        self.echo_pin = Pin(pin_eco, Pin.IN) # Cambio aquí
        self.SOUND_SPEED=340
```

### Probando nuevo sensores

Una vez modificada la librería `sensores.py`, procedemos a probar varios ultrasonicos con el siguiente código:

```python
from sensores import Ultrasonico
from time import sleep

sensor1 = Ultrasonico(18,19)
sensor2 = Ultrasonico(16,17)
sensor3 = Ultrasonico(11,12)

while True:

    print(f"sensor1:{sensor1.medir()}    sensor2:{sensor2.medir()}    sensor3:{sensor3.medir()}")
```
