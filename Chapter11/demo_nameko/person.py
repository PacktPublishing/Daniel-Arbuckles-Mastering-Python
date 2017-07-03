import sqlite3
import pkgutil


connection = sqlite3.connect('demo.sqlite', detect_types = sqlite3.PARSE_DECLTYPES)
connection.row_factory = sqlite3.Row
connection.executescript(pkgutil.get_data('demo_nameko', 'schema.sql').decode('utf8'))


class Person:
    def __init__(self, id, first_name, last_name, age, member):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.member = member

    @staticmethod
    def list():
        cursor = connection.cursor()
        cursor.execute('select * from person')
        rows = cursor.fetchmany()
        while rows:
            for row in rows:
                yield Person(row['id'], row['first_name'], row['last_name'], row['age'], bool(row['member']))
            rows = cursor.fetchmany()

    @staticmethod
    def create(first_name, last_name, age, member = False):
        cursor = connection.cursor()
        cursor.execute('insert into person (first_name, last_name, age, member) values (?, ?, ?, ?)',
                       [first_name, last_name, age, int(member)])
        connection.commit()
        return Person(cursor.lastrowid, first_name, last_name, age, member)

    @staticmethod
    def load(id):
        cursor = connection.cursor()
        cursor.execute('select * from person where id = ? limit 1', [id])
        row = cursor.fetchone()
        if row is None:
            raise KeyError(id)
        return Person(id, row['first_name'], row['last_name'], row['age'], bool(row['member']))

    def store(self):
        cursor = connection.cursor()
        cursor.execute('update person set first_name = ?, last_name = ?, age = ?, member = ? WHERE id = ?',
                       [self.first_name, self.last_name, self.age, int(self.member), self.id])
        connection.commit()

    def delete(self):
        cursor = connection.cursor()
        cursor.execute('delete from person where id = ?', [self.id])
        self.id = None
        connection.commit()

    def as_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'member': self.member,
        }

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

