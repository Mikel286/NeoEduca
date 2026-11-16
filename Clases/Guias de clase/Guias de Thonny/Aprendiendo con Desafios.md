# Aprendiendo con Dasafios

## 👋🏻 Presentación

Hola alumno del taller, esta es la guía para reforzar todo el contenido aprendiendo hasta ahora con los talleres.

Con esta guía, pondras a prueba desde otro angulo los distintos contenidos vistos en cada taller a traves de retos que pediran el uso de distintos contenidos.

## Desafios 1: Tablero (Ejercicio de memoria)

### Contenidos del desafio

Este desafio requiere el uso de los siguientes conceptos para ser resuelto:

- Respecto a componentes de robótica

    - Servomotores

    - Leds

    - Buzzer

- Respecto a contenidos de programación

    - Funciones (Opcional)

    - Ciclos (Opcional)

### Descripción y reglas del desafio

En este desafio tendras que hacer que tu robot recorra de un punto A a un punto B a traves de memoria. Para ello, tendras que construir un código que le de las instrucciones para cumplir el dasafio por su cuenta a traves de actuadores.

Las reglas del desafio son las siguientes:

1. No se puede usar ningun tipo de sensor.

2. Los movimientos deben ser en linea recta.

Las pistas de este desafio son las siguientes tres:

- En esta primera pista solo se da el uso de servomotores. Tienes que unicamente ir de un punto a otro y luego a la inversa a traves de movimientos completamente rectos.

    ![Imagen de desafio](assets/Proyecto%20Tablero%201.png)

    Para este desafio, se recomienda empezar con códigos como el siguiente, donde hacemos uso de los servomotores a través de funciones:

    ```python
    from motores import carro
    from time import sleep

    auto = carro(15, 14)
    auto.setvelocidad(180,0)

    def accion(movimiento, tiempo):
        
        if movimiento == 1:
            auto.moveadelante()
        elif movimiento == 2:
            auto.moveizquierda()
        elif movimiento == 3:
            auto.movederacha()
        elif movimiento == 4:
            auto.moveatras()
        else:
            print("El movimiento ingresado es invalido...")

        sleep(tiempo)
        auto.movedetener()

    accion(1, 0.7)
    accion(3, 0.5)
    ``` 

- En esta segunda pista, deberas agregar el uso de leds durante el desplazamiento. Tendras que encender y apagar el led que se te indique en cada punto de la pista.

    ![Imagen de desafio](assets/Proyecto%20Tablero%202.png)

    Para este desafio, se recomienda empezar con códigos como el siguiente, donde hacemos uso de los servomotores y led a través de funciones:

    ```python
    from motores import carro
    from machine import Pin
    from time import sleep

    led_izq = Pin(2, Pin.OUT)
    led_cen = Pin(3, Pin.OUT)
    led_der = Pin(4, Pin.OUT)

    auto = carro(15, 14)
    auto.setvelocidad(180,0)

    def comportamiento_motores(movimiento, tiempo):

        if movimiento == 1:
            auto.moveadelante()
        elif movimiento == 2:
            auto.moveizquierda()
        elif movimiento == 3:
            auto.movederacha()
        elif movimiento == 4:
            auto.moveatras()
        else:
            print("El movimiento ingresado es invalido...")

        sleep(tiempo)
        auto.movedetener()

    def comportamiento_leds(estado_izq, estado_cen, estado_der):

        led_izq.value(estado_izq)
        led_cen.value(estado_cen)
        led_der.value(estado_der)
        sleep(1)
        led_izq.off()
        led_cen.off()
        led_der.off()

    def accion(movimiento, estado_izq, estado_cen, estado_der, tiempo):

        comportamiento_motores(movimiento, tiempo)
        comportamiento_leds(estado_izq, estado_cen, estado_der)
        

    accion(1, 1, 0, 0, 0.7)
    accion(3, 0, 1, 1, 0.5)
    ``` 

- En esta tercera pista, deberas agregar el uso de buzzer durante el desplazamiento. Tendras que emitir sonido con una frecuencia distinta cada vez que se te indique en cada punto de la pista.

    ![Imagen de desafio](assets/Proyecto%20Tablero%203.png)

    La resolución de este ejercicio es similar a los dos anteriores, tendras que agregar una nueva acción (puede ser a traves de una función) que permita la emisión de sonidos a traves del buzzer.