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

## 💻 Librería `tone.ubl`

Para este proyecto es necesario que importes en microblocks la librería `tone.ubl` de la siguiente forma:

<img src="assets/Proyecto Radio 1.png" width="800">

Cuando hagas esto, aparecerá una nueva sección de bloques que se usarán en este proyecto.

## 💻 Código para empezar a probarlo

Una vez que se haya importado la librería `tone.ubl`, probaremos los leds y el buzzer con los siguientes bloques:

<p align="center">
  <img src="assets/Proyecto Radio 2.png" width="400">
</p>

## 💻 Desafios del proyecto

Ahora que ya lo tienes todo para empezar es hora de que pongamos a prueba tu propio desempeño con los siguientes ejercicios:

### Ejercicio 1: Emitiendo distintos tonos
Tendras que hacer un programa que emita sonidos con frecuencia distinta usando el zumbador. Si no sabes por donde empezar, no te preocupes porque te paso el siguiente código incompleto:

<p align="center">
  <img src="assets/Proyecto Radio 3.png" width="300">
</p>

Para este ejercicio tendras que usar la siguiente tabla de frecuencias:

<p align="center">
  <img src="assets/Proyecto Radio Tabla.png" width="200">
</p>

### Ejercicio 2: Juntando tonos y frecuencias
Tendras que hacer un código donde puedas emitir tres tonos distintos con el buzzer y que estos vayan acompañados con una secuencia de led particular para cada sonido. Si no sabes por donde empezar, no te preocupes porque te paso el siguiente código incompleto:

<p align="center">
  <img src="assets/Proyecto Radio 4.png" width="400">
</p>

### Ejercicio 3: Emitiendo una frecuencia y encendiendo un led al azar

Tendras que hacer un codigo que cada vez que se ejecute, haga las siguientes dos cosas:

- Encienda y apague un led al azar

- Emita un sonido a una frecuencia al azar

Te dejo el siguiente código para que te guies si estas perdido:

<p align="center">
  <img src="assets/Proyecto Radio 5.png" width="400">
</p>

### Ejercicio 4: Emitiendo una canción

Construye un código que te permita tocar una canción en 8 bits a traves del buzzer. Si no sabes por donde empezar, te dejo la siguiente canción y un código que te pueden ayudar:

#### Canción de Super Mario

La partitura de la canción es la siguiente:

- DO5  250ms - SOL5 250ms - LA5  250ms -SOL5 250ms

- MI5  250ms - SOL5 250ms - DO6  500ms

- LA5  250ms - SOL5 250ms - MI5  250ms - RE5  250ms

- DO5  500ms - SOL4 500ms

La frecuencia de las notas musicales es la siguiente

