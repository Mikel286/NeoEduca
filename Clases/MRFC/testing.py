from machine import Pin, SPI
from mfrc522 import MFRC522
import time

# Configurar SPI0
spi = SPI(0,
          baudrate=1000000,
          polarity=0,
          phase=0,
          sck=Pin(2),
          mosi=Pin(3),
          miso=Pin(4))

# Configurar RC522
rfid = MFRC522(spi=spi, cs=Pin(5), rst=Pin(0))  # RST puede ir a GP0 o 3.3V

print("Acerca una tarjeta RFID...")

while True:
    rfid.init()
    (stat, tag_type) = rfid.request(rfid.REQIDL)

    if stat == rfid.OK:
        print("Tarjeta detectada!")
        (stat, uid) = rfid.anticoll()
        if stat == rfid.OK:
            print("UID:", uid)
            print("-----")

    time.sleep(0.2)

