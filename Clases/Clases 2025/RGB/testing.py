from rgb import RGB
from time import sleep

def fase_0():
    return False 

def fase_1():
    rgb.set_color(60000,0,0)
    sleep(1)
    rgb.set_color(0,0,0)
    sleep(1)
    
    return True 
    
def fase_2():
    print("Se ejecuto la orden" + "\n")
    rgb.set_color(60000,0,0)
    sleep(1)
    rgb.set_color(0,60000,0)
    sleep(1)
    rgb.set_color(0,0,60000)
    sleep(1)
    rgb.set_color(0,0,0)
    sleep(1)
    
    return True

def fase_3():
    for x in range(600):
        rgb.set_color(x * 100, 0, 0)
        print()
        sleep(0.01)
    
rgb = RGB(7,8,9)
bucle = True 
dic_fases = {"0": fase_0, "1":fase_1, "2":fase_2, "3": fase_3}

while bucle:
    
    orden = input("Indique la fase que quiere ejecutar [0-2]: ")
    if orden in dic_fases.keys():
        bucle = dic_fases[orden]()
    else:
        print("Esa fase no se reconoce, pruebe de nuevo" + "\n")