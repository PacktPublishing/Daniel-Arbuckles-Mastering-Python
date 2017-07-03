from nameko.rpc import rpc

from .person import Person


class PersonAPI:
    name = 'person'

    @rpc
    def create(self, first_name, last_name, age, member = False):
        return Person.create(first_name, last_name, age, member).id

    @rpc
    def list(self):
        return [x.as_dict() for x in Person.list()]

    @rpc
    def get(self, id):
        return Person.load(id).as_dict()

    @rpc
    def set(self, id, **values):
        person = Person.load(id)

        for name, value in values.items():
            setattr(person, name, value)

        person.store()

    @rpc
    def delete(self, id):
        Person.load(id).delete()

