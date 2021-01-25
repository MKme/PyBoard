#main.py
import pyb
import upcd8544
from machine import SPI,Pin

def main():
    SPI    = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
    #DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
    #CLK =>SPI(1).SCK  'X6' SPI clock
    
    RST    = pyb.Pin('X1')
    CE     = pyb.Pin('X2')
    DC     = pyb.Pin('X3')
    LIGHT  = pyb.Pin('X4')
    lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
    
    lcd_5110.lcd_write_string('Hello EveryOne',0,0)
    lcd_5110.lcd_write_string('It',6,1)
    lcd_5110.lcd_write_string('Is',12,2)
    lcd_5110.lcd_write_string('Turnip',60,3)
    lcd_5110.lcd_write_string('Smart',0,4)
    

if __name__ == '__main__':
    main()
