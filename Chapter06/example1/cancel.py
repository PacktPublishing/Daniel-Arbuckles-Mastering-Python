from concurrent import futures

class FooError(Exception):
    pass

def foo(x, y):
    if x > y:
        raise FooError
    return y - x

with futures.ProcessPoolExecutor() as pool:
    running = [pool.submit(foo, 5, 8),
               pool.submit(foo, 6, 9)]

    if running[0].cancel():
        print('Successfully cancelled')
    else:
        print('Too late')

