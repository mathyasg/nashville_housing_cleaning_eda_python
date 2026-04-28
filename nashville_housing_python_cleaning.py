"""
Nashville Housing Data Cleaning Script
Author: Mathyas Tilahun
Purpose: Reproducible data cleaning pipeline
"""

import pandas as pd

print("🚀 Starting Nashville Housing Data Cleaning...\n")

# ==================== LOAD RAW DATA ====================
print("Loading raw Nashville Housing data...")
df = pd.read_excel('Nashville Housing Data for Data Cleaning.xlsx')

df_clean = df.copy() # Make a copy to not alter original data

print(f"Original rows: {len(df_clean):,}")

# 1. Convert SaleDate to proper datetime
df_clean['SaleDateConverted'] = pd.to_datetime(df_clean['SaleDate'], errors='coerce')

# 2. Populate missing PropertyAddress using ParcelID
missing = df_clean['PropertyAddress'].isnull()
if missing.any():
    address_map = (df_clean.dropna(subset=['PropertyAddress'])
                   .set_index('ParcelID')['PropertyAddress']
                   .to_dict())
    df_clean.loc[missing, 'PropertyAddress'] = df_clean.loc[missing, 'ParcelID'].map(address_map)

# 3. Split PropertyAddress
df_clean[['PropertySplitAddress', 'PropertySplitCity']] = df_clean['PropertyAddress'].str.split(',', n=1, expand=True)
df_clean['PropertySplitAddress'] = df_clean['PropertySplitAddress'].str.strip()
df_clean['PropertySplitCity']     = df_clean['PropertySplitCity'].str.strip()

# 4. Split OwnerAddress
owner_parts = df_clean['OwnerAddress'].str.replace(',', '.').str.split('.', expand=True)
df_clean['OwnerSplitAddress'] = owner_parts[0].str.strip()
df_clean['OwnerSplitCity']    = owner_parts[1].str.strip()
df_clean['OwnerSplitState']   = owner_parts[2].str.strip()

# 5. Standardize SoldAsVacant
df_clean['SoldAsVacant'] = df_clean['SoldAsVacant'].replace({'Y': 'Yes', 'N': 'No'})

# 6. Remove duplicates
duplicate_cols = ['ParcelID', 'PropertyAddress', 'SalePrice', 'SaleDate', 'LegalReference']
df_clean = df_clean.drop_duplicates(subset=duplicate_cols, keep='first').reset_index(drop=True)

print(f"Cleaned rows after deduplication: {len(df_clean):,}")

# 7. Drop unused columns
columns_to_drop = ['OwnerAddress', 'TaxDistrict', 'PropertyAddress', 'SaleDate']
df_clean = df_clean.drop(columns=columns_to_drop, errors='ignore')

# Final info
print("\n" + "="*60)
print("✅ CLEANING COMPLETED SUCCESSFULLY")
print(f"Final shape: {df_clean.shape}")
print("Final columns:", df_clean.columns.tolist())
print("="*60)

# ==================== SAVE WITH HEADERS ====================
df_clean.to_csv('housing_data_cleaned.csv', index=False)
print("\n✅ 'housing_data_cleaned.csv' created successfully with column headers!")