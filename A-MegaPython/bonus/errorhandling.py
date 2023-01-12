try:
    area = 0
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))
    if width == length:
        exit("That looks like a square")
    else:
        area = width * length
    print(area)
except ValueError:
    print('\033[91mNot a valid number')