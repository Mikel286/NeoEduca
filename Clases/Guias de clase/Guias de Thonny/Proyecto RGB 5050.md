# Proyecto RGB 5050

## 👋🏻 Presentación

Hola alumno del taller, esta es la guía para aprender con el componente **RGB 5050** desarrollado por el profesor Mikel Ania.

Con el, aprenderas sobre la conexión y la programación de un modulo RGB y su programación a traves del IDE Thonny con el lenguaje de programación Python.

## 🔌Conexión del proyecto

Para este proyecto deberas seguir la siguiente conexión que se te presenta a continucación:

- GND en puerto GND correspondiente de la placa
- Pin R en GP6
- Pin G en GP7
- Pin B en GP8

## 💻 Librería `rgb.py`

Para el funcionamiento del modulo rgb 5050, necesitamos guardar dentro de la placa el archivo `rgb.py`:

```python
from machine import PWM, Pin
from time import sleep

class RGB:
    
    def __init__(self, pin_red, pin_green, pin_blue):
        
        self.pin_red = PWM(Pin(pin_red, Pin.OUT))
        self.pin_green = PWM(Pin(pin_green, Pin.OUT))
        self.pin_blue = PWM(Pin(pin_blue, Pin.OUT))
        
        self.pin_red.freq(1000)
        self.pin_green.freq(1000)
        self.pin_blue.freq(1000)
        
    def set_color(self, r_value, g_value, b_value): # Maximo valor: 65535
        self.pin_red.duty_u16(r_value)
        self.pin_green.duty_u16(g_value)
        self.pin_blue.duty_u16(b_value)
        
    def ultra_rgb(self, distancia, r_value, g_value, b_value):
        self.set_color(r_value + distancia, g_value + distancia, b_value + distancia)
```

## 💻 Código para empezar a probarlo

Una vez la conexión este bien realizada y el archivo `rgb.py` este guardado dentro de la placa, en un archivo nuevo vamos a probar el siguiente código:

```python
from rgb import RGB
from time import sleep

rgb = RGB(6,7,8)

r = 60000
g = 0
b = 0

rgb.set_color(r,g,b)
sleep(1)
rgb.set_color(0,0,0)
sleep(1)
```

## 💻 Desafios del proyecto

Ahora que ya lo tienes todo para empezar es hora de que pongamos a prueba tu propio desempeño con los siguientes ejercicios:

### Ejercicio 1: Mostrando colores primarios

Tendras que hacer un programa que permita al modulo RGB mostrar los tres colores primarios (rojo, verde y azul) del componente por separado. Si no sabes por donde empezar, no te preocupes porque te paso el siguiente código incompleto:

```python

from rgb import RGB
from time import sleep

rgb = RGB(6,7,8)

r = # Coloca un numero entero aquí 👋🏻
g = # Coloca un numero entero aquí 👋🏻
b = # Coloca un numero entero aquí 👋🏻

rgb.set_color(r,g,b)
sleep(1)
rgb.set_color(0,0,0)
sleep(1)

r = # Coloca un numero entero aquí 👋🏻
g = # Coloca un numero entero aquí 👋🏻
b = # Coloca un numero entero aquí 👋🏻

rgb.set_color(r,g,b)
sleep(1)
rgb.set_color(0,0,0)
sleep(1)

r = # Coloca un numero entero aquí 👋🏻
g = # Coloca un numero entero aquí 👋🏻
b = # Coloca un numero entero aquí 👋🏻

rgb.set_color(r,g,b)
sleep(1)
rgb.set_color(0,0,0)
sleep(1)
```

### Ejercicio 2: Mostrando mezclas de colores

Tendras que hacer un programa que permita al modulo RGB mostrar mezclas de los colores primarios (rojo, verde y azul) del componente por separado. Si no sabes por donde empezar, no te preocupes porque te paso el siguiente código incompleto:

```python

from rgb import RGB
from time import sleep

rgb = RGB(6,7,8)

r = # Coloca un numero entero aquí 👋🏻
g = # Coloca un numero entero aquí 👋🏻
b = # Coloca un numero entero aquí 👋🏻

rgb.set_color(r,g,b)
sleep(1)
rgb.set_color(0,0,0)
sleep(1)

r = # Coloca un numero entero aquí 👋🏻
g = # Coloca un numero entero aquí 👋🏻
b = # Coloca un numero entero aquí 👋🏻

rgb.set_color(r,g,b)
sleep(1)
rgb.set_color(0,0,0)
sleep(1)

r = # Coloca un numero entero aquí 👋🏻
g = # Coloca un numero entero aquí 👋🏻
b = # Coloca un numero entero aquí 👋🏻

rgb.set_color(r,g,b)
sleep(1)
rgb.set_color(0,0,0)
sleep(1)
```