import re


def abbreviate(words):
    acronym = [word[0].upper() for word in re.split(r"[\s_-]+", words)]

    return "".join(acronym)
