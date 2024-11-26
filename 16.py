n = int(input("Enter a number: "))
print(f"Prime divisors of {n}: ", end="")
for i in range(2, n + 1):
    is_prime = True
    if n % i == 0:
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")
print()