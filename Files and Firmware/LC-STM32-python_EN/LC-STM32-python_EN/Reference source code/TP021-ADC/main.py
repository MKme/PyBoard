from pyb import Pin, ADC

adc = ADC(Pin('X19'))
adc.read() # read value, 0-4095