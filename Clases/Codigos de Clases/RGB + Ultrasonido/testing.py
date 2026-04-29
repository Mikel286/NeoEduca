from rgb import RGB
from sensores import Ultrasonico
from time import sleep

rgb = RGB(7,8,9)
rgb.def_ultra()

while True:
    
    rgb.ultra_rgb()
    sleep(0.1)
    print("Midiendo...")