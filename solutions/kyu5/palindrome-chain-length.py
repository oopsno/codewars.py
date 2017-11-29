# encoding: UTF-8

"""
https://www.codewars.com/kata/palindrome-chain-length
"""

import codewars


def palindrome_chain_length(x):
    def reverse(n):
        return int(str(n)[::-1])

    length = 0
    y = reverse(x)
    while x != y:
        x += y
        length += 1
        y = reverse(x)
    return length


with codewars.Test(namespace=globals()) as test:
    test.assert_equals(palindrome_chain_length(87), 4)
