# Primos menores que 20 --> 2, 5, 7, 11, 13, 17, 19
# Compostos             --> 4, 6, 8, 10, 12, 14, 16, 18, 20
# MMC (Compostos)       --> 2 * 2 * 2 * 2 * 3 * 3 * 5 --> 2**4 * 3**2 * 5
# MMC (1, 20)           --> 16 * 9 * 5 * 7 * 11 * 13 * 17 * 19

import numpy as np


def get_primes(limit):
    # 2 is already included because is the only
    # even number that is a prime number
    primes = [2]
    curr_number = 3

    while curr_number <= limit:
        # If it is not equal to zero means that
        # current number is divisible by other
        has_multiples = 0
        for divider in range(2, curr_number):
            if curr_number % divider == 0:
                has_multiples = has_multiples + 1

        if has_multiples == 0:
            primes.append(curr_number)

        curr_number = curr_number + 1

    return primes


def get_compound_numbers(limit):
    primes = set(get_primes(limit))
    all_numbers = set()

    for n in range(2, limit + 1):
        all_numbers.add(n)


print(get_compound_numbers(20))
