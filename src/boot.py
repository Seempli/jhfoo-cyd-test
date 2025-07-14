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
import util
import cyd
import touch

BLACK = color565(0,0,0)
CYAN = color565(0, 255, 255)
PURPLE = color565(255, 0, 255)
WHITE = color565(255, 255, 255)

SPRITE_DOT = bytearray(b'\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00')

class Demo(object):
    '''Touchscreen simple demo.'''

    def __init__(self, display, spi2):
        '''Initialize box.

        Args:
            display (ILI9341): display object
            spi2 (SPI): SPI bus
        '''
        self.display = display
        print (f'Display: {display.width} x {display.height}')
        # Display initial message
        self.display.draw_text8x8(self.display.width // 2 - 32,
                                  self.display.height - 9,
                                  "TOUCH ME",
                                  self.WHITE,
                                  background=self.PURPLE)

        # A small 5x5 sprite for the dot
        self.dot = bytearray(b'\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00')

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

def testScreen(display):
    display.clear(PURPLE)
    display.draw_text8x8(display.width // 2 - 32,
        int(display.height / 2),
        "TOUCH ME",
        WHITE,
        background=BLACK)
    sleep(2)
    display.draw_image('images/RaspberryPiWB128x128.raw', 0, 0, 128, 128)
    display.draw_image('images/MicroPython128x128.raw', 129, 0, 128, 128)
    display.draw_text8x8(display.width // 2 - 32,
        int(display.height / 2) + 20,
        str(cyd.getLdr()),
        BLACK,
        background=PURPLE)
    
    # ldr does not work
#    for idx in range(10):
#        print (cyd.getLdr())
#        sleep (1)

def onTouch(x, y):
    print (f'Touched: x = {x}, y = {y}')
    
def test():
    
    '''
    Display Pins:
    IO2 	TFT_RS 	AKA: TFT_DC
    IO12 	TFT_SDO 	AKA: TFT_MISO
    IO13 	TFT_SDI 	AKA: TFT_MOSI
    IO14 	TFT_SCK 	
    IO15 	TFT_CS 	
    IO21 	TFT_BL

    Touch Screen Pins:
    IO25 	XPT2046_CLK 	
    IO32 	XPT2046_MOSI 	
    IO33 	XPT2046_CS 	
    IO36 	XPT2046_IRQ 	
    IO39 	XPT2046_MISO
    '''
    
    
    ''' Set up the display - ili9341
        Baud rate of 40000000 seems about the max '''
    spi1 = util.getSpi(cyd)
    display = util.getDisplay(spi1, cyd)
    print (f'Display: {display.width} x {display.height}')
    tspi = util.getSpi(touch)
    tscreen = util.getTouch(tspi, touch, onTouch)
    testScreen(display)
    
    display.draw_sprite(SPRITE_DOT, 10 - 2, display.height - 10 - 2, 5, 5)
#    spi1 = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(13))
#    display = Display(spi1, dc=Pin(2), cs=Pin(15), rst=Pin(0))
    
    
#    bl_pin = Pin(21, Pin.OUT)
#    bl_pin.on()
    
    
    # Set up the touch screen digitizer - xpt2046
#    spi2 = SPI(2, baudrate=1000000, sck=Pin(25), mosi=Pin(32), miso=Pin(39))

 #   Demo(display, spi2)

    try:
        while True:
            idle()
    except KeyboardInterrupt:
        print("\nCtrl-C pressed.  Cleaning up and exiting...")
    finally:
        display.cleanup()
        cyd.setBacklight(False)

print ("Running")
cyd.setLed(True, False, True)
cyd.setBacklight()
test()