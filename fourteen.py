be = int(input("Valami: "))
counter = int(0)
two = "2*"
while be % 2 == 0:
    be = be / 2
    counter += int(1)
print(f"{two*counter}{be}")