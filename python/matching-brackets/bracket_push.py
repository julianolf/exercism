def is_paired(input_string: str = '') -> bool:
    brackets = '[{(]})'
    stack = []
    for char in input_string:
        if char in brackets[:3]:
            stack.append(char)
        elif char in brackets[3:]:
            if not stack or stack[-1] != brackets[brackets.index(char) % 3]:
                return False
            else:
                stack.pop()
    return not stack
