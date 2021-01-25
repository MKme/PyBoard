# main.py -- put your code here!

from pyb import Pin
x1 = Pin('X1',Pin.OUT_PP)
x2 = Pin('X2',Pin.OUT_PP)
x1.high()
x2.low()
