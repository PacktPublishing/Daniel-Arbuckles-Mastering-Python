from collections import ChainMap

class TransactionDict(dict):
    def __enter__(self):
        self.writes = dict()
        return ChainMap(self.writes, self)

    def __exit__(self, exc_type, exc_val, tb):
        if exc_type is None:
            self.update(self.writes)
        self.writes = None

if __name__ == '__main__':
    tdict = TransactionDict()
    with tdict as trans:
        trans['a'] = 1
