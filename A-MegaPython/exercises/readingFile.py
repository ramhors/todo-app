#SIMPLY READING A FILE
file = open("../files/essay.txt")
content = file.read()
print(content.title())
file.close()

# Return the numbers of characters in the file
file = open("../files/essay.txt", 'r')
content = file.read()
n_char = len(content)
print(n_char)

#ADDING MEMBERS IN THE FILE
member = input("Add a new member: ")
file = open("../files/members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("../files/members.txt", 'w')
members = file.writelines(existing_members)
file.close()
