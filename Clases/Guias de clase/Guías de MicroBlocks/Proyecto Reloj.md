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

### Librería `servo.ubl`

Para poder programar los servomotores, necesitaras cargar la librería `servo.ubl` de microblocks de la siguiente manera:

<p align="center">
  <img src="assets/Proyecto Reloj 1.png" width="800">
</p>

### Probando los servomotores

Para probar el funcionamiento de los servomotores, podemos usar el siguiente código de prueba:

<p align="center">
  <img src="assets/Proyecto Reloj 2.png" width="400">
</p>

## 🖥️ Código para empezar a probarlo

Una vez la conexión este bien realizada y el archivo `servo.ubl` se encuentra cargado en microblocks, en un archivo nuevo vamos a probar el siguiente código:

<p align="center">
  <img src="assets/Proyecto Reloj 3.png" width="400">
</p>

En este programa, podemos simular el movimiento de la aguja de un reloj.

## 🖥️ Ejercicios del proyecto

### Ejercicio 1: Definir los sentidos de giro

A traves del programa de prueba anterior, identifica con que angulo se realiza cada sentido de giro del motor. Si tienes dudas de por donde empezar, te dejo la siguiente ayuda:

- Sentido horario del motor : `completar`
- Sentido anti-horario del motor : `completar`

### Ejercicio 2: Tic Tac del reloj

Escribe un programa que te permita realizar el tic tac de un reloj. Si no sabes por donde empezar, te dejo el siguiente código como guía:

<p align="center">
  <img src="assets/Proyecto Reloj 4.png" width="400">
</p>

### Ejercicio 3: Implementación de Led

Incluye un led al proyecto y diseña un programa que te permita compaginar el encendido y apagado de un led con el tic tac del reloj. Si tienes dudas de por donde empezar, te dejo el siguiente código de ayuda:

<p align="center">
  <img src="assets/Proyecto Reloj 5.png" width="400">
</p>

### Ejercicio 4: Tic Tac con leds intercalados

Diseña un programa que permita al proyecto compaginar el encendido y apagado de dos leds con el tic tac del reloj. Cuando hablo de compaginar el encendido y apagado de dos leds, me refiero al fenomeno que ocurre en este codigo:

<p align="center">
  <img src="assets/Proyecto Reloj 6.png" width="400">
</p>

Si no sabes por donde empezar, te dejo el siguiente código como guía:

<p align="center">
  <img src="assets/Proyecto Reloj 7.png" width="400">
</p>

### Ejercicio 5: Tic Tac con leds y sonido intercalados
Diseña un programa que haga lo mismo que en el ejercicio 4 pero sumale un buzzer que emita un sonido con una frecuencia distinta para cada led. Si tienes dudas de por donde empezar, te paso el siguiente código para que te guies:

<p align="center">
  <img src="assets/Proyecto Reloj 8.png" width="400">
</p>