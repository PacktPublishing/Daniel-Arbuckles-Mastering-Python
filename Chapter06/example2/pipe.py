from multiprocessing import Pipe

near, far = Pipe()

# ... Pass far on to a different process ...

near.send(('hello', 5))

if near.poll(timeout = 2.5):
    data = near.recv()
