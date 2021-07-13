from ctypes import *
import ctypes as ctypes
c_lib = ctypes.CDLL("main.dll")    
c_lib.main.restype= ctypes.c_int
buf = create_string_buffer(128)
buf.value= b'Santiago & Roberto'  # GET PARAMS TO INIT 
answer= c_lib.main(buf)
if answer==0:
    print("\nAre my child names\n")
else:
    print("\nNot are my child names\n")
    
