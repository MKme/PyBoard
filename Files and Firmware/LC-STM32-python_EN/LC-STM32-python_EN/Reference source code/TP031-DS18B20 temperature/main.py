#main.py
import pyb
from pyb import Pin
from ds18x20 import DS18X20
Pin("Y11",Pin.OUT_PP).low()#GND
Pin("Y9",Pin.OUT_PP).high()#VCC
pyb.delay(100)
DQ=DS18X20(Pin('Y10'))#DQ
while True:
	tem = DQ.read_temp()
	print(tem)
	pyb.delay(1000)
