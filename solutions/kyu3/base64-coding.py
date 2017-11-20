# encoding: UTF-8

import codewars
from base64 import encodebytes
from six import StringIO

__BASE64__ = r'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
__DECODER__ = {c: i for i, c in enumerate(__BASE64__)}
__DECODER__['='] = 0


def from_base_64(b64):
    # 这道题并不需要后缀=
    # coded = len(b64)
    # if coded > 0 and (coded % 4 != 0 or 0 <= b64.find('=') < coded - 3):
    #     raise ValueError('Illegal base64 {!r}'.format(b64))
    binary, bits, xs = 0, 0, StringIO()
    for b in b64:
        padded = b == '='
        binary = (binary << 6) + __DECODER__.get(b)
        bits += 6
        while bits >= 8:
            byte = binary >> (bits - 8)
            if byte == 0 and padded:
                break
            xs.write(chr(byte))
            binary &= 2 ** (bits - 8) - 1
            bits -= 8
    return xs.getvalue()


def to_base_64(s):
    binary, bits, xs = 0, 0, StringIO()
    for c in s:
        binary = (binary << 8) + ord(c)
        bits += 8
        while bits >= 6:
            xs.write(__BASE64__[binary >> (bits - 6)])
            binary &= 2 ** (bits - 6) - 1
            bits -= 6
    if bits > 0:
        binary <<= 6 - bits
        xs.write(__BASE64__[binary])
    # 这道题并不需要后缀=
    # rem, b64 = xs.tell() % 4, xs.getvalue()
    # return b64 if rem == 0 else b64 + '=' * (4 - rem)
    return xs.getvalue()


with codewars.Test(namespace=globals()) as Test:
    tests = [["this is a string!!", "dGhpcyBpcyBhIHN0cmluZyEh"],
             ["this is a test!", "dGhpcyBpcyBhIHRlc3Qh"],
             ["now is the time for all good men to come to the aid of their country.",
              "bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"],
             ["1234567890  ", "MTIzNDU2Nzg5MCAg"],
             ["ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"],
             ["the quick brown fox jumps over the white fence. ",
              "dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"],
             ["dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4",
              "ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"],
             ["VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna", "VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"],
             ["TVRJek5EVTJOemc1TUNBZyAg", "VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"]]

    for test in ['', 'a', 'ab', 'abc', 'abcd', 'abcde', 'TUsuRIz7qOT0x']:
        result = to_base_64(test)
        # 这道题并不需要后缀=
        ref = encodebytes(test.encode()).decode().strip().replace('=', '')
        Test.assert_equals(result, ref)
        Test.assert_equals(from_base_64(result), test)

    for test in tests:
        result = to_base_64(test[0])
        try:
            Test.assert_equals(result, test[1])
            Test.assert_equals(from_base_64(result), test[0])
        except Exception as e:
            print(e)
