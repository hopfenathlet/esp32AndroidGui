from machine import Pin
from time import sleep_ms

led = Pin(15, Pin.OUT)

button = Pin(13, Pin.IN, Pin.PULL_DOWN)


while True:
    if button.value() == 1:
        led.value(1)
    else:
        led.value(0) 
    sleep_ms(100)