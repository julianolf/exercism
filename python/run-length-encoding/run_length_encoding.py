import re


def decode(string):
    if not string:
        return string

    chars = []

    for mtch in re.finditer(r"((?P<qtd>\d{0,2})(?P<chr>[a-zA-Z ]))", string):
        group = mtch.groupdict()
        qtd = int(group["qtd"]) if group["qtd"] else 1
        char = group["chr"]
        chars.append(char * qtd)

    return "".join(chars)


def encode(string):
    if not string:
        return string

    counter = []
    current = [1, string[0]]

    end = len(string) - 2

    for idx, char in enumerate(string[1:]):
        if char == current[1]:
            current[0] += 1
        else:
            counter.append(current)
            current = [1, char]

        if idx == end:
            counter.append(current)

    chars = [str(val) for item in counter for val in item if val != 1]

    return "".join(chars)
