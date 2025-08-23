import string

CHUNK_SIZE = 5

translation_table = str.maketrans(
    string.ascii_lowercase + string.digits,
    string.ascii_lowercase[::-1] + string.digits,
    string.punctuation + string.whitespace
)


def encode(plain_text):
    translation = plain_text.lower().translate(translation_table)
    chunks = []

    for index in range(0, len(translation), CHUNK_SIZE):
        chunk = translation[index:index+CHUNK_SIZE]
        chunks.append(chunk)

    return " ".join(chunks)


def decode(ciphered_text):
    return ciphered_text.translate(translation_table)
