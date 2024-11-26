# Írjunk oktatóprogramot, amely az összeadást és a kivonást gyakoroltatja! 
# Az egész számokat véletlenszerűen  állítsuk  elő!  
# A  felhasználó  csak -5  és  +15  között  képes  a  műveleteket elvégezni. 
# Adjunk 10 feladatot, és a felhasználó minden helyes megoldása 1 pontot érjen! 
# Osztályozzuk  le  a  feladatsort,  és  az  osztályzatot  írjuk  ki  a  képernyőre  úgy,  
# hogy  0-2-ig elégtelen,  3-4-ig  elégséges,  5-6-ig  közepes,  7-8-ig  jó,  e  fölött  pedig  jeles  legyen!

import random
counter = 0
for i in range(0, 10):
    n1 = random.randint(-5, 15)
    n2 = random.randint(-5, 15)
    ans = n1 - n2
    print(f"{n1} - {n2}")
    userAns = int(input("Oldd meg a feladatot"))
    if userAns == ans:
        counter += 1
if counter < 2:
    print("Elégtelen")
elif counter > 2 and counter <= 4:
    print("Elégségés")
elif counter > 4 and counter <= 6:
    print("Közepes")
elif counter > 6 and counter <= 8:
    print("Négyes")
else:
    print("Ötös")