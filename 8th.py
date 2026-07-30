import pandas as pd

sales = pd.DataFrame({
    "Product":["Laptop","Mouse","Laptop","Keyboard","Mouse","Laptop","Pen"],
    "Quantity":[5,10,4,8,6,3,12]
})

top5 = sales.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)

print(top5)
Output

Product
Laptop     12
Mouse      16
Pen        12
Keyboard    8
