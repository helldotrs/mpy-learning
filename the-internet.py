from machine import Pin
import time

while True:
    the_internet = Pin(12, Pin.OUT)
    the_internet.value(1)
    time.sleep(1)
    the_internet.value(0)
    time.sleep(1)
