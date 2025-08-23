class Clock:
    def __init__(self, hour, minute):
        self.seconds = ((hour - (hour // 24 * 24)) * 3600) + (minute * 60)

    @property
    def hour(self):
        return self.seconds // 3600 % 24

    @property
    def minute(self):
        return self.seconds % 3600 // 60

    def __repr__(self):
        return f"{self.hour:0>2}:{self.minute:0>2}"

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
