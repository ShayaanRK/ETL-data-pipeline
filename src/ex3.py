from pathlib import Path
import pandas as pd 
import os

import sys

sys.stdout.reconfigure(encoding='utf-8')
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "raw" / "INvideos.csv"

vids = pd.read_csv(DATA_PATH)

os.system('cls')
# print(vids)

# Task 1.1 (Positional Slice): Select the first 10 rows and the first 3 columns
print(vids.iloc[:10, :3])

# Task 1.2 (Single Position): Select only the first row across all columns using positional indexing.
print(vids.iloc[0, :])

# Task 1.3 (Label / Name Selection): Select specific named columns for the first 5 labeled rows using label indexing.
print(vids.loc[:4, ['channel_title', 'views', 'publish_time']])

# Task 1.4 (Compound Boolean Filtering): Filter the dataset for videos from the channel 'T-Series' and having views greater than or equal to 1,000,000.
bool_vids = vids.loc[(vids.channel_title == 'T-Series') & (vids.views >= 1000000)]
print(bool_vids.head(5))

# Task 1.5 (Membership Filtering): Filter for rows where category_id is in [10, 24] using .isin().
membership_vids = vids.loc[vids.category_id.isin([10, 24])]
print(membership_vids)

# Task 1.6 (Non-null Filtering): Filter the DataFrame to return only rows where description is not missing / not null.
nonull = vids.loc[vids.description.notnull()]
print(nonull)

## Summary Functions

# Task 2.1 (Numerical Overview): Generate a full statistical summary specifically for the views column.
print(vids.views.describe())

# Task 2.2 (Categorical Overview): Generate a statistical summary of the channel_title column showing total count, unique channels, top channel, and its frequency.
print(vids.channel_title.describe())

# Task 2.3 (Value Frequencies): Count how many times each channel_title appears in the dataset, ordered from most frequent to least frequent.
print(vids.channel_title.value_counts())

# Task 2.4 (Unique Elements): Retrieve a list/array of all distinct category_id values present in the dataset.
print(vids.category_id.unique())

# Task 2.5 (Count of Unique Elements): Find the exact number of unique channels (channel_title) in the dataset.
print(vids.channel_title.nunique())

## Maps & Transformations

# Task 3.1 (Series Mapping): Calculate the overall mean of views, then use .map() to adjust every view count by subtracting this mean.
views_mean = vids.views.mean()
print(vids.views.map(lambda v: v - views_mean))

# Task 3.2 (Vectorized Alternative): Perform the exact same mean-centering operation using native pandas vectorized arithmetic.
print(vids.views - views_mean)

# Task 3.3 (Row-wise Transformation): Use .apply(axis='columns') with a custom function inspecting likes and dislikes.
def inspect(row):
    if row.likes >= 50000 and row.dislikes <= 1000:
        return "High Engagement"
    return "Normal"

print(vids.apply(inspect, axis='columns'))