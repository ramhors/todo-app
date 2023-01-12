waiting_list = ['sen', 'Maurice', 'John', 'Noah', 'Korri']
waiting_list.sort()
a= '*' * 25
number = [1, 2, 3, 4, 5, 612, 345, 23, 1000]
number.sort(reverse=True)  #SORTING IN DESCENDING ORDER

ips = ['100.122.133.105', '100.122.133.111']


filename = ['document', 'report', 'presentation']
for index, item in enumerate(filename):
    row= f"{index}-{item}.txt"
    print(row)

print(a)

# user_input = int(input('Enter the index of the IP you want: '))
# match user_input:
#     case 0:
#         print('You chose ', ips[0])
#     case 1:
#         print('You chose ', ips[1])

# OR
user_choice = int(input('Enter the index of the IP you want: '))
message = f"You chose {ips[user_choice]}"
print(message)

print(a)

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)

print(a)

for i in number:
    print('Number: ', i)
