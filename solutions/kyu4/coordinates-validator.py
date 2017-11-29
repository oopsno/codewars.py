# encoding: UTF-8

"""
https://www.codewars.com/kata/coordinates-validator
"""

import codewars


def is_valid_coordinates(coordinates):
    import re
    match = re.match(r'^\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*$', coordinates)
    if match is None:
        return False
    latitude, longitude = map(float, match.groups())
    return 0 <= abs(latitude) <= 90 and 0 <= abs(longitude) <= 180


with codewars.Test(namespace=globals()) as test:
    test.describe("Example Test Cases")

    test.it("should return true for valid coordinates")
    valid_coordinates = [
        "-23, 25",
        "4, -3",
        "24.53525235, 23.45235",
        "04, -23.234235",
        "43.91343345, 143"
    ]

    for coordinate in valid_coordinates:
        test.expect(is_valid_coordinates(coordinate), "%s validation failed." % coordinate)

    test.it("should return false for invalid coordinates")
    invalid_coordinates = [
        "23.234, - 23.4234",
        "2342.43536, 34.324236",
        "N23.43345, E32.6457",
        "99.234, 12.324",
        "6.325624, 43.34345.345",
        "0, 1,2",
        "0.342q0832, 1.2324",
        "23.245, 1e1"
    ]

    for coordinate in invalid_coordinates:
        test.expect(not is_valid_coordinates(coordinate), "%s validation failed." % coordinate)
