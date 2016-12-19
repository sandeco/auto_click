# import the module
from pymouse import PyMouse
import time
import os
import pygame
# instantiate an mouse object
m = PyMouse()

# move the mouse to int x and int y (these are absolute positions)
## m.move(200, 200)

# click works about the same, except for int button possible values are 1: left, 2: right, 3: middle
while True :
    time.sleep(10)
    m.click(562, 565,1)

    time.sleep(2)
    m.click(506, 737,1)

    time.sleep(2)
    m.click(717, 570,1)




# get the screen size
## m.screen_size()
# (1024, 768)

# get the mouse position
## print m.position()
# (500, 300)