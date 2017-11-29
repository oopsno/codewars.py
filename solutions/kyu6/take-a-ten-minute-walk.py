# encoding: UTF-8

"""
https://www.codewars.com/kata/take-a-ten-minute-walk
"""

import random
import codewars


def isValidWalk(walk):
    if len(walk) != 10:
        return False
    n, w = 0, 0
    for step in walk:
        if step == 'n':
            n += 1
        elif step == 's':
            n -= 1
        elif step == 'w':
            w += 1
        else:
            w -= 1
    return n == w == 0


def create_tests(steps):
    xs = [random.choice(('w', 'e', 'n', 's')) for _ in range(steps)]
    return xs, isValidWalk(xs)


with codewars.Test(namespace=globals()) as test:
    for i in range(20):  # test as many times as you want, just change the number
        test1 = create_tests(random.randint(0, 20))
        test.assert_equals(isValidWalk(test1[0]), test1[1])
