from operator import itemgetter


def raindrops(number):
    rain = {3: "Pling", 5: "Plang", 7: "Plong"}
    drops = set(rain.keys())
    factors = {f for f in range(1, number + 1) if number % f == 0}

    if drops.isdisjoint(factors):
        return str(number)

    which = drops & factors
    speak = itemgetter(*which)(rain)

    return "".join(speak)
