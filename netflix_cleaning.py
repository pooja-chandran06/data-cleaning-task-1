import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles/netflix_titles.csv")

# Display first few rows
print("Original Data:")
print(df.head())

# 1. Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# 2. Handle missing values
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Not Available")
df['country'] = df['country'].fillna("Unknown")
df['rating'] = df['rating'].fillna("Not Rated")

# Drop rows where date_added is missing
df.dropna(subset=['date_added'], inplace=True)

# 3. Remove duplicates
df.drop_duplicates(inplace=True)

# 4. Standardize text values
df['country'] = df['country'].str.lower()
df['type'] = df['type'].str.lower()

# 5. Convert date format
df['date_added'] = pd.to_datetime(df['date_added'], format='mixed', errors='coerce')

# 6. Rename columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 7. Fix data types
df['release_year'] = df['release_year'].astype(int)

# Final info
print("\nCleaned Data Info:")
print(df.info())

# 8. Save cleaned dataset
df.to_csv("cleaned_netflix_data.csv", index=False)

print("\nData cleaning completed. File saved as cleaned_netflix_data.csv")
