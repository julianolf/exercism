def egg_count(display_value):
    counter = 0

    while display_value:
        display_value ^= display_value & (~display_value + 1)
        counter += 1

    return counter
