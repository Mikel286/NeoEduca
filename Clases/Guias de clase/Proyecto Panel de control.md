# Proyecto Panel de control

## 👋🏻 Presentación

Hola alumno del taller, esta es la guía para aprender con el proyecto **Panel de control** desarrollado por el profesor Mikel Ania.

Con el, aprenderas sobre la creación de panel de control por input que te ayudara a practicar los ciclos y el uso de inputs en tus programas. Ademas, aprenderas a dar instrucciones a tu proyecto sin depender de que la placa ejecute todo tu programa de golpe.

## 💻 Repasando conceptos

Para desenvolverte mejor en este proyecto, es necesario que recuerdes los siguientes conceptos de programación.

### Los `inputs`

En programación, input (entrada) se refiere a cualquier dato, señal o información que un programa recibe desde una fuente externa (usuario, archivo, sensor o red) para procesar. Es fundamental para la interactividad, convirtiendo programas estáticos en herramientas dinámicas que responden a comandos, clics, texto o voz.

Para entender esto a traves de la práctica, entrena con los siguientes códigos que te dejo:

- Con el primer codigo podras ver por pantalla la entrada de texto que le pases

```python

entrada = input("Entregame una entrada, la que sea: ")
print(entrada)

```
- Con el segundo código podrás ver como el programa diferencia entre numeros y letras:

```python

entrada = input("Entregame una entrada, la que sea: ")

if entrada.isdigit():
    print("Tu entrada es un texto...")
elif entrada.isnumeric():
    print("Tu entrada son numeros")
else:
    print("Tu entrada es una mezcla de ambos...")
```
### Los cilcos `while`

Un ciclo while (o bucle mientras) es una estructura de control que repite un bloque de código continuamente mientras una condición específica se evalúa como verdadera. Si la condición se vuelve falsa, el ciclo termina y el programa continúa su ejecución normal.

Para entender esto a traves de la práctica, entrena con el siguiente código que te dejo:

```python

from time import sleep

contador = 0
while contador < 100:
    print(contador)
    contador += 1
    sleep(0.3)
```

## 💻 Código para empezar a probarlo

Una vez que entendamos los conceptos de `input` y ciclos `while`, es momento de empezar a construir nuestro panel de control. En un archivo nuevo, vamos a probar el siguiente código:

```python

bucle = True

while bucle:

    entrada = input("Entregueme su entrada: ")

    if entrada == "Salir":
        bucle = False
    elif entrada == "Saludar":
        print("Hola, soy tu programa...")
    else:
        print("Comando no reconocido...")

```
## 💻 Desafios del proyecto

Ahora que ya lo tienes todo para empezar es hora de que pongamos a prueba tu propio desempeño con los siguientes ejercicios:

### Ejercicio 1: Controlar Leds

Tendras que hacer un programa que sea capaz de controlar el encendido y apagado de uno o mas leds a traves de la palabra. Si no sabes por donde empezar, no te preocupes porque porque te paso el siguiente código incompleto:

```python

bucle = True

led = Pin(2, Pin.OUT)

while bucle:
    entrada = input("Entregueme su entrada: ")

    if entrada == "Salir":
        bucle = False
    elif entrada == "Encender":
        # Tienes que colocar algo aqui 👋🏻
    elif entrada == "Apagar":
        # Tienes que colocar algo aqui
    else:
        print("El comando no se reconoce")
```

### Ejercicio 2: Controlar buzzer

Tendras que hacer un programa que sea capaz de controlar el encender por una determinada cantidad de tiempo un buzzer a una determinada frecuencia. Si no sabes por donde empezar, no te preocupes porque porque te paso el siguiente código incompleto:

```python

from tone import Buzzer

buzzer = Buzzer(5)

bucle = True

while bucle:
    entrada = input("Entregueme su entrada: ")

    if entrada == "Salir":
        bucle = False
    elif entrada == "Sonido":
        frecuencia = # Tienes que colocar algo aqui 👋🏻
        tiempo = # Tienes que colocar algo aqui 👋🏻
        buzzer.on(frecuencia)
        sleep(tiempo)
        buzzer.off()
    else:
        print("El comando no se reconoce")
```