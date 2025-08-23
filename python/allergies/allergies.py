class Allergies(object):
    known = [
        'eggs', 'peanuts', 'shellfish', 'strawberries',
        'tomatoes', 'chocolate', 'pollen', 'cats'
    ]

    def __init__(self, score):
        self.lst = [n for i, n in enumerate(self.known) if score & (1 << i)]

    def is_allergic_to(self, item):
        return item in self.lst
