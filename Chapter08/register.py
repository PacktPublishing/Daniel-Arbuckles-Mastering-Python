from collections import OrderedDict

class BasicMeta(type):
    @staticmethod
    def __prepare__(name, bases, **kwargs):
        return dict()

class OrderedMeta(type):
    @staticmethod
    def __prepare__(name, bases, **kwargs):
        return OrderedDict()

    def __new__(cls, name, bases, namespace, **kwargs):
        class_ = type.__new__(cls, name, bases, namespace)
        class_.order = type(namespace.keys())
        return class_

class RegisterDescendants(type):
    def __new__(cls, name, bases, namespace, **kwargs):
        class_ = type.__new__(cls, name, bases, namespace)
        registry = getattr(class_, 'REGISTRY', set())
        registry.add(class_)
        setattr(class_, 'REGISTRY', registry)
        return class_
