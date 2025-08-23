import re


class Phone(object):
    def __init__(self, phone_number):
        pn = re.sub(r'\D', '', phone_number)
        fn = re.fullmatch(
            r'^1?([2-9]\d{2})([2-9]\d{2})(\d{4})$', pn)
        if not fn:
            raise ValueError('Invalid phone number')
        self._number = fn.groups()

    @property
    def number(self):
        return ''.join(self._number)

    @property
    def area_code(self):
        return self._number[0]

    def pretty(self):
        return '(%s) %s-%s' % self._number
