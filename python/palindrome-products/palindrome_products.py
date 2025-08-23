from functools import wraps
from itertools import combinations_with_replacement


def validate(func):
    @wraps(func)
    def wrapper(max_factor, min_factor=0):
        if min_factor > max_factor:
            raise ValueError("min must be <= max")

        return func(max_factor, min_factor)

    return wrapper


def products(start, stop):
    seq = range(start, stop + 1)
    return (a * b for a, b in combinations_with_replacement(seq, 2))


def palindromes(numbers):
    return filter(lambda n: str(n) == str(n)[::-1], numbers)


def factors(number, min_factor, max_factor):
    facs = (
        (f, number // f)
        for f in range(min_factor, max_factor + 1)
        if (number % f == 0 and number // f >= min_factor and number // f <= max_factor)
    )
    return set(map(frozenset, facs))


def get_palindrome(which, min_factor, max_factor):
    pals = tuple(palindromes(products(min_factor, max_factor)))

    if not pals:
        return None, []

    some = which(pals)
    return some, factors(some, min_factor, max_factor)


@validate
def largest(max_factor, min_factor=0):
    return get_palindrome(max, min_factor, max_factor)


@validate
def smallest(max_factor, min_factor=0):
    if min_factor == 1:
        return 1, {(1, 1)}

    return get_palindrome(min, min_factor, max_factor)
