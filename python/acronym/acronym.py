import re


def abbreviate(words):
    if type(words) is not str:
        return ""

    word_list = re.split(r"[\s_-]", words)
    acronym = [word[0].upper() for word in word_list if word]

    return "".join(acronym)
