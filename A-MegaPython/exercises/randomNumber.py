import random

''' RANDOM METHODS '''
#choice1 = int(input("Enter the lower bound: "))
#choice2 = int(input("Enter the upper bound: "))
choice1 = 11
choice2 = 230

''' randint()'''
def randomNum():
    number = random.randint(choice1,choice2)
    return number

print(randomNum())

'''Shuffle'''
mylist = ["Bema","Rakoto","Andry","Tosy"]
random.shuffle(mylist)
print(mylist)

