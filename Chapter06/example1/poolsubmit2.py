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

    while True:
        try:
            data = future.result(timeout = 0.5)
        except futures.TimeoutError:
            print('Working...')
            continue
        except FooError:
            data = None

        break
