# Aprendiendo Funciones

## 👋🏻 Presentación

Hola alumno del taller, esta es la guía para aprender con el proyecto **Auto** desarrollado por el profesor Mikel.

Con esta guía, aprenderas sobre el uso de las funciones en programación y practicaras la construccion de estas por medio de la herramienta `pytest` dentro de Thonny.

## 🖥️ Reforzando conceptos

### Que son las funciones

Las funciones en Python son bloques de código reutilizables diseñados para realizar tareas específicas. Permiten organizar el programa, evitar la repetición de código y facilitar su mantenimiento.

Para profundizar en funciones, tenemos que comprender los siguientes conceptos:

- **Argumentos y Parámetros** 

    - **Parámetros:** Son las variables que defines dentro de los paréntesis en la función (ej. nombre).
    
    - **Argumentos:** Son los valores reales que le envías a la función cuando la llamas (ej. "Ana")

-  **Retorno de valores (`return`)**: La palabra clave `return` indica qué valor devolverá la función al finalizar su ejecución. Si no se utiliza return, la función devolverá por defecto `None`.

### Probando las funciones

Para entender esto en la practica, veamos los siguientes codigos que usan las funciones para condensar el código en distintas acciones:

- Codigo para imprimir saludos

```python
def saludo(nombre):
    return f"Hola {nombre}, que tal estas..."

saludo("Alejandro")
saludo("Martina")
saludo("Roberto")
```

- Codigo para calcular números

```python
def calcular(valor_a, valor_b):
    resultado = valor_a + valor_b
    return resultado

print(f"El resultado del calculo es {calcular(12,45)}")
print(f"El resultado del calculo es {calcular(34,101)}")
print(f"El resultado del calculo es {calcular(56,2034)}")
```

- Codigo para validar colores
```python
def validar_color(color):
    color = color..strip().lower()
    if color == "rojo":
        return True
    else:
        return False

print(f"El color es rojo: {validar_color("Rojo")}")
print(f"El color es rojo: {validar_color("azul")}")
print(f"El color es rojo: {validar_color("Rosa")}")
```

### Que es `pytest`

Pytest es un popular framework (marco de trabajo) de código abierto para Python que permite escribir pruebas de software. Su función principal es automatizar la verificación de tu código para asegurar que funciona correctamente y prevenir errores antes de ponerlo en producción.

En esta guía, usaremos `pytest` para que cada alumno pueda corroborar desde su casa que las funciones que esta creando estan bien.

### Instalando `pytest` en Thonny

Para instalar `pytest` en Thonny, tienes que ir al **_tools/manage packages_**. Dentro de esta, deberas buscar la librería `pytest` e instalarla. Te dejo la siguiente imagen.

![Captura de Thonny](assets/Aprendiendo%20Funciones.png)

Con esto, esta todo listo para empezar a probar nuestra nueva herramienta.

### Probando `pytest`

Para esta herramienta, necesitamos un par de cosas de antemano:

1. Necesitamos guardar el archivo con un nombre dentro de la carpeta que vayamos a trabajar en Thonny. En esta guía, se usará el nombre `funciones.py`.

2. El código tendra dos tipos de funciones:

    - Funciones que el alumno tendra que construir o completar.

    - Funciones que test que empezarán con `test_` y que **EL ALUMNO NO TIENE QUE TOCAR**.

Sabiendo esto, supongamos que quiero verificar que una función `suma` esta bien construida. Para esto, usamos este código:

```python
def suma(valor_a, valor_b):
    resultado = valor_a + valor_b
    return resultado

def test_1():
    assert suma(2,2) == 4

def test_2():
    assert suma(7,5) == 12
```

Con este código guardado como `funciones.py`, lo cargaremos de una forma diferente de lo habitual en Thonny. Hay que abrir el menu **_tools/open system shell_** tal que nos saldra una nueva ventana. En esa ventana escribiremos `pytest funciones.py` de la siguiente manera:

![Imagen de consola para pytest](assets/Aprendiendo%20Funciones%202.png)

### Comportamiento de los test

Los test pueden comportarse de dos maneras distintas:

- Si la función esta bien hecha, el test dara luz 🟢 a todo 

- Si la función esta mal hecha, el test dara luz 🔴 a los test que no reciban la respuesta que esperán.

Veamos esto con un código donde se crean dos funciones, la primera sera `suma` y estará bien construida, la segunda será `resta` y estará mas construida ya que sumara en vez de restar números. Veamos el siguiente código:

```python
def suma(valor_a, valor_b):
    resultado = valor_a + valor_b
    return resultado

def resta(valor_a, valor_b):
    resultado = valor_a + valor_b
    return resultado

def test_1():
    assert suma(2,2) == 4

def test_2():
    assert resta(2,2) == 0
```

Con este código obtenemos lo siguiente:

![Imagen de error en test 2](assets/Aprendiendo%20Funciones%203.png)

Cuando pasa esto **NO HAY QUE ALARMARSE**, lo unico que nos esta diciendo es que el `test_2` ha fallado porque ha retornado un valor de 4 en vez de 0 que es el que se espera de la resta entre dos numeros. Calquier duda, copiad el texto que os imprima en pantalla y se lo pasais a chat gpt para que os explique las cosas locas que esten pasando.

## Ejercicios de Aprendizaje

Para prácticar el concepto de funciones, se dejan los siguientes ejercicios.

### Ejercicio 1: Implementando Operaciones

Construye funciones que te permitan hacer las operaciones matematicas básicas. Se deja el siguiente código incompleto para que trabajes:

```python
#------------[Funciones que hay que completar]------------

def suma():
    pass

def resta():
    pass

def multiplicacion():
    pass

def division():
    pass

#------------[Test que no hay que tocar]------------

def test_suma():
    set_parametros = [(2,2,4), (7,5,12), (-12, 8, -4)]
    for valor_a, valor_b, resultado in set_parametros:
        assert suma(valor_a, valor_b) == resultado

def test_resta():
    set_parametros = [(2,2,0), (7,5,2), (-12, 8, -20)]
    for valor_a, valor_b, resultado in set_parametros:
        assert resta(valor_a, valor_b) == resultado

def test_multiplicacion():
    set_parametros = [(2,2,4), (7,5,35), (-12, 8, -96)]
    for valor_a, valor_b, resultado in set_parametros:
        assert multiplicacion(valor_a, valor_b) == resultado

def test_division():
    set_parametros = [(2,2,1), (21,3,7), (36, 6, 6)]
    for valor_a, valor_b, resultado in set_parametros:
        assert division(valor_a, valor_b) == resultado
```

