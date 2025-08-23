BOOK_PRICE = 8

DISCOUNT = {
    1: 0,
    2: 0.05,
    3: 0.1,
    4: 0.2,
    5: 0.25,
}


def calculate(books):
    discount = BOOK_PRICE * DISCOUNT.get(books, 0)

    return int(books * (BOOK_PRICE - discount) * 100)


def rearrange(groups):
    while {5, 3} <= set(groups):
        groups.remove(5)
        groups.remove(3)
        groups.extend([4, 4])


def total(basket):
    if len(basket) == 0:
        return 0

    basket_copy = basket[:]
    groups = []

    while len(basket_copy) > 0:
        group = set(basket_copy)

        for book in group:
            basket_copy.remove(book)

        groups.append(len(group))

    rearrange(groups)

    return sum(map(calculate, groups))
