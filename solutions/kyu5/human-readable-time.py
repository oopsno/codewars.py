# encoding: UTF-8

"""
https://www.codewars.com/kata/human-readable-time
"""

import codewars


def make_readable(seconds):
    assert 0 <= seconds <= 359999
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)


with codewars.Test(namespace=globals()) as test:
    test.assert_equals(make_readable(0), "00:00:00")
    test.assert_equals(make_readable(5), "00:00:05")
    test.assert_equals(make_readable(60), "00:01:00")
    test.assert_equals(make_readable(86399), "23:59:59")
    test.assert_equals(make_readable(359999), "99:59:59")
