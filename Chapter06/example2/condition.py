from multiprocessing import Manager

manager = Manager()

cond = manager.Condition()

cond.acquire()
cond.wait()

# ... manipulate data ...

cond.release()

# in another process

cond.acquire()

# ... manipulate data ...

cond.notify()
cond.release()
