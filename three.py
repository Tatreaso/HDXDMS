# Készítsünk programot, amely kiszámolja az első 100 db páros szám összegét
n = 200
ossz = 0
for i in range(2, n+1, 2):
    ossz = ossz + i
print(ossz)