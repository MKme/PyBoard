# main.py -- put your code here!

import pyb

uart = pyb.UART(4)
uart.init(9600, bits=8, parity=None, stop=1)
uart.write('HelloTurnip')