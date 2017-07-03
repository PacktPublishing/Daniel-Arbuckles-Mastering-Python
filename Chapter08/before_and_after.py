import contextlib

@contextlib.contextmanager
def before_and_after():
    print("Before")
    try:
        yield (lambda: print("During"))
    finally:
        print("After")
