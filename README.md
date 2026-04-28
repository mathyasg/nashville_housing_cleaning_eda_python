# Nashville Housing Data Cleaning & Analysis in Python

![Project Banner](https://via.placeholder.com/800x200/1e3a8a/ffffff?text=Nashville+Housing+Analysis)

## Project Overview
This project demonstrates a complete **end-to-end data analytics workflow** on the Nashville Housing dataset. It covers thorough data cleaning followed by Exploratory Data Analysis (EDA) and visualizations using Python.

The goal was to transform raw, messy real-world data into clean, insightful information and present it in easy to digest vizualizations.

## Dataset
- **Raw File**: `Nashville Housing Data for Data Cleaning.xlsx` (56,477 records)
- **Time Period**: 2013 – 2016
- **Main Challenges**: Missing addresses, inconsistent values, unsplit address fields, duplicates, and improper date formats.

**Cleaned Output**: `housing_data_cleaned.csv`

## Repository Structure
nashville-housing-data-cleaning-eda-python/
├── README.md
├── nashville_housing_python_cleaning.py     # Data cleaning pipeline
├── nashville_housing_eda.py                 # EDA and visualizations
├── Nashville Housing Data for Data Cleaning.xlsx   # Raw data
├── housing_data_cleaned.csv                 # Cleaned dataset
├── 01_avg_sale_price_per_year.png
├── 02_avg_price_by_year_built.png
├── 03_top_cities_by_sales.png
├── 04_average_saleprice_top5.png


## Results & Insights

### Data Cleaning Summary
I cleaned the raw dataset by addressing common real-world data quality issues:
- Converted Excel serial dates to proper datetime format
- Populated missing `PropertyAddress` using ParcelID logic
- Split `PropertyAddress` and `OwnerAddress` into structured components (Address, City, State)
- Standardized the `SoldAsVacant` column (Y/N → Yes/No)
- Removed duplicate records

### Key Insights from Exploratory Data Analysis

1. **Upward Price Trend (2013–2016)**  
   Average sale prices showed a steady increase over the four-year period, indicating a strengthening housing market in Nashville.

2. **Significant Premium for Newer Homes**  
   Homes built in the 2010s and later commanded substantially higher average sale prices compared to older properties. This reveals a strong buyer preference for modern construction and updated features.

3. **Geographic Concentration**  
   Housing sales are heavily concentrated in a small number of cities. The top 5 cities dominate both transaction volume and market value, highlighting uneven demand across the region.

4. **Market Segmentation**  
   Different cities serve different market segments — some are high-volume markets with moderate prices, while others are premium markets with fewer transactions but significantly higher average sale prices.

5. **Strong Feature Relationships**  
   Correlation analysis showed very high positive correlations between `SalePrice`, `TotalValue`, and `BuildingValue`. This confirms the internal consistency of the dataset and suggests that assessed values are reliable predictors of actual sale prices.

These insights demonstrate how proper data cleaning unlocks meaningful business understanding about price drivers, market trends, and geographic patterns in real estate.

**Note on `SoldAsVacant`**: I analyzed the impact of whether a property was sold as vacant or occupied. The feature was extremely imbalanced (~99% occupied vs ~1% vacant). Due to the very small sample size of vacant properties, this analysis was documented but excluded from the main visualizations to maintain focus on more reliable and insightful findings.

## Technologies Used
- **Python**: pandas, matplotlib, seaborn
- Reproducible workflows with clean, well-documented scripts

## How to Reproduce
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install pandas openpyxl matplotlib seaborn
3. Run data cleaning:
   ```bash
   python nashville_housing_python_cleaning.py
4. Run EDA and generate visualizations:
   ```bash
   python nashville_housing_eda.py

###Future Improvements
**Build an interactive Tableau/Power BI dashboard**
**Develop a machine learning model for price prediction**
