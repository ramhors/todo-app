ids = ['XSF@#$_34', 'ASDASF23455', 'XSD_SFS', '23423_234']
x= 0
for id in ids:
    if '_' in id:
        x = x + 1
print(x)

length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

if perimeter < 14 and area < 8:
    print("OK")
else:
    print("NOT OK")