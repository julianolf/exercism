def sum_of_multiples(limit, multiples):
    return sum(n for n in range(limit) if any(n % m == 0 for m in multiples))
