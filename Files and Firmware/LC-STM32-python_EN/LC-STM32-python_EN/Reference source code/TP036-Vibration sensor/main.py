# main.py -- put your code here!
import pyb
from pyb import Pin

a = Pin('X1',Pin.IN)
while 1:
    print(a.value())
    if a.value()==1 :
        pyb.LED(3).on()
        pyb.delay(1000)
        pyb.LED(3).off()