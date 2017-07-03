from multiprocessing import Process, Pipe, Queue

class Multiples(Process):
    """Process to calculate multiples of a base number.

    The set of multiples of a number is a countably infinite set, so
    this process can never complete its job. However, other processes
    can stop it when the list is long enough by sending 'stop' through
    the contol pipe. It can also be retasked to a new number by sending
    that number through the control pipe.

    """
    def __init__(self, base, control, output):
        super().__init__()
        self.base = base
        self.control = control
        self.output = output

    def run(self):
        """Perform the calculations."""
        base = self.base
        control = self.control
        output = self.output

        current = base

        while True:
            if control.poll(timeout = 0.1):
                try:
                    command = control.recv()
                except EOFError:
                    command = 'stop'

                if command == 'stop':
                    break
                else:
                    base = current = int(command)

            current = current + base
            output.put((base, current))

if __name__ == '__main__':
    maximum = 100
    numbers = set(range(2, maximum))
    tried = set()
    output = Queue()
    controls = {}

    for i in range(2, 5):
        near, far = Pipe()
        tried.add(i)
        proc = Multiples(i, far, output)
        proc.start()
        controls[i] = near

    while controls:
        base, num = output.get()

        if base not in controls:
            continue

        print(numbers)

        numbers.discard(num)

        if num > maximum:
            control = base
        elif num in controls:
            control = num
        else:
            control = 0

        if control > 0:
            ctrl = controls.get(control)
            if ctrl is not None:
                del controls[control]

                try:
                    new_base = next(iter(numbers - tried))
                except StopIteration:
                    ctrl.send('stop')
                else:
                    tried.add(new_base)
                    controls[new_base] = ctrl
                    ctrl.send(new_base)
