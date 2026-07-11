# Proyecto Coche

## 👋🏻 Presentación

Hola alumno del taller, esta es la guía para aprender con el proyecto **Auto** desarrollado por el taller NeoEduca.

Con el, aprenderas sobre la conexión y la programación de motores junto con el desarrollo de un auto autonomo a traves del IDE Thonny con el lenguaje de programación Python.

## 💡 Conociendo los componentes

### Que es un servomotor

Un servomotor es un motor especializado que permite un control preciso de posición, velocidad y torque en aplicaciones robóticas e industriales. Funciona en un sistema de lazo cerrado con retroalimentación (encoder o potenciómetro) para ajustar su posición exacta, siendo clave en automatización, brazos robóticos y CNC.

### Conexiones del servomotor

Para nuestra conexión en el microcontrolador, es importante conocer los siguientes aspectos:

- **🟠 Signal (PIN)**

- **🟤 GND (Tierra)**

- **🔴 VCC (Voltaje)**

Junto a lo anterior, es importante recordar que dentro de la placa los motores se conectan en los pines GP13, GP14 y GP15. Ademas, es **muy importante que conectes el portapilas como fuente de alimentación externa** para evitar el daño de los componentes.

### Librería `motores.py`

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

### Probando los servomotores

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

## 🖥️ Ejercicios del proyecto

### Ejercicio 1: Movimiento en L

Construye un programa que te permita hacer un movimiento en forma de L con el auto. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda para guiarte:

```python
from motores import carro
from time import sleep

auto = carro(14,15)

angulo_a = # Coloque el angulo aquí 👋🏻
angulo_b = # Coloque el angulo aquí 👋🏻
auto.setvelocidad()

# Coloque el movimiento para avanzar 👋🏻
sleep(1)
# Coloque el movimiento para girar👋🏻
sleep(1)
# Coloque el movimiento para avanzar 👋🏻
sleep(1)
auto.movedetener()
```

### Ejercicio 2: Giro sobre su propio eje
Construye un programa que te permita al auto girar sobre su propio eje. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda para guiarte:

```python
from motores import carro
from time import sleep

auto = carro(14,15)

angulo_a = # Coloque el angulo aquí 👋🏻
angulo_b = # Coloque el angulo aquí 👋🏻
auto.setvelocidad()

tiempo_giro = # Coloca el tiempo aquí 👋🏻

# Coloque el movimiento para girar👋🏻
sleep(tiempo_giro)
auto.movedetener()
```

### Ejercicio 3: Completando un cuadrado

Construye un programa que te permita recorrer un cuadrado completo con el auto usando el ciclo for. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda para guiarte:

```python
from motores import carro
from time import sleep

auto = carro(14,15)

angulo_a = # Coloque el angulo aquí 👋🏻
angulo_b = # Coloque el angulo aquí 👋🏻
auto.setvelocidad(angulo_a, angulo_b)

n_interaciones = # Coloca el numero de iteraciones
for _ in range(n_interaciones):
    # Código para hacer una L
auto.movedetener()
```

### Ejercicio 4: Rodeando un obstaculo

Construye un programa que te permita rodera un obstaculo en el suelo sin tocarlo. Si tienes dudas de por donde comenzar, te dejo el siguiente código que te ayuda para guiarte:

```python
from motores import carro
from time import sleep

auto = carro(14,15)

angulo_a = # Coloque el angulo aquí 👋🏻
angulo_b = # Coloque el angulo aquí 👋🏻
auto.setvelocidad()

# Código para rodear obstaculo

auto.movedetener()
```

### Ejercicio 5: Completando una pista

Construye un programa que te permita recorrer una pista completa con el auto. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda para guiarte:

```python
from motores import carro
from time import sleep

auto = carro(14,15)

angulo_a = # Coloque el angulo aquí 👋🏻
angulo_b = # Coloque el angulo aquí 👋🏻
auto.setvelocidad()

# Código para hacer pista

auto.movedetener()
```