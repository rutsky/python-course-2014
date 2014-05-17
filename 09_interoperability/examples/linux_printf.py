import ctypes
import math

libc = ctypes.CDLL('libc.so.6')
x = ctypes.c_double(math.pi)
res = libc.printf(b'Hello, %s! x = %.4f\n', b'User', x)
print(res)
