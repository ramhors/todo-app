# amount = float(input('How many dolloars have you got? '))
# rate = 0.95
# print(amount)
#
# print('The amount in euros is: ')
# result = amount * rate
# print(result)

# ranking = ['John', 'Sen', 'Lisa']
# rank = int(input('Enter rank number: ')) - 1
# name = ranking[rank]
# print(name)

# ranking = ['John', 'Sen', 'Lisa']
# user_input = input('Enter a name: ')
# user_input = user_input.strip()
# match  user_input:
#     case 'John':
#         print(1)
#     case 'Sen':
#         print(2)
#     case 'Lisa':
#         print(3)
#
# OR
# ranking = ['John', 'Sen', 'Lisa']
# user_input = input('Enter a name: ')
# name = ranking.index(user_input) + 1
# print(name)

# elements = ['a', 'b', 'c']
# new = 'x'
# elements[1] = new
# print(elements)
# char = ['a', 'b', 'c']
# print(char[1])

menu = ["pasta", "pizza", "salad"]

user_choice = int(input("Enter the index of the item: "))

message = f"You chose {menu[user_choice]}."
print(message)


for i, j in enumerate(menu):
    row = f"{i}.{j}"
    print(row)