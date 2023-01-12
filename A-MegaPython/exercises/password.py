password = input("Enter new password: ")

result = {}

if len(password) > 8:
    result['length'] = True
else:
    result['length'] = False

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result['upper-case'] = uppercase

digit = False

for i in password:
    if i.isdigit():
        digit = True

result['digit'] = digit

special_char = ['#', '&', '!', '^']

char = False

for i in password:
    if i in special_char:
        char = True
result['char'] = char

if all(result.values()):
    print("Strong password")
else:
    print("Weak password")
