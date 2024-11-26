# Készítsünk programot, amely kiszámolja az első 100 db természetes szám összegét, majd kiírja az eredményt.

n = 100
ossz = 0
for i in range(1, n+1):
    ossz = ossz + i
print(ossz)