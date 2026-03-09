from serial import Serial
import time

puerto = 'COM3'   # cambia si es necesario
baudrate = 115200

ser = Serial(puerto, baudrate, timeout=1)
time.sleep(2)  # Esperar a que se establezca la conexión

print("Conectado al Pico. Escribe '1' para encender o '0' para apagar el LED. Ctrl+C para salir.")

while True:
    cmd = input("Comando (1/0): ").strip()
    if cmd in ["1", "0"]:
        ser.write((cmd + "\n").encode())
        print(f"Enviado: {cmd}")
        respuesta = ser.readline().decode().strip()
        if respuesta:
            print("Pico:", respuesta)
    else:
        print("Por favor ingresa solo '1' o '0'")