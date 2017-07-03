from .libc import printf, scanf, localtime, asctime
from ctypes import c_int, create_string_buffer, byref, Structure

def input_pair():
    key = c_int()
    value = create_string_buffer(16)
    printf(b"[Input a pair as int:string] ")
    scanf(b"%i:%s", byref(key), byref(value))
    return key, value.value

def print_a_time():
    timer = c_int(12345678)
    printf(asctime(localtime(byref(timer))))

