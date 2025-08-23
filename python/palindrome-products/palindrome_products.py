def is_palindrome(number):
    string = str(number)
    return string == string[::-1]

def factors(palindrome, min_factor, max_factor):
    pairs = set()

    for number in range(min_factor, max_factor + 1):
        res, rem = divmod(palindrome, number)
        if rem == 0 and (min_factor <= res <= max_factor):
            pairs.add((number, res))

    return pairs

def palindrome_factors(min_factor, max_factor, products_range):
    pairs = set()

    for number in products_range:
        if is_palindrome(number):
            pairs = factors(number, min_factor, max_factor)
            if pairs:
                return number, pairs

    return None, pairs

def validate(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

def largest(max_factor, min_factor=0):
    validate(min_factor, max_factor)

    start = max_factor ** 2
    stop = min_factor ** 2 - 1
    products_range = range(start, stop, -1)

    return palindrome_factors(min_factor, max_factor, products_range)


def smallest(max_factor, min_factor=0):
    validate(min_factor, max_factor)

    start = min_factor ** 2
    stop = max_factor ** 2
    products_range = range(start, stop)

    return palindrome_factors(min_factor, max_factor, products_range)
