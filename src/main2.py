


# https://www.youtube.com/watch?v=XVcgVg4sy7s


from machine import Pin, I2C
import ssd1306
import gfx

from time import sleep

# ESP32 Pin assignment 
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = I2C(-1, scl=Pin(5), sda=Pin(4))


def reset():
    oled.fill(0)

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.invert(False)

# from the examples
# def fast_hline(x, y, width, color):
#     display.fill_rectangle(x, y, width, 1, color)
# 
# def fast_vline(x, y, height, color):
#     display.fill_rectangle(x, y, 1, height, color)

    
graphics = gfx.GFX(oled_width, oled_width, oled.pixel) # reminder: oled.pixel = function that draws pixels.

def demo():

    oled.text('Hello main 2!', 0, 0)
    oled.show()
    sleep(2)
    
    
    
    reset()

while True:
    demo()