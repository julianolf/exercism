import itertools


def rails_iterator(rails):
    indexes = list(range(rails))
    it = itertools.cycle(indexes + indexes[-2:0:-1])
    return it


def encode(message, rails):
    it = rails_iterator(rails)
    return "".join(sorted(message, key=lambda i: next(it)))


def decode(encoded_message, rails):
    it = rails_iterator(rails)
    indexes = sorted(range(len(encoded_message)), key=lambda i: next(it))
    return "".join(c for _, c in sorted(zip(indexes, encoded_message)))
