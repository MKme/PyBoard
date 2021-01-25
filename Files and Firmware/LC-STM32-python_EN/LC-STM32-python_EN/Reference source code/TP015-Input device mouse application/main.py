# main.py -- put your code here!

import math
import pyb
def osc(n, d):
    for i in range(n):
        pyb.hid((0, int(20 * math.sin(i / 10)), 0, 0))
        pyb.delay(d)
osc(100, 50)
