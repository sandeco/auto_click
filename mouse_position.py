from pymouse import PyMouse
import time

# instantiate an mouse object


m = PyMouse()

# move the mouse to int x and int y (these are absolute positions)
## m.move(200, 200)
# click works about the same, except for int button possible values are 1: left, 2: right, 3: middle
print m.position()