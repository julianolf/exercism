def is_isogram(string):
    """Determine if a word or phrase is an isogram.

    An isogram (also known as a "nonpattern word") is a word or phrase
    without a repeating letter, however spaces, hyphens and apostrophes
    are allowed to appear multiple times.

    Args:
        string: Word or phrase to be checked.

    Returns:
        True if string is an isogram, False otherwise.
    """
    if type(string) is not str:
        return False

    letters = string.replace(" ", "").replace("-", "").replace("'", "").lower()

    return len(letters) == len(set(letters))
