#broke the 7 seg, so need to find the other/order new
from machine import Pin
import time
"""
pin00 = Pin(0, Pin.OUT)
pin01 = Pin(1, Pin.OUT) #non

pin02 = Pin(2, Pin.OUT) #a
pin03 = Pin(3, Pin.OUT) #b
pin04 = Pin(4, Pin.OUT) #c
pin05 = Pin(5, Pin.OUT) #d

pin06 = Pin(6, Pin.OUT) #e
pin07 = Pin(7, Pin.OUT) #non
pin08 = Pin(8, Pin.OUT) #f
pin09 = Pin(9, Pin.OUT) #dot
pin10 = Pin(10, Pin.OUT) #non
pin11 = Pin(11, Pin.OUT) #non
pin15 = Pin(15, Pin.OUT)
pin16 = Pin(16, Pin.OUT)
"""
pins = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT), #non

    Pin(2, Pin.OUT), #a
    Pin(3, Pin.OUT), #b
    Pin(4, Pin.OUT), #c
    Pin(5, Pin.OUT), #d

    Pin(6, Pin.OUT), #
    Pin(7, Pin.OUT), #
    Pin(8, Pin.OUT), #
    Pin(9, Pin.OUT), #
    
    Pin(10, Pin.OUT), #
    Pin(11, Pin.OUT), #
    Pin(12, Pin.OUT), #
    Pin(13, Pin.OUT), #
    
    Pin(14, Pin.OUT),
    Pin(15, Pin.OUT),
    ]

lowest	= 1
highest	= 9

pins[15].value(0)

while True:
    for i in range(lowest, highest+1):
        pins[i].value(0)
        pins[i-1].value(1)
        
        """if i > lowest:
            pins[i - 1].value(1)
        else:
            pins[highest].value(1)"""
        time.sleep(1)


"""
pin00.toggle()
pin01.toggle()

pin02.toggle()
pin03.toggle()

pin04.toggle()
pin05.toggle()

pin06.toggle()
pin07.toggle()

pin08.toggle()
pin09.toggle()

pin10.toggle()
pin11.toggle()
pin15.toggle()
pin16.toggle()


#pin0 = Pin(, Pin.OUT)

"""
"""
pin15 = Pin(15, Pin.IN, Pin.PULL_DOWN)
"""
