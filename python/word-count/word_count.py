from collections import Counter
from re import findall


def word_count(phrase):
    words = findall(r'(\w+\'?\w|\d+)', phrase.replace('_', ' ').lower())
    return Counter(words)
