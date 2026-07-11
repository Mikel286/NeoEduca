# Proyecto QTI alto rendimiento

## 👋🏻 Presentación

Hola almuno del taller, esta guía esta diseñada para mejorar tus capacidades como competidor de la categoría rescate en alto rendimiento.

Con esta guía, fortaleceras tu lógica y código respecto al desafio de rescate de la liga de robotica.

## 💻 Reforzando QTI

En el desafío de rescate, la programación de los QTI es clave. Por eso, en esta sección reforzaremos el conocimiento sobre qti.

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
from acciones import Step_n, Step_Counter, Step_Avanzar

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

## 💻 Reforzando condicionales

### Que son las condiciones

Los condicionales en Python permiten ejecutar bloques de código específicos basados en si una condición es verdadera o falsa. Se estructuran mediante indentación (espaciado) y dos puntos (:), facilitando la toma de decisiones lógica. 

Las formas de establecer una condición en python se separan en los siguientes tres comandos:

- `if`: Evalúa la primera condición

- `elif`: Verifica condiciones adicionales

- `else`: Ejecuta código si las anteriores fallan.

Cuando yo evaluo dos condiciones en una misma linea, tengo dos comandos que puedo utilizar y **cuyo significado es totalmente distinto**:

- `and`: Sean A y B condiciones, usar `and` implica que tanto A como B deben ser verdaderas para que se cumpla la condición.

- `or`: Sean A y B condiciones, usar `or` implica que basta con que A o B sean verdaderas para que la condición se cumpla.

### Probando las condiciones

Para entender esto mejor veamos el siguiente ejemplo de codigo donde comprobamos si un numero es multiplo de 2 y 3:

```python

numero = int(input("Entregame un numero: "))

if numero % 2 == 0 and numero % 3 == 0:
    print("El numero es multiplo de 2 y 3...")
elif numero % 2 == 0 or numero % 3 == 0:
    print("El numero es multiplo de 2 o 3...")
else:
    print("El numero no es multiplo de 2 y 3...")
    
```

## 💻 Reforzando funciones

### Que son las funciones

Las funciones en Python son bloques de código reutilizables diseñados para realizar tareas específicas. Permiten organizar el programa, evitar la repetición de código y facilitar su mantenimiento.

Para profundizar en funciones, tenemos que comprender los siguientes conceptos:

- **Argumentos y Parámetros** 

    - **Parámetros:** Son las variables que defines dentro de los paréntesis en la función (ej. nombre).
    
    - **Argumentos:** Son los valores reales que le envías a la función cuando la llamas (ej. "Ana")

-  **Retorno de valores (`return`)**: La palabra clave `return` indica qué valor devolverá la función al finalizar su ejecución. Si no se utiliza return, la función devolverá por defecto `None`.

### Probando las funciones

Para entender esto en la practica, veamos los siguientes codigos que usan las funciones para condensar el código en componente que ya hemos trabajado:

- Codigo para el proyecto semaforo

```python

from machine import Pin
from time import sleep

led_izq = Pin(2, Pin.OUT)
led_cen = Pin(3, Pin.OUT)
led_der = Pin(4, Pin.OUT)

def semaforo(izq, cen, der, time):

    led_izq.value(izq)
    led_cen.value(cen)
    led_der.value(der)
    sleep(time)
    led_izq.value(0)
    led_cen.value(0)
    led_der.value(0)
    sleep(time)

semaforo(1,0,1,0.3)
semaforo(0,1,0,0.3)
semaforo(0,1,1,0.3)
semaforo(1,1,0,0.3)

```

## 💻 Aplicando logica al desafio

Programación no consiste en teclear comandos al azar, se trata de diseñar un algoritmo que resuleva en una serie de pasos finitos un proble de forma logica. Para esto, antes de pasar a programar es neceserio tener claro como voy a resolver ese problema.

Lograr lo anterior no siempre se puede mentalmente, por eso, es que en programación existe la herramienta llamada **diagrama de flujo**. Un diagrama de flujo  es la representación visual de un algoritmo o proceso, utilizando símbolos estandarizados conectados por flechas para mostrar la secuencia lógica de pasos, decisiones y flujo de datos.

Para nuestro desafio, un diagrama de flujo coherente podría ser el siguiente:

![Diagrama de flujo](assets/Qti%20alto%20rendimiento%201.png)

## 💻 Resolviendo el desafio de rescate

Cuando nos enfretamos a un desafio como el de rescate, es importante se metodico y resolver el problema por partes.

### Testeando motores

Tenemos que comprobar que ambos motores funcionen correctamente, para ello, podemos usar el siguiente código:

```python

from motores import servo360, carro
from time import sleep

motor_izq = servo360(14)
motor_der = servo360(15)

auto = carro(14, 15)

def test_motores():
    
    motor_izq.barrer()
    motor_der.barrer()

def calibracion():
    
    angulo_izq = int(input("Entregame el angulo del motor izq (0-180): "))
    angulo_der = int(input("Entregame el angulo del motor der (0-180): "))

    auto.calibrar(angulo_izq, angulo_der)

bucle = True
while bucle:

    accion = input("Indique la acción que desea realizar: ")

    if accion == "0":
        bucle = False
    elif accion == "1":
        test_motores()
    elif accion == "2":
        calibracion()
```

### Testeando QTI

Para testear los QTI, podemos usar el siguiente codigo que nos entregará el valor de cada medición:

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

### Testeando condiciones

Para testear que no hayamos cometido un error al establecer las condiciones, podemos usar el siguiente programa que nos ayudar a probar de forma segura que las condiciones hagan todo lo que quiero que hagan.

```python 

bucle = True

while bucle:

    medicion = input("Entregame una medicion: ") # Teneis que colocar algo como 11

    if medicion == "11":
        print("Avanzar y contar...")
    elif medicion == "10":
        print("Corregir a la izquierda...") 
    elif medicion == "01":
        print("Corregir a la derecha...")
    elif medicion == "00":
        print("Avanzar")
    else:
        print("Medicion no se reconoce...")
```

### Tabla de condiciones para 2 y 4 sensores

Antes de resolver el ejercicio de rescate, es importante conocer la cantidad de posibilidades existentes para tanto para el uso de 2 a 4 sensores QTI.

- Tabla de condiciones para 2 sensores QTI
![Imagen de condiciones para 2 qti](assets/Qti%20alto%20rendimiento%203.png)

- Tabla de condiciones para 4 sensores QTI
![Imagen de condiciones para 4 qti](assets/Qti%20alto%20rendimiento%204.png)

### Construyendo código `main.py`

Para una pista como la siguiente, hay que construir el siguiente tipo de código `main.py`:

![Imagen de pista versión 1](assets/Qti%20alto%20rendimiento%202.png)

```python
from motores import carro
from machine import Pin
from time import sleep

xtr_izq = Pin(7, Pin.IN, Pin.PULL_UP)
izq = Pin(8, Pin.IN, Pin.PULL_UP)
der = Pin(10, Pin.IN, Pin.PULL_UP)
xtr_der = Pin(11, Pin.IN, Pin.PULL_UP)

auto = carro(14, 15)

angulo_a = 0
angulo_b = 180

auto.setvelocidad(angulo_a, angulo_b)

time_step = 0.5
bucle = True 
while bucle:
    
    medicion = f"{xtr_izq.value()}{izq.value()}{der.value()}{xtr_der.value()}"
    print(medicion)

    if medicion == "0000": # Caso NNNN
        print("Negro")
    elif medicion == "0001": # Caso NNNB
        print("Girar Izquierda")
    elif medicion == "0010": # Caso NNBN
        print("Avanzar")
    elif medicion == "0011": # Caso NNBB
        print("Girar Izquierda")
    elif medicion == "0100": # Caso NBNN
        print("Avanzar")
    elif medicion == "0101": # Caso NBNB
        print("Avanzar")
    elif medicion == "0110": # Caso NBBN
        print("Avanzar")
    elif medicion == "0111": # Caso NBBB
        print("Girar Izquierda")
    elif medicion == "1000": # Caso BNNN
        print("Girar Derecha")
    elif medicion == "1001": # Caso BNNB
        print("Avanzar")
    elif medicion == "1010": # Caso BNBN
        print("Avanzar")
    elif medicion == "1011": # Caso BNBB
        print("Girar Izquierda")
    elif medicion == "1100": # Caso BBNN
        print("Girar Derecha")
    elif medicion == "1101": # Caso BBNB
        print("Girar Derecha")
    elif medicion == "1110": # Caso BNNN
        print("Girar Derecha")
    elif medicion == "1111": # Caso BBBB
        print("Avanzar")

    sleep(time_step)

```

## 💻 Recomendaciones del profe

Para ayudaros un poco mas, aquí se deja una sección de estrategías avanzadas para resolver el desafio de rescate.

### Calibración y condiciones

Para el código general del desafio, se recomienda el siguiente programa que aprovecha el uso de la estructura de datos `dict()` para el manejo de condiciones:

#### Archivo `main.py`

```python
from machine import Pin
from time import sleep

from motores import carro

# Blanco = 1
# Negro = 0

qti_eizq = Pin(0, Pin.IN, Pin.PULL_UP)
qti_izq = Pin(5, Pin.IN, Pin.PULL_UP)
qti_der = Pin(2, Pin.IN, Pin.PULL_UP)
qti_eder = Pin(1, Pin.IN, Pin.PULL_UP)

auto = carro(13,14)
auto.setvelocidad(97,83)

cont = 0

time_sleep = 0.2

def medir():
    medicion = f"{qti_eizq.value()}{qti_izq.value()}{qti_der.value()}{qti_eder.value()}"
    #print(medicion)
    return medicion

def condiciones(medicion):
    
    def adelante():
        print("Moverse adelante")
        auto.moveadelante()
    
    def izqurda():
        print("Moverse izquierda")
        auto.moveizquierda()
        
    def derecha():
        print("Moverse derecha")
        auto.movederecha()
        
    def negro():
        global cont
        cont += 1
        
        print(f"Negro: {cont}")
    
    acciones = {
    "0000": negro, #NNNN
    "0001": izqurda, #NNNB
    "0010": adelante, #NNBN
    "0011": izqurda, #NNBB
    "0100": adelante, #NBNN
    "0101": adelante, #NBNB
    "0110": adelante, #NBBN
    "0111": izqurda, #NBBB
    "1000": derecha, #BNNN
    "1001": adelante, #BNNB
    "1010": adelante, #BNBN
    "1011": izqurda, #BNBB
    "1100": derecha, #BBNN
    "1101": derecha, #BBNB
    "1110": derecha, #BBBN
    "1111": adelante  #BBBB
    }
    
    acciones[medicion]()

def main():
    
    medicion = medir()
    condiciones(medicion)
    sleep(time_sleep)
    
bucle = True
while bucle:
    main()
    
```