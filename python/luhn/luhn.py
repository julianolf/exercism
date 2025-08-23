class Luhn:
    def __init__(self, card_num):
        self.card_num = "".join(card_num.split())

    def double(self, index, digit):
        if index % 2 == 0:
            return digit

        number = digit * 2

        if number > 9:
            number = number - 9

        return number

    def valid(self):
        if not self.card_num.isdigit() or len(self.card_num) <= 1:
            return False

        digits = map(int, self.card_num[::-1])
        step1 = (self.double(i, d) for i, d in enumerate(digits))
        step2 = sum(step1)

        return step2 % 10 == 0
