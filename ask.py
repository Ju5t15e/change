import re
ask = (input("Enter your word: "))

result = (input("Type the letter that you want to change:"))

a = (input("Type the lesser which you want to replace: "))

if result in ask:
    d = re.sub(result, a, ask)
    print(d)
input()