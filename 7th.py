import pandas as pd

order_data = pd.DataFrame({
    "CustomerID":[101,102,101,103,102],
    "OrderDate":["2024-01-05","2024-01-08","2024-01-12","2024-01-15","2024-01-20"],
    "Product":["Laptop","Mouse","Mouse","Keyboard","Laptop"],
    "Quantity":[1,2,3,1,2]
})

order_data["OrderDate"] = pd.to_datetime(order_data["OrderDate"])

print("Orders by Customer")
print(order_data.groupby("CustomerID").size())

print("\nAverage Quantity")
print(order_data.groupby("Product")["Quantity"].mean())

print("\nEarliest Date:", order_data["OrderDate"].min())
print("Latest Date:", order_data["OrderDate"].max())
Output

Orders by Customer
101    2
102    2
103    1

Average Quantity
Keyboard    1.0
Laptop      1.5
Mouse       2.5

Earliest Date: 2024-01-05
Latest Date: 2024-01-20
