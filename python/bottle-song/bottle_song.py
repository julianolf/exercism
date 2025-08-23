import itertools

numbers = (
    "no",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
)


def recite(start, take=1):
    song = []

    for num1, num2 in itertools.pairwise(range(start, start - (take + 1), -1)):
        txt1 = numbers[num1].capitalize()
        txt2 = numbers[num2]
        btl1 = "bottle" if num1 == 1 else "bottles"
        btl2 = "bottle" if num2 == 1 else "bottles"

        verse = [
            f"{txt1} green {btl1} hanging on the wall,",
            f"{txt1} green {btl1} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {txt2} green {btl2} hanging on the wall.",
        ]

        take -= 1
        if take > 0:
            verse.append("")

        song.extend(verse)

    return song
