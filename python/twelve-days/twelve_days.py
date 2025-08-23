class TwelveDaysSong(object):
    _verse = 'On the %s day of Christmas my true love gave to me: %s.'
    _ordinal = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
        'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
    ]
    _gift = [
        'twelve Drummers Drumming', 'eleven Pipers Piping',
        'ten Lords-a-Leaping', 'nine Ladies Dancing',
        'eight Maids-a-Milking', 'seven Swans-a-Swimming',
        'six Geese-a-Laying', 'five Gold Rings',
        'four Calling Birds', 'three French Hens',
        'two Turtle Doves', 'a Partridge in a Pear Tree'
    ]

    def __init__(self, day: int = 1) -> None:
        self.day = day

    @property
    def verse(self) -> str:
        ordinal = self._ordinal[self.day - 1]
        gift_list = self._gift[-self.day:]
        gifts = gift_list.pop()
        if gift_list:
            gifts = '%s, and %s' % (', '.join(gift_list), gifts)
        return self._verse % (ordinal, gifts)

    def sing(self, till: int = 1) -> list:
        lyrics = []
        while self.day <= till:
            lyrics.append(self.verse)
            self.day += 1
        return lyrics


def recite(day: int, till: int) -> list:
    return TwelveDaysSong(day).sing(till)
