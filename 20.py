rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
for i in range(rows):
    for j in range(cols):
        if i % 2 == 0:  # Even row
            if j % 2 == 0:
                print("X", end="")
            else:
                print("O", end="")
        else:  # Odd row
            if j % 2 == 0:
                print("O", end="")
            else:
                print("X", end="")
    print()