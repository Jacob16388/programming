total = 11.00

day = input("day: ")
three_d = input("3D? (y/n): ")
popcorn = input("popcorn? (y/n): ")
if day.lower() == "tuesday":
    total = total - 3.00

if three_d.lower() == "y":
    total = total + 2.50
if popcorn.lower() == "y":
    total = total + 5.00
print(f"Total: ${total:.2f}")
