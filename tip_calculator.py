bill = float(input("What is the bill? "))
tip_percent = float(input("What is the tip percentage? ")) / 100

tip = bill * tip_percent
print()
print(f"The tip is ${tip:.2f}")
print(f"The total is ${(bill + tip):.2f}")