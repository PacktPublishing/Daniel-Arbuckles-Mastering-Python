from weakref import WeakValueDictionary

def factory_constructed(class_):
    cache = WeakValueDictionary()

    def factory(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        instance = cache.get(key)
        if instance is not None:
            return instance
        instance = class_(*args, **kwargs)
        cache[key] = instance
        return instance

    factory.type = class_

    return factory
