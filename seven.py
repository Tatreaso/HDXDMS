# Számítsd ki a felhasználó által megadott a-tól b-ig terjedő számok összegét, átlagát
a = int(input("Add meg az A számot: "))
b = int(input("Add meg a B számot: "))
ossz = 0
counter = 0
for i in range(a, b+1):
    ossz += i
    counter += 1
print(ossz/counter)