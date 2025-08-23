def prime_factors(natural_number):
    i = 2
    factors = []
    while i * i <= natural_number:
        if natural_number % i:
            i += 1
        else:
            natural_number //= i
            factors.append(i)
    if natural_number > 1:
        factors.append(natural_number)
    return factors
