import operator
import re

PATTERN = r"^What is((( -?\d+)?( (plus|minus|multiplied by|divided by))?)*)\?$"

operations = {
    "plus": "+",
    "minus": "-",
    "multiplied by": "*",
    "divided by": "/",
}

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}


def evaluate(expr):
    size = len(expr)

    if size == 1:
        return int(expr[0])

    if size >= 3:
        left = expr[:-2]
        op = expr[-2]
        right = expr[-1:]

        if op in operators:
            return operators[op](evaluate(left), evaluate(right))

    raise ValueError("syntax error")


def answer(question):
    match = re.fullmatch(PATTERN, question, re.I)

    if not match:
        raise ValueError("unknown operation")

    problem = match.group(1).strip()

    for key, value in operations.items():
        problem = problem.replace(key, value)

    problem = problem.split()

    if len(problem) % 2 == 0:
        raise ValueError("syntax error")

    return evaluate(problem)
