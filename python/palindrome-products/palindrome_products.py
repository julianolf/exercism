from collections import defaultdict
from functools import cache
from itertools import product


@cache
def is_palindrome(number):
    string = str(number)
    return string == string[::-1]

def get_palindrome(start, stop):
    palindromes = defaultdict(list)

    for a, b in product(range(start, stop + 1), repeat=2):
        number = a * b

        if is_palindrome(number):
            palindromes[number].append([a, b])

    return palindromes


def largest(max_factor, min_factor=0):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    palindromes = get_palindrome(min_factor, max_factor)

    if not palindromes:
        return None, []

    key = max(palindromes.keys())

    return key, palindromes[key]


def smallest(max_factor, min_factor=0):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    if min_factor == 1:
        return 1, {(1, 1)}

    palindromes = get_palindrome(min_factor, max_factor)

    if not palindromes:
        return None, []

    key = min(palindromes.keys())

    return key, palindromes[key]
