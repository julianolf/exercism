from string import ascii_lowercase as lc, ascii_uppercase as uc

def rotate(text, key):
    i = key % 26
    if i == 0:
        return text
    trans_table = str.maketrans((lc + uc), (lc[i:] + lc[:i] + uc[i:] + uc[:i]))
    return text.translate(trans_table)
