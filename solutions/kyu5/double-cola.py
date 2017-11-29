# encoding: UTF-8

"""
https://www.codewars.com/kata/double-cola/train/python
"""

import math


def whoIsNext(queue, nth):
    """
    第 loop 个循环完成之后，已经喝掉了 N{\cdot}(2^{loop}-1) 罐, N = \mathbf{len}(queue)
    """
    loop = int(math.floor(math.log2((nth - 1.) / len(queue) + 1)))
    offset = ((1 << loop) - 1) * len(queue)
    return queue[(nth - offset - 1) // (1 << loop)]


import codewars

with codewars.Test(namespace=globals()) as test:
    test.assert_equals(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1), "Sheldon")
    test.assert_equals(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52), "Penny")
    test.assert_equals(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951), "Leonard")
