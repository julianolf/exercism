from re import sub
from math import ceil, sqrt
from itertools import zip_longest


def encode(plain_text: str = '') -> str:
    normalized = sub(r'\W', '', plain_text).lower()
    if not normalized:
        return ''
    length = len(normalized)
    col = ceil(sqrt(length))
    org = [normalized[i:(i + col)] for i in range(0, length, col)]
    enc = [''.join(i) for i in zip_longest(*org, fillvalue='')]
    return ' '.join(enc)
