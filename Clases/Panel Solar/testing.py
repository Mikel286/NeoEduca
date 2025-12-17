from motores import servo360
from time import sleep

ejeH = servo360(15)
ejeV = servo360(14)

ejeH.girar(0)
sleep(0.05)
ejeH.detener()

sleep(1)

ejeV.girar(180)
sleep(0.05)
ejeV.detener()