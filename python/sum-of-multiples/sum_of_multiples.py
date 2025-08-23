def sum_of_multiples(limit, multiples):
	numbers = []
	for m in multiples:
		numbers += list(range(0, limit, m))
	return sum(set(numbers))
