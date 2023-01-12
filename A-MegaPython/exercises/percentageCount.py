try:
    total = float(input("Please enter the total value: "))
    value = float(input("Please enter value: "))

    percentage = (value / total) * 100
    print(f"That is {percentage}%")
except ValueError:
    print("\033[91mYou need to enter a number. Run the program again")
except ZeroDivisionError:
    print("\033[91mYour total value can not be zero")

# if total.strip().isdigit() and value.strip().isdigit():
#     percentage = (20 / 50) * 100
#     print(percentage, '%')
# elif len(total) == 0 or len(value) == 0:
#     print("You need to enter a number. Run the program again.")
#OR
