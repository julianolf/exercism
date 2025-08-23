from enum import IntEnum, auto
from collections import Counter

DECK = {
    '2C': (2, 'C'), '2D': (2, 'D'), '2H': (2, 'H'), '2S': (2, 'S'),
    '3C': (3, 'C'), '3D': (3, 'D'), '3H': (3, 'H'), '3S': (3, 'S'),
    '4C': (4, 'C'), '4D': (4, 'D'), '4H': (4, 'H'), '4S': (4, 'S'),
    '5C': (5, 'C'), '5D': (5, 'D'), '5H': (5, 'H'), '5S': (5, 'S'),
    '6C': (6, 'C'), '6D': (6, 'D'), '6H': (6, 'H'), '6S': (6, 'S'),
    '7C': (7, 'C'), '7D': (7, 'D'), '7H': (7, 'H'), '7S': (7, 'S'),
    '8C': (8, 'C'), '8D': (8, 'D'), '8H': (8, 'H'), '8S': (8, 'S'),
    '9C': (9, 'C'), '9D': (9, 'D'), '9H': (9, 'H'), '9S': (9, 'S'),
    '10C': (10, 'C'), '10D': (10, 'D'), '10H': (10, 'H'), '10S': (10, 'S'),
    'JC': (11, 'C'), 'JD': (11, 'D'), 'JH': (11, 'H'), 'JS': (11, 'S'),
    'QC': (12, 'C'), 'QD': (12, 'D'), 'QH': (12, 'H'), 'QS': (12, 'S'),
    'KC': (13, 'C'), 'KD': (13, 'D'), 'KH': (13, 'H'), 'KS': (13, 'S'),
    'AC': (14, 'C'), 'AD': (14, 'D'), 'AH': (14, 'H'), 'AS': (14, 'S')
}


class HandRanking(IntEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE_KIND = auto()
    STRAIGHT = auto()
    FLUSH = auto()
    FULL_HOUSE = auto()
    FOUR_KIND = auto()
    STRAIGHT_FLUSH = auto()


class Hand(object):
    _SEQ = list(range(2, 15))

    def __init__(self, hand=''):
        self.ihand = hand
        self.cards = sorted([DECK[c] for c in set(hand.split())])
        if len(self.cards) != 5:
            raise ValueError('Invalid number of cards')
        self.ranks = []
        self.suits = []
        for r, s in self.cards:
            self.ranks.append(r)
            self.suits.append(s)
        self.uranks = Counter(self.ranks)
        self.cranks = sorted(self.uranks.values())
        self.set_rank()
        self.rank_low()

    def __eq__(self, other):
        return self.rank == other.rank and self.ranks == other.ranks

    def __gt__(self, other):
        if self.rank == other.rank:
            if self.rank in [HandRanking.FOUR_KIND, HandRanking.FULL_HOUSE,
                             HandRanking.THREE_KIND, HandRanking.TWO_PAIR,
                             HandRanking.ONE_PAIR]:
                l1 = [v for v, _ in self.uranks.most_common()]
                l2 = [v for v, _ in other.uranks.most_common()]
                if self.rank == HandRanking.TWO_PAIR:
                    l1 = list(reversed(sorted(l1[0:2]))) + l1[2:3]
                    l2 = list(reversed(sorted(l2[0:2]))) + l2[2:3]
                elif self.rank != HandRanking.FULL_HOUSE:
                    l1 = l1[0:1] + list(reversed(sorted(l1[1:])))
                    l2 = l2[0:1] + list(reversed(sorted(l2[1:])))
                self_other = zip(l1, l2)
            else:
                self_other = zip(reversed(self.ranks), reversed(other.ranks))
            for s, o in self_other:
                if s == o:
                    continue
                return s > o
        return self.rank > other.rank

    def __ge__(self, other):
        return self > other or self == other

    def __repr__(self):
        return self.ihand

    def straight_flush(self):
        return self.straight() and self.flush()

    def four_of_a_kind(self):
        return [1, 4] == self.cranks

    def full_house(self):
        return [2, 3] == self.cranks

    def flush(self):
        return len(set(self.suits)) == 1

    def straight(self):
        start = self._SEQ.index(self.ranks[0])
        size = 4 if self.ranks[-1] == 14 else 5
        seq1 = self.ranks[:size]
        seq2 = self._SEQ[start:start+size]
        if seq1 == seq2:
            if len(seq1) == 5:
                return True
            else:
                return min(seq1) == 2 or max(seq1) == 13
        return False

    def three_of_a_kind(self):
        return [1, 1, 3] == self.cranks

    def two_pair(self):
        return [1, 2, 2] == self.cranks

    def one_pair(self):
        return [1, 1, 1, 2] == self.cranks

    def set_rank(self):
        if self.straight_flush():
            self.rank = HandRanking.STRAIGHT_FLUSH
        elif self.four_of_a_kind():
            self.rank = HandRanking.FOUR_KIND
        elif self.full_house():
            self.rank = HandRanking.FULL_HOUSE
        elif self.flush():
            self.rank = HandRanking.FLUSH
        elif self.straight():
            self.rank = HandRanking.STRAIGHT
        elif self.three_of_a_kind():
            self.rank = HandRanking.THREE_KIND
        elif self.two_pair():
            self.rank = HandRanking.TWO_PAIR
        elif self.one_pair():
            self.rank = HandRanking.ONE_PAIR
        else:
            self.rank = HandRanking.HIGH_CARD

    def rank_low(self):
        if ((self.rank == HandRanking.STRAIGHT_FLUSH
            or self.rank == HandRanking.STRAIGHT)
                and min(self.ranks) == 2
                and max(self.ranks) == 14):
            _, suit = self.cards.pop()
            rank = self.ranks.pop() - 13
            self.cards.insert(0, (rank, suit))
            self.ranks.insert(0, rank)
            self.uranks = Counter(self.ranks)


class Poker(object):
    def __init__(self, hands=[]):
        self.hands = hands

    def winners(self):
        highest_ranking = max(self.hands)
        return [str(h) for h in self.hands if h == highest_ranking]


def best_hands(hands):
    poker = Poker([Hand(h) for h in hands])
    return poker.winners()
