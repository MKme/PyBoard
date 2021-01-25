from pyb import Pin, Timer
tm2=Timer(2, freq=100)
tm3=Timer(3, freq=200)
led3=tm2.channel(1, Timer.PWM, pin=Pin.cpu.A15)
led3.pulse_width_percent(100)
led4=tm3.channel(1, Timer.PWM, pin=Pin.cpu.B4, pulse_width_percent=20)