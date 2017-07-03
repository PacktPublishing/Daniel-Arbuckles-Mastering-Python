from nameko.rpc import RpcProxy
from nameko.timer import timer
from pprint import pprint


class TestService:
    name = 'test_person'

    person = RpcProxy('person')

    @timer(interval = 10)
    def test(self):
        pprint(self.person.list())

        candide = self.person.create('Candide', 'Apples', 25)
        pprint(candide)

        pprint(self.person.list())

        self.person.set(candide, age = 27)

        pprint(self.person.get(candide))

        self.person.delete(candide)

        pprint(self.person.list())
