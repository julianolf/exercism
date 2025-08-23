def triplets_with_sum(N):
    triplets = []

    for a in range(1, N // 3):
        b = ((N ** 2) // 2 - N * a) // (N - a)
        c = N - a - b

        if a < b < c and (a ** 2) + (b ** 2) == (c ** 2):
            triplets.append([a, b, c])

    return triplets
