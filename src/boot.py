
from machine import Pin
from time import sleep_ms

# custom
from CheapYellowDisplay import CYD
from dice import Dice


def showCountdown(cyd, DotCount):
    text = '.' * DotCount
    cyd.setText(f'{text:<20}', row = 21)
    
def monitorDice(cyd, dice):
    WAIT_TIMEOUT_SEC = 2 
    SLEEP_INTERVAL_MSEC = 200
    isExit = False
    OldNumber = None
    CountdownMsec = None
    while not isExit:
        number = dice.roll()
        if number == 6:
            isExit = True
        else:
            if OldNumber == None:
                # ignore first reading since dice has not moved
                OldNumber = number
            elif not number == OldNumber:
                # number changed
                OldNumber = number
                device = dice.getDeviceByNumber(number)
                cyd.setText(f'{device["name"]:<20}', row = 20)
                CountdownMsec = WAIT_TIMEOUT_SEC * 1000
                DotCount = int(CountdownMsec / SLEEP_INTERVAL_MSEC)
                showCountdown(cyd, DotCount)
            else:
                # check if countdown set
                if not CountdownMsec == None:
                    DotCount = int(CountdownMsec / SLEEP_INTERVAL_MSEC)
                    showCountdown(cyd, DotCount)
                    
                    CountdownMsec -= SLEEP_INTERVAL_MSEC
                    print (f'CountdownMsec: {CountdownMsec}')
                    if CountdownMsec == 0:
                        CountdownMsec = None
                        cyd.setText(f'{"Action executed":<20}', row = 21)
            sleep_ms(SLEEP_INTERVAL_MSEC)


print ('x')
dice = Dice()

try:
    cyd = CYD()
    cyd.setLed(True, False, True)
    cyd.setBacklight()
    
    cyd.display.draw_image('images/RaspberryPiWB128x128.raw', 0, 0, 128, 128)
    cyd.setText('Roll the dice!', row = 20)

    monitorDice(cyd, dice)
    
except KeyboardInterrupt:
    print("\nCtrl-C pressed.  Cleaning up and exiting...")
finally:
    cyd.setLed(False, False, False)
    cyd.setDisplay(False)

