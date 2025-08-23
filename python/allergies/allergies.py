from enum import Flag, auto


class KnownAllergies(Flag):
    eggs = auto()
    peanuts = auto()
    shellfish = auto()
    strawberries = auto()
    tomatoes = auto()
    chocolate = auto()
    pollen = auto()
    cats = auto()


class Allergies(object):

    def __init__(self, score: int) -> None:
        self.has = KnownAllergies(score & 255)

    def is_allergic_to(self, item: str) -> bool:
        return KnownAllergies[item] in self.has
    
    @property
    def lst(self) -> list:
        return [i.name for i in list(KnownAllergies) if self.is_allergic_to(i.name)]
