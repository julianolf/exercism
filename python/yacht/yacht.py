# Score categories
# Change the values as you see fit
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12


class Dice:
    def __init__(self, values):
        self.values = values
    
    @property
    def values(self):
        return self._values
    
    @values.setter
    def values(self, values):
        if type(values) is not list or not all(type(v) is int for v in values):
            raise Exception('`values` must be a list of integers.')
        if len(values) != 5:
            raise Exception('`values` must contain exactly five elements.')
        if not all(v > 0 and v < 7 for v in values):
            raise Exception('`values` must be integers between 1 and 6.')
        
        self._values = values
        self._values.sort()
    
    @property
    def smaller(self):
        return self._values[0]
    
    @property
    def bigger(self):
        return self._values[-1]
    
    def count(self, value):
        return self._values.count(value)
    
    def sum(self):
        return sum(self._values)
    
    def biggie_smalls(self):
        '''Even when I was wrong, I got my point across. - Biggie Smalls'''
        biggie = self._values.count(self.bigger)
        smalls = self._values.count(self.smaller)
        return biggie, smalls
    
    def same(self):
        return len(set(self._values)) == 1


class Yacht:
    _categories = {
        ONES: '_sum_by_face',
        TWOS: '_sum_by_face',
        THREES: '_sum_by_face',
        FOURS: '_sum_by_face',
        FIVES: '_sum_by_face',
        SIXES: '_sum_by_face',
        FULL_HOUSE: '_full_house',
        FOUR_OF_A_KIND: '_four_of_a_kind',
        LITTLE_STRAIGHT: '_little_straight',
        BIG_STRAIGHT: '_big_straight',
        CHOICE: '_choice',
        YACHT: '_yacht'
    }

    def __init__(self, dice, category):
        self.dice = dice
        self.category = category
    
    @property
    def dice(self):
        return self._dice
    
    @dice.setter
    def dice(self, dice):
        if not isinstance(dice, Dice):
            raise Exception('`dice` is not a Dice instance.')
        
        self._dice = dice
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if type(category) is not int or category not in self._categories:
            raise Exception('invalid category.')
        
        self._category = category
    
    def _sum_by_face(self):
        face = self._category
        return face * self._dice.count(face)
    
    def _full_house(self):
        biggie, smalls = self._dice.biggie_smalls()
        if biggie == 4 or smalls == 4:
            return 0
        elif biggie + smalls == 5:
            return self._dice.sum()
        else:
            return 0
    
    def _four_of_a_kind(self):
        biggie, smalls = self._dice.biggie_smalls()
        if smalls >= 4:
            return self._dice.sum() - self._dice.bigger
        elif biggie == 4:
            return self._dice.sum() - self._dice.smaller
        else:
            return 0
    
    def _little_straight(self):
        if self._dice.values == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0
    
    def _big_straight(self):
        if self._dice.values == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0
    
    def _choice(self):
        return self._dice.sum()

    def _yacht(self):
        return 50 if self._dice.same() else 0

    def score(self):
        calc = getattr(self, self._categories[self._category])
        return calc()

def score(dice, category):
    dc = Dice(dice)
    game = Yacht(dc, category)
    return game.score()
