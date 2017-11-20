# encoding: UTF-8

import unittest
import inspect
import os


def make_translator(assertion):
    """
    根据预期的断言构造转译函数
    """
    from functools import wraps

    @wraps(assertion)
    def __after_instantiation__(translator, *args, **kwargs):
        def __assertion__(test_case):
            try:
                assertion(test_case, *args, **kwargs)
            except AssertionError as ae:
                raise ae

        serial = translator.__counter__
        name = 'test_{:03d}'.format(serial)
        translator.__counter__ += 1
        setattr(translator.translated, name, __assertion__)

    return __after_instantiation__


class TestTranslator:
    """
    用于将 Codewars Python Test Framework 动态转译成 unittest.TestCase 的派生类的 DSL
    """

    def __init__(self, namespace: dict = None):
        self.name, self.module = self.guess_name(namespace)
        self.namespace = namespace
        self.behaviors = []
        self.translated = type(self.name, (unittest.TestCase,),
                               dict(__name__=self.name, __builder__=self, behaviors=self.behaviors))
        self.translated.__module__ = self.module
        self.__counter__ = 0

    def inject(self):
        self.namespace[self.name] = self.translated

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.namespace.get('__name__', None) == '__main__':
            suite = unittest.defaultTestLoader.loadTestsFromTestCase(self.translated)
            runner = unittest.TextTestRunner()
            runner.run(suite)
        else:
            self.inject()

    def describe(self, description: str):
        setattr(self.translated, 'description', description)

    def it(self, behavior: str):
        self.behaviors.append(behavior)

    @make_translator
    def assert_equals(self: unittest.TestCase, actual, excepted, message=None):
        self.assertEqual(excepted, actual, msg=message)

    @make_translator
    def assert_not_equals(self: unittest.TestCase, actual, unexpected, message=None):
        self.assertNotEqual(unexpected, actual, msg=message)

    @make_translator
    def expect_error(self: unittest.TestCase, message, function_like):
        with self.assertRaises(Exception, msg=message):
            function_like()

    @make_translator
    def expect(self: unittest.TestCase, passed, message=None):
        self.assertTrue(passed, msg=message)

    @staticmethod
    def guess_name(namespace: dict):
        if namespace is not None:
            filename = namespace.get('__file__')
        else:
            frame = inspect.stack()[2]
            filename = frame.filename
        sp = os.path.split(filename)
        guessed_name, _ = os.path.splitext(sp[-1])
        guessed_module = os.path.split(sp[-2])[-1]
        return guessed_name, guessed_module
