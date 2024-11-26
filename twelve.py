# Írj programot, mely beolvas egy pozitív egész számot, és megmondja, hogy
# tökéletes szám-e! (A tökéletes számok azok, melyek osztóinak összege egyenlő a
# szám kétszeresével. Ilyen szám pl. a 6, mert 2*6 = 1 + 2 + 3 + 6.)

be = int(input("Mondj egy számot, megmondom hogy tökéletes-e: "))
ossz = 0
for i in range(1, be):
    if be % i == 0:
        ossz = ossz + i
if ossz == be:
    print("A szám tökéletes!")
else:
    print("A szám nem tökéletes!")