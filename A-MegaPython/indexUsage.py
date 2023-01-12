import glob
# GETTING THE LIST OF FILE IN ANY FOLDER
myfiles = glob.glob("bonus/files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())