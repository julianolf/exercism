def append(list1, list2):
    list1 += list2
    return list1


def concat(lists):
    return [val for elem in lists for val in elem]


def filter(function, list):
    return [val for val in list if function(val)]


def length(list):
    return sum(1 for _ in list)


def map(function, list):
    return [function(val) for val in list]


def foldl(function, list, initial):
    acc = initial

    for val in list:
        acc = function(acc, val)

    return acc


def foldr(function, list, initial):
    acc = initial

    for val in reverse(list):
        acc = function(val, acc)

    return acc


def reverse(list):
    return list[::-1]
