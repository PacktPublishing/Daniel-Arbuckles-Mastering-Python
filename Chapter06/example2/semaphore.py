from multiprocessing import Manager

manager = Manager()

sem = manager.BoundedSemaphore(3)

sem.acquire()

# ... access limited resource ...

sem.release()
