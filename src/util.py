from machine import Pin, SPI
from ili9341 import Display

def getSpi(mod):
    return SPI(mod.SPI_ID,
        baudrate=mod.SPI_BAUD,
        sck=Pin(mod.PIN_SCK),
        mosi=Pin(mod.PIN_MOSI))

def getDisplay(spi, mod):
    return Display(spi,
        dc=Pin(mod.PIN_DC),
        cs=Pin(mod.PIN_CS),
        rst=Pin(mod.PIN_RST))
