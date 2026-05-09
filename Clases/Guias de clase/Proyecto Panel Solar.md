# Proyecto Panel Solar

## 👋🏻 Presentación

Hola alumno del taller, esta es la guía para aprender con el proyecto **Panel Solar** desarrollado por el profesor Mikel Ania.

Con el, aprenderas sobre la conexión y la programación de motores junto con el desarrollo de un panel de control a traves del IDE Thonny con el lenguaje de programación Python.

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

motor_izq = servo360(14)
motor_der = servo360(15)

motor_izq.barrer()
motor_der.barrer()
```

### Que es un sensor LDR

Un sensor LDR (Light Dependent Resistor) o fotorresistencia es un componente electrónico cuya resistencia eléctrica disminuye al aumentar la intensidad de la luz incidente.

### Librería `sensores`

Para hacer funcionar uno o mas sensores LDR, necesitamos guardar dentro de la placa la librería `sensores.py` que tiene el siguiente código:

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

### Probando el sensor LDR

Para probar el funcionamiento de un sensor LDR, podemos usar el siguiente código que nos entregará las lecturas de un sensor LDR:

```python
from sensores import LDR
from time import sleep

sensor = LDR(6)

bucle = True
while bucle:
    print(f"El valor entregado por el sensor es: {sensor.medir()}")
    sleep(0.3)
```

## 🖥️ Código para empezar a probarlo

Una vez la conexión este bien realizada y el archivo `motores.py` este guardado dentro de la placa, en un archivo nuevo vamos a probar el siguiente código:

```python
from motores import servo360
from time import sleep

motor_x = servo360(14)
motor_y = servo360(15)

angulo_x = int(input("Ingrese el angulo (0-180) del eje x : "))
angulo_y = int(input("Ingrese el angulo (0-180) del eje y: "))

tiempo_x = float(input("Ingrese el tiempo de giro del eje x: "))
tiempo_y = float(input("Ingrese el tiempo de giro del eje y: "))

motor_x.girar(angulo_x)
sleep(tiempo_x)
motor_x.detener()

motor_y.girar(angulo_y)
sleep(tiempo_y)
motor_y.detener()
```

En este programa, podemos elegir el sentido y tiempo de giro de cada uno de los motores de este proyecto.

## 🖥️ Ejercicios del proyecto

### Ejercicio 1: Definir los sentidos de giro

A traves del programa de prueba anterior, identifica con que angulo se realiza cada sentido de giro del motor. Si tienes dudas de por donde empezar, te dejo la siguiente ayuda:

- Sentido horario del motor x : `completar`
- Sentido anti-horario del motor x : `completar`
- Sentido horario del motor y : `completar`
- Sentido anti-horario del motor y : `completar`

### Ejercicio 2: Movimiento + lectura

Escribe un programa que te permita mover en un angulo y tiempo especificos los motores del proyecto y luego realiza una lectura con el sensor LDR. Si no sabes por donde empezar, te paso el siguiente código para que te guies:

```python
from sensores import LDR
from motores import Servo360
from machine import Pin
from time import sleep

motor_x = servo360(14)
motor_y = servo360(15)

sensor = LDR(6)

angulo_x = # Escribe codigo aquí 👋🏻
angulo_y = # Escribe codigo aquí 👋🏻

tiempo_x = # Escribe codigo aquí 👋🏻
tiempo_y = # Escribe codigo aquí 👋🏻

motor_x.girar(angulo_x)
sleep(tiempo_x)
motor_x.detener()

motor_y.girar(angulo_y)
sleep(tiempo_y)
motor_y.detener()

# Escribe codigo aquí para el sensor LDR 👋🏻

```

### Ejercicio 3: Implementación de botones

Incluye botones y diseña un programa que te permitan controlar manualmente uno de los motores del proyecto. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda:

```python
from motores import servo360
from machine import Pin
from time import sleep

motor_x = servo360(14)
motor_y = servo360(15)

switch_izq = Pin(0, Pin.IN, Pin.PULL_UP)
switch_der = Pin(1, Pin.IN, Pin.PULL_UP)

bucle = True
while bucle:

    if switch_izq.value() == 0:
        print("🔘 El switch_izq está PRESIONADO")
        # Colocar código aquí 👋🏻
    elif switch_der.value() == 0:
        print("🔘 El switch_der está PRESIONADO")
        # Colocar código aquí 👋🏻

    sleep(0.2)
```

### Ejercicio 4: Añadiendo mas sensores

Conecta mas sensores LDR y diseña un programa que te permita gestionarlos. Si no sabes por donde empezar te dejo el siguiente código para que te guies:

```python
from sensores import LDR
from time import sleep

sensor1 = # Colocar código aquí 👋🏻
sensor2 = # Colocar código aquí 👋🏻
sensor3 = # Colocar código aquí 👋🏻

bucle = True
while bucle:
    medicion1 = # Colocar código aquí 👋🏻
    medicion2 = # Colocar código aquí 👋🏻
    medicion3 = # Colocar código aquí 👋🏻
    print(f"{medicion1} {medicion2} {medicion3}")

    sleep(0.3)
```

### Ejercicio 5: Interfaz de control del proyecto
Diseña un programa que entregue un panel de control donde a traves de `inputs` especificos puedas controlar los motores del proyecto. Si tienes dudas de por donde empezar, te paso el siguiente código para que te guies:

```python
from motores import servo360
from time import sleep

motor_x = Servo360(14)
motor_y = Servo360(15)

bucle = True

while bucle:

    accion = input("Indique la acción que quiere realizar: ")

    if accion == "0":
        print("Saliendo del programa...")
    else:
        print(f"La accion {accion} no se reconoce...")
```

