filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)

#CAPITALIZE ALL THE NAMES
names = ["john smith", "jay santi", "eva kuki"]
names = [new_names.title() for new_names in names]
print(names)

#PRINTING THE NUMBER OF CHARACTER FOR EACH USE NAMES
usernames =["john 1990", "alberto1970","magnola2000"]
usernames = [len(username) for username in usernames]
print(usernames)

#PRINTING CHANGING LIST VALUE AS FLOAT
user_entries = ['10', '19.1', '20']
float_number = [float(entries) for entries in user_entries]
print("Float result: ", float_number)

#PRINTING THE SAME OF THE LIST
user_input = ['10', '19.1', '20']
user_input = [float(item) for item in user_input]
print(sum(user_input))

#BUG FIX
temperatures = [10, 12, 14]
temperatures = [str(i) + '\n' for i in temperatures]
file = open("../files/file.txt", 'w')
file.writelines(temperatures)

#CONVERTING NUMBER INTO INT
numbers = [10.1, 12.3, 14.7]
numbers = [int(item) for item in numbers]
print(numbers)

