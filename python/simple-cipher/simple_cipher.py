from itertools import cycle
from operator import add, sub
from random import choice
from string import ascii_lowercase


class Cipher:
    def __init__(self, key=None):
        if isinstance(key, str) and len(key.strip()) > 0:
            self.key = key.lower()
        else:
            self.key = self._random_key()

    def _random_key(self):
        chars = [choice(ascii_lowercase) for _ in range(100)]
        return "".join(chars)

    def _translate(self, text, op):
        iterkey = cycle(self.key)
        chars = []

        for char in text:
            key = next(iterkey)
            key_idx = ascii_lowercase.index(key)
            chr_idx = ascii_lowercase.index(char)
            nxt_idx = op(chr_idx, key_idx) % 26
            nxt_chr = ascii_lowercase[nxt_idx]
            chars.append(nxt_chr)

        return "".join(chars)

    def encode(self, text):
        return self._translate(text, add)

    def decode(self, text):
        return self._translate(text, sub)
