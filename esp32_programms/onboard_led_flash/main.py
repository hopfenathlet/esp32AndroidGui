from machine import Pin
from time import sleep_ms

led = Pin(2, Pin.OUT)

for _ in range(10):
    led.value(1)
    sleep_ms(500)
    led.value(0)
    sleep_ms(500)