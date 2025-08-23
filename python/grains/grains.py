# The problem is a simple geometric progression.
# We can simplify the formulas by assuming that:
# The first term is 1;
# The common ratio is 2.

def check_interval(number):
    if number < 1 or number > 64:
        raise ValueError('Invalid position')


def on_square(nth):
    check_interval(nth)
    return 2 ** (nth - 1)


def total_after(nth):
    check_interval(nth)
    return (2 ** nth) - 1
