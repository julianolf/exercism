import itertools


def proverb(*words, qualifier=None):
    out = []

    for word1, word2 in itertools.pairwise(words):
        out.append(f"For want of a {word1} the {word2} was lost.")

    if words:
        last_word = words[0]

        if qualifier:
            last_word = f"{qualifier} {last_word}"

        out.append(f"And all for the want of a {last_word}.")

    return out
