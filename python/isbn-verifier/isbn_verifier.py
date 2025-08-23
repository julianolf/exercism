from re import ASCII, fullmatch

def verify(isbn):
    if not fullmatch(r'^\d[\-\ ]?\d{3}[\-\ ]?\d{5}[\-\ ]?[\dxX]$', isbn, ASCII):
        return False
    chrlst = list(isbn.replace('-', '').replace(' ', '')[::-1])
    digits = map(lambda d: int(d) if d.isdecimal() else 10, chrlst)
    return sum(x * y for x, y in enumerate(digits, 1)) % 11 == 0
