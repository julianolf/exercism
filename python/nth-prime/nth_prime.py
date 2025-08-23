def gen_primes():
    """
    Sieve of Eratosthenes
    Code by David Eppstein, UC Irvine, 28 Feb 2002
    http://code.activestate.com/recipes/117119/
    """
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")

    primes = gen_primes()

    for _ in range(number - 1):
        next(primes)

    return next(primes)
