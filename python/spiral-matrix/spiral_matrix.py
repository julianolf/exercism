def spiral_matrix(size):
    numbers = list(range(1, size**2 + 1))
    left, right, top, bottom = (0, size - 1, 0, size - 1)
    x, y = (0, 0)
    direction = (1, 0)
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    for number in numbers:
        matrix[y][x] = number

        if direction == (1, 0) and x + direction[0] > right:
            direction = (0, 1)
            top += 1
        elif direction == (0, 1) and y + direction[1] > bottom:
            direction = (-1, 0)
            right -= 1
        elif direction == (-1, 0) and x + direction[0] < left:
            direction = (0, -1)
            bottom -= 1
        elif direction == (0, -1) and y + direction[1] < top:
            direction = (1, 0)
            left += 1

        x += direction[0]
        y += direction[1]

    return matrix
