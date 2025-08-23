def is_triangle(a, b, c):
    if any(n <= 0 for n in [a, b, c]):
        return False
    elif any(x < y for x, y in [(a + b, c), (b + c, a), (a + c, b)]):
        return False
    else:
        return True


def is_equilateral(sides):
    a, b, c = sides
    return is_triangle(a, b, c) and (a == b == c)


def is_isosceles(sides):
    a, b, c = sides
    return is_triangle(a, b, c) and (a == b or b == c or a ==c)


def is_scalene(sides):
    a, b, c = sides
    return is_triangle(a, b, c) and (a != b != c)


def is_degenerate(sides):
    a, b, c = sides
    mix = [(a + b, c), (b + c, a), (a + c, b)]
    return is_triangle(a, b, c) and any(x == y for x, y in mix)
