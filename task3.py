
inp = input('Напишіть скобки: ')


s = []


def check_brackets(inp):
    for char in inp:
        if char == '(' or char == '[' or char == '{':
            s.append(char)
        elif char == ')' or char == ']' or char == '}':
            if not s:
                print('Несиметрично')
                return False
            top = s.pop()
            if (char == ')' and top != '(') or \
               (char == ']' and top != '[') or \
               (char == '}' and top != '{'):
                print('Несиметрично')
                return False
    if s:
        print('Несиметрично')
        return False
    print('Симетрично')
    return True


check_brackets(inp)