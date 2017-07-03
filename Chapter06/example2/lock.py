from multiprocessing import Manager

manager = Manager()

lock = manager.Lock()

lock.acquire()

# ... manipulate data ...

lock.release()
