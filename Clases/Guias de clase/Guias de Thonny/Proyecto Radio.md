# Proyecto Radio

## 👋🏻 Presentación

<div style="text-align: justify;">

Hola alumno del taller, esta es la guía para aprender con el proyecto **Radio** desarrollado por el profesor Mikel Ania.

Con el, aprenderas sobre la conexión y la programación tanto de leds como buzzer y su programación a traves del IDE Thonny con el lenguaje de programación Python.

</div>

## 💡Conociendo los componentes

<div style="text-align: justify;">

Un LED (diodo emisor de luz) es un componente electrónico semiconductor de dos terminales (ánodo y cátodo) que emite luz cuando una corriente eléctrica moderada lo atraviesa. Basado en la electroluminiscencia, convierte la energía eléctrica en luz de manera muy eficiente, consumiendo hasta un 90% menos energía que las bombillas incandescentes.

Un buzzer, o zumbador, es un transductor electroacústico que convierte energía eléctrica en sonido, emitiendo un tono agudo continuo o intermitente al recibir corriente. Funciona como alarma o señal de confirmación en dispositivos como electrodomésticos, automóviles y proyectos de electrónica. Dentro de los buzzer, existen dos grandes tipos:

- **Activo**: Incorpora un oscilador interno, por lo que emite sonido automáticamente al aplicarle voltaje directo (DC).

- **Pasivo**:  No tiene oscilador interno; requiere una señal eléctrica de onda cuadrada (frecuencia) para generar diferentes tonos.

En los buzzers o zumbadores, la frecuencia es la magnitud que determina el tono del sonido que emiten

</div>

## 🔌 Conexión del proyecto

Para este proyecto, tienes que recordar la conexión de los componentes led y buzzer dentro de la placa de la siguiente manera:

- LED izquierdo (PIN 2)
- LED centro (PIN 3)
- LED derecho (PIN 4)
- Buzzer (PIN 5)

## 💻 Librería `tone.py`

Para este proyecto es necesario que guardes en tu placa rasph berry pi pico el archivo `tone.py` que contiene el siguiente código:

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

## 💻 Código para empezar a probarlo

Una vez la conexión este bien realizada y el archivo `keyboard.py` este guardado dentro de la placa, en un archivo nuevo vamos a probar el siguiente código:

```python

from tone import Buzzer
from machine import Pin
from time import sleep

led_izq = Pin(2, Pin.OUT)
led_cen = Pin(3, Pin.OUT)
led_der = Pin(4, Pin.OUT)

buzzer = Buzzer(5)

led_izq.on()
led_cen.on()
led_der.on()
sleep(1)
led_izq.off()
led_cen.off()
led_der.off()

buzzer.on(440) # Frecuencia a la que trabaja el buzzer
sleep(1)
buzzer.off()

```

## 💻 Desafios del proyecto

Ahora que ya lo tienes todo para empezar es hora de que pongamos a prueba tu propio desempeño con los siguientes ejercicios:

### Ejercicio 1: Emitiendo distintos tonos
Tendras que hacer un programa que emita sonidos con frecuencia distinta usando el zumbador. Si no sabes por donde empezar, no te preocupes porque te paso el siguiente código incompleto:

```python
from tone import Buzzer
from time import sleep

buzzer = Buzzer(5)

buzzer.on() # Coloca la primera fecuencia
sleep(1)
buzzer.on() # Coloca la segunda fecuencia
sleep(1)
buzzer.on() # Coloca la tercera fecuencia
sleep(1)
buzzer.off()
```

Para este ejercicio tendras que usar la siguiente tabla de frecuencias:

![Tabla de frecuencias](assets/Radio%201.png)

### Ejercicio 2: Juntando tonos y frecuencias
Tendras que hacer un código donde puedas emitir tres tonos distintos con el buzzer y que estos vayan acompañados con una secuencia de led particular para cada sonido. Si no sabes por donde empezar, no te preocupes porque te paso el siguiente código incompleto:

```python

from tone import Buzzer
from machine import Pin
from time import sleep

led_izq = Pin(2, Pin.OUT)
led_cen = Pin(3, Pin.OUT)
led_der = Pin(4, Pin.OUT)

buzzer = Buzzer(5)

# Colocar la primera frecuencia y secuencia de leds 👋🏻
buzzer.on(440)
led_izq.()
led_cen.()
led_der.()

sleep(1)

# Colocar la segunda frecuencia y secuencia de leds 👋🏻
buzzer.on(440)
led_izq.()
led_cen.()
led_der.()

sleep(1)

# Colocar la tercera frecuencia y secuencia de leds 👋🏻
buzzer.on(440)
led_izq.()
led_cen.()
led_der.()

sleep(1)

```

### Ejercicio 3: Emitiendo una frecuencia y encendiendo un led al azar

Tendras que hacer un codigo que cada vez que se ejecute, haga las siguientes dos cosas:

- Encienda y apague un led al azar

- Emita un sonido a una frecuencia al azar

Para este ejercicio tendras que ver la siguiente mini sección sobre la libreria `random`:

#### Librería `random` 

La librería random es un módulo integrado en la biblioteca estándar de Python que permite generar números pseudoaleatorios y seleccionar elementos al azar. No requiere instalación previa; simplemente debes añadir `import random` al inicio de tu código para empezar a usar sus funciones.

De esta libreria vamos a usar el comando `randint`. La función `randint()` en Python, perteneciente al módulo `random`, genera un número entero aleatorio dentro de un rango específico, incluyendo tanto el valor mínimo como el máximo $[a, b]$.

Para entender mejor esto, prueba el siguiente codigo:

```python

from random import randint

print(f"Se genera el numero al azar: {randint(1,100)}")

```

#### Ayuda ejercicio 3

Una vez que hayas visto el comando `random`, te dejo el siguiente código para que te guies si estas perdido:

```python

from tone import Buzzer
from machine import Pin
from time import sleep

led_izq = Pin(2, Pin.OUT)
led_cen = Pin(3, Pin.OUT)
led_der = Pin(4, Pin.OUT)

buzzer = Buzzer(5)

numero_azar = # Coloca aqui el comando para generar un numero al azar entre 1 y 3

if numero_azar == 1:
    # Colocar primera acción
elif numero_azar == 2:
    # Colocar segunda acción
elif numero_azar == 3:
    # Colocar tercera acción 
```

### Ejercicio 4: Emitiendo una canción

Construye un código que te permita tocar una canción en 8 bits a traves del buzzer. Si no sabes por donde empezar, te dejo la siguiente canción y un código que te pueden ayudar:

#### Canción de Super Mario

La partitura de la canción es la siguiente:

- DO5  250ms - SOL5 250ms - LA5  250ms -SOL5 250ms

- MI5  250ms - SOL5 250ms - DO6  500ms

- LA5  250ms - SOL5 250ms - MI5  250ms - RE5  250ms

- DO5  500ms - SOL4 500ms

La frecuencia de las notas musicales es la siguiente

### Ejercicio 5: Aprovechando funciones y ciclos
Para este ejercicio se te pedira hacer un ciclo de 100 repeticiones de secuencia leds y nota musical de buzzer donde cada secuencia y nota sea distinta a la anterior. Para este ejercicio, tendrás que conocer los conceptos de `funciones` y `ciclos` que se te explica a continuación.

#### Los ciclos en programación
Los ciclos (o bucles) en Python permiten ejecutar un mismo bloque de código repetidamente mientras se cumpla una condición o se recorra una colección. Python utiliza principalmente dos tipos de estructuras:

- Ciclos `while`: Son ciclos condicionales que nos permiten repetir un programa hasta que se cumpla un caso especifico.

- Ciclos `for`: Son ciclos iterativo que permiten recorrer estruturas de datos o repetir un programa un cierto numero `n` de veces.

Para este proyecto, sera ideal usar los ciclos `for` de una manera como esta:

```python
from random import randint
from time import sleep

for x in range(100):
    numero_aleatorio = randint(1,100)
    print(f"Iteracion {x} con numero aleatorio: {numero_aleatorio}")
```

Con este programa, generamos en pocas lineas 100 números aleatorios.

#### Las funciones en programación
Las funciones en Python son bloques de código reutilizables diseñados para realizar tareas específicas. Permiten organizar el programa, evitar la repetición de código y facilitar su mantenimiento.

Para profundizar en funciones, tenemos que comprender los siguientes conceptos:

- **Argumentos y Parámetros** 

    - **Parámetros:** Son las variables que defines dentro de los paréntesis en la función (ej. nombre).
    
    - **Argumentos:** Son los valores reales que le envías a la función cuando la llamas (ej. "Ana")

-  **Retorno de valores (`return`)**: La palabra clave `return` indica qué valor devolverá la función al finalizar su ejecución. Si no se utiliza return, la función devolverá por defecto `None`.

Para un proyecto como la **radio**, una buena función sería la siguiente:

```python
from tone import Buzzer
from machine import Pin
from time import sleep

led_izq = Pin(2, Pin.OUT)
led_cen = Pin(3, Pin.OUT)
led_der = Pin(4, Pin.OUT)

buzzer = Buzzer(5)

def radio(izq, cen, der, frecuencia, time):
    led_izq.value(izq)
    led_cen.value(cen)
    led_der.value(der)
    buzzer.on(frecuencia)
    sleep(time)
    led_izq.value(0)
    led_cen.value(0)
    led_der.value(0)
    buzzer.off(0)
    sleep(0.2)

radio(1, 0, 1, 440, 0.5)
```

#### Ayuda para el ejercicio 
Si no sabes por donde empezar, te dejo el siguiente código que te guiará:

```python
from tone import Buzzer
from machine import Pin
from time import sleep

led_izq = Pin(2, Pin.OUT)
led_cen = Pin(3, Pin.OUT)
led_der = Pin(4, Pin.OUT)

# Aquí hay una pieza de código que falta 👋🏻

n = # Aqui hay que colocar código 👋🏻
for x in range()
    # Aquí hay que colocar código 👋🏻
```
