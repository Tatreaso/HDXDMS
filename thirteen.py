# Írj programot, ami csak pozitív számot hajlandó beolvasni
be = int(input("Adj meg egy SZIGORÚAN pozitív számot!"))
if be < 0:
    print("Ne csalj!")
    be = int(input("Adj meg egy SZIGORÚAN pozitív számot!"))