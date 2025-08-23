from functools import reduce

def largest_product(series, size):
    if size == 0:
        return 1
    elif not series.isdigit():
        raise ValueError('Series must be a digit only string.')
    elif len(series) < size or size < 0:
        raise ValueError('Size must be between one and series size.')
    
    ints = [int(x) for x in list(series)]
    ilen = (len(ints) - size + 1)
    prod = [reduce(lambda a, b: a * b, ints[i:(i + size)]) for i in range(ilen)]
    return max(prod)
