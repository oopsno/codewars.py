# encoding: UTF-8

"""
https://www.codewars.com/kata/simple-fun-number-159-middle-permutation
"""

import codewars


def middle_permutation(string):
    import io
    ss = io.StringIO()
    xs = sorted(string)
    quot, rem = divmod(len(xs), 2)
    if rem is 1:
        ss.write(xs.pop(quot))
    ss.write(xs.pop(quot - 1))
    ss.write(''.join(reversed(xs)))

    return ss.getvalue()


with codewars.Test(namespace=globals()) as Test:
    Test.assert_equals(middle_permutation("abc"), "bac")
    Test.assert_equals(middle_permutation("abcd"), "bdca")
    Test.assert_equals(middle_permutation("abcdx"), "cbxda")
    Test.assert_equals(middle_permutation("abcdxg"), "cxgdba")
    Test.assert_equals(middle_permutation("abcdxgz"), "dczxgba")
