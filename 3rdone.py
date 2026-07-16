import numpy as np

# Bedrooms, Square Feet, Sale Price
house_data = np.array([
    [3, 1200, 200000],
    [5, 2000, 350000],
    [4, 1800, 300000],
    [6, 2500, 450000]
])

houses = house_data[house_data[:, 0] > 4]

average_price = np.mean(houses[:, 2])

print("Average Sale Price:", average_price)
