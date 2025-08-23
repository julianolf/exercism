def collatz_steps(number):
    def count_steps(number):
        if number < 1:
            raise ValueError('Reached a dead end')
        if number == 1:
            return 0
        if number % 2:
            step = 3 * number + 1
        else:
            step = number // 2
        return 1 + count_steps(step)
    return count_steps(number)
