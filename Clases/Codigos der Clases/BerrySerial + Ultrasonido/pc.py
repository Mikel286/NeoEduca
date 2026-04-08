from threading import Thread
from serial import Serial
from time import sleep

def leer_serial():
    puerto = 'COM5'   # cambia si es necesario
    baudrate = 115200

    try:
        ser = Serial(puerto, baudrate, timeout=1)
        sleep(2)  # Esperar a que se establezca la conexión
        print("Conectado al Pico. Escribe '1' para encender o '2' para apagar el LED. Ctrl+C para salir.")

        global serial_info
        while True:
            serial_info = ser.readline().decode().strip()
            
    except Exception as e:
        print("Error al conectar con el Pico:", e)

def salir():
    global bucle
    bucle = False

def conocer_medicion():
    print(f"Último valor de medición: {serial_info}")

def determinar_cercania():
    global serial_info
    try:
        valor = float(serial_info)
        if valor < 10:
            print("Está cerca")
        else:
            print("Está lejos")
    except ValueError:
        print("No se pudo determinar la cercanía. Valor no numérico.")

acciones = {
    '1': conocer_medicion,
    '2': determinar_cercania,
    '3': salir}

if __name__ == "__main__":

    serial_info = "No hay datos"
    serial_thread = Thread(target=leer_serial, daemon=True)
    serial_thread.start()

    text = """Ingrese una de las siguientes opciones
    
    [1] Leer ultimo valor de medición
    [2] Determinar si esta cerca o lejos
    [3] Salir
    
    Que opción desea elegir:"""

    bucle = True
    while bucle:
        accion = input(text + "\n")
        if accion in acciones.keys():
            acciones[accion]()
        else:
            print("Opción no válida. Intente de nuevo.")

        
