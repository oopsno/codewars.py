# encoding: UTF-8

"""
https://www.codewars.com/kata/pete-the-baker
"""

import codewars


def cakes(recipe, available):
    return min([available.get(key, 0) // value for key, value in recipe.items()])


with codewars.Test(namespace=globals()) as test:
    test.describe('Testing Pete, the Baker')
    test.it('gives us the right number of cakes')

    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    test.assert_equals(cakes(recipe, available), 2, 'Wrong result for example #1')

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    test.assert_equals(cakes(recipe, available), 0, 'Wrong result for example #2')
