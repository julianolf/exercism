import re

pattern = re.compile(r"^(?!yt|xr)(y|[^aeiou]?qu|[^aeiouy]+)(.*)?", flags=re.I)

def translate(text):
    words = []

    for word in text.split():
        match = pattern.match(word)

        if match:
            words.append(match.group(2) + match.group(1) + "ay")
        else:
            words.append(word + "ay")

    return " ".join(words)
