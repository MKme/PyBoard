# main.py -- put your code here!
import pyb
from DS3231 import DS3231  
ds=DS3231(2)
#����ʱ��
#ds.DATE([17,06,03])
#ds.TIME([17,40,30])

#��ȡ��
ds.sec()
print(ds.sec())
#��ȡʱ��
ds.TIME()
print(ds.TIME())
#��ȡ����
ds.DATE()
print(ds.DATE())
#��ȡ�¶�
ds.TEMP()
print(ds.TEMP())