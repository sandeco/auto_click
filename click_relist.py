from pymouse import PyMouse
import time

# instantiate an mouse object
m = PyMouse()

# move the mouse to int x and int y (these are absolute positions)
## m.move(200, 200)

# click works about the same, except for int button possible values are 1: left, 2: right, 3: middle
while True :

    ##reload
    time.sleep(500)
    m.click(1030, 10,1) ## sai do descanco de tela
    time.sleep(1)
    m.click(138, 66, 1) ## recarrega a tela

    ##click transfer
    time.sleep(30)
    m.click(708, 283,1)

    ##click transfer list
    time.sleep(1)
    m.click(837, 313,1)

    ## relist
    time.sleep(15)
    m.click(1114, 536,1)

    ## remove sold
    ##time.sleep(5)
    ##m.click(439, 539,1)

