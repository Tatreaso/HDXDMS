# Írj programot, mely eldönti egy számról, hogy prímszám-e.

be = int(input("Mondj egy számot: "))
ossz = 0
for i in range(1, be+1):
    if be % i == 0:
        ossz = ossz + i
if ossz == be+1:
    print("A szám prím!")
else:
    print("A szám nem prím!")