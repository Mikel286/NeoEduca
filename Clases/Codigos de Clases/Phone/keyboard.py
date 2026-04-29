
from machine import Pin
from time import sleep
from random import randint

from tone import Buzzer

class Keyboard():
    
    def __init__(self):
        
        self.rows = [Pin(i, Pin.OUT) for i in [9,8,7,6]]
        self.cols = [Pin(i, Pin.IN, Pin.PULL_UP) for i in [13,12,11,10]]

        self.keys = [
            ["1","2","3","A"],
            ["4","5","6","B"],
            ["7","8","9","C"],
            ["*","0","#","D"]]

    def scan(self):
        for i, row in enumerate(self.rows):
            row.low()
            for j, col in enumerate(self.cols):
                if col.value() == 0:
                    return self.keys[i][j]
            row.high()
        return None
    
class Phone():
    
    def __init__(self):
        
        self.buzzer = Buzzer(5)
        
        self.rows = [Pin(i, Pin.OUT) for i in [9,8,7,6]]
        self.cols = [Pin(i, Pin.IN, Pin.PULL_UP) for i in [13,12,11,10]]

        self.keys = [
            ["1","2","3","A"],
            ["4","5","6","B"],
            ["7","8","9","C"],
            ["*","0","#","D"]]

    def scan(self):
        for i, row in enumerate(self.rows):
            row.low()
            for j, col in enumerate(self.cols):
                if col.value() == 0:
                    self.buzzer.on(randint(440, 480))
                    sleep(0.2)
                    self.buzzer.off()
                    return self.keys[i][j]
            row.high()
        return None
