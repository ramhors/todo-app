def get_average():
    with open("files/data.txt", 'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)


def get_max():
    grades = [9.6, 9.2, 9.7]
    max_value = max(grades)
    min_value = min(grades)
    message = f"Max: {max_value}, Min: {min_value}"
    return message


print(get_max())


def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()

fahrenheit = celsius * 1.8 + 32
print(fahrenheit)
