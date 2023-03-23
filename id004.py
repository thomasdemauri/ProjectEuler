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
            # last known palindromic, update it.
            if str(result) == palindromic and result > largest:
                largest = result

    return largest


begin = t.time()
print(palindromic())
end = t.time()
print(end - begin)
