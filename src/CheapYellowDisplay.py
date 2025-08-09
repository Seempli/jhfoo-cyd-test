# community
from machine import Pin

# custom
import util
import DisplayConfig
import touch
import color

class CYD:
    def __init__(self):
        print ('CYD init')
        self.display = util.getDisplay(util.getSpi(DisplayConfig),
            DisplayConfig)
        
        self.touch = util.getTouch(util.getSpi(touch),
            touch, self.onTouch)
        
    def onTouch(self, x, y):
        print ('onTouch')

    def setBacklight(self, isOn = True):
        pin = Pin(DisplayConfig.PIN_BL, Pin.OUT)
        pin.on() if isOn else pin.off()
            
    def setLed(self, red = True, green = True, blue = True):
        led = Pin(DisplayConfig.PIN_RGB_RED, Pin.OUT)
        led.off() if red else led.on()
        
        led = Pin(DisplayConfig.PIN_RGB_GREEN, Pin.OUT)
        led.off() if green else led.on()

        led = Pin(DisplayConfig.PIN_RGB_BLUE, Pin.OUT)
        led.off() if blue else led.on()

    def getLdr(self):
        return ldr.read_u16()
    
    def setDisplay(self, isOn = True):
        self.display.cleanup()
        self.setBacklight(False)
        
    def setText(self, text, y = None, row = None):
        CHAR_WIDTH = 8
        CHAR_HEIGHT = 8
        if not row == None:
            y = row * CHAR_HEIGHT
        elif y == None:
            y = int((self.display.height-CHAR_HEIGHT) / 2)
        TextWidth = len(text) * CHAR_WIDTH
        x = int((self.display.width - TextWidth) / 2)
        self.display.draw_text8x8(x, y,
            text,
            color.WHITE,
            background=color.BLACK)
