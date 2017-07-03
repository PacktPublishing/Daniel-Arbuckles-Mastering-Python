import flask
import json

from .endpoint import Endpoint
from .person import Person


class PersonAPI(Endpoint):
    def post(self):
        first_name = flask.request.form['first_name']
        last_name = flask.request.form['last_name']
        age = int(flask.request.form['age'])
        try:
            member = flask.request.form['member'] == 'true'
        except KeyError:
            member = False

        person = Person.create(first_name, last_name, age, member)

        return json.dumps(person.as_dict()), 200, {'Content-Type': 'application/json'}

    def get(self, id):
        if id is None:
            return json.dumps([x.as_dict() for x in Person.list()]), 200, {'Content-Type': 'application/json'}

        try:
            person = Person.load(id)
        except KeyError:
            return json.dumps({'error': 'invalid id'}), 404, {'Content-Type': 'application/json'}

        return json.dumps(person.as_dict()), 200, {'Content-Type': 'application/json'}

    def put(self, id):
        try:
            person = Person.load(id)
        except KeyError:
            return json.dumps({'error': 'invalid id'}), 404, {'Content-Type': 'application/json'}

        def update(field_name, proc = (lambda x: x)):
            try:
                setattr(person, field_name, proc(flask.request.form[field_name]))
            except KeyError:
                pass

        update('first_name')
        update('last_name')
        update('age')
        update('member', (lambda x: x == 'true'))

        person.store()

        return json.dumps(person.as_dict()), 200, {'Content-Type': 'application/json'}

    def delete(self, id):
        try:
            person = Person.load(id)
        except KeyError:
            return json.dumps({'error': 'invalid id'}), 404, {'Content-Type': 'application/json'}

        person.delete()

        return json.dumps({'deleted': id}), 200, {'Content-Type': 'application/json'}

app = flask.Flask('Flask Microservice Demo')
PersonAPI.register(app)
