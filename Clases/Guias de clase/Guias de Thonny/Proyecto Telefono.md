# Proyecto Keyboard

## 👋🏻 Presentación

Hola alumno del taller, esta es la guía para aprender con el proyecto **Telefono** desarrollado por el profesor Mikel Ania.

Con el, aprenderas sobre la conexión y la programación de un teclado numérico (keyboard) y su programación a traves del IDE Thonny con el lenguaje de programación Python.

## 🔌Conexión del proyecto

Para este proyecto deberas seguir la siguiente conexión que se te presenta en la imagen.

![Imagen de la conexión](assets/Keyboard%201.jpeg)

## 💻 Librería `keyboard.py`

Para este proyecto es necesario que guardes en tu placa rasph berry pi pico el archivo `keyboard.py` que contiene el siguiente código:

```python

from machine import Pin
from time import sleep
from random import randint

from tone import Buzzer

class Keyboard():
    
    def __init__(self):
        
        self.rows = [Pin(i, Pin.OUT) for i in [9,8,7,6]]
        self.cols = [Pin(i, Pin.IN, Pin.PULL_UP) for i in [13,12,11,10]]

        self.keys = [
            ["1","2","3","A"],
            ["4","5","6","B"],
            ["7","8","9","C"],
            ["*","0","#","D"]]

    def scan(self):
        for i, row in enumerate(self.rows):
            row.low()
            for j, col in enumerate(self.cols):
                if col.value() == 0:
                    return self.keys[i][j]
            row.high()
        return None
```

## 💻 Código para empezar a probarlo

Una vez la conexión este bien realizada y el archivo `keyboard.py` este guardado dentro de la placa, en un archivo nuevo vamos a probar el siguiente código:

```python

from keyboard import Keyboard
from machine import Pin
import time

teclado = Keyboard()
while True:
    tecla = teclado.scan()
    if tecla is not None:
        print("Tecla:", tecla)
        time.sleep(0.3)
```
Con este programa, podremos imprimir en pantalla las teclas que estamos presionando en nuestro teclado y verificar que la conexión esta bien hecha.

## 💻 Desafios del proyecto

Ahora que ya lo tienes todo para empezar es hora de que pongamos a prueba tu propio desempeño con los siguientes ejercicios:

### Ejercicio 1: Distinguir entre numeros y letras
Tendras que hacer un programa donde cada vez que una tecla es presionada el programa sea capaz de distinguir si esta es una letra o un número. Si no sabes por donde empezar, no te preocupes porque te paso el siguiente código incompleto:

```python

from keyboard import Keyboard
from machine import Pin
import time

teclado = Keyboard()
while True:
    tecla = teclado.scan()
    if tecla is not None:
        print("Tecla:", tecla)
        if tecla in ("1234567890"):
            # Tienes que colocar algo aqui 👋🏻
        else:
            # Tienes que colocar algo aquí 👋🏻
        time.sleep(0.3)

```
### Ejercicio 2: Encender y apagar leds con teclado
Tendras que hacer un programa donde el codigo haga lo siguiente:

1. Cada vez que **presione 1 el led izquierdo se encienda** y **presione 4 el led izquierdo se apague**.

2. Cada vez que **presione 2 el led del centro se encienda** y **presione 5 el led del centro se apague**.

3. Cada vez que **presione 3 el led derecho se encienda** y **presione 6 el led derecho se apague**.

Si no sabes por donde empezar te dejo el siguiente código incompleto:

```python

from keyboard import Keyboard
from machine import Pin
import time

led_izq = Pin(2, Pin.OUT)
led_cen = Pin(3, Pin.OUT)
led_der = Pin(4, Pin.OUT)

teclado = Keyboard()
while True:
    tecla = teclado.scan()
    if tecla is not None:
        print("Tecla:", tecla)
        if tecla in ("1234567890"):
            
            if # Tienes que colocar condición 1 aqui 👋🏻

            elif # Tienes que colocar condición 2 aqui 👋🏻

            elif # Tienes que colocar condición 3 aqui 👋🏻

            elif # Tienes que colocar condición 4 aqui 👋🏻

            elif # Tienes que colocar condición 5 aqui 👋🏻

            elif # Tienes que colocar condición 6 aqui 👋🏻
        
        time.sleep(0.3)
```

### Ejercicio 3: Dandole sonido al telefono
Tienes que hacer un programa que permita que cada vez que presiones una tecla, está emita un sonido a una frecuencia aleatoria entre 440-480hz. Para este ejercicio, tendras que añadir dos librerías:

- Para el buzzer la librería `tone.py` donde usamos `Buzzer()` -> Esta en la placa e importarla

- Para la aleatoriedad la librería `random` donde usamos `randint()` -> Esta solo importarla

Si no sabes por donde empezar, te dejo el siguiente que te ayudara a guiarte:

```python
from keyboard import Keyboard
from tone import Buzzer
from random import randint
import time

teclado = Keyboard()
buzzer = Buzzer(5)

while True:
    tecla = teclado.scan()
    if tecla is not None:
        # Codigo para emitir sonido al azar 👋🏻
        print("Tecla:", tecla)
        if tecla in ("1234567890"):
            # Tienes que colocar algo aqui 👋🏻
        else:
            # Tienes que colocar algo aquí 👋🏻
        time.sleep(0.3)

```

### Ejercicio 4: Registro de numeros telefonicos
Tienes que hacer un programa que permita registrar numeros telefónicos en una agenda, la cual, se pueda ver a traves del computador como una agenda. Para este ejercicio, deberás conocer la estructura de datos llamada `list()` que te permitirá guardar datos.

#### Que son las `list()`

Las listas en programación son estructuras de datos que permiten almacenar una colección ordenada de elementos bajo un mismo nombre. Funcionan como una secuencia lineal donde cada dato ocupa una posición específica llamada índice, facilitando organizar, buscar y modificar información de manera eficiente.

Una representación visual de como se dan las listas es la siguiente:

![Imagen de lista](assets/Keyboard%201.png)

Para python, la construcción y manipulación de listas se dá con los siguientes comandos:

- `nombres = []` -> Creación de una lista

- `nombres.append("Alex")` -> Comando para agregar elementos a una lista

- `nombres.pop()` -> Comando para eliminar el último elemento de la lista

- `print(nombres)` -> Comando para imprimir la lista completa

- `print(nombres[n])` -> Comando para imprimir el valor en la posición `n` de la lista. 


#### Ayuda para el ejercicio
Si no sabes por donde empezar, te paso el siguiente código que te ayudará a guiarte:

```python
from keyboard import Keyboard
from tone import Buzzer
from random import randint
import time

teclado = Keyboard()
buzzer = Buzzer(5)

agenda = []
numero = ""

while True:
    tecla = teclado.scan()
    if tecla is not None:
        print("Tecla:", tecla)
        if tecla in ("1234567890"):
            # Codigo para emitir sonido al azar 👋🏻
            numero += tecla # Tienes que colocar algo aquí para guardar los numeros que ingreses 👋🏻
        else:
            if tecla == "A": 
                # Tienes que colocar algo aquí para guardar el numero en la agenda 👋🏻
            elif tecla == "B": 
                # Tienes que colocar algo aquí para cargar cada numero en la agenda 👋🏻

        time.sleep(0.3)
```

### Ejercicio 5: Llamando a un numero de telefono
Tienes que hacer un programa que no solo te permita hacer lo mismo que en el ejercicio 4, sino que tambien te permita llamar a los numeros que marques y te diga si el numero existe o no. Si no sabe por donde empezar, te dejo el siguiente código que te servirá de guía:

```python
from keyboard import Keyboard
from tone import Buzzer
from random import randint
import time

teclado = Keyboard()
buzzer = Buzzer(5)

agenda = []
numero = ""

while True:
    tecla = teclado.scan()
    if tecla is not None:
        print("Tecla:", tecla)
        if tecla in ("1234567890"):
            # Codigo para emitir sonido al azar 👋🏻
            numero += tecla # Tienes que colocar algo aquí para guardar los numeros que ingreses 👋🏻
        else:
            if tecla == "A": 
                # Tienes que colocar algo aquí para guardar el numero en la agenda 👋🏻
            elif tecla == "B": 
                # Tienes que colocar algo aquí para cargar cada numero en la agenda 👋🏻
            elif tecla == "C":
                if numero in agenda:
                    # Coloca tu código aqui
                else:
                    # Coloca tu código aquí

        time.sleep(0.3)
```