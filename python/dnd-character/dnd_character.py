import random


class Character:
    def __init__(self):
        self.strength = self.random_score()
        self.dexterity = self.random_score()
        self.constitution = self.random_score()
        self.intelligence = self.random_score()
        self.wisdom = self.random_score()
        self.charisma = self.random_score()
        self.modifier = modifier(self.constitution)
        self.hitpoints = 10 + self.modifier

    def random_score(self):
        dices = sorted(random.randint(1, 6) for _ in range(4))

        return sum(dices[1:])

    def ability(self):
        return max(
            (
                self.strength,
                self.dexterity,
                self.constitution,
                self.intelligence,
                self.wisdom,
                self.charisma,
            )
        )


def modifier(constitution):
    return (constitution - 10) // 2
