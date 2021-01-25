# main.py -- put your code here!

from pyb import Timer

tim4 = pyb.Timer(4)
tim7 = pyb.Timer(7)
tim4.init(freq=10)
tim7.init(freq=20)
led1 = pyb.LED(2)
led2 = pyb.LED(4)
tim4.callback(lambda t:led1.toggle())
tim7.callback(lambda t:led2.toggle())