"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time as t


def palindromic():
    largest = 0
    for x in range(900, 999):
        for y in range(900, 999):
            result = x * y
            palindromic = ""

            for i in str(result):
                palindromic = i + palindromic

            # If they are palindromic and the number is greater than the
            # last known largest palindromic, update it.
            if str(result) == palindromic and result > largest:
                largest = result

    return largest


start = t.time()
print(palindromic())
end = t.time()
print(end - start)
