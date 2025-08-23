from secrets import choice
from string import ascii_uppercase, digits

class Robot(object):
    def __init__(self):
        self._gen_name()
    
    def _gen_name(self):
        ch = [choice(ascii_uppercase) for _ in range(2)]
        dg = [choice(digits) for _ in range(3)]
        self.name = ''.join(ch + dg)
    
    def reset(self):
        self._gen_name()
