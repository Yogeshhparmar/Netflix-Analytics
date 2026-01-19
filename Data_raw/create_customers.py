import pandas as pd

# Load raw users data
users = pd.read_csv("Data_raw/users.csv")

# Select required columns
customers = users[
    [
        'user_id',
        'age',
        'gender',
        'country',
        'subscription_plan',
        'subscription_start_date'
    ]
].copy()

# Rename columns
customers.rename(columns={
    'user_id': 'customer_id',
    'subscription_plan': 'plan_type',
    'subscription_start_date': 'signup_date'
}, inplace=True)

# Convert signup_date to datetime
customers['signup_date'] = pd.to_datetime(customers['signup_date'])

# Calculate tenure in months
customers['tenure_months'] = (
    pd.to_datetime('today') - customers['signup_date']
).dt.days // 30

# Save processed customers table
customers.to_csv("Processed_data/customers.csv", index=False)

print("customers table created successfully")
print(customers.head())

import pandas as pd

cust = pd.read_csv("Processed_data/customers.csv")

# 1️⃣ Remove duplicate customer_id
cust = cust.drop_duplicates(subset=['customer_id'])

# 2️⃣ Normalize gender (short values)
cust['gender'] = cust['gender'].replace({
    'Male': 'M',
    'Female': 'F',
    'Non-binary': 'NB',
    'Prefer not to say': 'NA'
})

# 3️⃣ Ensure no leading/trailing spaces
cust['customer_id'] = cust['customer_id'].str.strip()

# Save cleaned customers
cust.to_csv("Processed_data/customers.csv", index=False)

print("Clean customers:", cust.shape)
print(cust['gender'].value_counts())
import pandas as pd
import numpy as np

cust = pd.read_csv("Processed_data/customers.csv")

# Convert empty strings to NaN
cust['age'] = pd.to_numeric(cust['age'], errors='coerce')

# Optional: sanity check
print(cust['age'].isna().sum(), "missing age values")

# Save with MySQL-friendly NULLs
cust.to_csv(
    "Processed_data/customers.csv",
    index=False,
    na_rep='NULL'
)

print("customers.csv cleaned for age column")
            
