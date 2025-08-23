SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0


def sublist(list_one: list, list_two: list) -> int:
    if list_one == list_two:
        return EQUAL

    if is_sublist(list_one, list_two):
        return SUBLIST

    if is_sublist(list_two, list_one):
        return SUPERLIST

    return UNEQUAL

def is_sublist(one: list, two: list) -> bool:
    len_one = len(one)
    len_two = len(two)

    if len_one == 0 and len_two != 0:
        return True

    iter_limit = len_two - len_one + 1

    for idx in range(iter_limit):
        if one == two[idx:(idx + len_one)]:
            return True

    return False
