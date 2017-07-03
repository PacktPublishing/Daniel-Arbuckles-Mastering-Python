from concurrent import futures

def foo(x, y):
    return y - x

with futures.ProcessPoolExecutor() as pool:
    pool.map(foo, [1, 2, 3], [4, 5, 6])

<<< means >>>

foo(1, 4)
foo(2, 5)
foo(3, 6)

