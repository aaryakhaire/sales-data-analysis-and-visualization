import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Create Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

print("\nDataset Preview:")
print(df.head())

# ------------------------------
# 1. Total Revenue
# ------------------------------
total_revenue = df['Revenue'].sum()
print("\nTotal Revenue:", total_revenue)

# ------------------------------
# 2. Monthly Sales Trend
# ------------------------------
df['Month'] = df['Date'].dt.month
monthly_sales = df.groupby('Month')['Revenue'].sum()

plt.figure()
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

# ------------------------------
# 3. Top Products by Revenue
# ------------------------------
product_sales = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

plt.figure()
product_sales.plot(kind='bar')
plt.title("Top Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

# ------------------------------
# 4. Region-wise Sales
# ------------------------------
region_sales = df.groupby('Region')['Revenue'].sum()

plt.figure()
region_sales.plot(kind='bar')
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()

# ------------------------------
# 5. Category-wise Contribution
# ------------------------------
category_sales = df.groupby('Category')['Revenue'].sum()

plt.figure()
category_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Category-wise Sales Contribution")
plt.ylabel("")
plt.show()
