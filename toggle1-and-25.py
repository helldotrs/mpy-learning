from machine import Pin
import utime 
pin25 = Pin(25, Pin.OUT)
pin01 = Pin(1, Pin.OUT)

def toggle_sleep(x):
    x.toggle()
    utime.sleep(1)


#main
while True:
    toggle_sleep(pin25)
    toggle_sleep(pin01)

