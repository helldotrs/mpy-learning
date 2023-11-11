from machine import Pin
import time

pin00 = Pin(0, Pin.OUT)
pin01 = Pin(1, Pin.OUT)
pin02 = Pin(2, Pin.OUT)
pin03 = Pin(3, Pin.OUT)
pin04 = Pin(4, Pin.OUT)

pin14 = Pin(14, Pin.IN, Pin.PULL_DOWN)
pin15 = Pin(15, Pin.IN, Pin.PULL_DOWN)

leds = (pin00, pin01, pin02, pin03, pin04)

key_plus = pin15
key_minus = pin14

index = 0

while True:
    if key_plus.value() == 1:
        # Increment the index when key_plus is pressed
        index = (index + 1) % len(leds)
        time.sleep(0.2)  # Add a small delay to debounce the button

    if key_minus.value() == 1:
        # Decrement the index when key_minus is pressed
        index = (index - 1) % len(leds)
        time.sleep(0.2)  # Add a small delay to debounce the button

    # Turn off all LEDs
    for led in leds:
        led.off()

    # Turn on the LED at the current index
    leds[index].on()

    time.sleep(0.1)  # Adjust the delay based on your preference

