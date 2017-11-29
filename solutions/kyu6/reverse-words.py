# encoding: UTF-8

"""
https://www.codewars.com/kata/reverse-words
"""

import codewars
from io import StringIO


def reverse_words(words: str):
    cs = []
    ss = StringIO()
    for c in words:
        if c.isspace():
            ss.writelines(cs[::-1])
            ss.write(c)
            cs.clear()
        else:
            cs.append(c)
    ss.writelines(cs[::-1])
    return ss.getvalue()


with codewars.Test(namespace=globals()) as test:
    test.assert_equals(reverse_words('This is an example!'), 'sihT si na !elpmaxe');
