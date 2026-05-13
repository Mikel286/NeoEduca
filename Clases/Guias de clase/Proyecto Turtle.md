# Proyecto Turtle

## 👋🏻 Presentación

Hola alumno del taller, esta es la guía para aprender con la librería **Tortuga** a traves de esta guía desarrollada por el profesor Mikel Ania.

Con esta, aprenderas sobre el uso basico de una librería de intefaz gráfica y el uso de metodos para utilizar el objeto `Turtle()` de la librería.

## 💡 Conociendo la librería `turtle`

### Que es la librería `turtle`

La librería turtle en Python es una herramienta integrada diseñada para principiantes, que permite crear gráficos, formas y dibujos vectoriales mediante comandos sencillos en una ventana virtual. Funciona como una "tortuga" o cursor que se mueve por la pantalla, dejando un rastro para dibujar.

Para empezar a trabajar con esta librería, debemos importar la librería y construir el objeto de esta con el siguiente código:

```python
import turtle as T

tortuga = T.Turtle()

def main():
    T.done()

if __name__ == "__main__":
    main()
```

### Comandos básicos de la librería

Para empezar a trabajar con esta librería tenemos que saber que esta librería se divide en dos tipos de métodos:

- **Métodos de configuración**: Son los métodos que controlan las propiedades del objeto `Turtle()`.

- **Métodos de acción**: Son los metodos que se encargan del movimiento del objeto `Turtle()` dentro de la interfaz gráfica.

En lo que respecta a los comandos de configuración, debemos conocer los siguientes métodos al momento de empezar a trabajar con la librería:

- `.pendown()` : Bajar el pincel y empezar a pintar cuando se mueve.

- `.penup()` : Subir el pincel y dejar de pintar cuando se mueve.

- `.pensize(px)` : Cambiar el tamaño (en pixeles) del pincel.

- `.color(r,g,b)` : Cambiar el color (formato rgb) del pincel.

- `.begin_fill()` y `.end_fill()` : Rellenar un dibujo con el color configurado.

En lo que respecta a los comandos de acción, debemos conocer los siguientes métodos al momento de empezar a trabajar con la librería:

- `.forward(px)` : Movimiento (en pixeles) hacia delante del pincel.

- `.backward(px)` : Movimiento (en pixeles) hacia atras del pincel.

- `.right(grades)` : Giro (en grados) del pincel hacia la derecha.

- `.left(grades)` : Giro (en grados) del pincel hacia la izquierda.

### Probando la librería `turtle`

Para probar la librería `turtle` podemos usar el siguiente codígo que aplicará los conceptos basico de la librería:

```python
import turtle as T

tortuga = T.Turtle()

def init_config():
    tortuga.pensize(4)
    tortuga.color("#000000")

def main():

    tortuga.forward(90)
    tortuga.right(90)
    tortuga.forward(90)

    T.done()

if __name__ == "__main__":

    init_config()
    main()
```

## 💻 Ejercicios del proyecto

### Ejercicio 1: El cuadrado

Diseña un programa que te permita dibujar un cuadrado perfecto. Si no sabes por donde empezar, te dejo el siguiente código para que te guies:

```python
import turtle as T

tortuga = T.Turtle()

def init_config():
    tortuga.pensize(4)
    tortuga.color("#000000")

def main():

    # Debes escribir el código aquí 👋🏻

    T.done()

if __name__ == "__main__":

    init_config()
    main()
```

### Ejercicio 2: El triangulo

Diseña un programa que te permita dibujar un triangulo. Si no sabes por donde empezar, te dejo el siguiente código para que te guies:

```python
import turtle as T

tortuga = T.Turtle()

def init_config():
    tortuga.pensize(4)
    tortuga.color("#000000")

def main():

    # Debes escribir el código aquí 👋🏻

    T.done()

if __name__ == "__main__":

    init_config()
    main()
```

### Ejericio 3: El circulo

Diseña un programa que te permita dibujar un circulo perfecto. Si no sabes por donde empezar, te dejo el siguiente código para que te guies:

```python
import turtle as T

tortuga = T.Turtle()

def init_config():
    tortuga.pensize(4)
    tortuga.color("#000000")

def main():

    tortuga.penup()
    tortuga.forward(90)
    tortuga.right(90)

    tortuga.pendown()

    n = # Coloca un numero entero aquí

    for _ in range(n):
        # Coloca código aquí 👋🏻

    T.done()


if __name__ == "__main__":

    init_config()
    main()
```

### Ejercicio 4: Figuras pintadas

Diseña un programa que te permita dibujar y pintar por dentro varias figuras (ractangulo, diamante, circulo) en la interfaz. Si no sabes por donde empezar, te dejo el siguiente código para que te guies:

```python
import turtle as T

tortuga = T.Turtle()

def init_config():
    tortuga.pensize(4)
    tortuga.color("#000000")

def main():

    # Debes escribir el código del rectangulo aquí 👋🏻

    # Debes escribir el código del diamante aquí 👋🏻

    # Debes escribir el código del circulo aquí 👋🏻

    T.done()

if __name__ == "__main__":

    init_config()
    main()
```

### Ejercicio 5: Desafía Emoji

Diseña un programa que te permita dibujar y pintar un emoji a tu elección en la interfaz.

![Imagen de emojis](assets/Proyecto%20Turtle%201.jpg)