# main.py -- put your code here!
leds = [pyb.LED(i) for i in range(1,5)]

sw=pyb.Switch()
def test():
    pyb.LED(1).on()
    pyb.LED(2).on()
    pyb.LED(3).on()
    pyb.LED(4).on()
    pyb.delay(2000)
sw.callback(test)

for l in leds:
    l.off()

n = 0

try:
   while True:
      n = (n + 1) % 4
      leds[n].toggle()
      pyb.delay(50)
finally:
    for l in leds:
        l.off()