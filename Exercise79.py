import random
maximum = random.randint(1, 100)
update_count = 0

print("Initial maximum:", maximum)

for _ in range(99):
    number = random.randint(1, 100)
    print(number, end=" ")
    
    if number > maximum:
        maximum = number
        update_count += 1
        print("(New Maximum)", end=" ")
    
print("\n\nMaximum value encountered:", maximum)
print("Number of updates:", update_count)