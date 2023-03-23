def fib(limit):
    sumEven = 0
    a, b = 0, 1
    while b < limit:
        if b % 2 == 0: sumEven += b
        tmp = a + b
        a, b = b, tmp

    return sumEven


print(fib(4000000))
