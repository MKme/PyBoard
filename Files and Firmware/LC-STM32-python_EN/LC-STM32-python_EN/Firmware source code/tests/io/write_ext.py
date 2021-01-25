import uio

try:
    uio.BytesIO
except AttributeError:
    import sys
    print('SKIP')
    sys.exit()

buf = uio.BytesIO()

buf.write(b"foo", 2)
print(buf.getvalue())

buf.write(b"foo", 100)
print(buf.getvalue())

buf.write(b"foobar", 1, 3)
print(buf.getvalue())

buf.write(b"foobar", 1, 100)
print(buf.getvalue())

buf.write(b"foobar", 100, 100)
print(buf.getvalue())
