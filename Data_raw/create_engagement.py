import pandas as pd

# Load watch history data
watch = pd.read_csv("Data_raw/watch_history.csv")

# Convert watch_date to datetime
watch['watch_date'] = pd.to_datetime(watch['watch_date'])

# Convert minutes to hours
watch['watch_hours'] = watch['watch_duration_minutes'] / 60

# Create month column
watch['month'] = watch['watch_date'].dt.to_period('M').dt.to_timestamp()

# Aggregate engagement metrics per customer per month
engagement = (
    watch.groupby(['user_id', 'month'])
    .agg(
        watch_hours=('watch_hours', 'sum'),
        login_days=('watch_date', 'nunique'),
        num_titles_watched=('movie_id', 'nunique')
    )
    .reset_index()
)

# Create engagement_id
engagement['engagement_id'] = range(1, len(engagement) + 1)

# Rename user_id to customer_id
engagement.rename(columns={'user_id': 'customer_id'}, inplace=True)

# Reorder columns
engagement = engagement[
    [
        'engagement_id',
        'customer_id',
        'month',
        'watch_hours',
        'login_days',
        'num_titles_watched'
    ]
]

# Save processed engagement table
engagement.to_csv("Processed_data/engagement.csv", index=False)

print("engagement table created successfully")
print(engagement.head())
import pandas as pd

eng = pd.read_csv("Processed_data/engagement.csv")
cust = pd.read_csv("Processed_data/customers.csv")

# Strip spaces
eng['customer_id'] = eng['customer_id'].str.strip()
cust['customer_id'] = cust['customer_id'].str.strip()

# Keep only valid customers
eng = eng[eng['customer_id'].isin(cust['customer_id'])]

# Save clean engagement
eng.to_csv("Processed_data/engagement.csv", index=False)

print("Clean engagement rows:", eng.shape)
