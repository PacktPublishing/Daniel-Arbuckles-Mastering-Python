import .b

class A:
    def __init__(self):
        print(str(self))

class C(b.B):
    def __str__(self):
        return 'C'
