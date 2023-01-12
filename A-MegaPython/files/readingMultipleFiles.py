filenames = ["a.txt", "b.txt", "c.txt"]

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)

#BUG FIXES
mfile = open("data.txt", 'w')
content = mfile.write("100.12\n")
content = mfile.write("111.23\n")
mfile.close()

