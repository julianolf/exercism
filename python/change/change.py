from itertools import combinations_with_replacement


def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    if target == 0:
        return []

    if target in coins:
        return [target]

    valid_coins = [coin for coin in coins if coin < target]

    if valid_coins:
        max_coins = (target // min(valid_coins)) + 1

        for number_of_coins in range(2, max_coins):
            it = combinations_with_replacement(valid_coins, number_of_coins)
            for combination in it:
                if sum(combination) == target:
                    return sorted(combination)

    raise ValueError("can't make target with given coins")
