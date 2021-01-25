# main.py -- put your code here!
import pyb
from DS3231 import DS3231  
ds=DS3231(2)
#设置时间
#ds.DATE([17,06,03])
#ds.TIME([17,40,30])

#读取秒
ds.sec()
print(ds.sec())
#读取时间
ds.TIME()
print(ds.TIME())
#读取日期
ds.DATE()
print(ds.DATE())
#读取温度
ds.TEMP()
print(ds.TEMP())