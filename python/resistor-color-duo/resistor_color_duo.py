color_bands = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):
    first_digit = color_bands.index(colors[0])
    second_digit = color_bands.index(colors[1])

    return first_digit * 10 + second_digit
