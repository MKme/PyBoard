# main.py -- put your code here!

import pyb
hid = pyb.USB_HID()
def release_key_once():
    buf = bytearray(8)
    buf[2] = 0
    hid.send(buf)
    pyb.delay(10)
    
def press_key_once(key):
    buf = bytearray(8)
    buf[2] = key
    hid.send(buf)
    pyb.delay(10)
    
def press_2key(key1,key2):
    buf = bytearray(8)
    buf[2] = key1
    buf[3] = key2
    hid.send(buf)
    pyb.delay(10)

def release_2key():
    buf = bytearray(8)
    buf[2] = 0
    buf[3] = 0
    hid.send(buf)
    pyb.delay(10)

pyb.delay(5000)
press_key_once(0x04)
release_key_once()
pyb.delay(1000)
press_key_once(0x05)
release_key_once()
pyb.delay(1000)
press_key_once(0x2B)
release_key_once()
pyb.delay(1000)
press_key_once(0x28)
release_key_once()
pyb.delay(1000)
press_key_once(0x06)
release_key_once()
pyb.delay(1000)
press_key_once(0x07)
release_key_once()
pyb.delay(1000)
press_2key(0x08,0x09)
release_2key()

pyb.delay(1000)
