import re


class StackUnderflowError(Exception):
    pass


def add(stack):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")

    b = stack.pop()
    a = stack.pop()
    stack.append(a + b)


def sub(stack):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")

    b = stack.pop()
    a = stack.pop()
    stack.append(a - b)


def mul(stack):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")

    b = stack.pop()
    a = stack.pop()
    stack.append(a * b)


def div(stack):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")

    if stack[-1] == 0:
        raise ZeroDivisionError("divide by zero")

    b = stack.pop()
    a = stack.pop()
    stack.append(a // b)


def dup(stack):
    if len(stack) == 0:
        raise StackUnderflowError("Insufficient number of items in stack")

    stack.append(stack[-1])


def drop(stack):
    if len(stack) == 0:
        raise StackUnderflowError("Insufficient number of items in stack")

    stack.pop()


def swap(stack):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")

    right = stack.pop()
    left = stack.pop()

    stack.append(right)
    stack.append(left)


def over(stack):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")

    stack.append(stack[-2])


words = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "DUP": dup,
    "DROP": drop,
    "SWAP": swap,
    "OVER": over,
}

number_pattern = re.compile(r"^-?\d+$")
word_pattern = re.compile(r"^: ([+\-*/]|[A-Z]\S*) (.+) ;$")


def create_word(instructions, custom_words):
    word_match = word_pattern.fullmatch(instructions)

    if not word_match:
        raise ValueError("illegal operation")

    word, value = word_match.groups()
    values = []

    for val in value.split():
        if val in custom_words:
            op = custom_words[val]
            op(values)
            continue

        if number_pattern.fullmatch(val):
            val = int(val)

        values.append(val)

    custom_words[word] = lambda s: s.extend(values)


def evaluate(input_data):
    stack = []
    custom_words = {}

    for entry in input_data:
        instructions = entry.upper()

        if instructions.startswith(":") and instructions.endswith(";"):
            create_word(instructions, custom_words)
        else:
            for instruction in instructions.split():
                if number_pattern.fullmatch(instruction):
                    number = int(instruction)
                    stack.append(number)
                else:
                    op = None

                    if instruction in custom_words:
                        op = custom_words[instruction]
                    elif instruction in words:
                        op = words[instruction]

                    if op is None:
                        raise ValueError("undefined operation")

                    op(stack)

    if any(isinstance(value, str) for value in stack):
        return evaluate([" ".join(map(str, stack))])

    return stack
