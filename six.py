# Számítsd ki a felhasználó által bevitt n szám átlagát
be = int(input("Adj meg egy számot: "))
counter = 1
ossz = 0
while counter < 5:
    be = int(input("Adj meg még számot: "))
    ossz += be
    counter += 1
print(ossz/counter)