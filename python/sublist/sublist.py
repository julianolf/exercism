"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    length_one = len(list_one)
    length_two = len(list_two)

    if length_one + length_two == 0:
        return EQUAL

    if length_two == 0:
        return SUPERLIST

    if length_one == 0:
        return SUBLIST

    if list_one == list_two:
        return EQUAL

    if length_one == length_two:
        return UNEQUAL

    if length_one < length_two:
        start = 0

        while start < length_two:
            try:
                idx = list_two.index(list_one[0], start)
            except ValueError:
                return UNEQUAL

            if list_one == list_two[idx:idx + length_one]:
                return SUBLIST

            start = idx + 1

        return UNEQUAL

    if length_one > length_two:
        start = 0

        while start < length_one:
            try:
                idx = list_one.index(list_two[0], start)
            except ValueError:
                return UNEQUAL

            if list_two == list_one[idx:idx + length_two]:
                return SUPERLIST

            start = idx + 1

        return UNEQUAL
