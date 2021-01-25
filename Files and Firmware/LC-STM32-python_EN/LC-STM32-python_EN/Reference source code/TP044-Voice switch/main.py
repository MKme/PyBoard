# main.py -- put your code here!
import pyb
from pyb import Pin

a = Pin('Y1',Pin.IN)
print('start')
while 1:
    if a.value()==1:
        print(a.value())
        pyb.LED(2).off()
        pyb.LED(4).on()     
    else:
        print(a.value())
        pyb.LED(4).off()
        pyb.LED(2).on()
        pyb.delay(3000)
            