import numpy as np

# 3x3 sales price matrix
sales = np.array([
    [100, 120, 110],
    [200, 210, 190],
    [150, 160, 170]
])

print("Sales Price Matrix:")
print(sales)

# Find average price
average_price = np.mean(sales)

print("\nAverage Price of All Products Sold:", average_price)
