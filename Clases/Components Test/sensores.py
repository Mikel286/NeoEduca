from machine import Pin, time_pulse_us
from time import sleep_ms, sleep_us, ticks_diff, ticks_us
class Ldr:
    def __init__(self, pin):
        self.pin = pin
        
    
    def RCtime(self):    
        sensor = Pin(self.pin, Pin.OUT)
        sensor.on() 
        sleep_ms(1)
        
        sensor = Pin(self.pin, Pin.IN) 
        sensor.off()
        start_time = ticks_us()
        while sensor.value():
            pass
        end_time = ticks_us()

        return ticks_diff(end_time, start_time)
    

    def medir(self):
        return self.RCtime()

class Qti:
    def __init__(self, pin):
        self.pin = pin
        
    
    def RCtime(self):    
        sensor = Pin(self.pin, Pin.OUT)
        sensor.on() 
        sleep_ms(1)
        
        sensor = Pin(self.pin, Pin.IN) 
        sensor.off()
        start_time = ticks_us()
        while sensor.value():
            pass
        end_time = ticks_us()

        return ticks_diff(end_time, start_time)
    

    def medir(self):
        return self.RCtime()

class Ultrasonico:   
    def __init__(self):
        self.trig_pin = Pin(18, Pin.OUT) 
        self.echo_pin = Pin(19, Pin.IN)
        self.SOUND_SPEED=340
        
    def medir(self):
        self.trig_pin.value(0)
        sleep_us(5)
        self.trig_pin.value(1)
        sleep_us(10)
        self.trig_pin.value(0)
        ultrason_duration = time_pulse_us(self.echo_pin, 1, 30000)
        distance_cm = self.SOUND_SPEED * ultrason_duration / 20000
        return distance_cm
