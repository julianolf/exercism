def is_paired(input_string: str = '') -> bool:
    brackets = {'[': ']', '{': '}', '(': ')'}
    stack = []
    for char in input_string:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack[-1]] != char:
                return False
            else:
                stack.pop()
    return not stack
