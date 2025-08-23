import re


class Phone(object):
    def __init__(self, phone_number):
        pn = re.sub(r'\D', '', phone_number)
        if not re.fullmatch(r'^1?([2-9]\d{2}){2}\d{4}$', pn):
            raise ValueError('Invalid phone number')
        self.number = pn[-10:]

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return '(%s) %s-%s' % (self.number[:3],
                               self.number[3:6],
                               self.number[6:10])
