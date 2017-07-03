from multiprocessing import Manager

manager = Manager()

dictionary = manager.dict()
sequence = manager.list()
obj = manager.Namespace()

dictionary['hello'] = 'world'
sequence.append(57)
obj.attribute = 'This is shared data'

lock = manager.Lock()
event = manager.Event()
cond = manager.Condition()
sem = manager.BoundedSemaphore(3)
