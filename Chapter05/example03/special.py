from getpass import getpass
from pprint import pprint

password = getpass('Password: ')
pprint([{1: 2, 3: 4}, {5: 6, 7: list(range(25))}])
