def primes(limit):
    if limit < 1:
        return []

    numbers = {k: True for k in range(2, limit + 1)}

    for i in range(2, int(limit ** 0.5) + 1):
        if numbers[i]:
            for j in range(i ** 2, limit + 1, i):
                numbers[j] = False

    return [k for k, v in numbers.items() if v]
