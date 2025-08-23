from collections import Counter

def is_anagram(wrd1, wrd2):
    if wrd1.isupper() or wrd2.isupper():
        return False
    return Counter(wrd1.lower()) == Counter(wrd2.lower())

def find_anagrams(word, candidates):
    return [c for c in candidates if is_anagram(word, c)]
