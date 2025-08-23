import math


def score(x, y):
    radius = math.ceil(math.sqrt(pow(x, 2) + pow(y, 2)))

    if 0 <= radius <= 1:
        return 10

    if 2 <= radius <= 5:
        return 5

    if 6 <= radius <= 10:
        return 1

    return 0
