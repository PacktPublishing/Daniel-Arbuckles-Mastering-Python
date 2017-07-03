from multiprocessing import Manager

manager = Manager()

event = manager.Event()

event.clear()
event.wait()

# In a different process

event.set()


