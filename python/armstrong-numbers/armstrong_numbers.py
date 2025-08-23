def is_armstrong(number):
    if type(number) != int or number < 0:
        raise ValueError('Not a natural number')
    if number == 0:
        return True
    str_nm = str(number)
    digits = len(str_nm)
    return number == sum(int(d) ** digits for d in str_nm)
