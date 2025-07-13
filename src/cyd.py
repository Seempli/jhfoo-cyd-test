from machine import Pin

SPI_ID = 1
#SPI_BAUD =  10000000
SPI_BAUD = 40000000

PIN_RST = 0
PIN_DC = 2
PIN_MOSI = 13
PIN_SCK = 14
PIN_CS = 15
PIN_BL = 21

PIN_RGB_RED = 4
PIN_RGB_GREEN = 16
PIN_RGB_BLUE = 17

def setBacklight(isOn = True):
    pin = Pin(PIN_BL, Pin.OUT)
    pin.on() if isOn else pin.off()
        
def setLed(red = True, green = True, blue = True):
    led = Pin(PIN_RGB_RED, Pin.OUT)
    led.off() if red else led.on()
    
    led = Pin(PIN_RGB_GREEN, Pin.OUT)
    led.off() if green else led.on()

    led = Pin(PIN_RGB_BLUE, Pin.OUT)
    led.off() if blue else led.on()
