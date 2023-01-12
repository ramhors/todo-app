#CREATING A MULTIPLE TEXT FILES

filenames = ["textOne.txt","textTwo.txt","textThree.txt","textFour.txt"]

for filename in filenames:
    file = open(filename, 'w')
    file.write("Hello")
    file.close()