# Készítsünk programot, amely kiszámolja az első 7 db természetes szám szorzatát egy ciklus segítségével.
n = 7
ossz = 1
for i in range(1, n):
    ossz = ossz * i
print(ossz)