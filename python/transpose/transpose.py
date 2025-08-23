import itertools

FILLVALUE = "💩"


def transpose(lines):
    matrix = []
    rows = lines.splitlines()
    iterator = itertools.zip_longest(*rows, fillvalue=FILLVALUE)

    for chars in iterator:
        string = "".join(chars)
        string = string.rstrip(FILLVALUE)
        string = string.replace(FILLVALUE, " ")
        matrix.append(string)

    return "\n".join(matrix)
