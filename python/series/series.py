def slices(s, l):
    if not s:
        raise ValueError('Invalid serie')
    elif not l:
        raise ValueError('Length cannot be zero')
    elif l < 0:
        raise ValueError('Length cannot be negative')
    elif l > len(s):
        raise ValueError('Length cannot be greater than series')

    return [s[i:i+l] for i in range(len(s) - l + 1)]
