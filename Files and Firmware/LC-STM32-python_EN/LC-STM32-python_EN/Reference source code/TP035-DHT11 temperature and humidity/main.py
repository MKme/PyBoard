import pyb
from pyb import UART
from pyb import Pin
from DHT11 import DHT11

#***************获取温湿度*********************
while 1:
    S=DHT11('Y2')
    A=S.read_temps()
    print(A)
    pyb.delay(1000)