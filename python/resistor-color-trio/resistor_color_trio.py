bands = (
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
)


def label(colors):
    ohms = bands.index(colors[0]) * 10
    ohms += bands.index(colors[1])
    ohms *= 10 ** bands.index(colors[2])

    return f"{ohms} ohms" if ohms < 1000 else f"{ohms // 1000} kiloohms"
