from collections import deque

text = input('Напишіть що небудь: ')

d = deque()

def palindrome(text):
    d.extend(text.lower().replace(' ', ''))
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

print('Це паліндром' if palindrome(text) else 'Це не паліндром')