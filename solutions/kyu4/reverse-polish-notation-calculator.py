# encoding: UTF-8

"""
https://www.codewars.com/kata/reverse-polish-notation-calculator
"""

import codewars
import operator


def calc(expr):
    stack = [0]
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    for token in expr.split():
        op = ops.get(token, None)
        if op is None:
            stack.append(float(token) if '.' in token else int(token))
        else:
            rhs = stack.pop()
            lhs = stack.pop()
            stack.append(op(lhs, rhs))
    return stack.pop()


with codewars.Test(namespace=globals()) as Test:
    Test.assert_equals(calc(""), 0, "Should work with empty string")
    Test.assert_equals(calc("1 2 3"), 3, "Should parse numbers")
    Test.assert_equals(calc("1 2 3.5"), 3.5, "Should parse float numbers")
    Test.assert_equals(calc("1 3 +"), 4, "Should support addition")
    Test.assert_equals(calc("1 3 *"), 3, "Should support multiplication")
    Test.assert_equals(calc("1 3 -"), -2, "Should support subtraction")
    Test.assert_equals(calc("4 2 /"), 2, "Should support division")
