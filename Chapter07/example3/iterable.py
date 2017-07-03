import asyncio

class SlowSequence:
    class Iterator:
        def __init__(self, slowseq):
            self.values = list(slowseq.values)

        async def __anext__(self):
            await asyncio.sleep(2)
            try:
                return self.values.pop(0)
            except IndexError:
                raise StopAsyncIteration

    def __init__(self, *values):
        self.values = values

    async def __aiter__(self):
        return SlowSequence.Iterator(self)

async def main():
    seq = SlowSequence(1, 2, 3, 4, 5)

    async for value in seq:
        print(value)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(main()))
loop.close()
