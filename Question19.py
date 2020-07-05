#19. Write a Python class to find validity of a string of parentheses, '(',')', '{', '}', '[' and ']. 
# These brackets must be close in the correct order, 
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid


def check_brackets(brackets):
    opening_bracket_stack = []
    for b in brackets:
        if "{([".__contains__(b):
            opening_bracket_stack.append(b)
        elif "})]".__contains__(b):
            if b == '}':
                if '{' != opening_bracket_stack.pop():
                    return False
            elif b == ']':
                if '[' != opening_bracket_stack.pop():
                    return False
            elif b == ')':
                if '(' != opening_bracket_stack.pop():
                    return False
    return True

print(check_brackets("([{}{(){[)})"))
print(check_brackets("({}[](){[})"))
print(check_brackets("({}[](){[]})"))
print(check_brackets("({]}}(){[})"))
print(check_brackets("({{[](){[]})"))
