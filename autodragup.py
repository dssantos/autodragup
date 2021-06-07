from random import randrange, uniform
from time import sleep

import pyautogui as pg


while True:

    xstart = 1150
    ystart = 495
    longwait = randrange(6,19)
    shortwait = uniform(0.6, 0.9)

    sleep(longwait)

    if longwait >= 10:
        pg.moveTo(1347, 447)
        pg.click()
        sleep(shortwait-0.4)        

    pg.moveTo(xstart+randrange(-10, 10), ystart+randrange(-2, 2))
    sleep(shortwait)
    pg.drag(0, -420, duration=shortwait)
