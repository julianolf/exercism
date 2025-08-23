import copy
import itertools


def is_chain(dominoes):
    if dominoes[0][0] != dominoes[-1][1]:
        return False

    for i in range(len(dominoes) - 1):
        if dominoes[i][1] != dominoes[i + 1][0]:
            return False

    return True


def can_chain(dominoes):
    number_of_stones = len(dominoes)

    if number_of_stones == 0:
        return dominoes

    if number_of_stones == 1:
        if dominoes[0][0] == dominoes[0][1]:
            return dominoes
        else:
            return None

    if is_chain(dominoes):
        return dominoes

    sorted_dominoes = sorted(dominoes, key=lambda d: (d[0], d[1]))

    if is_chain(sorted_dominoes):
        return sorted_dominoes

    for chain in itertools.permutations(dominoes):
        if is_chain(chain):
            return chain

    indexes = tuple(range(number_of_stones))

    for swaps in range(1, number_of_stones + 1):
        for index_group in itertools.combinations(indexes, swaps):
            dominoes_copy = copy.deepcopy(dominoes)
            for idx in index_group:
                dominoes_copy[idx] = dominoes_copy[idx][::-1]
            for chain in itertools.permutations(dominoes_copy):
                if is_chain(chain):
                    return chain
