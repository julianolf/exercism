from math import gcd
from itertools import product, combinations


def primitive_triplets(b):
    if b % 4:
        raise ValueError('`b` must be an integer divisible by 4')

    def is_valid_mn(m, n):
        return (m > n and (m - n) > 0
                and (m - n) % 2 and gcd(m, n) == 1)

    seq = range(1, b)
    mns = [(m, n) for m, n in product(seq, seq)
           if is_valid_mn(m, n) and (2 * m * n) == b]

    triples = []
    for m, n in mns:
        a = (m ** 2) - (n ** 2)
        c = (m ** 2) + (n ** 2)
        t = (a, b, c)
        if is_triplet(t):
            triple = tuple(sorted(t))
            triples.append(triple)

    return set(triples)


def triplets_in_range(range_start, range_end):
    triples = []
    for b in range(range_start, range_end + 1):
        try:
            triples += list(primitive_triplets(b))
        except ValueError:
            pass  # Invalid value for b

    return set([t for t in triples
                if min(t) >= range_start and max(t) <= range_end])


def is_triplet(triple):
        a, b, c = sorted(triple)
        return ((a ** 2) + (b ** 2) == (c ** 2)
                and all(gcd(x, y) == 1
                        for x, y in combinations((a, b, c), 2)))
