# encoding: UTF-8

import os
import re
import sys
import importlib
import unittest


def for_each_case(handle: callable):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(root)
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
                    handle(kyu, cls)
    from test.test_framework import TestFramework
    handle('', TestFramework)


class Run:
    def __init__(self):
        self.runner = unittest.TextTestRunner()

    def __call__(self, kyu: str, cls: str):
        show_name = '{}::{}'.format(kyu, cls.__name__)
        print('Testing: {}'.format(show_name), file=sys.stderr)
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(cls)
        self.runner.run(suite)


class Inject:
    def __init__(self, namespace: dict):
        self.namespace = namespace

    def __call__(self, kyu: str, cls: str):
        # 强制 Unittest 逐 kyu 按字典非减序执行
        self.namespace[kyu + cls.__name__] = cls


if __name__ == '__main__':
    for_each_case(Run())
else:
    for_each_case(Inject(globals()))
