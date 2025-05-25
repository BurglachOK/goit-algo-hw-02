def check_if_correct(s):
    opened_parentheses = []
    closed_to_open = {'}': '{', ']': '[', ')': '('}
    for i in s:
        if i in ('(', '[', '{'):
            opened_parentheses.append(i)
        elif i in (')', ']', '}'):
            if (not opened_parentheses) or (closed_to_open[i] != opened_parentheses.pop()):
                return False
    return opened_parentheses == []


while p := input():
    print(check_if_correct(p))