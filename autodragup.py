from random import randrange, uniform
from time import sleep

import pyautogui as pg


def openapp(x, y):
    pg.moveTo(1123, 707)
    pg.click()
    sleep(0.5)
    pg.moveTo(x, y)
    pg.click()

def like():
    if longwait >= 10:
        pg.moveTo(1176, 338)
        pg.click()
        sleep(0.1)
        pg.click()
        sleep(shortwait)

def dragup():
    pg.moveTo(xstart, ystart)
    sleep(shortwait)
    pg.drag(0, -460, duration=shortwait)

token = True
sleep(5)
openapp(1168, 306)
while True:

    xstart = 1150+randrange(-10, 10)
    ystart = 600+randrange(-2, 2)
    longwait = randrange(6,15)
    shortwait = uniform(0.5, 0.9)
    
    sleep(longwait)
    if longwait == 6:
        token = not token
        if token:
            openapp(1168, 306) 
        else:
            openapp(1168, 403)
    like()
    dragup()
