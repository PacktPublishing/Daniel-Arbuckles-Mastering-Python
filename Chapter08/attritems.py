def attritems(class_):
    def _getitem(self, key):
        return getattr(self, key)

    setattr(class_, '__getitem__', _getitem)

    if getattr(class_, '__setitem__', None):
        delattr(class_, '__setitem__')

    if getattr(class_, '__delitem__', None):
        delattr(class_, '__delitem__')

    return class_

@attritems
class Foo:
    def __init__(self):
        self.a = 'hello'
        self.b = 'world'

f = Foo()

assert f['a'] == 'hello'
assert f['b'] == 'world'
