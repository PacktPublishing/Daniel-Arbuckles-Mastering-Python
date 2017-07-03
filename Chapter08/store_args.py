from functools import wraps

def store_args(func):
    @wraps(func)
    def wrapper(self, **kwargs):
        for name, value in kwargs.items():
            attrib = func.__annotations__.get(name)
            if attrib is True:
                attrib = name
            if isinstance(attrib, str):
                setattr(self, attrib, value)
        return func(self, **kwargs)
    return wrapper

class A:
    @store_args
    def __init__(self, first: True, second: 'example'):
        pass

a = A(first = 5, second = 6)
assert a.first == 5
assert a.example == 6
