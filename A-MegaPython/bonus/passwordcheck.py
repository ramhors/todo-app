password = input("Enter your password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

# CHECKING FOR DIGIT
digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

#CHECKING FOR UPPERCASE
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

print(result)
if all(result.values()):
    print("Strong password")
else:
    print("Weak password")
