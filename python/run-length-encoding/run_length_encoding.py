import itertools
import re


def decode(string):
    chars = []

    for mtch in re.finditer(r"((?P<qtd>\d{0,2})(?P<chr>[a-zA-Z ]))", string):
        group = mtch.groupdict()
        qtd = int(group["qtd"]) if group["qtd"] else 1
        char = group["chr"]
        chars.append(char * qtd)

    return "".join(chars)


def encode(string):
    chars = []

    for char, group in itertools.groupby(string):
        qtd = len(list(group))

        if qtd > 1:
            chars.append(str(qtd))

        chars.append(char)

    return "".join(chars)
