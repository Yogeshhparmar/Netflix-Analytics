import pandas as pd

# Load engagement data
engagement = pd.read_csv("Processed_data/engagement.csv")
customers = pd.read_csv("Processed_data/customers.csv")

engagement['month'] = pd.to_datetime(engagement['month'])

# Last activity per customer
last_activity = (
    engagement.groupby('customer_id')['month']
    .max()
    .reset_index()
    .rename(columns={'month': 'last_active_month'})
)

# Reference date
reference_date = engagement['month'].max()

# Inactivity days
last_activity['days_inactive'] = (
    reference_date - last_activity['last_active_month']
).dt.days

# Churn rule
CHURN_DAYS = 60
last_activity['is_churned'] = (last_activity['days_inactive'] > CHURN_DAYS).astype(int)

# Churn date
last_activity['churn_date'] = last_activity.apply(
    lambda x: x['last_active_month'] if x['is_churned'] == 1 else None,
    axis=1
)

# 🔥 KEEP ONLY CUSTOMERS THAT EXIST
churn = last_activity.merge(
    customers[['customer_id']],
    on='customer_id',
    how='inner'
)

# Final table
churn = churn[['customer_id', 'is_churned', 'churn_date']]

# 🔥 Force MySQL-friendly CSV
churn.to_csv(
    "Processed_data/churn.csv",
    index=False,
    na_rep='NULL'
)

print("churn table created successfully")
print(churn.head())
