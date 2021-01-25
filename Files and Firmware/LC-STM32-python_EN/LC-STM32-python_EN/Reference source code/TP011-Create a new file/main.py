# main.py -- put your code here!
import pyb

pyb.LED(3).on()
log=open('log.txt','w')
for i in range(100):
    log.write("%d ok\r\n" %i)
log.close()
pyb.LED(3).off()

