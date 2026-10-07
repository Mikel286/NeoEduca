from random import randint
from pet import Pet

# ---------------------------[FUNCIONES DEL MAIN]---------------------------

def main():

    print("Iniciando programa...")

    pet = Pet("Kuri")

    bucle = True
    while bucle:

        opcion = seleccionar_opcion()
        print(f"Opcion {opcion} ingresada...")

        if opcion == 0:
            bucle = False
        elif opcion == 1:
            print(pet)
        else:
            print("Opcion ingresada no valida...")
        reducir_status(pet, opcion)

# ---------------------------[FUNCIONES DEL MENU]---------------------------

def desplegar_opciones():

    text = """

    _____[MENU DE ACCIONES]_____
    
    [0] Salir
    [1] Revisar Status \n"""

    print(text)

def seleccionar_opcion():

    desplegar_opciones()
    try:
        opcion = int(input("Indique la accion que desea realizar: "))
        return opcion
    except:
        print("El valor ingresado no es un numero entero...")
        return -1

# ---------------------------[FUNCIONES DEL JUEGO]---------------------------

def reducir_status(pet, opcion):

    if opcion != 1 and opcion != 2: 
        pet.hambre += randint(1, 10)
    if opcion != 1 and opcion != 3:
        pet.felicidad -= randint(1, 10)

# ---------------------------[FUNCIONES DEL MAIN]---------------------------

if __name__ == "__main__":

    main()