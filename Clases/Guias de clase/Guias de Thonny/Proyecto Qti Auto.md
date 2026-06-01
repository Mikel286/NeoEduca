# Proyecto Qti auto

## 👋🏻 Presentación

Hola alumno del taller, esta es la guía para aprender con el proyecto **Qti Auto** desarrollado por el taller NeoEduca.

Con el, aprenderas sobre la conexión y la programación de sensores qti junto con el desarrollo de un auto autonomo capaz de seguir lineas a traves del IDE Thonny con el lenguaje de programación Python.

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

### Que son los QTI

Un sensor QTI (Charge Transfer Infrared o Infrarrojo por Transferencia de Carga) es un dispositivo óptico que combina un emisor y un receptor de luz infrarroja. Se utiliza principalmente en robótica para detectar la diferencia de color y reflectividad entre superficies claras y oscuras.

Su funcionamiento puede separarse en los siguientes tres grandes procesos:

1. **Emisión y Reflexión**: El emisor proyecta luz infrarroja hacia el suelo. Dependiendo del color de la superficie, esta luz se absorbe o se refleja.

2. **Detección**: Si el sensor está sobre una superficie blanca o clara, la luz rebota intensamente; si está sobre una superficie oscura o negra, la luz es absorbida.

3. **Medición**: El receptor (un fototransistor) capta la luz reflejada y utiliza un condensador para medir la tasa de transferencia de carga. A mayor luz reflejada, más rápido se carga el sensor.

### Probando los QTI

Para probar el correcto funcionamiento de los QTI, utilice el siguiente código:

```python

from machine import Pin
from time import sleep

xtr_izq = Pin(7, Pin.IN, Pin.PULL_UP)
izq = Pin(8, Pin.IN, Pin.PULL_UP)
cen = Pin(9, Pin.IN, Pin.PULL_UP)
der = Pin(10, Pin.IN, Pin.PULL_UP)
xtr_der = Pin(11, Pin.IN, Pin.PULL_UP)

time_step = 0.5
bucle = True 
while bucle:
    
    medicion = f"{xtr_izq.value()}{izq.value()}{cen.value()}{der.value()}{xtr_der.value()}"
    print(medicion)
    sleep(time_step)
```

Con este código podremos ver la respuesta digital (0-1) de un sensor compuesto por 5 QTI.

## 🖥️ Ejercicios del proyecto

### Ejercicio 1: Definiiendo casos para dos Qti
En una hoja, redacta cada uno de los posibles casos que se pueden dar al usar 2 sensores qti. Como pista para guiarte, te dejo la cantidad de casos posibles que se pueden dar:

- Caos 1: 
- Caso 2:
- Caos 3: 
- Caso 4:

### Ejercicio 2: Aplicando casos para dos QTI
Construye un programa que te permita reconocer los casos planteados en el ejercicio 1. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda para guiarte:

```python
from machine import Pin
from time import sleep

xtr_izq = Pin(7, Pin.IN, Pin.PULL_UP)
xtr_der = Pin(11, Pin.IN, Pin.PULL_UP)

time_step = 0.5
bucle = True 
while bucle:
    
    medicion = f"{xtr_izq.value()}{izq.value()}{cen.value()}{der.value()}{xtr_der.value()}"
    print(medicion)

    if #caso 1:
        #codigo de acción aquí
    elif #caso 2:
        #codigo de acción aquí
    elif #caso 3:
        #codigo de acción aquí
    elif #caso 4:
        #codigo de acción aquí

    sleep(time_step)
```

### Ejercicio 3: Recorriendo la pista con dos sensores

Construye un programa que te permita recorrer la pista usando motores y sensores qti. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda para guiarte:

```python
from motores import carro
from machine import Pin
from time import sleep

xtr_izq = Pin(7, Pin.IN, Pin.PULL_UP)
xtr_der = Pin(11, Pin.IN, Pin.PULL_UP)

auto = carro(14,15)

angulo_a = # Coloque el angulo aquí 👋🏻
angulo_b = # Coloque el angulo aquí 👋🏻
auto.setvelocidad()

time_step = 0.5

bucle = True
while bucle:
    medicion = f"{xtr_izq.value()}{izq.value()}{cen.value()}{der.value()}{xtr_der.value()}"

    if #caso 1:
        #codigo de motores aquí
    elif #caso 2:
        #codigo de motores aquí
    elif #caso 3:
        #codigo de motores aquí
    elif #caso 4:
        #codigo de motores aquí

```

### Ejercicio 4: Definiiendo casos para cuatro Qti
En una hoja, redacta cada uno de los posibles casos que se pueden dar al usar 2 sensores qti. Como pista para guiarte, te dejo la cantidad de casos posibles que se pueden dar:

- Caos 1: 
- Caso 2:
- Caos 3: 
- Caso 4:
- Caos 5: 
- Caso 6:
- Caos 7: 
- Caso 8:
- Caos 9: 
- Caso 10:
- Caos 11: 
- Caso 12:
- Caos 13: 
- Caso 14:
- Caos 15: 
- Caso 16:

### Ejercicio 5: Aplicando casos para cuatro QTI
Construye un programa que te permita reconocer los casos planteados en el ejercicio 4. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda para guiarte:

```python
from machine import Pin
from time import sleep

xtr_izq = Pin(7, Pin.IN, Pin.PULL_UP)
xtr_der = Pin(11, Pin.IN, Pin.PULL_UP)

time_step = 0.5
bucle = True 
while bucle:
    
    medicion = f"{xtr_izq.value()}{izq.value()}{cen.value()}{der.value()}{xtr_der.value()}"
    print(medicion)

    if #caso 1:
        #codigo de acción aquí
    elif #caso 2:
        #codigo de acción aquí
    elif #caso 3:
        #codigo de acción aquí
    elif #caso 4:
        #codigo de acción aquí
    elif #caso 5:
        #codigo de acción aquí
    elif #caso 6:
        #codigo de acción aquí
    elif #caso 7:
        #codigo de acción aquí
    elif #caso 8:
        #codigo de acción aquí
    elif #caso 9:
        #codigo de acción aquí
    elif #caso 10:
        #codigo de acción aquí
    elif #caso 11:
        #codigo de acción aquí
    elif #caso 12:
        #codigo de acción aquí
    elif #caso 13:
        #codigo de acción aquí
    elif #caso 14:
        #codigo de acción aquí
    elif #caso 15:
        #codigo de acción aquí
    elif #caso 16:
        #codigo de acción aquí

    sleep(time_step)
```

### Ejercicio 6: Recorriendo la pista con cuatro sensores

Construye un programa que te permita recorrer la pista usando motores y sensores qti. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda para guiarte:

```python
from motores import carro
from machine import Pin
from time import sleep

xtr_izq = Pin(7, Pin.IN, Pin.PULL_UP)
xtr_der = Pin(11, Pin.IN, Pin.PULL_UP)

auto = carro(14,15)

angulo_a = # Coloque el angulo aquí 👋🏻
angulo_b = # Coloque el angulo aquí 👋🏻
auto.setvelocidad()

time_step = 0.5

bucle = True
while bucle:
    medicion = f"{xtr_izq.value()}{izq.value()}{cen.value()}{der.value()}{xtr_der.value()}"

    if #caso 1:
        #codigo de motores aquí
    elif #caso 2:
        #codigo de motores aquí
    elif #caso 3:
        #codigo de motores aquí
    elif #caso 4:
        #codigo de motores aquí
    elif #caso 5:
        #codigo de motores aquí
    elif #caso 6:
        #codigo de motores aquí
    elif #caso 7:
        #codigo de motores aquí
    elif #caso 8:
        #codigo de motores aquí
    elif #caso 9:
        #codigo de motores aquí
    elif #caso 10:
        #codigo de motores aquí
    elif #caso 11:
        #codigo de motores aquí
    elif #caso 12:
        #codigo de motores aquí
    elif #caso 13:
        #codigo de motores aquí
    elif #caso 14:
        #codigo de motores aquí
    elif #caso 15:
        #codigo de motores aquí
    elif #caso 16:
        #codigo de motores aquí

```