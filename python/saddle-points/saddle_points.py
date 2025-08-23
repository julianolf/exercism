from itertools import product, starmap


def is_saddle_point(value, row, column):
    return value >= max(row) and value <= min(column)


def saddle_points(matrix):
    if not matrix:
        return set()

    l_size = len(matrix)
    c_size = len(matrix[0])

    if l_size > 1:
        if not all(len(row) == c_size for row in matrix[1:]):
            raise ValueError("Columns size does not match")

    i_list = product(range(l_size), range(c_size))
    rows = matrix
    cols = list(zip(*matrix))

    indexes = filter(
        lambda p: is_saddle_point(
            matrix[p[0]][p[1]],
            rows[p[0]],
            cols[p[1]]
        ),
        i_list
    )

    return set(starmap(lambda a, b: (a + 1, b + 1), indexes))
