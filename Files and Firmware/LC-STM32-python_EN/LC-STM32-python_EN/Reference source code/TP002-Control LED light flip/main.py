# main.py -- put your code here!
import pyb
led = pyb.LED(4)
while True:
    led.toggle()
    pyb.delay(700)