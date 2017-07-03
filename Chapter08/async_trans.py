from collections import ChainMap

class AsyncTransactionDict(dict):
    async def __aenter__(self):
        self.writes = dict()
        return ChainMap(self.writes, self)

    async def __aexit__(self, exc_type, exc_val, tb):
        if exc_type is None:
            self.update(self.writes)
        self.writes = None
