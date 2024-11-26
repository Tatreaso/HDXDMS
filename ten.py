# Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóinak az
# összegét!
ossz = 0
be = int(input("SZÁM: "))
for i in range(1, be+1):
    if be % i == 0:
        ossz += i
print(ossz)