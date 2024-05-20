# add your code here
"""
import pandas as pd

wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

new_df = wine_reviews.groupby('country').agg({'country':'count', 'points': 'mean'}).round(1)

new_df = new_df.rename(columns = {'country': 'count'}).reset_index()

new_df = new_df.sort_values('count', ascending=False)

new_df = new_df.reset_index(drop=True)

new_df.to_csv('data/reviews-per-country.csv', index = False)

print(new_df)
"""

import pandas as pd

# Read the CSV file into a DataFrame
wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

# Group by 'country' and calculate both count and mean points
new_df = wine_reviews.groupby('country').agg(
    count=('country', 'size'),  # count the occurrences of each country
    points=('points', 'mean')  # calculate the mean points for each country
).round({'points': 1}).reset_index()  # round mean points to 1 decimal place

# Sort DataFrame by review count in descending order
new_df = new_df.sort_values('count', ascending=False)

# Reset index
new_df = new_df.reset_index(drop=True)

# Save the DataFrame to a CSV file without index
new_df.to_csv('data/reviews-per-country.csv', index=False)

print(new_df)
