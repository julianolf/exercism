def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if not all(0 <= d < input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    input_val = sum(d * (input_base ** p) for p, d in enumerate(digits[::-1]))

    if input_val == 0:
        return [0]

    output_digits = []
    res = input_val
    rem = 0

    while res > 0:
        res, rem = divmod(res, output_base)
        output_digits.insert(0, rem)

    return output_digits
