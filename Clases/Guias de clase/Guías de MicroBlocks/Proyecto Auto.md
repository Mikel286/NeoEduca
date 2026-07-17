# Proyecto Coche

## 👋🏻 Presentación

Hola alumno del taller, esta es la guía para aprender con el proyecto **Auto** desarrollado por el taller NeoEduca.

Con el, aprenderas sobre la conexión y la programación de motores junto con el desarrollo de un auto autonomo a traves del IDE Thonny con el lenguaje de programación Python.

## 💡 Conociendo los componentes

### Que es un servomotor

Un servomotor es un motor especializado que permite un control preciso de posición, velocidad y torque en aplicaciones robóticas e industriales. Funciona en un sistema de lazo cerrado con retroalimentación (encoder o potenciómetro) para ajustar su posición exacta, siendo clave en automatización, brazos robóticos y CNC.

### Conexiones del servomotor

Para nuestra conexión en el microcontrolador, es importante conocer los siguientes aspectos:

- **🟠 Signal (PIN)**

- **🟤 GND (Tierra)**

- **🔴 VCC (Voltaje)**

Junto a lo anterior, es importante recordar que dentro de la placa los motores se conectan en los pines GP13, GP14 y GP15. Ademas, es **muy importante que conectes el portapilas como fuente de alimentación externa** para evitar el daño de los componentes.

### Librería `servo.ubl`

Para poder programar los servomotores, necesitaras cargar la librería `servo.ubl` de microblocks de la siguiente manera:

<p align="center">
  <img src="assets/Proyecto Auto 1.png" width="800">
</p>

### Probando los servomotores

Para el correcto funcionamiento de los servomotores, debemos seguir el siguiente conjunto de pasos con tal de ver que ambos motores funcionan adecuadamente:

#### Funcionamiento de motores

Para ver que los motores funcionan correctamente usamos los bloques de `servo.ubl` que nos permite probar el funcionamiento de cada motor por separado:

<p align="center">
  <img src="assets/Proyecto Auto 2.png" width="400">
</p>

#### Calibración de los motores

Una vez se ha comprobado el movimiento de los motores, es importante pasar a calibrar los motores. Para esto, usamos la clase `carro` donde por medio del siguiente código logramos la calibración:

<p align="center">
  <img src="assets/Proyecto Auto 3.png" width="400">
</p>

Con el código anterior, podemos ir ingresando distintos angulos y comprobar con que par de angulos es capaz nuestro auto de moverse adelante.

#### Definiendo velocidad y movimientos del auto

Una vez definidos los angulos que nos servirán para el auto, hay que definir la velocidad a la que se moverá y probar los movimiento basicos del auto:

<p align="center">
  <img src="assets/Proyecto Auto 4.png" width="400">
</p>

Para entender mejor esto, vea el siguiente código:

<p align="center">
  <img src="assets/Proyecto Auto 5.png" width="400">
</p>

## 🖥️ Ejercicios del proyecto

### Ejercicio 1: Movimiento en L

Construye un programa que te permita hacer un movimiento en forma de L con el auto. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda para guiarte:

<p align="center">
  <img src="assets/Proyecto Auto 6.png" width="400">
</p>


### Ejercicio 2: Giro sobre su propio eje
Construye un programa que te permita al auto girar sobre su propio eje. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda para guiarte:

<p align="center">
  <img src="assets/Proyecto Auto 7.png" width="400">
</p>

### Ejercicio 3: Completando un cuadrado

Construye un programa que te permita recorrer un cuadrado completo con el auto usando el ciclo for. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda para guiarte:

<p align="center">
  <img src="assets/Proyecto Auto 8.png" width="400">
</p>


### Ejercicio 4: Rodeando un obstaculo

Construye un programa que te permita rodera un obstaculo en el suelo sin tocarlo. Te dejo la siguiente ilustración de referencia:

<p align="center">
  <img src="assets/Proyecto Auto 9.png" width="800">
</p>

### Ejercicio 5: Completando una pista

Construye un programa que te permita recorrer una pista completa con el auto. Si no tienes una pista a mano, te dejo el siguiente modelo para que te guies:

<p align="center">
  <img src="assets/Proyecto Auto 10.png" width="800">
</p>