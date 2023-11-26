from machine import Pin, ADC
import utime
import pyautogui

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    xStatus = "middle"
    yStatus = "middle"
    buttonStatus = "not pressed"

    if xValue <= 600:
        xStatus = "left"
        pyautogui.moveRel(-10, 0)  # Adjust the values based on your preferences
    elif xValue >= 60000:
        xStatus = "right"
        pyautogui.moveRel(10, 0)  # Adjust the values based on your preferences

    if yValue <= 600:
        yStatus = "up"
        pyautogui.moveRel(0, -10)  # Adjust the values based on your preferences
    elif yValue >= 60000:
        yStatus = "down"
        pyautogui.moveRel(0, 10)  # Adjust the values based on your preferences

    if buttonValue == 0:
        buttonStatus = "pressed"
        # Add additional actions for when the button is pressed

    print("X: " + xStatus + ", Y: " + yStatus + " -- button " + buttonStatus)
    utime.sleep(0.1)
