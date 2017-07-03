from functools import wraps

def ints_only(func):
    @wraps(func):
    def wrapper(*args, **kawrgs):
        args = [int(x) for x in args]
        kwargs = {n: int(v)
                  for n, v
                  in kwargs.items()}
        return func(*args, **kwargs)
    return wrapper

@ints_only
def add(left, right):
    return left + right

add('57', 99.5)
