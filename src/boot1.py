'''
Ref
- https://github.com/JettIsOnTheNet/Micropython-Examples-for-ESP32-Cheap-Yellow-Display/tree/main?tab=readme-ov-file
- https://github.com/rdagger/micropython-ili9341/tree/master
- https://shopee.co.th/ESP32-%E0%B8%9A%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%94%E0%B8%9E%E0%B8%B1%E0%B8%92%E0%B8%99%E0%B8%B2-2.8-%E0%B8%99%E0%B8%B4%E0%B9%89%E0%B8%A7-Touch-Display-%E0%B8%AA%E0%B9%8D%E0%B8%B2%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A-LVGL-WIFI-%E0%B8%9A%E0%B8%A5%E0%B8%B9%E0%B8%97%E0%B8%B9%E0%B8%98-240x320-%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%88%E0%B8%AD-LCD-TFT-%E0%B9%82%E0%B8%A1%E0%B8%94%E0%B8%B9%E0%B8%A5-i.110871174.27486883104
'''

# core
from machine import idle, Pin, SPI
from time import sleep

# community
from ili9341 import Display, color565

# custom
from CheapYellowDisplay import CYD
import util
import DisplayConfig
import touch
import color


SPRITE_DOT = bytearray(b'\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00')

class Demo(object):
  
    def touchscreen_press(self, x, y):
        '''Process touchscreen press events.'''
        print("Display touched.")
        
        # Y needs to be flipped
        y = (self.display.height - 1) - y
        # Display coordinates
        self.display.draw_text8x8(self.display.width // 2 - 32,
                                  self.display.height - 9,
                                  "{0:03d}, {1:03d}".format(x, y),
                                  self.CYAN)
        # Draw dot
        self.display.draw_sprite(self.dot, x - 2, y - 2, 5, 5)

def drawSprite(display,x,y):
    display.draw_sprite(SPRITE_DOT, x - 2, y - 2, 5, 5)
    
def testScreen(display):
    display.clear(color.PURPLE)
    display.draw_text8x8(display.width // 2 - 32,
        int(display.height / 2),
        "TOUCH ME",
        color.WHITE,
        background=color.BLACK)
    sleep(2)
    display.draw_image('images/RaspberryPiWB128x128.raw', 0, 0, 128, 128)
    display.draw_image('images/MicroPython128x128.raw', 129, 0, 128, 128)
    display.draw_text8x8(display.width // 2 - 32,
        int(display.height / 2) + 20,
        str(DisplayConfig.getLdr()),
        color.BLACK,
        background=color.PURPLE)
    
    # ldr does not work
#    for idx in range(10):
#        print (cyd.getLdr())
#        sleep (1)

def onTouch(x, y):
    z = y
    y = x
    x = z
    print (f'Touched: x = {x}, y = {y}')
    #drawSprite(x,y)
    



print ("Running")
try:
    cyd = CYD()
    cyd.setLed(True, False, True)
    cyd.setBacklight()

    while True:
        idle()
except KeyboardInterrupt:
    print("\nCtrl-C pressed.  Cleaning up and exiting...")
finally:
    cyd.setLed(False, False, False)
    cyd.setDisplay(False)

#test()
