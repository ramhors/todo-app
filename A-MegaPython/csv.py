import csv

with open("bonus/files/weather.csv", 'r') as file:
    data = list(file.read())

city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])