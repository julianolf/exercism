from re import sub
from math import ceil, sqrt


def encode(plain_text: str = '') -> str:
    normalized = sub(r'\W', '', plain_text).lower()
    if not normalized:
        return ''
    length = len(normalized)
    col = ceil(sqrt(length))
    org = [normalized[i:(i + col)].ljust(col) for i in range(0, length, col)]
    enc = [''.join(i) for i in zip(*org)]
    return ' '.join(enc)
