import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/Car_sales.csv")

# Remove missing sales values
df = df.dropna(subset=["Sales_in_thousands"])

# Group and sort
model_sales = df.groupby("Model")["Sales_in_thousands"].sum()
model_sales = model_sales.sort_values(ascending=False)

# Take top 10
top10 = model_sales.head(10)

# Plot bar chart
plt.figure()
top10.plot(kind="bar")

plt.title("Top 10 Selling Car Models")
plt.xlabel("Car Model")
plt.ylabel("Sales (in thousands)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Pie chart for top 5 models
top5 = model_sales.head(5)

plt.figure()
plt.pie(top5, labels=top5.index, autopct='%1.1f%%')
plt.title("Sales Distribution - Top 5 Models")
plt.show()

# Sales by Manufacturer
manufacturer_sales = df.groupby("Manufacturer")["Sales_in_thousands"].sum()
manufacturer_sales = manufacturer_sales.sort_values(ascending=False)

top10_manufacturers = manufacturer_sales.head(10)

plt.figure()
top10_manufacturers.plot(kind="bar")

plt.title("Top 10 Manufacturers by Sales")
plt.xlabel("Manufacturer")
plt.ylabel("Sales (in thousands)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Calculate Ford total sales
ford_total = manufacturer_sales["Ford"]

# F-Series sales
f_series_sales = model_sales["F-Series"]

# Percentage contribution
percentage = (f_series_sales / ford_total) * 100

print(f"\nF-Series contributes {percentage:.2f}% of Ford's total sales.")