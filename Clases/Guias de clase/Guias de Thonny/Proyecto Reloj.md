# Proyecto Panel Solar

## 👋🏻 Presentación

Hola alumno del taller, esta es la guía para aprender con el proyecto **Reloj** desarrollado por el profesor Mikel Ania.

Con el, aprenderas sobre la conexión y la programación tanto de motores como de componentes basicos a traves del IDE Thonny con el lenguaje de programación Python.

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

Para probar el funcionamiento de los servomotores, podemos usar el siguiente código de prueba:

```python
from motores import servo360

motor = servo360(14)

motor.barrer()
```

## 🖥️ Código para empezar a probarlo

Una vez la conexión este bien realizada y el archivo `motores.py` este guardado dentro de la placa, en un archivo nuevo vamos a probar el siguiente código:

```python
from motores import servo360
from time import sleep

motor = servo360(14)

angulo = 180
tiempo = 1

bucle = True

while bucle:
    motor.girar(angulo)
    sleep(tiempo)
    motor.detener()
```

En este programa, podemos simular el movimiento de la aguja de un reloj.

## 🖥️ Ejercicios del proyecto

### Ejercicio 1: Definir los sentidos de giro

A traves del programa de prueba anterior, identifica con que angulo se realiza cada sentido de giro del motor. Si tienes dudas de por donde empezar, te dejo la siguiente ayuda:

- Sentido horario del motor : `completar`
- Sentido anti-horario del motor : `completar`

### Ejercicio 2: Tic Tac del reloj

Escribe un programa que te permita realizar el tic tac de un reloj. Si no sabes por donde empezar, te dejo el siguiente código como guía:

```python
from motores import servo360
from time import sleep

motor = servo360(14)
sensor = Ultrasonico()

angulo = # Escribe codigo aquí 👋🏻
tiempo = # Escribe codigo aquí 👋🏻

bucle = True
while bucle:
    motor.girar(angulo)
    sleep(tiempo)
    motor.detener()
```

### Ejercicio 3: Implementación de Led

Incluye un led al proyecto y diseña un programa que te permita compaginar el encendido y apagado de un led con el tic tac del reloj. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda:

```python
from motores import servo360
from machine import Pin
from time import sleep

motor = servo360(14)
led = Pin(2, Pin.ON)

angulo = # Colaca código aquí 👋🏻
tiempo = # Coloca código aquí 👋🏻

bucle = True
while bucle:

    motor.girar(angulo)
    # Coloca código aquí 👋🏻
    sleep(tiempo)
    motor.detener()
    # Coloca código aquí 👋🏻

    sleep(0.2)
```

### Ejercicio 4: Tic Tac con leds intercalados

Diseña un programa que permita al proyecto compaginar el encendido y apagado de dos leds con el tic tac del reloj. Cuando hablo de compaginar el encendido y apagado de dos leds, me refiero al fenomeno que ocurre en este codigo:

```python
from machine import Pin
from time import sleep

led1 = Pin(2, Pin.OUT)
led2 = Pin(3, Pin.OUT)

contador = 1
while contador < 20:
    if contador % 2 == 0:
        led1.on()
        sleep(0.5)
        led1.off()
    elif contador % 2 == 1:
        led2.on()
        sleep(0.5)
        led2.off()
    contador += 1
```

Si no sabes por donde empezar, te dejo el siguiente código como guía:

```python
from motores import servo360
from machine import Pin
from time import sleep

motor = servo360(14)
led = Pin(2, Pin.OUT)

angulo = 180
tiempo = 0.02

bucle = True
contador = 1
while bucle:

    motor.girar(angulo)

    if # Coloca código aquí 👋🏻
        # Coloca código aquí 👋🏻
    elif # Coloca código aquí 👋🏻
        # Coloca código aquí 👋🏻
    
    motor.detener()
    sleep(0.02)
    contador += 1
```


### Ejercicio 5: Interfaz de control del proyecto
Diseña un programa que haga lo mismo que en el ejercicio 4 pero sumale un buzzer que emita un sonido con una frecuencia distinta para cada led. Si tienes dudas de por donde empezar, te paso el siguiente código para que te guies:

```python
from motores import servo360
from machine import Pin
from time import sleep

motor = servo360(14)
led = Pin(2, Pin.OUT)

angulo = 180
tiempo = 0.02

bucle = True
contador = 1
while bucle:

    motor.girar(angulo)

    if # Coloca código aquí 👋🏻
        # Coloca código aquí 👋🏻
    elif # Coloca código aquí 👋🏻
        # Coloca código aquí 👋🏻
    
    motor.detener()
    sleep(0.02)
    contador += 1
```

