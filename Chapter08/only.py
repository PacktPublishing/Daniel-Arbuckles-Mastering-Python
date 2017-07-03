from functools import wraps

def only(adapt = int):
    def decorator(func):
        @wraps(func):
        def wrapper(*args, **kawrgs):
            args = [adapt(x) for x in args]
            kwargs = {n: adapt(v)
                             for n, v
                             in kwargs.items()}
            return func(*args, **kwargs)
        return wrapper
    return decorator

@only(float)
def add(left, right):
    return left + right
