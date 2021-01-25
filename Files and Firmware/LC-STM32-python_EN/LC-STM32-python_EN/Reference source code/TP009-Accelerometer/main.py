# main.py -- put your code here!
import pyb

accel = pyb.Accel()
x = accel.x()
y = accel.y()
z = accel.z()
print (x,y,z)