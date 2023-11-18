n = int(input("Enter an integer greater than or equal to 2: "))
if n < 2:
    print("Invalid input. Please enter an integer greater than or equal to 2.")
else:
    factor = 2
    while factor <= n:
        if n % factor == 0:
            print(factor)
            n = n // factor
        else:
            factor += 1