from machine import Pin, SPI
from ili9341 import Display

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
