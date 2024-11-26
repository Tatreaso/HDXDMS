# Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóit!
be = int(input("SZÁM: "))
for i in range(1, be+1):
    if be % i == 0:
        print(i)