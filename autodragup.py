from random import randrange, uniform
from time import sleep

import pyautogui as pg


while True:

    xstart=1100
    ystart=450
    sleep(randrange(30,50))

    pg.moveTo(xstart+randrange(-50, 50), ystart+randrange(-50, 50))
    pg.drag(0, -200, duration=uniform(0.1, 0.4))



