from serial import Serial
import time

puerto = 'COM5'   # cambia si es necesario
baudrate = 115200

ser = Serial(puerto, baudrate, timeout=1)
time.sleep(2)  # Esperar a que se establezca la conexión

print("Conectado al Pico. Escribe '1' para encender o '2' para apagar el LED. Ctrl+C para salir.")

while True:
    cmd = input("Comando ([0-2]]): ").strip()
    if cmd in ["2", "1", "0"]:
        ser.write((cmd + "\n").encode())
        print(f"Enviado: {cmd}")
        respuesta = ser.readline().decode().strip()
        if respuesta:
            print("Pico:", respuesta)
    else:
        print("Por favor ingresa solo '2', '1', '0'")