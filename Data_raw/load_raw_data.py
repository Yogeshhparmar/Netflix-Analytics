import pandas as pd

users = pd.read_csv('Data_raw/users.csv')
movies = pd.read_csv('Data_raw/movies.csv')
watch_history = pd.read_csv('Data_raw/watch_history.csv')
reco = pd.read_csv('Data_raw/recommendation_logs.csv')
search = pd.read_csv('Data_raw/search_logs.csv')
reviews = pd.read_csv('Data_raw/reviews.csv')

print("Users:", users.shape)
print("Movies:", movies.shape)
print("Watch History:", watch_history.shape)
print("Recommendations:", reco.shape)
print("Search Logs:", search.shape)
print("Reviews:", reviews.shape)