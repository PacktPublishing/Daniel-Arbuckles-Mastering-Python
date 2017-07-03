from http.client import HTTPConnection
from urllib.parse import urlencode
from pprint import pprint
import json

def call(conn, method, path, body = None, content_type = 'application/x-www-form-urlencoded'):
    if isinstance(body, dict):
        body = urlencode(body)

    conn.request(method, path, body, {'Content-Type': content_type})
    resp = conn.getresponse()
    print(resp.status, resp.reason)
    if resp.status != 200:
        return

    result = json.loads(resp.read().decode('utf8'))
    pprint(result)
    return result

if __name__ == '__main__':
    conn = HTTPConnection('127.0.0.1', 5000)

    call(conn, 'GET', '/personapi')

    call(conn, 'POST', '/personapi', {
        'first_name': 'Alice',
        'last_name': 'Example',
    })

    call(conn, 'GET', '/personapi')

    alice = call(conn, 'POST', '/personapi', {
        'first_name': 'Alice',
        'last_name': 'Example',
        'age': (6 * 8) + (4 * 7) + 98 + 11
    })['id']

    bob = call(conn, 'POST', '/personapi', {
        'first_name': 'Bob',
        'last_name': 'Example',
        'age': 37
    })['id']

    call(conn, 'GET', '/personapi')

    call(conn, 'PUT', '/personapi/{}'.format(alice), {
        'age': 33,
        'member': 'true'
    })

    call(conn, 'GET', '/personapi')

    call(conn, 'DELETE', '/personapi/{}'.format(bob))

    call(conn, 'GET', '/personapi')
