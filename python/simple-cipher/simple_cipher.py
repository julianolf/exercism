from itertools import cycle
from operator import add, sub
from random import choice
from string import ascii_lowercase as chars

S = 97
L = 26


class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = "".join(choice(chars) for _ in range(100))
        else:
            self.key = key.lower()

    def _translate(self, text, op):
        it = zip(text, cycle(self.key))

        return "".join(chars[op(ord(a) % S, ord(b) % S) % L] for a, b in it)

    def encode(self, text):
        return self._translate(text, add)

    def decode(self, text):
        return self._translate(text, sub)
