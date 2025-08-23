import re
from collections import Counter


def is_isogram(string):
    string = re.sub(r"[\s-]+", "", string.lower())
    if not string:
        return True
    most_common = Counter(string).most_common(1)
    return 1 == most_common[0][1]
