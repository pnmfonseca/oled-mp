# fastblink.py
import time
from machine import Pin
led = Pin(2, Pin.OUT)

for i in range(0, 6):
    led.value(i % 2 == 0)
    time.sleep_ms(80)
