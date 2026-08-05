# Electrónica Básica (Parte I)

## 👋🏻 Presentación

Hola alumno del taller, esta es la guía de **Electrónica Básica** desarrollado por el profesor Mikel. 

Con esta guía se estudiaran los fundamentos prácticos básicos de la electrónica en robótica. A traves de ejemplos básicos y desafíos prácticos, aprenderas sobre la construcción de circuitos simple tanto en ambientes simulados de Tinkercad como de manera presencial en el taller.

## ⚡ Reforzando Contenidos

### Fuente de alimentación
Una fuente de alimentación es el dispositivo encargado de suministrar energía eléctrica a un circuito o a un dispositivo electrónico. Su función es proporcionar el voltaje y la corriente necesarios para que los componentes electrónicos puedan funcionar correctamente.

Todos los circuitos necesitan una fuente de energía para funcionar. Esta energía puede provenir de una pila, una batería, un puerto USB, un adaptador de corriente o una fuente de laboratorio. Sin una fuente de alimentación, no existe flujo de corriente y el circuito no puede operar. Para los proyectos de esta guía, se usará como fuente de alimentación una batería de 9V.

### Resistencia
Una resistencia es un componente electrónico que limita el paso de la corriente eléctrica dentro de un circuito. Su función es controlar la cantidad de corriente que circula por un circuito, protegiendo otros componentes y permitiendo que funcionen de forma segura.

La resistencia actúa como un "freno" para la corriente eléctrica. Cuanto mayor es su valor, más difícil es el paso de la corriente. Por esta razón, se utiliza para evitar que componentes como los LED reciban demasiada corriente y se dañen. La resistencia se mide bajo la unidad de medida ohmnios $Ω$ y se conoce el valor de una resistencia a traves de sus colores.

<p align="center">
  <img src="assets/Electronica Basica 1.png" width="400">
</p>

### Diodo Emisor de Luz (LED)
Un LED es un componente electrónico que emite luz cuando la corriente eléctrica circula a través de él. Su función es indicar el estado de un circuito, proporcionar iluminación o mostrar información mediante diferentes colores.

A diferencia de una ampolleta tradicional, un LED solo permite que la corriente circule en un único sentido. Por ello, debe conectarse respetando su polaridad: el ánodo (+) se conecta al terminal positivo de la fuente de alimentación y el cátodo (-) al terminal negativo. Además, siempre debe utilizarse junto con una resistencia para evitar que reciba demasiada corriente y se dañe.

Como ya se ha mencioando, los componentes de un LED son los siguientes:

- **Ánodo (+)**: Terminal positivo, generalmente la pata más larga.

- **Cátodo (-)**: Terminal negativo, generalmente la pata más corta y ubicado junto al lado plano del encapsulado.

### Ley de Ohm
La Ley de Ohm es una regla fundamental de la electrónica que describe la relación entre el voltaje, la corriente y la resistencia en un circuito eléctrico. Permite calcular el valor de una de estas tres magnitudes cuando se conocen las otras dos, facilitando el diseño y análisis de circuitos. La formula e ilustración que explica mejor todo esto es la siguiente:

<p align="center">
  <img src="assets/Electronica Basica 2.png" width="1000">
</p>

La Ley de Ohm establece que la corriente eléctrica que circula por un circuito depende del voltaje aplicado y de la resistencia que se opone a su paso.

- **Voltaje (V)**: Es la fuerza que impulsa la corriente.
- **Corriente (I)**: Es el flujo de electricidad que circula por el circuito.
- **Resistencia (R)**: Es la oposición al paso de la corriente.

La relación entre estas tres magnitudes se expresa mediante la fórmula:

$$
I = \frac{V}{R}
$$

Como ejemplo si conectamos una fuente de 9 V a una resistencia de 300 Ω, la corriente que circulará será:

$$
I = \frac{9}{300} = 0.3A (30mA)
$$

### Conexión en Serie
Una conexión en serie es aquella en la que los componentes se conectan uno después de otro, formando un único camino para que circule la corriente eléctrica. Se utiliza cuando se desea que la misma corriente pase por todos los componentes del circuito.

En una conexión en serie, la corriente atraviesa todos los componentes en el mismo orden. Si uno de ellos deja de funcionar o se desconecta, el circuito se abre y la corriente deja de circular por todos los demás. Algunos ejemplos de este tipo de conexión son los siguientes:

- Guirnaldas de luces antiguas.
- Resistencias conectadas para obtener una resistencia total mayor.
- Baterías conectadas para aumentar el voltaje.

### Conexión en Paralelo
Una conexión en paralelo es aquella en la que los componentes se conectan entre los mismos terminales de la fuente de alimentación, formando varios caminos para que circule la corriente. Se utiliza cuando se desea que cada componente funcione de forma independiente y reciba el mismo voltaje.

En una conexión en paralelo, la corriente se divide entre las distintas ramas del circuito. Si uno de los componentes deja de funcionar, los demás continúan funcionando porque cada uno tiene su propio camino para recibir energía. Algunos ejemplos de este tipo de conexión son los siguientes:

- Instalación eléctrica de una casa.
- Varios LED conectados de forma independiente.
- Electrodomésticos conectados a la red eléctrica.

## ⚡Simulaciones de circuito

Para entender todo lo anterior, se trabajan los siguientes circuitos en el sistema de simulación de electrónica de Tinkercad.

### Conexión de un led

<p align="center">
  <img src="assets/Electronica Basica 3.png" width="1000">
</p>

### 1

<p align="center">
  <img src="assets/Electronica Basica 4.png" width="1000">
</p>
