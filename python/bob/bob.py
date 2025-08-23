class Teenager(object):
    brain = [
        (lambda msg: not msg, 'Fine. Be that way!'),
        (lambda msg: msg.isupper() and msg[-1] == '?', 'Calm down, I know what I\'m doing!'),
        (lambda msg: msg.isupper(), 'Whoa, chill out!'),
        (lambda msg: msg[-1] == '?', 'Sure.'),
        (lambda msg: True, 'Whatever.')
    ]

    def __init__(self, name: str) -> None:
        self.name = name

    def talk(self, something: str) -> str:
        message = something.strip()
        for func, resp in self.brain:
            if func(message):
                return resp

def hey(phrase):
    return Teenager('Bob').talk(phrase)
