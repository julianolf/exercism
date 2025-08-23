from itertools import combinations

def is_triangle(f):
    return lambda s: all(s) and (2 * max(s) <= sum(s)) and f(s)


@is_triangle
def is_equilateral(sides):
    return len(set(sides)) == 1


@is_triangle
def is_isosceles(sides):
    return len(set(sides)) < 3


@is_triangle
def is_scalene(sides):
    return len(set(sides)) == 3


@is_triangle
def is_degenerate(sides):
    return any(x == sum(sides) - x for x in map(sum, combinations(sides, 2)))
