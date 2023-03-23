n = 600851475143.0
i = 2.0
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1

print(n)
