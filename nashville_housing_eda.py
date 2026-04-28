"""
Nashville Housing EDA & Visualization Script
Author: Mathyas Tilahun
Purpose: Exploratory Data Analysis and visualizations
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

print("📊 Starting Nashville Housing EDA...\n")

# Load the cleaned CSV
print("Loading cleaned Nashville Housing .csv data...")
df = pd.read_csv('housing_data_cleaned.csv')

# Remove "Unknown" city to 
df_vis = df[
    df['PropertySplitCity'].notna() & 
    (df['PropertySplitCity'].str.strip().str.lower() != 'unknown')
].copy()

print(f"Original rows: {len(df):,}")
print(f"Rows after excluding 'Unknown' city: {len(df_vis):,}\n")
print(f"Dataset shape: {df.shape}")


# ====================== 1. Average Sale Price per Year ======================
df_vis["SaleDateConverted"] = pd.to_datetime(df_vis["SaleDateConverted"], errors='coerce')
df_vis["SaleYear"] = df_vis["SaleDateConverted"].dt.year

# Group by year, compute average, and sort
saleYear_distribution = (
    df_vis.groupby("SaleYear")["SalePrice"]
          .mean()
          .reset_index(name="Avg_Sale_price")
          .sort_values("SaleYear")
)
years_to_plot = [2013, 2014, 2015, 2016]
filtered_distribution = saleYear_distribution[
    saleYear_distribution["SaleYear"].isin(years_to_plot)
]
plt.figure(figsize=(12,6))
plt.plot(
    filtered_distribution["SaleYear"],
    filtered_distribution["Avg_Sale_price"],
    marker="o",
    markersize=10,
    linewidth=2.5,
    color="#1f77b4"
)
plt.xticks(filtered_distribution["SaleYear"]) 
plt.title('Average Sale Price per Year')
plt.xlabel('Year of Sale')
plt.ylabel('Average Sale Price (USD)')
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.savefig('01_avg_sale_price_per_year.png', dpi=300, bbox_inches='tight')
print("✅ Saved: 01_avg_sale_price_per_year.png")


# ====================== 2. Average Sale Price by Year Built ======================
df_vis['YearBuiltGroup'] = pd.cut(df_vis['YearBuilt'], 
                                  bins=[0, 1980, 1990, 2000, 2010, 2020, 2030],
                                  labels=['<1980', '1980s', '1990s', '2000s', '2010s', '2020+'])
avg_price_year = df_vis.groupby('YearBuiltGroup')['SalePrice'].mean().round(0)
blue_color = sns.color_palette("Blues")[3]
ax = avg_price_year.plot(kind='bar', figsize=(12, 6), color=blue_color)
plt.title('Average Sale Price by Year Built')
plt.xlabel('Year Built Group')
plt.ylabel('Average Sale Price (USD)')
plt.xticks(rotation=0)
for container in ax.containers:
    ax.bar_label(container,labels=[f"{v.get_height():,.0f}" for v in container], label_type='edge', padding=3)
plt.tight_layout()
plt.savefig('02_avg_price_by_year_built.png', dpi=300, bbox_inches='tight')
print("✅ Saved: 02_avg_price_by_year_built.png")

"""
# ====================== 3. Occupied vs Vacant listings ======================
#This section was analyzed but commented out because the data is highly imbalanced (~99% Occupied vs ~1% Vacant), making the insight less reliable and visually weak.

soldasvacant_distribution = (
    df.groupby("SoldAsVacant")
      .size()                               
      .reset_index(name="Number of properties")   
)
# Map values
soldasvacant_distribution["SoldAsVacant"] = soldasvacant_distribution["SoldAsVacant"].map({
    "No": "Occupied",
    "Yes": "Vacant"
})
plt.title("Distribution of SoldAsVacant")
plt.xlabel("Status")
plt.ylabel("Count")
plt.figure(figsize=(12,6))
ax = sns.barplot(
        data=soldasvacant_distribution,
        x="SoldAsVacant",
        y="Number of properties",
        hue="SoldAsVacant",
        legend=False,
        palette="Blues"
    )
plt.title("Vacant vs occupied property sales")
plt.xlabel("Sold as")
plt.ylabel("Number of properties")
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.savefig('03_Vacant_vs_occupied.png', dpi=300, bbox_inches='tight')
print("✅ Saved: 03_Vacant_vs_occupied.png")
"""

# ====================== 3. Top 5 Cities by Number of Sales ======================
top_cities = (
    df_vis['PropertySplitCity']
    .value_counts()
    .head(5)
    .reset_index()
)
top_cities.columns = ['PropertySplitCity', 'NumberOfSales']
plt.figure(figsize=(12, 6))
ax = sns.barplot(
    data=top_cities,
    x='PropertySplitCity',
    y='NumberOfSales',
    hue="PropertySplitCity",
    legend=False,
    palette="Blues_d"
)

plt.title('Top 5 Cities by Number of Housing Sales', fontsize=14, pad=20)
plt.xlabel('City', fontsize=12)
plt.ylabel('Number of Sales', fontsize=12)
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
for container in ax.containers:
    ax.bar_label(container, labels=[f"{v.get_height():,.0f}" for v in container], label_type='edge', padding=3)
plt.tight_layout()
plt.savefig('03_top_cities.png', dpi=300, bbox_inches='tight')
print("✅ Saved: 03_top_cities.png")

"""
# ====================== 4. Correlation Heatmap ======================
numeric_cols = ['SalePrice', 'Acreage', 'LandValue', 'BuildingValue', 
                'TotalValue', 'YearBuilt', 'Bedrooms', 'FullBath']
corr = df_vis[numeric_cols].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, cbar_kws={'shrink': 0.8})
plt.title('Correlation Matrix of Housing Features', fontsize=14, pad=20)
plt.tight_layout()
plt.savefig('04_correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("✅ Saved: 04_correlation_heatmap.png")
"""

# ====================== 4. Top 5 Cities by Average Sale Price ======================
avg_saleprice_by_city = (
    df_vis.groupby("PropertySplitCity")["SalePrice"]
          .mean()
          .reset_index(name="AvgSalePrice")
          .sort_values("AvgSalePrice", ascending=False)
          .head(5)
)
plt.figure(figsize=(12, 6))
ax = sns.barplot(
    data=avg_saleprice_by_city,
    x="PropertySplitCity",
    y="AvgSalePrice",
    hue="PropertySplitCity",
    legend=False,
    palette="Blues_d"
)

plt.title("Top 5 Cities by Average Sale Price", fontsize=14, pad=20)
plt.xlabel("City", fontsize=12)
plt.ylabel("Average Sale Price (USD)", fontsize=12)
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
for container in ax.containers:
    ax.bar_label(container, labels=[f"{v.get_height():,.0f}" for v in container], label_type='edge', padding=3)
plt.tight_layout()
plt.savefig('04_average_sale_price_top5.png', dpi=300, bbox_inches='tight')
print("✅ Saved: 04_average_saleprice_top5.png")

print("\n🎉 All 4 EDA charts saved!")