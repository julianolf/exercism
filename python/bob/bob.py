class Teenager(object):
    brain = [
        (lambda msg: not msg, 'Fine. Be that way!'),
        (lambda msg: msg.isupper() and msg.endswith('?'), 'Calm down, I know what I\'m doing!'),
        (lambda msg: msg.isupper(), 'Whoa, chill out!'),
        (lambda msg: msg.endswith('?'), 'Sure.'),
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
