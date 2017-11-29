# encoding: UTF-8

"""
https://www.codewars.com/kata/human-readable-duration-format
"""

import codewars


def format_duration(duration):
    def unitilze(n, unit):
        if n is 0:
            return None
        else:
            return '{} {}{}'.format(n, unit, '' if n is 1 else 's')

    if duration is 0:
        return 'now'
    minutes, seconds = divmod(duration, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)
    values = [years, days, hours, minutes, seconds]
    units = ['year', 'day', 'hour', 'minute', 'second']
    splits = list(filter(bool, [unitilze(n, unit) for n, unit in zip(values, units)]))
    csv = ', '.join(splits[:-2])
    tail = ' and '.join(splits[-2:])
    return csv + ', ' + tail if csv else tail


with codewars.Test(namespace=globals()) as test:
    test.assert_equals(format_duration(1), "1 second")
    test.assert_equals(format_duration(62), "1 minute and 2 seconds")
    test.assert_equals(format_duration(120), "2 minutes")
    test.assert_equals(format_duration(3600), "1 hour")
    test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
