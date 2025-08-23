from string import ascii_uppercase


def rows(letter):
    chars = list(ascii_uppercase[:ascii_uppercase.index(letter) + 1])
    letters = chars[:-1] + chars[::-1]
    mirror = chars[::-1] + chars[1:]

    diamond = []

    for char in letters:
        row = []

        for m_char in mirror:
            if m_char == char:
                row.append(char)
            else:
                row.append(" ")

        diamond.append("".join(row))

    return diamond
