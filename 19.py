count = 0
for i in range(ord('a'), ord('z') + 1):
    print(f"{chr(i)} {i}", end="\t")
    count += 1
    if count == 10:
        print()
        count = 0