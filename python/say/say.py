NUMBERS = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
    18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
    40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
    80: 'eighty', 90: 'ninety'
}

SCALE = ['billion', 'million', 'thousand', 'hundred']


def number_to_words(number):
    h = number // 100
    d = number % 100
    u = number % 10
    words = []

    if h:
        words.append('%s %s' % (NUMBERS.get(h), SCALE[-1]))
    if d:
        if d in NUMBERS:
            words.append(NUMBERS.get(d))
        else:
            words.append('%s-%s' % (NUMBERS.get(d-u),
                                    NUMBERS.get(u)))
    elif u:
        words.append(NUMBERS.get(u))

    return ' and '.join(words)


def say(number):
    if not (-1 < number < 1e12):
        raise ValueError('Number out of limit.')

    if number in NUMBERS:
        return NUMBERS.get(number)

    words = []
    for i, scale in enumerate((1e9, 1e6, 1e3)):
        diff = number // scale
        if diff:
            num = '%s %s' % (number_to_words(diff), SCALE[i])
            words.append(num)
            number -= (diff * scale)
    else:
        if number:
            num = number_to_words(number)
            words.append(num)

    return ' '.join(words)
