import codewars
import unittest
import io


def raise_something():
    raise RuntimeError('Just raise')


def raise_nothing():
    pass


class TestFramework(unittest.TestCase):
    def setUp(self):
        namespace = dict(__file__=__file__)
        with codewars.Test(namespace=namespace) as test:
            test.describe('a dummy test case')
            test.it('should works')
            test.assert_equals(1 + 1, 2, '1 + 1 = 2')
            test.assert_not_equals(2 ** 3, 6, '2 ^ 3 != 6')
            test.expect(not False, 'passed')
            test.expect_error('Just raise', raise_something)
            self.expect_pass = test.translated
        with codewars.Test(namespace=namespace) as test:
            test.assert_equals(1, 2)
            self.expect_fail_equal = test.translated
        with codewars.Test(namespace=namespace) as test:
            test.assert_not_equals(1, 1)
            self.expect_fail_not_equal = test.translated
        with codewars.Test(namespace=namespace) as test:
            test.expect_error('', raise_nothing)
            self.expect_fail_error = test.translated
        with codewars.Test(namespace=namespace) as test:
            test.expect(False)
            self.expect_fail_pass = test.translated
        self.stream = io.StringIO()
        self.runner = unittest.TextTestRunner(stream=self.stream)

    def test_pass(self):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(self.expect_pass)
        result = self.runner.run(suite)
        self.assertTrue(result.wasSuccessful())

    def test_fail_equal(self):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(self.expect_fail_equal)
        result = self.runner.run(suite)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(1, len(result.failures))

    def test_fail_not_equal(self):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(self.expect_fail_not_equal)
        result = self.runner.run(suite)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(1, len(result.failures))

    def test_fail_error(self):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(self.expect_fail_error)
        result = self.runner.run(suite)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(1, len(result.failures))

    def test_fail_pass(self):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(self.expect_fail_pass)
        result = self.runner.run(suite)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(1, len(result.failures))

    def tearDown(self):
        self.stream.close()
