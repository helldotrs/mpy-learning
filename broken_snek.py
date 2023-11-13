from machine import Pin
import time

pins = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT), 
#ground
    Pin(2, Pin.OUT), #a
    Pin(3, Pin.OUT), #b
    Pin(4, Pin.OUT), #dot
    Pin(5, Pin.OUT), #c
#ground
    Pin(6, Pin.OUT), #
    Pin(7, Pin.OUT), #
    Pin(8, Pin.OUT), #
    Pin(9, Pin.OUT), #
#ground
    Pin(10, Pin.OUT), #
    Pin(11, Pin.OUT), #
    Pin(12, Pin.OUT), #
    Pin(13, Pin.OUT), #
#ground
    Pin(14, Pin.OUT),
    Pin(15, Pin.OUT),
#end of side one
]

broken_snek = [
    3,
    5,
    6,
    7,
    8,
]

num_leds = len(broken_snek)

while True:
    # Move right
    for i in range(1, num_leds):
        pins[broken_snek[i]].value(0)
        pins[broken_snek[i - 1]].value(1)
        time.sleep(0.1)

    # Move left
    for i in range(num_leds - 2, -1, -1):
        pins[broken_snek[i]].value(0)
        pins[broken_snek[i + 1]].value(1)
        time.sleep(0.1)


#pin15 = Pin(15, Pin.IN, Pin.PULL_DOWN) #button
