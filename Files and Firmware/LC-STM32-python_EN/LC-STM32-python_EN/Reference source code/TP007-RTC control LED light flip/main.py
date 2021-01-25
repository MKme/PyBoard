import pyb
rtc = pyb.RTC()
rtc.datetime((2014,5,1,4,13,0,0,0))
print(rtc.datetime())
led = pyb.LED(3)
rtc.wakeup(500,lambda t:led.toggle())