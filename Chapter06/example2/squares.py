from multiprocessing import Process

class Squares(Process):
    def run(self):
        for i in range(10):
            print(i ** 2)

squares = Squares()

squares.start()

