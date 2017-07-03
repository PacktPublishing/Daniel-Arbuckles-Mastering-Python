import unittest
import os

class SharedEnv(unittest.TestCase):
    def setUp(self):
        with open('test.txt', 'w') as f:
            f.write('a\nb\n')

    def tearDown(self):
        os.unlink('test.txt')

    def test_append(self):
        with open('test.txt', 'r') as f:
            lines = f.read().splitlines()

        self.assertEqual(lines, ['a', 'b'])

        lines.append('c')

        with open('test.txt', 'w') as f:
            f.write('\n'.join(lines))

    def test_replace(self):
        with open('test.txt', 'r') as f:
            lines = f.read().splitlines()

        self.assertEqual(lines, ['a', 'b'])

        lines[0] = 'q'

        with open('test.txt', 'w') as f:
            f.write('\n'.join(lines))
