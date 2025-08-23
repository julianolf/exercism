HS = {
    'wink': 1,
    'double blink': 2,
    'close your eyes': 4,
    'jump': 8
}
RV = 16


def handshake(code):
    secret = [h for h, c in HS.items() if code & c]
    return secret[::-1] if code & RV else secret


def secret_code(actions):
    code = [HS.get(a, 0) for a in actions]
    if code != sorted(code):
        code.append(RV)
    return sum(code)
