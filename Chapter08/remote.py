import asyncio

class RemoteResource:
    def __init__(self, name):
        self.name = name

    def to_str(self, val):
        return str(val)

    def from_str(self, val):
        return val

    async def _fetcher(self, instance, name, future):
        out = instance.out
        in_ = instance.in_
        pk = instance.pk
        out.write('fetch {} {}\n'.format(pk, name)
        value = await in_.readline()
        future.set_result(self.from_str(value))

    def __get__(self, instance, class_):
        if instance is None:
            return self
        future = asyncio.Future()
        coro = self._fetcher(instance, self.name, future)
        asyncio.ensure_future(coro)
        return future

    def __set__(self, instance, value):
        pk = instance.pk
        name = self.name
        value = self.to_str(value)
        template = 'set {} {}\n{}\n'
        command = template.format(pk, name, value)
        instance.out.write(command)

    def __delete__(self, instance):
        pk = instance.pk
        name = self.name
        command = 'delete {} {}\n'.format(pk, name)
        instance.out.write(command)

class RemoteInt(RemoteResource):
    def from_string(self, value):
        return int(value)

class Record:
    name = RemoteResource('name')
    age = RemoteInt('age')

    def __init__(self, pk, reader, writer):
        self.out = writer
        self.in_ = reader
        self.pk = pk
