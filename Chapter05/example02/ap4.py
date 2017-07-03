import argparse
parser = argparse.ArgumentParser(
    prog = 'python -m apdemo',
    description="Hello world"
)
parser.add_argument('-p', '--print', action='store_true', default = False)
parser.add_argument('name', nargs='+')
args = parser.parse_args()
