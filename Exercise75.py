n = int(input("Enter first positive integer: ")) 
m = int(input("Enter second positive integer: "))

d = min(m, n)

while n % d != 0 or m % d != 0: 
    d -= 1

print("The greatest common divisor of", n, "and", m, "is", d)