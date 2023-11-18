print("   ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()

# Print horizontal line
print("   ", end="")
print("-" * 44)

# Print table body
for i in range(1, 11):
    # Print row label
    print(f"{i:2} |", end="")

    # Print row values
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    
    print()