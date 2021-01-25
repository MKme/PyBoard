# main.py -- put your code here!
import pyb
sw = pyb.Switch()
def f():
    pyb.LED(4).toggle()
sw.callback(f)