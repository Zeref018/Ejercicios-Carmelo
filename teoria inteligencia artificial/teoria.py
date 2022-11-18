import pandas as pd
import matplotlib.pyplot as plt

productos = pd.read_csv("products.csv")
print(productos)
bins = [0, 50, 100, 500]
grupos = ["stock crítico", "stock normal", "stock"]
df = productos[["unitsInStock"]]
df["unitsInStock"] = pd.cut(df["unitsInStock"], bins, grupos)
print(df["unitsInStock"])

df.unitsInStock.value_counts().plot.pie()
plt.show()
