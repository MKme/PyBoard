# main.py -- put your code here!
import pyb

pyb.LED(3).on()
log=open('/sd/log.txt','w')
for i in range(1000):
    log.write("%d ok\r\n" %i)
log.close()
pyb.LED(3).off()

