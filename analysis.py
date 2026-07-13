import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("dataset/vgsales.csv")

# Show first rows
print(data.head())

# Sales by Genre
genre_sales = data.groupby("Genre")["Global_Sales"].sum()

# Plot graph
genre_sales.sort_values(ascending=False).plot(kind="bar")

plt.title("Global Video Game Sales by Genre")
plt.xlabel("Genre")
plt.ylabel("Global Sales")

plt.show()