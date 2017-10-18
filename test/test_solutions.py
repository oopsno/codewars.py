# encoding: UTF-8

import os
import re
import sys
import importlib
import unittest


def main():
    runner = unittest.TextTestRunner()
    root = os.path.abspath(os.path.relpath('..', start=os.path.dirname(__file__)))
    solutions = os.path.join(root, 'solutions')
    kyus = [item for item in os.listdir(solutions) if re.match(r'kyu\d', item)]
    for kyu in kyus:
        prefix = 'solutions.{}'.format(kyu)
        for item in os.listdir(os.path.join(solutions, kyu)):
            name = '{}.{}'.format(prefix, os.path.splitext(os.path.basename(item))[0])
            s = importlib.import_module(name)
            for key in dir(s):
                cls = getattr(s, key)
                if type(cls) is type and issubclass(cls, unittest.TestCase):
                    show_name = '::'.join(s.capitalize() for s in name.split('.'))
                    print('Running test: {}'.format(show_name), file=sys.stderr)
                    suite = unittest.defaultTestLoader.loadTestsFromTestCase(cls)
                    runner.run(suite)


if __name__ == '__main__':
    main()
