MASK = 128

def encode(numbers):
    encoded = []
    for number in reversed(numbers):
        encoded.insert(0, 0)
        while True:
            encoded[0] |= number & (MASK - 1)
            number >>= 7
            if number <= 0:
                break
            encoded.insert(0, MASK)
    return encoded

def decode(bytes_):
    decoded = []
    value = 0
    for byte in bytes_:
        value = (value << 7) | (byte & ~(MASK))
        if (byte & MASK) <= 0:
            decoded.append(value)
            value = 0
    
    if (byte & MASK) != 0:
        raise ValueError('Invalid sequence.')
    
    return decoded
