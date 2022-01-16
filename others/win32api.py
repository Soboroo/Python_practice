from ctypes import *

libc = cdll.LoadLibrary("libllbc.so")
print(libc.printf)