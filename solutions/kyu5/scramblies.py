# encoding: UTF-8

"""
https://www.codewars.com/kata/scramblies
"""

import codewars


def encode(string):
    counting = [0] * 26
    offset = ord('a')
    for char in string:
        counting[ord(char) - offset] += 1
    return counting


def scramble(s1, s2):
    c1, c2 = encode(s1), encode(s2)
    return all(x >= y for x, y in zip(c1, c2))


with codewars.Test(namespace=globals()) as Test:
    Test.assert_equals(scramble('rkqodlw', 'world'), True)
    Test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
    Test.assert_equals(scramble('katas', 'steak'), False)
    Test.assert_equals(scramble('scriptjava', 'javascript'), True)
    Test.assert_equals(scramble('scriptingjava', 'javascript'), True)
