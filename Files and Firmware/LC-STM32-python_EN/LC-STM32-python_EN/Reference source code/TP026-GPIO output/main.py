# main.py -- put your code here!

from pyb import Pin,delay

x1 = Pin('X1',Pin.OUT_PP)
while True:
    x1.value(0)
    print(x1.value())
    delay(1000)
    x1.value(1)
    print(x1.value())
    delay(1000)
