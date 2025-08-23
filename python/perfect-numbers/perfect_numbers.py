def classify(number):
    if number < 1:
        raise ValueError('`numer` must be a positive integer.')
    aliquot_sum = sum(n for n in range(1, number) if number % n == 0)
    if aliquot_sum == number:
        return 'perfect'
    elif aliquot_sum > number:
        return 'abundant'
    else:
        return 'deficient'
