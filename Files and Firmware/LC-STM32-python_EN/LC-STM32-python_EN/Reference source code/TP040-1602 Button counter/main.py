# main.py -- put your code here!
import pyb
from pyb import Pin
from pyb import delay, udelay,millis
from tpyb_lcd1602 import TPYBoardLcd1602Api
from tpyb_gpio_lcd1602 import TPYBoardGpioLcd1602
 
 
lcd = TPYBoardGpioLcd1602(rs_pin=Pin.board.Y10,
              enable_pin=Pin.board.Y9,
              d4_pin=Pin.board.Y5,
              d5_pin=Pin.board.Y6,
              d6_pin=Pin.board.Y7,
              d7_pin=Pin.board.Y8,
              num_lines=2, num_columns=16)
sw=pyb.Switch()
def test():
    global count
    lcd.clear()
    count = 0
 
sw.callback(test)
 

count=0
while True:
    lcd.move_to(0, 0)
    delay(1000)
    count += 1
lcd.lcd1602_write_string(str(count))  