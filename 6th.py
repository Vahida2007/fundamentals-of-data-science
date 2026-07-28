prices = [50, 100, 80]
quantity = [2, 1, 3]

discount = 10
tax = 5

total = 0

for i in range(len(prices)):
    total += prices[i] * quantity[i]

after_discount = total - (total * discount / 100)
final = after_discount + (after_discount * tax / 100)

print("Total Cost =", final)
