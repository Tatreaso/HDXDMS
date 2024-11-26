# Írj programot, mely beolvas egy pozitív egész számot, és kiírja az egész számokat a
# képernyőre eddig a számig, egymástól szóközzel elválasztva!
be = int(input("Add meg a számot: "))
for i in range(1, be+1):
    print(i, end=", ")