from enum import Enum
from typing import Tuple, Union

ONE_KILOOHM = 1_000
ONE_MEGAOHM = 1_000_000

bands = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

tolerances = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}


class Unit(Enum):
    Ohms = "ohms"
    KiloOhms = "kiloohms"
    MegaOhms = "megaohms"


def into_unit(resistance: int) -> Tuple[Union[int, float], str]:
    if resistance >= ONE_MEGAOHM:
        return (resistance / ONE_MEGAOHM, Unit.MegaOhms.value)
    elif resistance >= ONE_KILOOHM:
        return (resistance / ONE_KILOOHM, Unit.KiloOhms.value)
    else:
        return (resistance, Unit.Ohms.value)


def calculate_resistance(value: int, multiplier: int) -> int:
    return value * (10**multiplier)


def resistor_label(colors):
    number = 0

    match colors:
        case [_]:
            return f"0 {Unit.Ohms.value}"
        case [colo1, colo2, _, _]:
            digit1 = bands[colo1]
            digit2 = bands[colo2]
            number = int(f"{digit1}{digit2}")
        case [colo1, colo2, colo3, _, _]:
            digit1 = bands[colo1]
            digit2 = bands[colo2]
            digit3 = bands[colo3]
            number = int(f"{digit1}{digit2}{digit3}")
        case _:
            raise ValueError(f"Invalid colors size: {colors}")

    multiplier = bands[colors[-2]]
    tolerance = tolerances[colors[-1]]

    resistance = calculate_resistance(number, multiplier)
    resistance, unit = into_unit(resistance)
    resistance = int(resistance) if resistance % 1 == 0 else resistance

    return f"{resistance} {unit} ±{tolerance}"
