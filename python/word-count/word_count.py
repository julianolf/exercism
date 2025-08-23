from re import findall
from collections import Counter


def word_count(phrase):
    words = findall(r'\b[a-z0-9]+\'?[a-z]?\b', phrase.replace('_', ' ').lower())
    return dict(Counter(words))
