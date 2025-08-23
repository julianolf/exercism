from math import ceil


def to_binary(number):
    bnum = bin(number)[2:]
    fsize = 7 * ceil(len(bnum) / 7)
    return bnum.zfill(fsize)


def to_base128(number):
    bnum = to_binary(number)
    nlen = len(bnum)
    func = lambda n, b: ('1', '0')[b] + n
    return tuple(func(bnum[i:(i+7)], int(i+7 == nlen)) for i in range(0, nlen, 7))


def encode(numbers):
    bin_list = [to_base128(n) for n in numbers]
    encoded = []
    for b in bin_list:
        for n in b:
            encoded.append(int(n, 2))
    return encoded


def decode(bytes_):
    bin_list = [bin(b)[2:].zfill(8) for b in bytes_]
    num_list = ['']
    blen = len(bin_list)
    valid = False
    for i, n in enumerate(bin_list):
        first_char = n[0]
        num_list[-1] += n[1:]
        if first_char == '1':
            valid = False
        else:
            valid = True
            if (i + 1) != blen:
                num_list.append('')
    
    if not valid:
        raise ValueError('Invalid sequence.')
    
    return [int(n, 2) for n in num_list]
