try:
    waiting_list = ["John", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")

except ValueError:
    print(f"{name} is not in the list")