filename = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filename:
    #Replace only the first incurrence of the dot
    filename = filename.replace('.', '-', 1)
    print(filename)