# main.py -- put your code here!
import pyb

switch = pyb.Switch()
accel = pyb.Accel()
while not switch():
    pyb.hid((0, -accel.x(), accel.y(), 0))
    pyb.delay(20)
