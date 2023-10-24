from machine import Pin
from time import sleep_ms

onBoardLed = Pin(15 ,Pin.OUT)

for _ in range(10):
    onBoardLed.value(1)
    sleep_ms(100)
    onBoardLed.value(0)
    sleep_ms(100)