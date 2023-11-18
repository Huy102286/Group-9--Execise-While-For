print("Discount is 60%.")
for i in (4.95, 9.95, 14.95, 19.95, 24.95):
    print("Original price",i)
    i *= 0.60
    print("Discounted price = ", round(i,2))
    print()
    print("-" * 5)