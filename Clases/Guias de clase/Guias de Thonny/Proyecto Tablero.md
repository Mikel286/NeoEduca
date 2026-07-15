## 💻 Proyecto Tablebro (Nivel Básico)

## 👋🏻 Presentación

Hola alumno del taller, esta es la guía para aprender con el proyecto **Keyboard** desarrollado por el profesor Mikel Ania.

Con el, aprenderas distintas habilidades de programación a traves del IDE Thonny con el lenguaje de programación Python.

## 🔌 Conociendo los componente

### Componente Led

#### ¿Qué es un led?

Un LED (diodo emisor de luz) es un componente electrónico semiconductor de dos terminales (ánodo y cátodo) que emite luz cuando una corriente eléctrica moderada lo atraviesa. Basado en la electroluminiscencia, convierte la energía eléctrica en luz de manera muy eficiente, consumiendo hasta un 90% menos energía que las bombillas incandescentes.

#### ¿Cómo es su conexión?

Cuando trabajamos con este componente (3 en esta tutoría), es comun conectarlo de esta manera:

- LED izquierdo (PIN 2)
- LED centro (PIN 3)
- LED derecho (PIN 4)

#### Probando componente

Para probar el funcionamiento de este componente, se puede usar el siguiente código que encendera durante un segundo los led, para despues terminar el programa apagandolos.

```python
from machine import Pin
from time import sleep

led_izq = Pin(2, Pin.OUT)
led_cen = Pin(3, Pin.OUT)
led_der = Pin(4, Pin.OUT)

led_izq.value(1)
led_cen.value(1)
led_der.value(1)
sleep(1)
led_izq.value(0)
led_cen.value(0)
led_der.value(0)
```

### Componente Buzzer

#### ¿Qué es un buzzer?

Un buzzer, o zumbador, es un transductor electroacústico que convierte energía eléctrica en sonido, emitiendo un tono agudo continuo o intermitente al recibir corriente. Funciona como alarma o señal de confirmación en dispositivos como electrodomésticos, automóviles y proyectos de electrónica. Dentro de los buzzer, existen dos grandes tipos:

- **Activo**: Incorpora un oscilador interno, por lo que emite sonido automáticamente al aplicarle voltaje directo (DC).

- **Pasivo**:  No tiene oscilador interno; requiere una señal eléctrica de onda cuadrada (frecuencia) para generar diferentes tonos.

En los buzzers o zumbadores, la frecuencia es la magnitud que determina el tono del sonido que emiten.

#### ¿Cómo es su conexión?

Cuando trabajamos con este componente, es comun conectarlo de la siguiente manera:

- Buzzer (PIN 5)

#### Librería `tone.py`

Para usar el componente buzzer es necesario que guardes en tu placa rasph berry pi pico el archivo `tone.py` que contiene el siguiente código:

```python

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
```

#### Probando componente
Para probar el funcionamiento de este componente, se puede usar el siguiente código que emite durante un segundo un sonido a una frecuencia de *440Hz*:

```python
from tone import Buzzer
from time import sleep

buzzer = Buzzer(5)

frecuencia = 440

buzzer.on(frecuencia)
sleep(1)
buzzer.off()
```

### Componente Servomotor

Un servomotor es un motor especializado que permite un control preciso de posición, velocidad y torque en aplicaciones robóticas e industriales. Funciona en un sistema de lazo cerrado con retroalimentación (encoder o potenciómetro) para ajustar su posición exacta, siendo clave en automatización, brazos robóticos y CNC.

#### Conexiones del servomotor

Para nuestra conexión en el microcontrolador, es importante conocer los siguientes aspectos:

- **🟠 Signal (PIN)**

- **🟤 GND (Tierra)**

- **🔴 VCC (Voltaje)**

Junto a lo anterior, es importante recordar que dentro de la placa los motores se conectan en los pines GP13, GP14 y GP15. Ademas, es **muy importante que conectes el portapilas como fuente de alimentación externa** para evitar el daño de los componentes.

#### Librería `motores.py`

Para poder programar los servomotores, necesitaras guardar dentro de la placa la librería `motores.py`. Esta librería contiene el siguiente código:

```python
import utime as time
from time import sleep
from machine import Pin, PWM

class servo360:
    def __init__(self, servo_pin:int):
        self.servo = PWM(Pin(servo_pin))
        self.servo.freq(50)
        self.grados_anterior= 90
        
    def girar(self, grados):
        duty = int((12.346*grados**2 + 7777.8*grados + 700000))
        self.servo.duty_ns(duty)

    def detener(self):
        self.servo.duty_ns(0)
    
    def barrer(self):
        for i in range(0, 180, 5):
            print(i)
            self.girar(i)
            sleep(0.2)
        self.detener()

class SG90:
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.OUT)
        self._angulo = -1  
        self.pwm = PWM(self.pin)
        self.pwm.freq(50)
        
    def angulo(self, angulo=None):
        if angulo is None:
            return self._angulo 
        self._angulo = angulo
        ton = (int(angulo)+45)*100_000/9
        self.pwm.duty_ns(int(ton))
        sleep(0.5)
        self.pwm.deinit()

class carro:
    def __init__(self, motor_pin1, motor_pin2):
        
        _servo_pin1 = Pin(motor_pin1 )
        _servo_pin2 = Pin(motor_pin2 )
        self._servo_1 = PWM(_servo_pin1)
        self._servo_2 = PWM(_servo_pin2)
        self._servo_1.freq(50)
        self._servo_2.freq(50)
        self._grados_1=90
        self._grados_2=90
        self._grados_fast1=90
        self._estado=0
        self._grados_fast2=90
        
    def calibrar(self,grados_1, grados_2):
        self._girar(grados_1, grados_2)
        time.sleep_ms(5000)
        print("frenando....")
        self.movedetener()
        print("Si no frena, llame a su profesor")
        time.sleep_ms(1000)  
        
        
    def setvelocidad(self, grados_1, grados_2):
        self._grados_1=grados_1
        self._grados_2=grados_2
    
    def setvelocidad2(self, grados_1, grados_2):
        self._grados_fast1=grados_1
        self._grados_fast2=grados_2
        
        
    def moveadelante(self):
        if self._estado!=1:
            self._girar(self._grados_1,self._grados_2)
            self._estado=1

    def moveadelante2(self):
        if self._estado!=5:
            self._girar(self._grados_fast1,self._grados_fast2)
            self._estado=5
            
    def movedetener(self):
        if self._estado!=4:
            self._servo_1.duty_ns(0)
            self._servo_2.duty_ns(0) 
            self._estado=4

    def moveatras(self):
        if self._estado!=6:
            self._girar(self._grados_2,self._grados_1)
            self._estado=6
            
    def moveizquierda(self):
        if self._estado!=2:
            self._girar(self._grados_2,self._grados_2)
            self._estado=2

    def movederecha(self):
        if self._estado!=3:
            self._girar(self._grados_1,self._grados_1)
            self._estado=3

    def _girar(self, grado1, grado2):
            duty1 = int((12.346*grado1**2 + 7777.8*grado1 + 700000))
            duty2 = int((12.346*grado2**2 + 7777.8*grado2 + 700000))
            self._servo_1.duty_ns(duty1)
            self._servo_2.duty_ns(duty2) 
```

#### Probando los servomotores

Para el correcto funcionamiento de los servomotores, debemos seguir el siguiente conjunto de pasos con tal de ver que ambos motores funcionan adecuadamente:

#### Funcionamiento de motores

Para ver que los motores funcionan correctamente usamos la clase `servo360` que nos permite probar el funcionamiento de cada motor por separado:

```python
from motores import servo360

motor_izq = servo360(14)
motor_der = servo360(15)

motor_izq.barrer()
motor_der.barrer()
```

**Nota**: Si has cargado el programa, te habras fijado que en pantalla aparece en serie de angulos en incremento de 5 que muestran como cada uno de los motores funciona para el rango de angulos [0-180] grados. Lo anterior se puede ver en el siguiente código:

``` python
def barrer(self):
    for i in range(0, 180, 5):
        print(i)
        self.girar(i)
        sleep(0.2)
    self.detener()
```

#### Calibración de los motores

Una vez se ha comprobado el movimiento de los motores, es importante pasar a calibrar los motores. Para esto, usamos la clase `carro` donde por medio del siguiente código logramos la calibración:

```python
from motores import carro

auto = carro(14, 15)
angulo_a = int(input("Ingrese el primer angulo: "))
angulo_b = int(input("Ingrese el segundo angulo: "))
auto.calibrar(angulo_a, angulo_b)
```

Con el código anterior, podemos ir ingresando distintos angulos y comprobar con que par de angulos es capaz nuestro auto de moverse adelante.

#### Definiendo velocidad y movimientos del auto

Una vez definidos los angulos que nos servirán para el auto, hay que definir la velocidad a la que se moverá y probar los movimiento basicos del auto:

- `auto.setvelocidad(angulo_a, angulo_b)`: Definir angulos de giro.

- `auto.moveadelante()`: Comando para moverse hacia adelante.

- `auto.moveizquierda()`: Comando para girar hacia la izquierda.

- `auto.movederacha()`: Comando para girar hacia la derecha.

- `auto.movedetener()`: Comando para detenerse.

Para entender mejor esto, vea el siguiente código:

```python
from motores import carro
from time import sleep

auto = carro(14,15)

angulo_a = # Coloque angulo 👋🏻
angulo_b = # Coloque angulo 👋🏻
auto.setvelocidad(angulo_a, angulo_b)

auto.moveadelante()
sleep(1)
auto.moveizquierda()
sleep(1)
auto.movederecha()
sleep(1)
auto.movedetener()
```

## Ejercicios del proyecto

Para aplicar lo aprendido, deberás completar cada uno de los ejercicios que se te presentan a continuación.

### Ejercicio 1: Siguiendo la ruta
Construye un programa que te permita completar cada una de las siguientes rutas que se te muestran a continuación:

![Tableros de ejercicio 1](assets/Proyecto%20Tablero%201.png)

### Ejercicio 2: Alumbrando la ruta
Construye un programa que te permita completar cada una de las siguientes rutas usando leds en los puntos de cada ruta donde estos sean requeridos:

![Tableros de ejercicio 2](assets/Proyecto%20Tablero%202.png)

### Ejercicio 3: Camino de música y luces
Construye un programa que te permita completar cada una de las siguientes rutas usando leds y buzzer en los puntos de cada ruta donde estos sean requeridos:

![Tableros de ejercicio 3](assets/Proyecto%20Tablero%203.png)