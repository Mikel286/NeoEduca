# Tutoría 1 (Parte 1): Entendiendo los fundamentos de python

## 👋🏻 Presentación 👋🏻

Hola alumno, en esta guía de tutoria 1 aprenderas sobre que es python y como introducirse al mundo de la programación y la róbotica a traves de este.

## 💻 Repasando Conceptos 💻

### ¿Qué es python?
Python es un lenguaje de programación de código abierto, de alto nivel y muy versátil, famoso por su sintaxis sencilla y legible. Es ampliamente utilizado en el desarrollo web, la inteligencia artificial, el análisis de datos y la automatización de tareas.

### ¿Cómo se usa python?
Para poder construir un programa de lenguaje python que posteriormente se pueda ejecutar, hay que usar lo que se conoce como un editor de código. Un editor de código es una aplicación diseñada específicamente para escribir y editar el código fuente de programas o páginas web. A diferencia de los editores de texto básicos, están optimizados para la programación, ayudando a los desarrolladores a escribir código de forma más rápida, ordenada y con menos errores.

En estas tutorías, usaremos un editor de código centrado en python, el cual, trae todo lo necesario para empezar a trabar en nuestros proyectos desde el minuto cero. El nombre de este editor es Thonny y se descarga en el siguiente [link](https://thonny.org/).

### ¿Que es un microcontrolador?
Un microcontrolador es un circuito integrado programable que funciona como una pequeña computadora. Integra una Unidad Central de Procesamiento (CPU), memoria y puertos de entrada/salida (periféricos) en un solo chip. Está diseñado para controlar tareas específicas en dispositivos electrónicos de forma autónoma. Un microcontrolador se compone internamente de tres bloques fundamentales:

- **CPU (Unidad Central de Procesamiento)**: Es el "cerebro" que lee y ejecuta las instrucciones del programa.

- **Memoria**: Aloja el código de instrucciones (Memoria Flash/ROM), los datos temporales en uso (RAM) y parámetros de configuración.

- **Periféricos de Entrada/Salida (E/S)**: Permiten al chip conectarse con el mundo exterior. Incluyen pines para leer sensores, activar motores o luces y puertos de comunicación.

## 💻Poniendo en práctica lo aprendido 💻

### Conectando el microcontrolador al editor
Para trabajar con un microcontrolador en thonny, debemos conectarlo a traves de un sub-menu que se encuentra dentro de thonny:

Para entenderlo mejor, siga los pasos de las siguientes imagenes:

![Imagen 1](assets/Tutoria_1%201.png)
![Imagen 2](assets/Tutoria_1%202.png)
![Imagen 3](assets/Tutoria_1%203.png)

### Ejecutando nuestro primer código
Para verificar el correcto funcionamiento entre nuestro editor, el código y el microcontrolador, contruyamos y carguemos el siguiente mini programa:

```python
nombre = input("Indiqueme su nombre: ")
print(f"Hola {nombre}")
```

Con este programa podemos entrega un valor de entrada al código que utilizará para imprimir el mensaje de "Hola {nombre}".

## 💻 Introducción a componentes 💻

### ¿Que son los sensores y actuadores?

En robótica, existen dos grandes categorías que separan a los componentes de un robot:

- **Actuadores**: Componente que recibe una señal eléctrica proveniente de un controlador y la transforma en una acción física o movimiento mecánico.

- **Sensor**: Componente que detecta magnitudes físicas o químicas del entorno y las convierte en señales eléctricas.

En la primeras tutorias, trabajaremos unicamento con actuadores.

### Componente LED

#### ¿Qué es un led?

n LED (diodo emisor de luz) es un componente electrónico semiconductor de dos terminales (ánodo y cátodo) que emite luz cuando una corriente eléctrica moderada lo atraviesa. Basado en la electroluminiscencia, convierte la energía eléctrica en luz de manera muy eficiente, consumiendo hasta un 90% menos energía que las bombillas incandescentes.

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

## Ejercicios
Ahora que ya conoces todos los conceptos de la tutoria, se te invita a probar tu aprendizaje con los siguientes ejercicios.

### Ejercicio 1: Diseñando secuencias de luces

Diseña un programa que te permita ejecutar 5 secuencias de led distintas con tiempos de espera distintos entre cada una. Si no sabes por donde empezar, se te deja el siguiente código para guiarte:

```python
from machine import Pin
from time import sleep

led_izq = # Completa este código 👋🏻
led_cen = # Completa este código 👋🏻
led_der = # Completa este código 👋🏻

# Código para la primera secuencia 

# Código para la segunda secuencia 

# Código para la tercera secuencia 

# Código para la cuarta secuencia 

# Código para la quinta secuencia 
```

### Ejercicio 2: Diseñando notas musicales

Diseña un programa que te permita reproducir 5 notas musicales con frecuencias (*Hz*) y tiempos de espera distintos entre cada nota. Si no sabes por donde empezar, se te deja el siguiente código para guiarte:

```python
from Buzzer import buzzer
from time import sleep

buzzer = # Completa el código 👋🏻

frecuencia_1 = # Completa el código 👋🏻
frecuencia_2 = # Completa el código 👋🏻
frecuencia_3 = # Completa el código 👋🏻
frecuencia_4 = # Completa el código 👋🏻
frecuencia_5 = # Completa el código 👋🏻

# Código para la primera nota musical 

# Código para la segunda nota musical 

# Código para la tercera nota musical 

# Código para la cuarta nota musical 

# Código para la quinta nota musical 
```

Ademas del código, se te deja la siguiente tabla de frecuencias

### Ejercicio 3: Mezclando secuencias de luces y notas musicales

Diseña un programa que te permita reproducir 5 secuencias de luces donde cada una este acompañada de una nota musical distinta y un tiempo de espera distinto entre cada nota. Si no sabes por donde empezar, se te deja el siguiente código para guiarte:

```python
from Buzzer import buzzer
from machine import Pin
from time import sleep

led_izq = # Completa este código 👋🏻
led_cen = # Completa este código 👋🏻
led_der = # Completa este código 👋🏻
buzzer = # Completa el código 👋🏻

# Diseñar secuencias aquí
```

## Desafio de la tutoría: Las 100 secuencias

Si los ejercicios has sido poco para probar tus habilidades, te entrego el siguiente desafio de alta dificultad para esta tutoría. A partir de los conceptos vistos en la tutoría, construye un programa que te permita ejecutar 100 se cuencias de luces distintas acompañadas de notas musicales y tiempos de espera distintos para cada secuencia.

```python
from Buzzer import buzzer
from machine import Pin
from time import sleep

led_izq = # Completa este código 👋🏻
led_cen = # Completa este código 👋🏻
led_der = # Completa este código 👋🏻
buzzer = # Completa el código 👋🏻

# Diseñar secuencias aquí
```

# Tutoría 1 (Parte 2): Introducción a gitub

## Introducción a conceptos

### ¿Que es git?

Git es un sistema de control de versiones distribuido, gratuito y de código abierto. En términos sencillos, es una herramienta que registra todos los cambios realizados en el código fuente de un proyecto (o cualquier tipo de archivo de texto), permitiendo volver a versiones anteriores, comparar cambios y colaborar en equipo sin perder información.

### ¿Que es github?

GitHub es una plataforma en la nube que funciona como una gran carpeta digital para guardar proyectos de programación. Permite almacenar código, llevar un registro de cada cambio realizado y colaborar con otros desarrolladores en equipo.

### ¿Que diferencia hay entre git y github?

Git es un programa que instalas en tu computadora para rastrear y gestionar los cambios en tu código. GitHub es una plataforma en la nube que te permite alojar esos proyectos para hacer respaldos y colaborar con otros desarrolladores.

## Preparando nuestro primer repositorio

### Elementos necesarios
Para trabajar en github y administrar repositorios dentro de esta página, son necesarios los siguientes elementos:

- Tener una cuenta en **[github](https://github.com)**.

- Tener **[git](https://git-scm.com/install/)** instalado en nuestro computador.

### Creando repositorio en github
Lo primero que hay que hacer es crear el repositorio en github, para ello tenemos que seguir los siguientes pasos

![Imagen de github 1](assets/Tutoria_1%204.png)

![Imagen de github 1](assets/Tutoria_1%205.png)

![Imagen de github 1](assets/Tutoria_1%206.png)

### Clonando nuestro repositorio en el pc
Una vez que ya tenemos el repositorio creado, hay que clonarlo dentro de nuestro computador, para ello tenemos que conseguir el link de ruta del repositorio:

![Imagen de github 1](assets/Tutoria_1%207.png)

![Imagen de github 1](assets/Tutoria_1%208.png)

Una vez se tiene el link del sitio (ejemplo: https://github.com/Mikel286/NeoEduca.git), lo siguiente es abrir nuestra terminal de comandos cmd dentro de la ruta donde queramos clonar el repositorio. Para clonarlo, hay que usar el siguiente comando dentro de la cmd:

```git
git clone https://github.com/Mikel286/NeoEduca.git
```

Con esto, tendremos nuestro repositorio dentro de la pc.

### Trabajando con el repositorio

Git es una herramienta que trabaja en el control de versiones, esto quiere decir que siempre debemos subir el material nuevo que se cree o edite, el cual, va acompañado de un mensaje de version. Para hacer esto, tenemos que seguir los siguientes pasos en la cmd:

- Preparar el contenido/cambios para ser subido: `git add .`

- Agregar un comentario de versión que acompañe a este: `git commit -m "Cambios en mi repositorio"`

- Subir los cambios a nuestro repositorio: `git push`

Todo lo anterior se resume a los siguiente en la cmd:

```git
git add .
git commit -m "Cambios en el repositorio"
git push
```

Para segurar que los cambios se han subido y no hay nada que actualizar, se usa el comando `git status`, que comprueba si existen cambios por subir.

## Ejercicios

Para probar todo lo aprendido en esta tutoria, se te invita a realizar los siguientes ejercicios.

### Ejercicio 1: Creando repositorio
En tu cuenta de github, crea un repositorio llamado **Tutoria** que puedas usar para subir tu progreso en las tutorias.

### Ejercicio 2: Subiendo contenido al repositorio
En tu repositorio **Tutoria**, sube todos los ejercicios de la tuturia 1 que has realizado en una carpeta que ponga **tutoria 1** y sube la información con el comentario de versión _**"Ejercicios de la tutoria 1"**_