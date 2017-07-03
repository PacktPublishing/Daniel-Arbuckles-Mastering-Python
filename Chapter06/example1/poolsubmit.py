from concurrent import futures

class FooError(Exception):
    pass

def foo(x, y):
    if x > y:
        raise FooError
    return y - x

with futures.ProcessPoolExecutor() as pool:
    future = pool.submit(foo, 4, 7)

    while not future.done():
        ... do other stuff ...

    try:
        data = future.result()
    except FooError:
        data = None
