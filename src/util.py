from machine import Pin, SPI
from ili9341 import Display
from xpt2046 import Touch

def getSpi(mod):
    return SPI(mod.SPI_ID,
        baudrate=mod.SPI_BAUD,
        sck=Pin(mod.PIN_SCK),
        miso = Pin(mod.PIN_MISO),
        mosi=Pin(mod.PIN_MOSI))

def getDisplay(spi, mod):
    return Display(spi,
        dc=Pin(mod.PIN_DC),
        cs=Pin(mod.PIN_CS),
        rst=Pin(mod.PIN_RST),
        width=320,
        height=240)

def getTouch(spi, mod, callback):
    return Touch(spi,
        cs = Pin(mod.PIN_CS),
        int_pin = Pin(mod.PIN_IRQ),
        int_handler = callback)       
