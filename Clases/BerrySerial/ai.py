from serial import Serial
import time
from transformers import pipeline

puerto = 'COM3'   # cambia si es necesario
baudrate = 115200

ser = Serial(puerto, baudrate, timeout=1)
time.sleep(2)  # Esperar a que se establezca la conexión

# Carga un modelo de análisis de sentimiento
clasificador = pipeline("sentiment-analysis")

while True:
    texto = input("Coloque el texto que desea analizar: ")
    resultado = clasificador(texto)
    cmd = resultado[0]['label']
    print(cmd + "\n")

    ser.write((cmd + "\n").encode())
    print(f"Enviado: {cmd}")
    respuesta = ser.readline().decode().strip()
    if respuesta:
        print("Pico:", respuesta)

