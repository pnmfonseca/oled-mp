


# https://www.youtube.com/watch?v=XVcgVg4sy7s


from machine import Pin, I2C
import ssd1306
import gfx

from time import sleep, sleep_us, sleep_ms

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

    # graphics.line(0,0,20,20, 1)
    # oled.show()
    # sleep(1)
    # reset()

    max_diam = 90
    step = 10
    for diam in range (0, max_diam, step):
        graphics.circle(oled_width//2, oled_height//2, diam, 1)
        oled.show()
    # sleep_us(10)
    for diam in range (0, max_diam, step):
        graphics.circle(oled_width//2, oled_height//2, diam, 0)
        oled.show()
    sleep_ms(150)

    reset()

    for l in range(10):
        oled.text('Aramitos {}!'.format(l), 0, l*8)
    oled.show()
    sleep_ms(150)
    reset()

    oled.text('By pixels', 0, 0)
    for p in range(oled_width):
        for h in range(0, oled_height, 4):
            oled.pixel(p, h, 1)            
    oled.show()
    sleep_ms(150)
    reset()

    oled.rect(0, 0, oled_width, oled_height, 1)

    oled.text('By gfx line', 0, 0)
    for p in range(0, oled_width, 10):
        graphics.line(0, 0, p, oled_height, 1)
        oled.show()

    for p in range(oled_width, 0, -10):
        graphics.line(oled_width, 0, p, oled_height, 1)
        oled.show()

    sleep_ms(1000)
    reset()

while True:
    demo()