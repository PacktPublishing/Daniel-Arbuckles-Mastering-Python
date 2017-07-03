class Frood:
    def __init__(self, age):
        self.age = age
        print("Frood initialized")

    def anniversary(self):
        self.age += 1
        print("Frood is now {} years old".format(self.age))

f1 = Frood(12)
f2 = Frood(97)
f1.anniversary()
f2.anniversary()
f1.anniversary()
f2.anniversary()
