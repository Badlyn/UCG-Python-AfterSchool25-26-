tip_rate = 0.15
tax_rate = 0.0825

bill = float(input("Enter bill amount: "))

tax = bill * tax_rate
tip = bill * tip_rate
total = bill + tax + tip

per_person = float(input("How many people are sharing the bill?: "))

print(" 💵 Restuarant Bill Splitter 💵  ")

#uh, what the ahh haha

print("-----------------------------")
print("Original bill", bill)
print("Sales Tax:", tax_rate * bill)
print("Tip:", tip_rate * bill)
print("Total:", total)
print("Each Person Pays:", total / per_person)
print("--------------------------")
