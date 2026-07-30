import pandas as pd

property_data = pd.DataFrame({
    "PropertyID":[1,2,3,4],
    "Location":["Chennai","Hyderabad","Chennai","Bangalore"],
    "Bedrooms":[2,3,4,2],
    "Area":[1200,1500,1800,1100],
    "Price":[5000000,6500000,8000000,4500000]
})

print("Average Price:", property_data["Price"].mean())
print("Largest Area:", property_data["Area"].max())

print("\nProperties by Location")
print(property_data["Location"].value_counts())
Output

Average Price: 6000000.0
Largest Area: 1800

Properties by Location
Chennai      2
Hyderabad    1
Bangalore    1
