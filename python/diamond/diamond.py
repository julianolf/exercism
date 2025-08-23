from string import ascii_uppercase


def rows(letter):
    if letter == "A":
        return [letter]

    pos = ascii_uppercase.index(letter)
    size = pos * 2 + 1
    chars = list(ascii_uppercase[:pos])
    matrix = [f"{chars[0]:^{size}}"]

    for spaces, char in zip(range(1, len(chars[1:]) * 2, 2), chars[1:]):
        piece = char + (" " * spaces) + char
        row = f"{piece:^{size}}"
        matrix.append(row)

    middle = letter + (" " * (size - 2)) + letter

    matrix.append(middle)
    matrix.extend(matrix[:-1][::-1])

    return matrix
