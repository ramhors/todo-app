from bonus.converter import convert
from bonus.parsers import parse

feet_inches = input("Enter your height: ")

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

if result < 1:
    print("You a little short to ride theslide")
else:
    print("You can ride the slide")
