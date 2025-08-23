import math


def primes(limit):
    if limit < 1:
        return []
    a = {k: True for k in range(2, limit + 1)}
    for i in range(2, round(math.sqrt(limit)) + 1):
        if a[i]:
            for j in range(i**2, limit + 1, i):
                a[j] = False
    primes = dict(filter(lambda i: i[1], a.items()))
    return list(primes.keys())
