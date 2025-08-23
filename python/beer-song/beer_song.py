class BeerSong(object):
    verses = {
        'one': '%s of beer on the wall, %s of beer.',
        'two': 'Take %s down and pass it around, %s of beer on the wall.',
        'end': 'Go to the store and buy some more, 99 bottles of beer on the wall.'
    }

    def __init__(self, bottles: int = 0) -> None:
        self.bottles = bottles
    
    @property
    def first_verse(self) -> str:
        bottles = self._how_many()
        return self.verses['one'] % (bottles.capitalize(), bottles)
    
    @property
    def second_verse(self) -> str:
        if self.bottles:
            return self.verses['two'] % self._take_one()
        else:
            return self.verses['end']

    def _how_many(self) -> str:
        n = self.bottles if self.bottles > 0 else 'no more'
        b = 'bottles' if self.bottles != 1 else 'bottle'
        return '%s %s' % (n, b)
    
    def _take_one(self) -> tuple:
        n = 'it' if self.bottles == 1 else 'one'
        self.bottles -= 1
        b = self._how_many()
        return (n, b)
    
    def cheers(self) -> list:
        return [self.first_verse, self.second_verse]

def recite(start: int, take: int = 1) -> list:
    song = BeerSong(start)
    lyrics = []
    for i in range(take):
        lyrics += song.cheers()
        if i < (take - 1):
            lyrics += [''] # WHYYYYYY?!?!
    return lyrics
