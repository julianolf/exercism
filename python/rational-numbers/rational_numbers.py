from __future__ import division
from math import gcd


class Rational(object):
    def __init__(self, numer, denom):
        sign = (-1 if denom < 0 else 1)
        self.numer = (int(numer / gcd(numer, denom)) * sign)
        self.denom = (int(denom / gcd(numer, denom)) * sign)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = (self.numer * other.denom) + (other.numer * self.denom)
        denom = (self.denom * other.denom)
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = (self.numer * other.denom) - (other.numer * self.denom)
        denom = (self.denom * other.denom)
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = (self.numer * other.numer)
        denom = (self.denom * other.denom)
        return Rational(numer, denom)

    def __truediv__(self, other):
        sign = (-1 if other.numer < 0 else 1)
        numer = (self.numer * (other.denom * sign))
        denom = (self.denom * (other.numer * sign))
        if denom == 0:
            raise ZeroDivisionError
        return Rational(numer, denom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if type(power) is Rational:
            raise NotImplementedError
        numer = (self.denom if power < 0 else self.numer) ** abs(power)
        denom = (self.numer if power < 0 else self.denom) ** abs(power)
        return Rational(numer, denom)

    def __rpow__(self, base):
        if type(base) is Rational:
            raise NotImplementedError
        return (base ** self.numer) ** (1. / self.denom)
